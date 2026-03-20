"""
DETAILED PROJECT CONTEXT
Contexto SUPER EXPANDIDO dos projetos Petmob com estrutura, endpoints, componentes, telas, etc
"""

# ==================================================================================
# PET.ON.API - BACKEND .NET
# ==================================================================================

PETAPI_STRUCTURE = {
    "project": "Pet.ON.Api",
    "path": "C:\\Castanheira Holding\\Pet.ON.Api",
    "stack": ".NET 8, C#, Entity Framework Core, SQL Server",
    "base_url": "https://api.petmob.com.br/api",
    "dev_url": "https://dev-api.petmob.com.br/api",
    
    "folder_structure": {
        "src/": {
            "Controllers/": {
                "description": "Endpoints REST da API",
                "pattern": "[EntityName]Controller : ControllerBase",
                "files": [
                    "ServiceController.cs - GET/POST/PUT/DELETE serviços",
                    # Esperados: UsersController, PetsController, PetshopsController, 
                    # AppointmentsController, ReviewsController, etc
                ]
            },
            "Models/": {
                "description": "Entidades do banco de dados",
                "pattern": "Herda de BaseEntity (Id, CreatedAt, UpdatedAt)",
                "files": [
                    "Service.cs - Serviço oferecido por uma petshop",
                    "SubService.cs - Subserviço (variações de um serviço)",
                    # Esperados: User, Pet, Petshop, Appointment, Review, Address, etc
                ]
            },
            "ViewModels/": {
                "description": "DTOs para requisições/respostas",
                "pattern": "[Entity]ViewModel, [Entity]CreateModel, [Entity]UpdateModel",
                "files": [
                    "ServiceViewModel.cs - Retorno de serviço",
                    "ServiceCreateModel.cs - Criar serviço",
                    "ServiceUpdateModel.cs - Atualizar serviço",
                ]
            },
            "Services/": {
                "description": "Lógica de negócio",
                "pattern": "IServiceName : Service, ServiceName(IRepository, IMapper, IValidator)",
                "files": [
                    "ServiceService.cs - Lógica de serviços",
                    # Esperados: UserService, PetService, AppointmentService, etc
                ]
            },
            "Repositories/": {
                "description": "Acesso a dados",
                "pattern": "IRepository<T>, Repository<T> : IRepository<T>",
                "files": [
                    "ServiceRepository.cs - CRUD de serviços",
                    # Esperados: UserRepository, PetRepository, etc
                ]
            },
            "Database/": {
                "description": "Configuração do EF Core",
                "files": [
                    "PetmobDbContext.cs - DbContext principal",
                    "Configuration/*.cs - ModelBuilder configs",
                ]
            },
        }
    },
    
    "key_endpoints": {
        "Services": {
            "GET /api/services": "Listar todos os serviços",
            "GET /api/services/{id}": "Detalhe de um serviço",
            "POST /api/services": "Criar novo serviço",
            "PUT /api/services/{id}": "Atualizar serviço",
            "DELETE /api/services/{id}": "Deletar serviço",
            "GET /api/services/search?q=...": "Buscar serviços por nome",
        },
        # Esperados endpoints para:
        "Users": {
            "POST /api/users/register": "Registrar novo usuário",
            "POST /api/users/login": "Login (retorna JWT)",
            "GET /api/users/{id}": "Dados do usuário",
            "PUT /api/users/{id}": "Atualizar perfil",
        },
        "Pets": {
            "GET /api/users/{userId}/pets": "Listar pets de um usuário",
            "POST /api/pets": "Criar novo pet",
            "PUT /api/pets/{id}": "Atualizar dados do pet",
            "DELETE /api/pets/{id}": "Deletar pet",
        },
        "Petshops": {
            "GET /api/petshops": "Listar todas as petshops",
            "GET /api/petshops/{id}": "Detalhe de uma petshop",
            "GET /api/petshops/search?lat=X&lng=Y&radius=5km": "Buscar por geolocation",
            "GET /api/petshops/{id}/services": "Serviços dessa petshop",
            "GET /api/petshops/{id}/availability": "Horários disponíveis",
        },
        "Appointments": {
            "GET /api/appointments": "Meus agendamentos",
            "POST /api/appointments": "Agendar novo serviço",
            "PUT /api/appointments/{id}": "Alterar agendamento",
            "DELETE /api/appointments/{id}": "Cancelar agendamento",
            "GET /api/appointments/{id}/status": "Status do agendamento",
        },
    },
    
    "models_database": {
        "Service": {
            "fields": ["Id", "Name", "Description", "Price", "PetShopId", "Duration", "IsActive"],
            "relationships": ["PetShop", "SubServices", "Appointments"],
        },
        "SubService": {
            "fields": ["Id", "ServiceId", "Name", "VariationType", "Price"],
            "relationships": ["Service"],
        },
        # Esperados:
        "User": {
            "fields": ["Id", "Email", "Phone", "FullName", "CPF", "DateOfBirth", "ProfilePicture", "CreatedAt", "UpdatedAt"],
            "relationships": ["Pets", "Addresses", "Appointments", "Reviews"],
        },
        "Pet": {
            "fields": ["Id", "UserId", "Name", "Type", "Breed", "Weight", "DateOfBirth", "Photo"],
            "relationships": ["User", "Appointments"],
        },
        "Petshop": {
            "fields": ["Id", "Name", "CNPJ", "Rating", "Address", "Phone", "Email", "Logo", "OpeningHours"],
            "relationships": ["Services", "Appointments", "Reviews"],
        },
        "Appointment": {
            "fields": ["Id", "UserId", "PetShopId", "PetId", "ServiceId", "ScheduledDate", "Status", "Notes"],
            "relationships": ["User", "Pet", "Petshop", "Service"],
        },
    },
    
    "validation_rules": {
        "Service": [
            "Name: required, max 100 chars",
            "Price: required, decimal, > 0",
            "Duration: required, min 15 mins",
        ],
        "User": [
            "Email: required, valid email",
            "Phone: required, valid Brazilian format",
            "CPF: required, valid Brazilian CPF",
            "Password: min 8 chars, 1 uppercase, 1 number, 1 special char",
        ],
        "Pet": [
            "Name: required, max 50 chars",
            "Type: required (Dog/Cat/Other)",
            "Weight: required, decimal > 0",
        ],
        "Appointment": [
            "ScheduledDate: must be future, within petshop opening hours",
            "PetId: must belong to logged user",
            "Validation: check service availability at that time",
        ],
    },
    
    "common_patterns": [
        "Async/await for all I/O operations",
        "FluentValidation for input validation",
        "AutoMapper for DTO mapping",
        "Dependency Injection (IServiceCollection.AddScoped)",
        "Repository pattern for data access",
        "Service layer for business logic",
        "JWT Bearer token for authentication",
        "CORS enabled for frontend/mobile",
        "Exception handling middleware",
        "Logging with Serilog",
    ],
}

