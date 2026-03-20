"""
Knowledge Base EXPANDIDO para múltiplos projetos Petmob
Contém: Estrutura de pastas, Endpoints, Componentes, Funcionalidades, Telas, Fluxos
"""

from dataclasses import dataclass
from typing import Dict, List
import json

@dataclass
class ProjectStructure:
    """Estrutura exata de um projeto"""
    name: str
    path: str
    folders: Dict[str, str]  # path: descrição
    
@dataclass
class APIEndpoint:
    """Endpoint da API"""
    method: str
    path: str
    description: str
    params: List[str]
    response: str
    auth_required: bool
    
@dataclass
class UIComponent:
    """Componente de UI"""
    name: str
    path: str
    type: str  # Vue component, React Native screen, etc
    description: str
    props: List[str]
    dependencies: List[str]

@dataclass
class Feature:
    """Feature/Funcionalidade"""
    name: str
    description: str
    affected_entities: List[str]
    endpoints: List[str]
    components: List[str]
    stack: List[str]

# ============================================================================
# PET.ON.API - Backend C#/.NET
# ============================================================================

PET_ON_API_STRUCTURE = {
    "src/Controllers": "Endpoints HTTP - segregados por entidade (User, Pet, Service, Appointment, etc)",
    "src/Services": "Lógica de negócio - cada service orquestra repositórios",
    "src/Repositories": "Acesso a dados - queries ao banco, filtros, operações CRUD",
    "src/Models": "Entidades do banco (Pet, User, PetShop, Service, Appointment, etc)",
    "src/ViewModels": "DTOs de entrada/saída para cliente",
    "src/Context": "DbContext - configuração do EF Core, migrations",
    "src/Validators": "FluentValidation - validações de entrada",
    "src/Mappings": "AutoMapper profiles - mapeamento Model → ViewModel",
    "src/Middleware": "CORS, auth, error handling, logging",
    "src/Enums": "Status, tipos, categorias (ServiceType, AppointmentStatus, PetType, etc)",
    "src/Exceptions": "Custom exceptions para erros de negócio",
    "src/Configurations": "DI container, app settings",
}

PET_ON_API_ENTITIES = {
    "User": {
        "description": "Usuário da aplicação (cliente ou admin)",
        "fields": ["Id", "Name", "Email", "Phone", "ProfileImage", "AddressId", "CreatedAt"],
        "relationships": ["Pets", "Addresses", "Appointments"],
    },
    "Pet": {
        "description": "Animal de estimação (cachorro, gato, etc)",
        "fields": ["Id", "Name", "Type", "Breed", "Age", "Weight", "UserId", "Photo", "VaccineStatus"],
        "relationships": ["User", "Appointments", "Services"],
    },
    "PetShop": {
        "description": "Prestador de serviço (clínica, grooming, hotel, etc)",
        "fields": ["Id", "Name", "Email", "Phone", "Logo", "Banner", "AddressId", "Rating", "OpeningHours"],
        "relationships": ["Address", "Services", "Appointments", "Employees"],
    },
    "Service": {
        "description": "Serviço oferecido por petshop (banho, tosa, consulta, hotel, etc)",
        "fields": ["Id", "Name", "Description", "Price", "Duration", "PetShopId", "Category", "IsActive"],
        "relationships": ["PetShop", "Appointments", "SubServices"],
    },
    "SubService": {
        "description": "Sub-serviço ou add-on de um serviço (ex: hidratação em banho)",
        "fields": ["Id", "Name", "Price", "ServiceId", "Duration"],
        "relationships": ["Service"],
    },
    "Appointment": {
        "description": "Agendamento de serviço",
        "fields": ["Id", "PetId", "ServiceId", "PetShopId", "ScheduledDate", "Status", "Notes", "CreatedAt"],
        "relationships": ["Pet", "Service", "PetShop", "User"],
    },
    "Address": {
        "description": "Endereço de usuário ou petshop",
        "fields": ["Id", "Street", "Number", "City", "State", "ZipCode", "Latitude", "Longitude"],
        "relationships": ["User", "PetShop"],
    },
}

