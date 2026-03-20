"""
Clarification System
===================

Identifica possíveis ambiguidades na demanda e gera CLARIFICATION TASKS
para Planner questionar ANTES de implementar.

Exemplo:
  Demanda: "Implementar Selo de Qualidade"
  
  ❓ DEVE PERGUNTAR:
    1. Selode Qualidade é um novo objeto ou propriedade de Empresa?
    2. Existe Empresa já? Devemos estender ou criar nova entidade?
    3. Que campos deve ter (nome, descrição, validade)?
    4. Qual a relação com Agendamento/Servico?
"""

from typing import List, Dict
from pathlib import Path
from tools.artifact_discoverer import ArtifactDiscoverer


class ClarificationQuestion:
    """Representa uma pergunta de clarificação"""
    
    def __init__(self, question: str, context: str, options: List[str] = None):
        self.question = question
        self.context = context
        self.options = options or []
    
    def to_markdown(self) -> str:
        result = f"**❓ {self.question}**\n"
        if self.context:
            result += f"   Contexto: {self.context}\n"
        if self.options:
            result += "   Opções:\n"
            for i, option in enumerate(self.options, 1):
                result += f"   {i}. {option}\n"
        return result


class ClarificationGenerator:
    """Gera clarification questions baseado na demanda e artifacts descobertos"""
    
    def __init__(self, repo_path: Path = Path("c:\\Castanheira Holding\\Pet.ON.Api")):
        self.discoverer = ArtifactDiscoverer(repo_path)
        self.inventory = self.discoverer.get_full_inventory()
    
    def generate_clarifications(self, demand_text: str, entity_names: List[str]) -> List[ClarificationQuestion]:
        """
        Gera clarification questions para uma demanda específica.
        
        Args:
            demand_text: Texto completo da demanda
            entity_names: Nomes de entidades mencionadas (ex: ["Empresa", "SeloQualidade"])
        
        Returns:
            Lista de ClarificationQuestion
        """
        questions = []
        
        for entity_name in entity_names:
            # Verifica se entidade já existe
            if self.discoverer.does_entity_exist(entity_name):
                # Pergunta se deve estender ou criar nova
                questions.append(ClarificationQuestion(
                    question=f"A entidade '{entity_name}' JÁ EXISTE. Devemos estender ou criar nova?",
                    context=f"{entity_name} já está definida. Adicionar propriedades a ela ou criar entidade separada?",
                    options=[
                        f"Estender {entity_name} com novas propriedades",
                        f"Criar nova entidade separada de {entity_name}",
                        f"Usar padrão Value Object dentro de {entity_name}",
                    ]
                ))
            
            # Pergunta sobre propriedades específicas
            related_artifacts = self.discoverer.get_related_artifacts(entity_name)
            if related_artifacts["entity"]:
                existing_props = related_artifacts["entity"].get("properties", [])
                questions.append(ClarificationQuestion(
                    question=f"Quais propriedades '{entity_name}' deve ter?",
                    context=f"Propriedades existentes: {', '.join(existing_props[:5])}. Adicionar ou modificar?",
                    options=[
                        "Adicionar novas propriedades (especificar nomes e tipos)",
                        "Modificar propriedades existentes",
                        "Remover propriedades não usadas",
                        "Manter como está",
                    ]
                ))
        
        return questions
    
    def generate_reuse_suggestions(self, demand_text: str) -> Dict[str, List[str]]:
        """
        Analisa a demanda e sugere artifacts que PODEM SER REUTILIZADOS.
        
        Retorna dict com:
        - "entities_to_extend": entidades existentes que podem ser expandidas
        - "repositories_to_update": repos que precisarão novos métodos
        - "services_to_update": services que precisarão novos métodos
        - "dtos_needed": novos DTOs necessários
        """
        
        demand_lower = demand_text.lower()
        suggestions = {
            "entities_to_extend": [],
            "repositories_to_update": [],
            "services_to_update": [],
            "dtos_needed": [],
        }
        
        # Procura por keywords de entidades e sugere reutilização
        entity_keywords = {
            "usuario": "Usuario",
            "animal": "Animal",
            "pet": "Animal",
            "empresa": "Empresa",
            "petshop": "Empresa",
            "servico": "Servico",
            "agendamento": "Agendamento",
        }
        
        for keyword, entity_name in entity_keywords.items():
            if keyword in demand_lower:
                if self.discoverer.does_entity_exist(entity_name):
                    suggestions["entities_to_extend"].append(entity_name)
                    
                    # Se há entidade, provavelmente há repo
                    repo_name = f"{entity_name}Repositorio"
                    if self.discoverer.does_repository_exist(repo_name):
                        suggestions["repositories_to_update"].append(repo_name)
        
        return suggestions
    
    def generate_clarification_prompt_for_planner(self, demand_text: str, entity_names: List[str]) -> str:
        """
        Gera um prompt especial para o Planner fazer perguntas de clarificação ANTES de criar o plano.
        
        Deve ser executado ANTES do task_plan normal.
        """
        
        clarifications = self.generate_clarifications(demand_text, entity_names)
        reuse_suggestions = self.generate_reuse_suggestions(demand_text)
        
        prompt = """
## ⚠️ FASE DE CLARIFICAÇÃO - ANTES DO PLANO TÉCNICO

Antes de criar o plano técnico, responda às seguintes perguntas.
Elas são CRÍTICAS para evitar recriação desnecessária de código.

"""
        
        # Adicionar artifacts que podem ser reutilizados
        if reuse_suggestions["entities_to_extend"]:
            prompt += f"### ✅ Entidades Existentes para REUTILIZAR:\n"
            for entity in reuse_suggestions["entities_to_extend"]:
                entity_details = self.discoverer.get_entity_details(entity)
                prompt += f"- **{entity}**: {entity_details.get('description', 'N/A')}\n"
                if entity_details.get("properties"):
                    prompt += f"  Propriedades atuais: {', '.join(entity_details['properties'][:5])}\n"
            prompt += "\n"
        
        if reuse_suggestions["repositories_to_update"]:
            prompt += f"### ✅ Repositories para ESTENDER:\n"
            for repo in reuse_suggestions["repositories_to_update"]:
                prompt += f"- **{repo}** (adicione novos métodos, não crie novo repositório)\n"
            prompt += "\n"
        
        # Adicionar clarification questions
        if clarifications:
            prompt += "### ❓ Perguntas de Clarificação:\n\n"
            for i, clar in enumerate(clarifications, 1):
                prompt += f"{i}. {clar.to_markdown()}\n"
        else:
            prompt += "Nenhuma ambiguidade detectada - proceda com a criação do plano técnico.\n"
        
        return prompt
    
    def should_ask_clarifications(self, entity_names: List[str]) -> bool:
        """Verifica se há entidades ambíguas que requerem clarificação"""
        for entity_name in entity_names:
            if self.discoverer.does_entity_exist(entity_name):
                return True
        return False