# ==================================================================================
# PETSHOP.WEBAPP - VUE.JS FRONTEND
# ==================================================================================

PETSHOPWEBAPP_STRUCTURE = {
    "project": "PetShop.WebApp",
    "path": "C:\\Castanheira Holding\\PetShop.WebApp\\petshop",
    "stack": "Vue.js 3, JavaScript/TypeScript, Pinia (state), TailwindCSS",
    "deployed_url": "https://petshop.petmob.com.br",
    "dev_url": "http://localhost:5173",
    
    "folder_structure": {
        "src/": {
            "components/": {
                "description": "Componentes reutilizáveis",
                "pattern": "[ComponentName].vue",
                "examples": [
                    "Button.vue - Botão genérico",
                    "Modal.vue - Modal/dialog",
                    "ServiceCard.vue - Card de serviço",
                    "PetshopCard.vue - Card de petshop",
                    "LoadingSpinner.vue - Loader",
                    "Header/NavBar.vue - Navegação",
                ]
            },
            "pages/": {
                "description": "Páginas da aplicação (views principais)",
                "examples": [
                    "Dashboard.vue - Home da petshop",
                    "Services.vue - Gerenciar serviços",
                    "Appointments.vue - Ver agendamentos",
                    "Settings.vue - Configurações da loja",
                    "Analytics.vue - Relatórios e estatísticas",
                ]
            },
            "views/": {
                "description": "Estrutura de telas",
                "examples": [
                    "Layout/Default.vue - Layout padrão",
                    "Layout/Empty.vue - Layout sem sidebar",
                ]
            },
            "router/": {
                "description": "Configuração de rotas",
                "files": ["index.ts", "routes.ts"],
                "key_routes": [
                    "/dashboard - Home",
                    "/services - Gerenciar serviços",
                    "/appointments - Agendamentos",
                    "/analytics - Relatórios",
                    "/settings - Configurações",
                    "/login - Login",
                ]
            },
            "store/": {
                "description": "Pinia store (state management)",
                "pattern": "defineStore('[name]Store')",
                "modules": [
                    "authStore - Login, tokens, permissões",
                    "userStore - Dados do usuário logado",
                    "petshopStore - Dados da petshop",
                    "servicesStore - Serviços da petshop",
                    "appointmentsStore - Agendamentos",
                ]
            },
            "services/": {
                "description": "API clients (chamadas ao backend)",
                "pattern": "async function(params) → api.post/get/put/delete",
                "examples": [
                    "authService.ts - Login, tokens",
                    "servicesService.ts - CRUD de serviços",
                    "appointmentsService.ts - Gerenciar agendamentos",
                    "petshopService.ts - Dados da petshop",
                ]
            },
            "composables/": {
                "description": "Composables (lógica reutilizável)",
                "pattern": "export function useXxx() { return { ... } }",
                "examples": [
                    "useAuth.ts - Lógica de autenticação",
                    "useForm.ts - Validação de forms",
                    "usePagination.ts - Pagination",
                    "useNotification.ts - Toast/notificações",
                ]
            },
            "assets/": {
                "description": "Images, icons, fonts",
            },
            "style/": {
                "description": "CSS global, Tailwind config",
                "files": ["global.css", "variables.css"],
            },
            "ui/": {
                "description": "UI library/theme",
            },
            "utils/": {
                "description": "Funções utilitárias",
                "examples": [
                    "formatters.ts - Formatar datas, moeda, etc",
                    "validators.ts - Validações customizadas",
                    "constants.ts - Constantes da app",
                ],
            },
        }
    },
    
    "key_features": {
        "Dashboard": [
            "Cards com métricas (agendamentos today, receita, clientes)",
            "Gráfico de receita por dia/semana/mês",
            "Lista de próximos agendamentos",
            "Notificações de novos agendamentos",
        ],
        "Services Management": [
            "Listar, criar, editar, deletar serviços",
            "Definir preço, duração, descrição",
            "Criar variações (sub-serviços)",
            "Status ativo/inativo",
            "Fotos do serviço",
        ],
        "Appointments": [
            "Visualizar calendar com agendamentos",
            "Ver detalhes (cliente, pet, serviço, horário)",
            "Confirmar/cancelar agendamentos",
            "Marcar como realizado/não compareceu",
            "Notas para o serviço",
        ],
        "Settings": [
            "Dados da petshop (nome, telefone, endereço)",
            "Logo e fotos da loja",
            "Horário de funcionamento",
            "Dias/horários de indisponibilidade",
            "Gerenciar funcionários",
        ],
    },
    
    "components_used": [
        "Form inputs (text, email, phone, date, select, checkbox)",
        "Tables com paginação e ordenação",
        "Modal forms para CREATE/EDIT",
        "Calendar para agendamentos",
        "Charts para analytics",
        "Notifications/Toasts",
        "Loading spinners",
        "Breadcrumbs de navegação",
    ],
    
    "authentication": {
        "method": "JWT Bearer Token",
        "login_flow": "Email/Password → /api/users/login → JWT token armazenado em localStorage",
        "token_validation": "Token enviado em cada request no header Authorization: Bearer <token>",
    },
}