PET_ON_API_ENDPOINTS = {
    "Users": [
        {
            "method": "GET",
            "path": "/api/users",
            "description": "Listar todos os usuários",
            "params": ["page", "limit", "search"],
            "response": "IEnumerable<UserViewModel>",
            "auth": True,
        },
        {
            "method": "GET",
            "path": "/api/users/{id}",
            "description": "Obter usuário por ID com pets e endereços",
            "params": ["id"],
            "response": "UserDetailViewModel",
            "auth": True,
        },
        {
            "method": "POST",
            "path": "/api/users",
            "description": "Criar novo usuário",
            "body": "UserCreateModel",
            "response": "UserViewModel",
            "auth": False,
        },
        {
            "method": "PUT",
            "path": "/api/users/{id}",
            "description": "Atualizar perfil do usuário",
            "params": ["id"],
            "body": "UserUpdateModel",
            "response": "UserViewModel",
            "auth": True,
        },
    ],
    "Pets": [
        {
            "method": "GET",
            "path": "/api/users/{userId}/pets",
            "description": "Listar pets de um usuário",
            "params": ["userId"],
            "response": "IEnumerable<PetViewModel>",
            "auth": True,
        },
        {
            "method": "POST",
            "path": "/api/users/{userId}/pets",
            "description": "Adicionar novo pet ao usuário",
            "params": ["userId"],
            "body": "PetCreateModel",
            "response": "PetViewModel",
            "auth": True,
        },
        {
            "method": "PUT",
            "path": "/api/pets/{id}",
            "description": "Editar dados do pet",
            "params": ["id"],
            "body": "PetUpdateModel",
            "response": "PetViewModel",
            "auth": True,
        },
        {
            "method": "DELETE",
            "path": "/api/pets/{id}",
            "description": "Deletar pet (soft delete com flag IsDeleted)",
            "params": ["id"],
            "response": "204 NoContent",
            "auth": True,
        },
    ],
    "PetShops": [
        {
            "method": "GET",
            "path": "/api/petshops",
            "description": "Listar petshops próximos com filtro de distância",
            "params": ["latitude", "longitude", "radius", "serviceType"],
            "response": "IEnumerable<PetShopViewModel>",
            "auth": False,
        },
        {
            "method": "GET",
            "path": "/api/petshops/{id}",
            "description": "Detalhes completo do petshop + serviços + horários",
            "params": ["id"],
            "response": "PetShopDetailViewModel",
            "auth": False,
        },
        {
            "method": "GET",
            "path": "/api/petshops/{id}/services",
            "description": "Listar serviços de um petshop",
            "params": ["id", "category"],
            "response": "IEnumerable<ServiceViewModel>",
            "auth": False,
        },
        {
            "method": "GET",
            "path": "/api/petshops/search",
            "description": "Buscar petshops por nome, tipo, com paginação",
            "params": ["search", "category", "rating_min", "page"],
            "response": "PagedResult<PetShopListViewModel>",
            "auth": False,
        },
    ],
    "Services": [
        {
            "method": "GET",
            "path": "/api/services/{id}",
            "description": "Detalhes do serviço + preço + sub-serviços",
            "params": ["id"],
            "response": "ServiceDetailViewModel",
            "auth": False,
        },
        {
            "method": "GET",
            "path": "/api/services/{id}/availability",
            "description": "Horários disponíveis para agendamento",
            "params": ["id", "date", "petType"],
            "response": "IEnumerable<TimeSlot>",
            "auth": False,
        },
        {
            "method": "POST",
            "path": "/api/petshops/{petshopId}/services",
            "description": "Criar novo serviço no petshop (admin)",
            "params": ["petshopId"],
            "body": "ServiceCreateModel",
            "response": "ServiceViewModel",
            "auth": True,
        },
    ],
    "Appointments": [
        {
            "method": "GET",
            "path": "/api/users/{userId}/appointments",
            "description": "Listar agendamentos do usuário (com filtro por status)",
            "params": ["userId", "status", "dateFrom", "dateTo"],
            "response": "IEnumerable<AppointmentViewModel>",
            "auth": True,
        },
        {
            "method": "POST",
            "path": "/api/appointments",
            "description": "Criar novo agendamento",
            "body": "AppointmentCreateModel",
            "response": "AppointmentViewModel",
            "auth": True,
        },
        {
            "method": "PUT",
            "path": "/api/appointments/{id}",
            "description": "Atualizar agendamento (data/hora/notas)",
            "params": ["id"],
            "body": "AppointmentUpdateModel",
            "response": "AppointmentViewModel",
            "auth": True,
        },
        {
            "method": "PUT",
            "path": "/api/appointments/{id}/cancel",
            "description": "Cancelar agendamento",
            "params": ["id"],
            "body": "CancellationModel",
            "response": "204 NoContent",
            "auth": True,
        },
        {
            "method": "PUT",
            "path": "/api/appointments/{id}/confirm",
            "description": "Confirmar presença no agendamento",
            "params": ["id"],
            "response": "AppointmentViewModel",
            "auth": True,
        },
    ],
    "Addresses": [
        {
            "method": "GET",
            "path": "/api/users/{userId}/addresses",
            "description": "Listar endereços do usuário",
            "params": ["userId"],
            "response": "IEnumerable<AddressViewModel>",
            "auth": True,
        },
        {
            "method": "POST",
            "path": "/api/users/{userId}/addresses",
            "description": "Adicionar novo endereço",
            "params": ["userId"],
            "body": "AddressCreateModel",
            "response": "AddressViewModel",
            "auth": True,
        },
    ],
}

