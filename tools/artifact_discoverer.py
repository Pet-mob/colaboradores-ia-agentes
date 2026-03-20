"""
Artifact Discovery System
========================

Mapeia automaticamente os artifacts que JÁ EXISTEM no codebase:
- Entidades (Domain)
- Repositories
- Services
- DTOs
- Controllers
- Validators

Evita que agents RECRIE o que já existe e REUTILIZE o que já está lá.
"""

from pathlib import Path
from typing import Dict, List, Set, Tuple
import re


class ArtifactDiscoverer:
    """Descobre artifacts existentes no codebase Petmob"""
    
    def __init__(self, repo_path: Path = Path("c:\\Castanheira Holding\\Pet.ON.Api")):
        self.repo_path = Path(repo_path)
        self.domain_path = self.repo_path / "Pet.ON.Domain"
        self.infra_path = self.repo_path / "Pet.ON.Infra"
        self.app_path = self.repo_path / "Pet.ON.Application"
        self.api_path = self.repo_path / "Pet.ON.Api"
        
    def discover_entities(self) -> Dict[str, Dict]:
        """Descobre todas as entidades no Domain"""
        entidade_path = self.domain_path / "Entidade"
        entities = {}
        
        if not entidade_path.exists():
            return entities
        
        # Scan de pastas e arquivos .cs no Entidade
        for folder in entidade_path.iterdir():
            if folder.is_dir() and folder.name not in ['__pycache__']:
                for cs_file in folder.glob("*.cs"):
                    entity_name = cs_file.stem
                    properties = self._extract_properties(cs_file)
                    methods = self._extract_methods(cs_file)
                    
                    entities[entity_name] = {
                        "path": str(cs_file),
                        "folder": folder.name,
                        "properties": properties,
                        "methods": methods,
                        "description": self._extract_xml_summary(cs_file),
                    }
        
        return entities
    
    def discover_repositories(self) -> Dict[str, Dict]:
        """Descobre todos os Repositories"""
        repo_base_path = self.infra_path / "Repositorio"
        repositories = {}
        
        if not repo_base_path.exists():
            return repositories
        
        # Scan de pastas (Animal, Usuario, Empresa, etc)
        for folder in repo_base_path.iterdir():
            if folder.is_dir() and folder.name not in ['__pycache__']:
                for cs_file in folder.glob("*.cs"):
                    repo_name = cs_file.stem
                    methods = self._extract_methods(cs_file)
                    
                    repositories[repo_name] = {
                        "path": str(cs_file),
                        "folder": folder.name,
                        "methods": methods,
                        "description": self._extract_xml_summary(cs_file),
                    }
        
        return repositories
    
    def discover_services(self) -> Dict[str, Dict]:
        """Descobre todos os Services"""
        service_path = self.app_path / "Servicos" if (self.app_path / "Servicos").exists() else None
        services = {}
        
        if not service_path or not service_path.exists():
            return services
        
        for cs_file in service_path.glob("*.cs"):
            service_name = cs_file.stem
            methods = self._extract_methods(cs_file)
            
            services[service_name] = {
                "path": str(cs_file),
                "methods": methods,
                "description": self._extract_xml_summary(cs_file),
            }
        
        return services
    
    def discover_dtos(self) -> Dict[str, Dict]:
        """Descobre todos os DTOs"""
        dto_path = self.domain_path / "Dtos"
        dtos = {}
        
        if not dto_path.exists():
            return dtos
        
        for cs_file in dto_path.glob("*.cs"):
            dto_name = cs_file.stem
            properties = self._extract_properties(cs_file)
            
            dtos[dto_name] = {
                "path": str(cs_file),
                "properties": properties,
                "description": self._extract_xml_summary(cs_file),
            }
        
        return dtos
    
    def discover_controllers(self) -> Dict[str, Dict]:
        """Descobre todos os Controllers"""
        controller_path = self.api_path / "Controllers"
        controllers = {}
        
        if not controller_path.exists():
            return controllers
        
        for cs_file in controller_path.glob("*.cs"):
            controller_name = cs_file.stem
            methods = self._extract_methods(cs_file)
            
            controllers[controller_name] = {
                "path": str(cs_file),
                "methods": methods,
                "description": self._extract_xml_summary(cs_file),
            }
        
        return controllers
    
    def _extract_properties(self, file_path: Path) -> List[str]:
        """Extrai nomes de propriedades públicas de um arquivo C#"""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            # Padrão: public <type> <name> { get; set; }
            pattern = r'public\s+(?:async\s+)?[\w<>,\s]+\s+(\w+)\s*\{(?:get|set)'
            properties = re.findall(pattern, content)
            return list(set(properties))  # Remove duplicatas
        except:
            return []
    
    def _extract_methods(self, file_path: Path) -> List[Tuple[str, str]]:
        """Extrai nomes e assinaturas de métodos públicos"""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            # Padrão: public (async) <return> MethodName(params)
            pattern = r'public\s+(?:async\s+)?(?:\w+[\s<>,]*)\s+(\w+)\s*\((.*?)\)'
            matches = re.findall(pattern, content)
            return [(name, params) for name, params in matches]
        except:
            return []
    
    def _extract_xml_summary(self, file_path: Path) -> str:
        """Extrai comentário XML /// <summary> do arquivo"""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            # Procura por <summary>...</summary>
            pattern = r'<summary>\s*(.*?)\s*</summary>'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                return match.group(1).strip().replace('\n', ' ')
            return ""
        except:
            return ""
    
    def get_full_inventory(self) -> Dict:
        """Retorna inventário completo de todos os artifacts"""
        return {
            "entities": self.discover_entities(),
            "repositories": self.discover_repositories(),
            "services": self.discover_services(),
            "dtos": self.discover_dtos(),
            "controllers": self.discover_controllers(),
        }
    
    def does_entity_exist(self, entity_name: str) -> bool:
        """Verifica se uma entidade existe"""
        entities = self.discover_entities()
        return entity_name in entities
    
    def does_repository_exist(self, repo_name: str) -> bool:
        """Verifica se um repository existe"""
        repositories = self.discover_repositories()
        return repo_name in repositories
    
    def get_entity_details(self, entity_name: str) -> Dict:
        """Retorna detalhes de uma entidade específica"""
        entities = self.discover_entities()
        return entities.get(entity_name, {})
    
    def get_related_artifacts(self, entity_name: str) -> Dict:
        """Retorna artifacts relacionados a uma entidade (repo, service, controller, dtos)"""
        related = {"entity": {}, "repository": {}, "services": {}, "dtos": {}, "controllers": {}}
        
        # Entity
        entities = self.discover_entities()
        if entity_name in entities:
            related["entity"] = entities[entity_name]
        
        # Repository (procura por padrão ${Entity}Repositorio)
        repositories = self.discover_repositories()
        repo_name = f"{entity_name}Repositorio"
        if repo_name in repositories:
            related["repository"] = repositories[repo_name]
        
        # DTOs (procura por padrões ${Entity}ReqDto, ${Entity}ResDto)
        dtos = self.discover_dtos()
        for dto_pattern in [f"{entity_name}ReqDto", f"{entity_name}ResDto", f"Buscar{entity_name}ReqDto", f"{entity_name}Dto"]:
            if dto_pattern in dtos:
                related["dtos"][dto_pattern] = dtos[dto_pattern]
        
        # Controllers (procura por padrão ${Entity}Controller)
        controllers = self.discover_controllers()
        controller_name = f"{entity_name}Controller"
        if controller_name in controllers:
            related["controllers"][controller_name] = controllers[controller_name]
        
        return related