# ==================================================================================
# PET.ON.APP - REACT NATIVE MOBILE
# ==================================================================================

PETONAPP_STRUCTURE = {
    "project": "Pet.ON.App",
    "path": "C:\\Castanheira Holding\\Pet.ON.App",
    "stack": "React Native, JavaScript/TypeScript, Redux, Expo",
    "platforms": "iOS, Android",
    "target": "Usuários finais agendando serviços",
    
    "folder_structure": {
        "src/": {
            "screens/": {
                "description": "Telas principais da app",
                "pattern": "[ScreenName]Screen.js / [ScreenName].screen.ts",
                "screens": [
                    "HomeScreen - Busca petshops por localização",
                    "SearchScreen - Busca filtrada de petshops",
                    "PetshopDetailScreen - Detalhe da petshop + serviços",
                    "AppointmentScreen - Agendamento (wizard com passos)",
                    "ConfirmationScreen - Confirmação do agendamento",
                    "MyAppointmentsScreen - Histórico de agendamentos",
                    "MyPetsScreen - Gerenciar meus pets",
                    "ProfileScreen - Perfil do usuário",
                    "LoginScreen - Autenticação",
                    "RegisterScreen - Cadastro novo usuário",
                ]
            },
            "components/": {
                "description": "Componentes reutilizáveis",
                "examples": [
                    "Button.tsx - Botão customizado",
                    "Input.tsx - Input com validação",
                    "Card.tsx - Card genérico",
                    "PetshopCard.tsx - Card de petshop com rating",
                    "AppointmentCard.tsx - Card de agendamento",
                    "PetCard.tsx - Card de pet",
                    "LoadingOverlay.tsx - Loading overlay",
                    "BottomSheet.tsx - Bottom sheet modal",
                ]
            },
            "routes/": {
                "description": "Navegação (React Navigation)",
                "pattern": "Stack navigator, Tab navigator, Drawer navigator",
                "structure": [
                    "RootNavigator - Determina autenticado/não autenticado",
                    "AuthNavigator - Stack com Login, Register",
                    "MainNavigator - Tab bottom com Home, Appointments, Profile",
                    "HomeStack - Stack dentro da aba Home",
                ]
            },
            "store/": {
                "description": "Redux store",
                "modules": [
                    "authSlice - Login, tokens, usuário",
                    "petsSlice - Meus pets",
                    "appointmentsSlice - Meus agendamentos",
                    "petshopsSlice - Petshops (cache)",
                    "uiSlice - Loading, erros, notificações",
                ]
            },
            "Service/": {
                "description": "API clients",
                "files": [
                    "api.ts - Configuração axios/fetch",
                    "requests.ts - Função base de requisição",
                    "authService.ts - Login, registro",
                    "petshopsService.ts - Buscar petshops",
                    "appointmentsService.ts - Agendar, listar",
                    "petsService.ts - CRUD de pets",
                ]
            },
            "theme/": {
                "description": "Cores, fonts, estilos globais",
                "files": [
                    "colors.ts - Paleta de cores",
                    "typography.ts - Fontes e tamanhos",
                    "spacing.ts - Dimensões padrão",
                ]
            },
        }
    },
    
    "key_flows": {
        "Discovery": [
            "1. User abre app → HomeScreen",
            "2. Geolocation ativa → busca petshops próximas",
            "3. Lista mostra petshops com rating, distância, imagem",
            "4. Click em petshop → PetshopDetailScreen",
            "5. Mostra serviços disponíveis + horários",
        ],
        "Scheduling": [
            "1. Choose pet → AppointmentScreen (wizard)",
            "2. Choose serviço",
            "3. Choose data/hora (select disponíveis)",
            "4. Adicionar notas (opcional)",
            "5. Confirmar → ConfirmationScreen",
            "6. Notificação de agendamento realizado",
        ],
        "Profile": [
            "1. MyPetsScreen - Adicionar, editar, deletar pets",
            "2. MyAppointmentsScreen - Ver histórico, cancelar",
            "3. ProfileScreen - Editar dados pessoais",
        ],
    },
    
    "key_features": {
        "Geolocation": "Buscar petshops próximas (raio configurável)",
        "Ratings": "Ver avaliações de clientes",
        "Real-time availability": "Horários disponíveis em tempo real",
        "Photo Gallery": "Ver fotos da petshop e resultados",
        "Favorites": "Marcar petshops favoritas",
        "Reviews": "Avaliar serviço após conclusão",
        "Push Notifications": "Notificar quando agendamento é confirmado",
        "Offline Support": "Cache de dados críticos (AsyncStorage)",
    },
    
    "native_integrations": [
        "Geolocation API - GPS do celular",
        "Camera/Photo Library - Fotos de pets e petshops",
        "AsyncStorage - Cache local de dados",
        "Notifications - Push notifications",
        "Maps - Mostrar petshops no mapa",
    ],
}