# ============================================================================
# PETSHOP.WEBAPP - Frontend Vue.js
# ============================================================================

PETSHOP_WEBAPP_STRUCTURE = {
    "src/components": "Componentes reutilizáveis (Card, Button, Modal, Input, etc)",
    "src/views": "Páginas principais (Dashboard, ServiceList, AppointmentList, etc)",
    "src/stores": "Pinia stores - global state (auth, user, appointments, etc)",
    "src/services": "Chamadas HTTP para API (api.js, userService.ts, petshopService.ts)",
    "src/router": "Vue Router - rotas e navegação",
    "src/assets": "Imagens, fontes, ícones SVG",
    "src/styles": "Tailwind CSS - configuração global, themes",
    "src/utils": "Helpers - formatação de data, validação, cálculo de distância",
    "src/types": "TypeScript interfaces (User, Pet, PetShop, etc)",
}

PETSHOP_WEBAPP_SCREENS = [
    {
        "name": "Home/Dashboard",
        "path": "/",
        "description": "Listagem de petshops próximos, busca, filtros",
        "components": ["PetShopCard", "SearchBar", "FiltersPanel", "MapView"],
        "state": ["nearby_petshops", "user_location", "search_query"],
    },
    {
        "name": "PetShop Detail",
        "path": "/petshop/:id",
        "description": "Detalhes completo: serviços, avaliações, horários, contact",
        "components": ["ServiceList", "ReviewCard", "BookingButton", "PhotoGallery"],
        "state": ["selected_petshop", "petshop_services", "reviews"],
    },
    {
        "name": "Service Detail",
        "path": "/service/:id",
        "description": "Detalhes do serviço, preço, sub-serviços, disponibilidade",
        "components": ["ServiceInfo", "PriceBreakdown", "TimeSlotPicker", "AddToCart"],
        "state": ["selected_service", "time_slots"],
    },
    {
        "name": "My Pets",
        "path": "/my-pets",
        "description": "Listagem e gerenciamento de pets do usuário",
        "components": ["PetList", "PetCard", "AddPetModal", "EditPetModal"],
        "state": ["user_pets"],
    },
    {
        "name": "My Appointments",
        "path": "/my-appointments",
        "description": "Histórico e agendamentos futuros",
        "components": ["AppointmentList", "AppointmentCard", "TimelineView"],
        "state": ["user_appointments", "filter_status"],
    },
    {
        "name": "Booking Checkout",
        "path": "/checkout",
        "description": "Confirmação: pet, serviço, data/hora, observações",
        "components": ["BookingSummary", "DateTimePicker", "NotesInput", "ConfirmButton"],
        "state": ["checkout_data", "selected_pet", "selected_slot"],
    },
    {
        "name": "Profile",
        "path": "/profile",
        "description": "Dados do usuário, foto, endereços, preferências",
        "components": ["ProfileForm", "AddressList", "SettingsPanel"],
        "state": ["user_profile", "user_addresses"],
    },
]

# ============================================================================
# PET.ON.APP - Mobile React Native
# ============================================================================

