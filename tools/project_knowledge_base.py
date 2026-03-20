"""
Knowledge Base do Projeto
Consolida contexto sobre Petmob, tecnologias, padrões e regras de negócio
"""

import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional


@dataclass
class ProjectInfo:
    """Informações sobre um projeto"""
    name: str
    description: str
    stack: List[str]
    type: str  # api, frontend, mobile
    local_path: str
    key_technologies: List[str]
    architecture_notes: str = ""
    common_patterns: List[str] = None
    
    def to_dict(self):
        return asdict(self)


class ProjectKnowledgeBase:
    """
    Base de conhecimento centralizada sobre os projetos
    Fornece contexto rico aos agents
    """
    
    def __init__(self, projects_dir: Path = None):
        self.projects_dir = projects_dir or Path(__file__).parent.parent / "projects"
        self.projects = {}
        self.business_context = self._define_business_context()
        self.tech_patterns = self._define_tech_patterns()
        self.load_projects()
    
    def load_projects(self):
        """Carrega informações dos projetos"""
        
        # Pet.ON.Api (.NET Backend)
        self.projects["pet.on.api"] = ProjectInfo(
            name="Pet.ON.Api",
            description="Backend API principal da plataforma Petmob - responsável por toda a lógica de negócio",
            stack=[".NET 8", "C#", "Entity Framework Core", "SQL Server"],
            type="api",
            local_path="C:\\Castanheira Holding\\Pet.ON.Api",
            key_technologies=["REST API", "JWT", "Dependency Injection", "Repository Pattern"],
            architecture_notes="""
- Arquitetura em camadas (Controllers → Services → Repositories → Database)
- Database First com SQL Server
- Controllers mapeiam endpoints REST
- Services contêm lógica de negócio
- Repositories fazem acesso a dados
            """,
            common_patterns=[
                "Controller + Service + Repository",
                "AsyncAwait para operações I/O",
                "Validation com FluentValidation",
                "Mapping com AutoMapper",
                "DI Container para injeção"
            ]
        )
        
        # PetShop.WebApp (Vue.js Frontend)
        self.projects["petshop.webapp"] = ProjectInfo(
            name="PetShop.WebApp",
            description="Aplicação web para petshops gerenciarem seus serviços, agendamentos e configurações",
            stack=["Vue.js 3", "JavaScript/TypeScript", "Vuex/Pinia", "TailwindCSS"],
            type="frontend",
            local_path="C:\\Castanheira Holding\\PetShop.WebApp",
            key_technologies=["Components", "State Management", "API Integration", "Responsive Design"],
            architecture_notes="""
- Estrutura de componentes reutilizáveis
- State management para dados globais
- Comunicação com Pet.ON.Api via REST
- Temas e branding específico para petshops
- Responsivo para desktop e tablet
            """,
            common_patterns=[
                "Single File Components",
                "Composable API",
                "Props e Events para comunicação",
                "API service layer",
                "Form validation"
            ]
        )
        
        # Pet.ON.App (React Native)
        self.projects["pet.on.app"] = ProjectInfo(
            name="Pet.ON.App",
            description="App mobile para usuários finais agendarem serviços em petshops e gerenciarem seus pets",
            stack=["React Native", "JavaScript/TypeScript", "Redux", "Native APIs"],
            type="mobile",
            local_path="C:\\Castanheira Holding\\Pet.ON.App",
            key_technologies=["Native Modules", "Navigation", "Local Storage", "Geolocation"],
            architecture_notes="""
- Componentes funcionais com Hooks
- Navegação em abas e stack
- Sincronização com backend
- Armazenamento local com AsyncStorage
- Integração com câmera e geolocalização
            """,
            common_patterns=[
                "Functional Components + Hooks",
                "Redux para state global",
                "Service layer para API",
                "Custom hooks reutilizáveis",
                "Screen components grandes"
            ]
        )
    
    def _define_business_context(self) -> Dict:
        """Define contexto de negócio da Petmob"""
        return {
            "company": "Petmob",
            "domain": "PetShop Management & Pet Services Platform",
            "core_entities": {
                "Petshop": "Loja que oferece serviços para pets (banho, tosa, consulta, etc)",
                "Pet": "Animal de estimação (cão, gato, etc) cadastrado no sistema",
                "User": "Usuário final que agenda serviços para seus pets",
                "Service": "Tipo de serviço oferecido (banho, tosa, consulta, etc)",
                "Appointment": "Agendamento de um serviço em uma petshop",
                "Review": "Avaliação e comentário sobre uma petshop ou serviço"
            },
            "key_workflows": [
                "User busca petshop próxima → visualiza serviços → agenda → recebe notificação",
                "Petshop cria serviços → define preços e disponibilidade → gerencia agendamentos",
                "Admin gerencia plataforma → modela petshops → resolve conflitos"
            ],
            "constraints": [
                "Horários devem respeitar funcionamento da petshop",
                "Cada pet tem necessidades específicas (tamanho, tipo, raça)",
                "Competição entre petshops deve ser por qualidade, não por preço",
                "Dados de pets são sensíveis - LGPD compliant"
            ],
            "high_value_features": [
                "Geolocation - encontrar petshops próximas",
                "Real-time availability - saber horários disponíveis em tempo real",
                "User reviews - confiança na plataforma",
                "Photo integration - visualizar o resultado final do serviço"
            ]
        }
    
    def _define_tech_patterns(self) -> Dict:
        """Define padrões técnicos comuns nos projetos"""
        return {
            "backend_patterns": {
                "MVC": "Model-View-Controller com separação de responsabilidades",
                "Repository": "Abstração para acesso a dados",
                "Service": "Lógica de negócio isolada",
                "DTO": "Data Transfer Objects para transferência entre camadas",
                "Validation": "Validação centralizada com FluentValidation",
                "Logging": "ILogger para rastreamento de execução"
            },
            "frontend_patterns": {
                "Component": "Componente reutilizável com clara interface",
                "Container": "Componente que gerencia estado (Smart Component)",
                "Presentational": "Componente que apenas renderiza (Dumb Component)",
                "Custom Hook": "Lógica reutilizável em forma de hook",
                "Service Layer": "Separação de chamadas API"
            },
            "common_across_all": {
                "Error Handling": "Tratamento consistente de erros com feedback ao usuário",
                "Loading States": "Indicadores de carregamento para melhor UX",
                "Caching": "Cache para reduzir chamadas desnecessárias",
                "Validation": "Validação no lado cliente e servidor",
                "Logging": "Logs estruturados para debug e monitoring"
            }
        }
    
    def get_project_info(self, project_name: str) -> Optional[ProjectInfo]:
        """Obtém informações de um projeto específico"""
        key = project_name.lower().strip()
        for k, v in self.projects.items():
            if k in key or project_name.lower() in k:
                return v
        return None
    
    def get_context_for_planner(self, project_name: str, demand_type: str) -> str:
        """Gera contexto específico para o Planner Agent"""
        project = self.get_project_info(project_name)
        
        if not project:
            return self._get_default_context()
        
        context = f"""
# CONTEXTO DO PROJETO

## Projeto: {project.name}
**Descrição:** {project.description}

## Stack Tecnológico
- Linguagens: {', '.join(project.stack)}
- Arquitetura: {project.architecture_notes}

## Padrões Comuns
{chr(10).join(f'- {p}' for p in (project.common_patterns or []))}

## Entidades de Negócio Principais
{chr(10).join(f'- **{k}**: {v}' for k, v in self.business_context.get('core_entities', {}).items())}

## Contexto de Negócio
- **Domínio**: {self.business_context.get('domain')}
- **Restrições Importantes**:
{chr(10).join(f'  • {r}' for r in self.business_context.get('constraints', []))}

## Ao Planejar
1. Considere os padrões arquiteturais da stack
2. Identifique qual entidade de negócio será impactada
3. Verifique se há dependências com outros projetos
4. Respeite as constraints de negócio
        """
        
        return context
    
    def get_context_for_developer(self, project_name: str) -> str:
        """Gera contexto específico para o Developer Agent"""
        project = self.get_project_info(project_name)
        
        if not project:
            return self._get_default_context()
        
        patterns = self.tech_patterns.get(f"{project.type}_patterns", {})
        
        context = f"""
# CONTEXTO TÉCNICO PARA DESENVOLVIMENTO

## Projeto: {project.name}
**Stack**: {', '.join(project.stack)}

## Padrões Recomendados
{chr(10).join(f'- **{k}**: {v}' for k, v in patterns.items())}

## Padrões Comuns no Projeto
{chr(10).join(f'- {p}' for p in (project.common_patterns or []))}

## Guias de Implementação

### Estrutura de Diretórios
Para {project.type}:
"""
        
        if project.type == "api":
            context += """
```
src/
  Controllers/     # Endpoints HTTP
  Services/        # Lógica de negócio
  Repositories/    # Acesso a dados
  Models/          # Entidades do domínio
  DTOs/            # Modelos de transferência
  Validators/      # Validações
  Exceptions/      # Exceções customizadas
```
"""
        elif project.type == "frontend":
            context += """
```
src/
  components/      # Componentes reutilizáveis
  pages/           # Pages/Views
  services/        # Chamadas API
  store/           # State management
  composables/     # Custom hooks/composables
  utils/           # Funções utilitárias
```
"""
        elif project.type == "mobile":
            context += """
```
src/
  screens/         # Telas da aplicação
  components/      # Componentes reutilizáveis
  services/        # Chamadas API
  store/           # Redux store
  hooks/           # Custom hooks
  utils/           # Funções utilitárias
```
"""
        
        context += f"""

## Checklist de Implementação
- [ ] Código segue padrões da stack
- [ ] Validação implementada
- [ ] Tratamento de erros apropriado
- [ ] Logs/Debugging adequados
- [ ] Comentários em partes complexas
- [ ] Reutiliza componentes/patterns existentes
        """
        
        return context
    
    def get_context_for_qa(self, project_name: str) -> str:
        """Gera contexto específico para o QA Agent"""
        project = self.get_project_info(project_name)
        
        context = f"""
# CONTEXTO PARA ANÁLISE DE QUALIDADE

## Projeto: {project.name if project else 'Unknown'}

## Aspectos Críticos a Verificar
1. **Segurança**
   - Validação de entrada (SQL injection, XSS)
   - Autenticação/Autorização correta
   - Dados sensíveis (LGPD compliant se pet data)

2. **Performance**
   - N+1 queries (se DB)
   - Timeouts apropriados
   - Caching onde necessário

3. **Funcionalidade**
   - Casos de uso feliz funcionam
   - Edge cases tratados
   - Integrações com outros sistemas

4. **Código**
   - Segue padrões do projeto
   - Legível e manutenível
   - Sem duplicação desnecessária

5. **Testes**
   - Cobertura adequada (>70%)
   - Testes cobrem paths críticos
   - Testes são independentes

## Padrões a Procurar em Code Review
- Falta tratamento de erro?
- Variáveis com nomes obscuros?
- Lógica muito complexa?
- Dependências não injetadas?
        """
        
        return context
    
    def _get_default_context(self) -> str:
        """Retorna contexto padrão quando projeto não é identificado"""
        return """
# CONTEXTO PADRÃO

Você está trabalhando no Petmob - uma plataforma de gerenciamento de petshops.

Sempre considere:
- Segurança de dados de pets (LGPD)
- Experiência do usuário (usuário e petshop)
- Performance
- Escalabilidade
        """


# Instância global
_knowledge_base = None


def get_knowledge_base() -> ProjectKnowledgeBase:
    """Retorna instância singleton da knowledge base"""
    global _knowledge_base
    if _knowledge_base is None:
        _knowledge_base = ProjectKnowledgeBase()
    return _knowledge_base


if __name__ == "__main__":
    # Teste
    kb = get_knowledge_base()
    
    print("\n" + "="*70)
    print("KNOWLEDGE BASE TEST")
    print("="*70)
    
    print("\n📚 Projetos Carregados:")
    for name, project in kb.projects.items():
        print(f"  • {project.name} ({project.type})")
    
    print("\n" + "="*70)
    print("CONTEXTO PARA PLANNER - Pet.ON.Api")
    print("="*70)
    print(kb.get_context_for_planner("pet.on.api", "feature"))
    
    print("\n" + "="*70)
    print("CONTEXTO PARA DEVELOPER")
    print("="*70)
    print(kb.get_context_for_developer("petshop.webapp"))