# ==================================================================================
# SHARED/CROSS-PROJECT PATTERNS
# ==================================================================================

SHARED_PATTERNS = {
    "authentication": {
        "mechanism": "JWT Bearer Token",
        "token_structure": "Header.Payload.Signature",
        "token_claims": ["sub (userId)", "email", "iat (issued at)", "exp (expiration)"],
        "refresh_token": "Refresh token para renovar JWT",
    },
    
    "error_handling": {
        "http_codes": {
            "200": "OK - Sucesso",
            "201": "Created - Recurso criado",
            "400": "Bad Request - Erro de validação",
            "401": "Unauthorized - Não autenticado",
            "403": "Forbidden - Não autorizado",
            "404": "Not Found - Recurso não existe",
            "500": "Internal Server Error - Erro interno",
        },
        "error_response": {
            "structure": "{ status: 'error', message: '...', errors: {} }",
        }
    },
    
    "data_formats": {
        "dates": "ISO 8601 (2024-03-20T15:30:00Z)",
        "decimals": "String ou Decimal com separador '.' (1.50 para R$1,50)",
        "phone": "+55 (11) 98765-4321",
        "currency": "BRL",
    },
    
    "business_rules": [
        "Service duration mínimo 15 minutos",
        "Appointment deve ser agendado com antecedência mínima",
        "Petshop não pode ter agendamentos sobrepostos para mesmo pet",
        "User não pode agendar fora do horário de funcionamento",
        "Cancelamento com 24h antes = reembolso total",
        "Dados sensíveis (pet, user) devem estar LGPD compliant",
    ],
}