PET_ON_APP_STRUCTURE = {
    "src/screens": "Telas da aplicação (HomeScreen, PetShopDetailScreen, etc)",
    "src/components": "Componentes reutilizáveis (Button, Card, Input, Modal, etc)",
    "src/navigation": "React Navigation - stack, tab, drawer navigation",
    "src/store": "Redux store - auth, user, appointments, filters",
    "src/services": "Chamadas HTTP para API",
    "src/utils": "Helpers - validação, formatação, cálculo de distância",
    "src/assets": "Imagens, ícones, fontes",
    "src/styles": "Estilos globais",
    "src/types": "TypeScript types",
}

PET_ON_APP_SCREENS = [
    {
        "name": "Splash Screen",
        "description": "Tela inicial com logo e animação",
        "navigation_to": ["Login", "HomeTab"],
    },
    {
        "name": "Login Screen",
        "description": "Email/senha com opção de cadastro",
        "form_fields": ["email", "password", "remember_me"],
        "navigation_to": ["HomeTab", "RegisterScreen"],
    },
    {
        "name": "Register Screen",
        "description": "Cadastro de novo usuário",
        "form_fields": ["name", "email", "phone", "password", "confirm_password"],
        "navigation_to": ["HomeTab", "LoginScreen"],
    },
    {
        "name": "Home Tab",
        "description": "Tab principal - petshops próximos com mapa",
        "components": ["MapView", "PetShopList", "SearchBar", "FilterButton"],
        "state": ["user_location", "nearby_petshops", "search_query"],
    },
    {
        "name": "PetShop Detail Screen",
        "description": "Detalhes: info, serviços, avaliações, galeria",
        "components": ["HeaderImage", "InfoSection", "ServiceList", "ReviewSection"],
        "state": ["selected_petshop"],
    },
    {
        "name": "Booking Screen",
        "description": "Agendamento multi-passo: pet → serviço → data/hora → confirmar",
        "steps": ["SelectPet", "SelectService", "SelectDateTime", "Notes", "Confirm"],
        "state": ["checkout_data"],
    },
    {
        "name": "My Appointments Tab",
        "description": "Listagem de agendamentos com status",
        "components": ["AppointmentCard", "StatusBadge", "CancelButton"],
        "state": ["user_appointments"],
    },
    {
        "name": "My Pets Tab",
        "description": "Gerenciamento de pets do usuário",
        "components": ["PetCard", "AddPetButton", "PetModal"],
        "state": ["user_pets"],
    },
    {
        "name": "Profile Tab",
        "description": "Perfil do usuário com settings",
        "components": ["ProfileHeader", "InfoSection", "SettingsPanel"],
        "state": ["user_profile"],
    },
]

# ============================================================================
# FUNCIONALIDADES CORE
# ============================================================================

CORE_FEATURES = {
    "Agendamento": {
        "description": "Fluxo completo de agendamento de serviço",
        "steps": [
            "Login/Cadastro",
            "Localizar petshop",
            "Selecionar serviço",
            "Escolher pet",
            "Selecionar data/hora",
            "Adicionar observações",
            "Confirmar e pagar",
        ],
        "affected_entities": ["User", "Pet", "PetShop", "Service", "Appointment"],
        "affected_screens_web": ["Home", "PetShop Detail", "Service Detail", "Checkout"],
        "affected_screens_mobile": ["Home Tab", "PetShop Detail", "Booking Screen"],
        "apis": [
            "/api/petshops",
            "/api/services/{id}/availability",
            "/api/appointments",
        ],
    },
    "Gerenciamento de Pets": {
        "description": "CRUD de pets do usuário",
        "operations": ["Criar", "Editar", "Deletar", "Listar"],
        "affected_entities": ["Pet", "User"],
        "affected_screens_web": ["My Pets"],
        "affected_screens_mobile": ["My Pets Tab"],
        "apis": ["/api/users/{id}/pets", "/api/pets/{id}"],
    },
    "Histórico de Agendamentos": {
        "description": "Visualizar, cancelar, reagendar agendamentos",
        "operations": ["Listar", "Detalhar", "Cancelar", "Confirmar"],
        "affected_entities": ["Appointment", "Service", "PetShop"],
        "affected_screens_web": ["My Appointments"],
        "affected_screens_mobile": ["My Appointments Tab"],
        "apis": [
            "/api/users/{id}/appointments",
            "/api/appointments/{id}/cancel",
            "/api/appointments/{id}/confirm",
        ],
    },
    "Busca e Filtro": {
        "description": "Localizar petshops por nome, tipo, distância, rating",
        "filters": ["search", "category", "distance", "rating", "price_range"],
        "affected_entities": ["PetShop", "Service"],
        "affected_screens_web": ["Home"],
        "affected_screens_mobile": ["Home Tab"],
        "apis": ["/api/petshops/search", "/api/petshops"],
    },
    "Autenticação": {
        "description": "Login, cadastro, token management",
        "flows": ["Login", "Register", "Logout", "Refresh Token"],
        "security": ["JWT", "HttpOnly cookies", "CORS"],
        "affected_entities": ["User"],
        "affected_screens_web": [],
        "affected_screens_mobile": ["Login Screen", "Register Screen"],
        "apis": [],
    },
}