def extract_entity_names_from_demand(demand_text: str) -> List[str]:
    """
    Tenta extrair nomes de entidades mencionadas na demanda.
    
    Procura por padrões como:
    - "Entidade X"
    - "Objeto X"
    - "Nova entidade X"
    - "Campo X"
    - "Implementar X" (novo objeto)
    - Nomes próprios capitalizados: "Selo", "Qualidade", "Status"
    """
    
    import re
    
    entity_patterns = [
        # Padrões explícitos: "entidade X", "objeto X", "classe X"
        r"(?:entidade|objeto|modelo|classe)\s+([A-Za-z]+(?:[A-Z][a-z]+)*)",
        # Padrões com "novo/novo": "novo X", "nova entidade X"
        r"novo(?:a)?\s+(?:(?:entidade|objeto)\s+)?([A-Za-z]+(?:[A-Z][a-z]+)*)",
        # Padrões de criação: "criar X", "implementar X", "adicionar X"
        r"(?:criar|implementar|adicionar|refatorar)\s+(?:(?:entidade|objeto|campo)\s+)?([A-Za-z]+(?:[A-Z][a-z]+)*)",
        # Títulos: "# Demanda: X" ou "## X"
        r"(?:#+ )?(?:Demanda|Feature|Implementação):\s*([A-Za-z]+(?:\s+[A-Za-z]+)*)",
    ]
    
    entities = set()
    
    for pattern in entity_patterns:
        matches = re.findall(pattern, demand_text, re.MULTILINE)
        for match in matches:
            # Clean up: remover espaços e converter para CamelCase
            cleaned = match.strip().title().replace(" ", "")
            if len(cleaned) > 1:  # Ignorar palavras muito curtas
                entities.add(cleaned)
    
    # Também procura por PascalCase palavras já capitalizadas no texto
    pascal_case_pattern = r"\b([A-Z][a-z]+(?:[A-Z][a-z]+)*)\b"
    for match in re.finditer(pascal_case_pattern, demand_text):
        word = match.group(1)
        # Ignorar palavras muito comuns
        if word.lower() not in ["demanda", "feature", "implementação", "projeto", "api", "web", "app"]:
            entities.add(word)
    
    # Remover duplicatas (case-insensitive) e retornar
    result = []
    seen = set()
    for e in sorted(entities):
        lower = e.lower()
        if lower not in seen:
            result.append(e)
            seen.add(lower)
    
    return result


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("TEST: Clarification System")
    print("=" * 80)
    
    # Teste com demanda de Selo de Qualidade
    test_demand = """
    # Demanda: Implementar Selo de Qualidade da Loja
    
    **Projeto:** Pet.ON.Api
    **Tipo:** Feature
    
    ## Descrição
    Implementar um sistema de Selo de Qualidade para as lojas.
    Cada PetShop pode ter um selo indicando certificação de qualidade.
    O selo tem validade e critérios que devem ser cumpridos.
    """
    
    gen = ClarificationGenerator()
    
    # Extrai entidades mencionadas
    entities = extract_entity_names_from_demand(test_demand)
    print(f"\n📋 Entidades mencionadas: {entities}")
    
    # Gera clarifications
    should_ask = gen.should_ask_clarifications(entities)
    print(f"❓ Precisa clarificação? {should_ask}")
    
    if should_ask:
        prompt = gen.generate_clarification_prompt_for_planner(test_demand, entities)
        print("\n" + "=" * 80)
        print("CLARIFICATION PROMPT PARA PLANNER:")
        print("=" * 80)
        print(prompt)
    
    # Reuse suggestions
    reuse = gen.generate_reuse_suggestions(test_demand)
    print("\n" + "=" * 80)
    print("REUSE SUGGESTIONS:")
    print("=" * 80)
    print(f"Entities to extend: {reuse['entities_to_extend']}")
    print(f"Repositories to update: {reuse['repositories_to_update']}")