def generate_artifact_markdown(inventory: Dict) -> str:
    """Gera markdown documentando todos os artifacts descobertos"""
    
    markdown = "# Artifacts Descobertos no Codebase\n\n"
    
    # Entidades
    markdown += "## Entidades (Domain)\n\n"
    for entity_name, details in inventory["entities"].items():
        markdown += f"### {entity_name}\n"
        if details.get("description"):
            markdown += f"**Descrição:** {details['description']}\n\n"
        markdown += f"**Folder:** `{details['folder']}`\n\n"
        
        if details.get("properties"):
            markdown += f"**Propriedades({len(details['properties'])}):**\n"
            for prop in sorted(details["properties"])[:10]:  # Max 10
                markdown += f"- {prop}\n"
            if len(details["properties"]) > 10:
                markdown += f"- ... e {len(details['properties']) - 10} mais\n"
            markdown += "\n"
        
        if details.get("methods"):
            markdown += f"**Métodos({len(details['methods'])}):**\n"
            for method_name, params in details["methods"][:5]:  # Max 5
                markdown += f"- {method_name}({params[:40]}...)\n"
            if len(details["methods"]) > 5:
                markdown += f"- ... e {len(details['methods']) - 5} mais\n"
            markdown += "\n"
    
    # Repositories
    markdown += "## Repositories (Infra)\n\n"
    for repo_name, details in inventory["repositories"].items():
        markdown += f"### {repo_name}\n"
        if details.get("methods"):
            markdown += f"**Métodos({len(details['methods'])}):**\n"
            for method_name, _ in details["methods"][:5]:
                markdown += f"- {method_name}()\n"
            if len(details["methods"]) > 5:
                markdown += f"- ... e {len(details['methods']) - 5} mais\n"
        markdown += "\n"
    
    # DTOs
    if inventory["dtos"]:
        markdown += "## DTOs Existentes\n\n"
        for dto_name, details in inventory["dtos"].items():
            markdown += f"### {dto_name}\n"
            if details.get("properties"):
                markdown += f"**Propriedades:** {', '.join(details['properties'][:5])}\n"
                if len(details["properties"]) > 5:
                    markdown += f"... e {len(details['properties']) - 5} mais\n"
            markdown += "\n"
    
    return markdown


if __name__ == "__main__":
    discoverer = ArtifactDiscoverer()
    inventory = discoverer.get_full_inventory()
    
    print("\n" + "=" * 80)
    print("ARTIFACT DISCOVERY REPORT")
    print("=" * 80 + "\n")
    
    print(f"✅ {len(inventory['entities'])} Entidades descobertas")
    for name in inventory['entities']:
        print(f"   - {name}")
    
    print(f"\n✅ {len(inventory['repositories'])} Repositories descobertos")
    for name in inventory['repositories']:
        print(f"   - {name}")
    
    print(f"\n✅ {len(inventory['dtos'])} DTOs descobertos")
    for name in inventory['dtos']:
        print(f"   - {name}")
    
    print(f"\n✅ {len(inventory['controllers'])} Controllers descobertos")
    for name in inventory['controllers']:
        print(f"   - {name}")
    
    print("\n" + "=" * 80)
    print("\nExemplo - Artifacts relacionados a 'Empresa':")
    print("=" * 80)
    related = discoverer.get_related_artifacts("Empresa")
    print(f"Entity: {related['entity'].get('description', 'N/A')}")
    print(f"Repository: {'EmpresaRepositorio' in inventory['repositories']}")
    print(f"DTOs: {list(related['dtos'].keys())}")
    print(f"Controllers: {list(related['controllers'].keys())}")