# ============================================================================
# PADRÕES ARQUITETURAIS
# ============================================================================

ARCHITECTURE_PATTERNS = {
    "Backend (.NET)": {
        "Controller": "Entrada HTTP, validação de rota",
        "Service": "Lógica de negócio, orquestra repositórios",
        "Repository": "Acesso a dados com EF Core",
        "Model": "Entidade do banco de dados",
        "ViewModel": "DTO para resposta HTTP",
        "Validator": "Validação FluentValidation",
        "Mapper": "AutoMapper Model → ViewModel",
        "Middleware": "CORS, Auth, Error Handling",
    },
    "Frontend (Vue.js)": {
        "Component": "UI + lógica local",
        "View": "Página inteira",
        "Store": "Pinia - estado global",
        "Service": "Chamadas HTTP fetch/axios",
        "Router": "Navegação entre páginas",
        "Utils": "Helpers reutilizáveis",
        "Types": "TypeScript interfaces",
    },
    "Mobile (React Native)": {
        "Screen": "Página inteira",
        "Component": "Componente reutilizável",
        "Store": "Redux - estado global",
        "Service": "Chamadas HTTP fetch",
        "Navigation": "React Navigation",
        "Utils": "Helpers reutilizáveis",
        "Styles": "StyleSheet",
    },
}

# ============================================================================
# HELPER FUNCTION
# ============================================================================

def get_full_knowledge_base():
    """Retorna todo o knowledge base estruturado"""
    return {
        "version": "2.0",
        "projects": {
            "Pet.ON.Api": {
                "description": "Backend C# .NET 8",
                "structure": PET_ON_API_STRUCTURE,
                "entities": PET_ON_API_ENTITIES,
                "endpoints": PET_ON_API_ENDPOINTS,
                "path": "C:/Castanheira Holding/Pet.ON.Api",
            },
            "PetShop.WebApp": {
                "description": "Frontend Vue.js 3",
                "structure": PETSHOP_WEBAPP_STRUCTURE,
                "screens": PETSHOP_WEBAPP_SCREENS,
                "path": "C:/Castanheira Holding/petshop-webapp",
            },
            "Pet.ON.App": {
                "description": "Mobile React Native",
                "structure": PET_ON_APP_STRUCTURE,
                "screens": PET_ON_APP_SCREENS,
                "path": "C:/Castanheira Holding/pet-on-app",
            },
        },
        "core_features": CORE_FEATURES,
        "architecture_patterns": ARCHITECTURE_PATTERNS,
    }


def get_context_for_agent(agent_type: str) -> str:
    """
    Retorna contexto específico para cada tipo de agente
    
    Args:
        agent_type: 'planner', 'developer', 'qa'
    
    Returns:
        String com contexto formatado
    """
    kb = get_full_knowledge_base()
    
    if agent_type == "planner":
        return format_planner_context(kb)
    elif agent_type == "developer":
        return format_developer_context(kb)
    else:  # qa
        return format_qa_context(kb)


def format_planner_context(kb) -> str:
    """Contexto para Planner Agent"""
    context = "# CONTEXTO DE PROJETO PARA PLANNER\n\n"
    context += "## ESTRUTURA DOS PROJETOS\n\n"
    
    for project_name, project_info in kb["projects"].items():
        context += f"### {project_name}\n"
        context += f"{project_info['description']}\n\n"
        context += "**Estrutura de Pastas:**\n"
        for folder, desc in project_info.get("structure", {}).items():
            context += f"- `{folder}`: {desc}\n"
        context += "\n"
    
    context += "## FUNCIONALIDADES CORE\n\n"
    for feature_name, feature_data in kb["core_features"].items():
        context += f"### {feature_name}\n"
        context += f"{feature_data['description']}\n"
        if "steps" in feature_data:
            context += "**Passos:** " + " → ".join(feature_data["steps"]) + "\n"
        context += "\n"
    
    return context