# ==================================================================================
# ENVIRONMENT CONFIGURATIONS
# ==================================================================================

ENVIRONMENTS = {
    "development": {
        "api_base_url": "http://localhost:5000/api",
        "webapp_url": "http://localhost:5173",
        "app_api_url": "http://localhost:5000/api",
        "debug": True,
        "logging": "verbose",
    },
    "staging": {
        "api_base_url": "https://dev-api.petmob.com.br/api",
        "webapp_url": "https://dev-petshop.petmob.com.br",
        "app_api_url": "https://dev-api.petmob.com.br/api",
        "debug": True,
    },
    "production": {
        "api_base_url": "https://api.petmob.com.br/api",
        "webapp_url": "https://petshop.petmob.com.br",
        "app_api_url": "https://api.petmob.com.br/api",
        "debug": False,
    },
}

# ==================================================================================
# MAIN FUNCTION - GET DETAILED CONTEXT
# ==================================================================================

def get_full_project_context_for_agents(agent_type: str = None) -> str:
    """
    Retorna contexto SUPER EXPANDIDO para os agents
    
    Args:
        agent_type: 'planner', 'developer', 'qa', ou None (todos)
    
    Returns:
        String com contexto completo formatado
    """
    context = f"""
╭─────────────────────────────────────────────────────────────────╮
│         CONTEXTO DETALHADO - ECOSYSTEM PETMOB                   │
╰─────────────────────────────────────────────────────────────────╯

## ESTRUTURA GERAL
- 3 Projetos principales: Backend API, Frontend Web, Mobile App
- Localização: C:\\Castanheira Holding\\
- Stack: .NET 8 (backend), Vue.js (frontend), React Native (mobile)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 1️⃣  PET.ON.API (.NET Backend)
Path: {PETAPI_STRUCTURE['path']}

### Estrutura de Pastas
{format_dict_pretty(PETAPI_STRUCTURE['folder_structure'])}

### Principais Endpoints
{format_dict_pretty(PETAPI_STRUCTURE['key_endpoints'])}

### Models do Banco
{format_dict_pretty(PETAPI_STRUCTURE['models_database'])}

### Regras de Validação
{format_dict_pretty(PETAPI_STRUCTURE['validation_rules'])}

### Padrões Comuns
- {chr(10).join(['- ' + p for p in PETAPI_STRUCTURE['common_patterns']])}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 2️⃣  PETSHOP.WEBAPP (Vue.js Frontend)
Path: {PETSHOPWEBAPP_STRUCTURE['path']}
URL: {PETSHOPWEBAPP_STRUCTURE['deployed_url']}

### Estrutura de Pastas
{format_dict_pretty(PETSHOPWEBAPP_STRUCTURE['folder_structure'])}

### Funcionalidades Principais
{format_dict_pretty(PETSHOPWEBAPP_STRUCTURE['key_features'])}

### Rotas
{chr(10).join(['- ' + r for r in PETSHOPWEBAPP_STRUCTURE['router']['key_routes']])}

### Componentes Base
{chr(10).join(['- ' + c for c in PETSHOPWEBAPP_STRUCTURE['components_used']])}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 3️⃣  PET.ON.APP (React Native Mobile)
Path: {PETONAPP_STRUCTURE['path']}
Platforms: {', '.join(PETONAPP_STRUCTURE['platforms'])}

### Telas Principais
{chr(10).join(['- ' + s for s in PETONAPP_STRUCTURE['folder_structure']['src/']['screens/']['screens']])}

### Fluxos Principais
{format_dict_pretty(PETONAPP_STRUCTURE['key_flows'])}

### Funcionalidades
{format_dict_pretty(PETONAPP_STRUCTURE['key_features'])}

### Integrações Nativas
{chr(10).join(['- ' + i for i in PETONAPP_STRUCTURE['native_integrations']])}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🔐 PADRÕES COMPARTILHADOS

### Autenticação
{format_dict_pretty(SHARED_PATTERNS['authentication'])}

### Tratamento de Erros
{format_dict_pretty(SHARED_PATTERNS['error_handling'])}

### Formatos de Dados
{format_dict_pretty(SHARED_PATTERNS['data_formats'])}

### Regras de Negócio
{chr(10).join(['- ' + r for r in SHARED_PATTERNS['business_rules']])}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🌍 AMBIENTES

Development: {ENVIRONMENTS['development']['api_base_url']}
Staging: {ENVIRONMENTS['staging']['api_base_url']}
Production: {ENVIRONMENTS['production']['api_base_url']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return context


def format_dict_pretty(d, indent=0):
    """Helper para formatar dicts de forma legível"""
    lines = []
    for k, v in d.items():
        lines.append(" " * indent + f"**{k}**:")
        if isinstance(v, dict):
            lines.append(format_dict_pretty(v, indent + 2))
        elif isinstance(v, list):
            for item in v:
                lines.append(" " * (indent + 2) + f"- {item}")
        else:
            lines.append(" " * (indent + 2) + str(v))
    return "\n".join(lines)