def format_developer_context(kb) -> str:
    """Contexto para Developer Agent"""
    context = "# CONTEXTO TÉCNICO DETALHADO PARA DEVELOPER\n\n"
    
    # Entidades e seus relacionamentos
    context += "## ENTIDADES DO BANCO DE DADOS\n\n"
    api_project = kb["projects"]["Pet.ON.Api"]
    for entity_name, entity_data in api_project["entities"].items():
        context += f"### {entity_name}\n"
        context += f"{entity_data['description']}\n"
        context += f"**Fields:** {', '.join(entity_data['fields'])}\n"
        context += f"**Relationships:** {', '.join(entity_data['relationships'])}\n\n"
    
    # Endpoints disponíveis
    context += "## APIs DISPONÍVEIS\n\n"
    for resource_name, endpoints in api_project["endpoints"].items():
        context += f"### {resource_name}\n"
        for ep in endpoints:
            context += f"- `{ep['method']} {ep['path']}` - {ep['description']}\n"
        context += "\n"
    
    # Screens do Web
    context += "## TELAS DO PETSHOP WEBAPP (Vue.js)\n\n"
    web_project = kb["projects"]["PetShop.WebApp"]
    for screen in web_project["screens"]:
        context += f"### {screen['name']} - `{screen['path']}`\n"
        context += f"{screen['description']}\n"
        context += f"**Componentes:** {', '.join(screen['components'])}\n\n"
    
    # Screens do Mobile
    context += "## TELAS DO PET.ON.APP (React Native)\n\n"
    mobile_project = kb["projects"]["Pet.ON.App"]
    for screen in mobile_project["screens"]:
        context += f"### {screen['name']}\n"
        context += f"{screen['description']}\n"
        if "components" in screen:
            context += f"**Componentes:** {', '.join(screen['components'])}\n"
        context += "\n"
    
    # Padrões arquiteturais
    context += "## PADRÕES ARQUITETURAIS A SEGUIR\n\n"
    for platform, patterns in kb["architecture_patterns"].items():
        context += f"### {platform}\n"
        for pattern_name, description in patterns.items():
            context += f"- **{pattern_name}:** {description}\n"
        context += "\n"
    
    return context


def format_qa_context(kb) -> str:
    """Contexto para QA Agent"""
    context = "# CONTEXTO DE TESTES PARA QA\n\n"
    
    context += "## FUNCIONALIDADES PRINCIPAIS A TESTAR\n\n"
    for feature_name, feature_data in kb["core_features"].items():
        context += f"### {feature_name}\n"
        context += f"{feature_data['description']}\n"
        
        context += "**Entidades Afetadas:** "
        context += ", ".join(feature_data["affected_entities"]) + "\n"
        
        context += "**APIs Envolvidas:**\n"
        for api in feature_data.get("apis", []):
            context += f"  - {api}\n"
        
        context += "**Telas Web:** "
        context += ", ".join(feature_data.get("affected_screens_web", [])) + "\n"
        
        context += "**Telas Mobile:** "
        context += ", ".join(feature_data.get("affected_screens_mobile", [])) + "\n"
        context += "\n"
    
    context += "## CHECKLIST DE QUALIDADE\n\n"
    context += """
- ✓ Validações de entrada (FluentValidation no backend)
- ✓ Tratamento de erros (try-catch, response padrão)
- ✓ Segurança (auth, CORS, validação)
- ✓ Performance (N+1 queries, caching)
- ✓ Relacionamentos (verified FK constraints)
- ✓ Edge cases (valores nulos, datas inválidas)
- ✓ Integração entre APIs e telas
- ✓ Testes unitários (services, repositories)
- ✓ Testes de integração (API endpoints)
"""
    
    return context


if __name__ == "__main__":
    # Teste do novo KB
    kb = get_full_knowledge_base()
    print("✅ Knowledge Base V2 carregado com sucesso!")
    print(f"   - Projetos: {len(kb['projects'])}")
    print(f"   - Funcionalidades: {len(kb['core_features'])}")
    print(f"   - Padrões: {len(kb['architecture_patterns'])}")
