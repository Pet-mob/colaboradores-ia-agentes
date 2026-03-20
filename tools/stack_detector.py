"""
Stack Detection System
====================

Detecta qual technology stack deve ser alterado em cada demanda.
Evita misturar API, Frontend e Mobile em um mesmo processamento.

Restrições:
- Uma demanda pode afetar múltiplos projetos
- MAS os agents devem gerar código correto para CADA stack específico
- NÃO misturar Entity Framework com Dapper
- Cada repositório tem suas próprias convenções
"""

from enum import Enum
from typing import List, Dict, Set
from pathlib import Path
from tools.database_knowledge_base import DATABASE_SCHEMA, STACK_CONSTRAINTS

class Stack(Enum):
    """Tecnologias/projetos que podem ser afetados"""
    BACKEND_API = "backend_api"  # Pet.ON.Api - .NET, Dapper
    FRONTEND_WEBAPP = "frontend_webapp"  # PetShop.WebApp - Vue.js 3
    MOBILE_APP = "mobile_app"  # Pet.ON.App - React Native


STACK_DETAILS = {
    Stack.BACKEND_API: {
        "name": "Backend API",
        "repo": "Pet.ON.Api",
        "language": "C#",
        "framework": ".NET 8",
        "orm": "Dapper",
        "paths": ["Pet.ON.Api/", "Pet.ON.Domain/", "Pet.ON.Infra/", "Pet.ON.Application/"],
        "forbidden_patterns": ["Entity Framework", "_context", "DbContext", "DbSet"],
        "keywords": ["repository", "service", "controller", "api", "endpoint", "database", "sql", "dapper", "usuário", "animal", "agendamento", "empresa"],
    },
    Stack.FRONTEND_WEBAPP: {
        "name": "Frontend Webapp",
        "repo": "petshop-webapp",
        "language": "TypeScript/Vue.js",
        "framework": "Vue 3 + Pinia",
        "paths": ["src/", "components/", "views/", "stores/"],
        "keywords": ["component", "vue", "pinia", "store", "page", "frontend", "view", "tela", "interface"],
    },
    Stack.MOBILE_APP: {
        "name": "Mobile App",
        "repo": "pet-on-app",
        "language": "JavaScript",
        "framework": "React Native",
        "paths": ["src/", "screens/", "components/", "reducers/"],
        "keywords": ["screen", "native", "react", "mobile", "app", "tela", "aplicativo"],
    }
}


def detect_stacks_from_demand(demand_text: str, project_name: str) -> Dict[Stack, float]:
    """
    Detecta qual(is) stacks serão afetados baseado no texto da demanda.
    
    Retorna um dict com scores 0.0 a 1.0 para cada stack.
    Score > 0.6 = alto indício de que o stack será afetado.
    
    Args:
        demand_text: Conteúdo completo da demanda markdown
        project_name: Nome do projeto (pode vir do campo "Projeto:" da demanda)
    
    Returns:
        {"backend_api": 0.85, "frontend_webapp": 0.3, "mobile_app": 0.2}
    """
    
    demand_lower = demand_text.lower()
    project_lower = project_name.lower() if project_name else ""
    
    scores = {stack: 0.0 for stack in Stack}
    
    # Análise por projeto mencionado
    if "pet.on.api" in project_lower or "backend" in project_lower or "api" in project_lower:
        scores[Stack.BACKEND_API] += 0.8
    elif "petshop.webapp" in project_lower or "frontend" in project_lower or "web" in project_lower:
        scores[Stack.FRONTEND_WEBAPP] += 0.8
    elif "pet.on.app" in project_lower or "mobile" in project_lower or "app" in project_lower:
        scores[Stack.MOBILE_APP] += 0.8
    
    # Análise por keywords na descrição
    for stack, details in STACK_DETAILS.items():
        for keyword in details["keywords"]:
            if keyword in demand_lower:
                scores[stack] += 0.15
    
    # Análise por padrões de código mencionados
    if "repositório" in demand_lower or "banco" in demand_lower or "database" in demand_lower:
        scores[Stack.BACKEND_API] = min(1.0, scores[Stack.BACKEND_API] + 0.3)
    
    if "componente" in demand_lower or "tela" in demand_lower or "página" in demand_lower:
        scores[Stack.FRONTEND_WEBAPP] = min(1.0, scores[Stack.FRONTEND_WEBAPP] + 0.25)
        scores[Stack.MOBILE_APP] = min(1.0, scores[Stack.MOBILE_APP] + 0.25)
    
    if "agendamento" in demand_lower or "serviço" in demand_lower or "usuário" in demand_lower:
        # Essas são funcionalidades que podem tocar API
        scores[Stack.BACKEND_API] = min(1.0, scores[Stack.BACKEND_API] + 0.2)
    
    # Normalizar scores para 0-1
    for stack in scores:
        scores[stack] = min(1.0, max(0.0, scores[stack]))
    
    return scores


def get_primary_stack(scores: Dict[Stack, float]) -> Stack:
    """
    Retorna o stack primário (maior score) com threshold mínimo de 0.3.
    Se nenhum atinge 0.3, retorna o com maior score.
    """
    valid_stacks = {s: score for s, score in scores.items() if score >= 0.3}
    
    if not valid_stacks:
        # Fallback: retorna o com maior score
        return max(scores.items(), key=lambda x: x[1])[0]
    
    return max(valid_stacks.items(), key=lambda x: x[1])[0]


def get_affected_stacks(scores: Dict[Stack, float], threshold: float = 0.5) -> List[Stack]:
    """
    Retorna lista de stacks que serão afetados (score >= threshold).
    
    Padrão: threshold=0.5 (mínimo moderado de confiança)
    """
    return [stack for stack, score in scores.items() if score >= threshold]


def get_stack_appropriate_context(stack: Stack) -> str:
    """
    Retorna contexto técnico apropriado para o stack específico.
    
    Para Backend: Inclui Dapper patterns, DB schema, retry logic
    Para Frontend: Inclui Vue/Pinia patterns
    Para Mobile: Inclui React Native patterns
    """
    
    if stack == Stack.BACKEND_API:
        from tools.database_knowledge_base import get_database_context_for_developer
        return get_database_context_for_developer()
    
    elif stack == Stack.FRONTEND_WEBAPP:
        return """
## Frontend: Vue.js 3 + Pinia

### Padrão de Componente
```vue
<script setup lang="ts">
import { ref } from 'vue'
import { usePetShopStore } from '@/stores/petshop'

const store = usePetShopStore()
const data = ref([])

const handleAction = async () => {
  data.value = await store.fetchResources()
}
</script>

<template>
  <div>
    <h1>Title</h1>
    <button @click="handleAction">Action</button>
  </div>
</template>
```

### Pinia Store (State Management)
```typescript
import { defineStore } from 'pinia'

export const usePetShopStore = defineStore('petshop', () => {
  const state = ref([])
  
  const fetchResources = async () => {
    const response = await fetch('/api/...')
    return response.json()
  }
  
  return { state, fetchResources }
})
```

### Estrutura de Pastas
- src/components/ - Componentes reutilizáveis
- src/views/ - Páginas completas
- src/stores/ - Pinia stores
- src/services/ - HTTP calls
- src/types/ - TypeScript interfaces

### NÃO FAZER
❌ Entity Framework queries no frontend
❌ Direct SQL no frontend
❌ Compartilhar estado sem Pinia
"""
    
    elif stack == Stack.MOBILE_APP:
        return """
## Mobile: React Native

### Padrão de Screen
```javascript
import React, { useState } from 'react'
import { View, Text, Button } from 'react-native'
import { useDispatch } from 'react-redux'

const ScreenName = ({ route }) => {
  const [data, setData] = useState([])
  const dispatch = useDispatch()
  
  const handleAction = () => {
    // Lógica aqui
  }
  
  return (
    <View>
      <Text>Title</Text>
      <Button title="Action" onPress={handleAction} />
    </View>
  )
}

export default ScreenName
```

### Redux Pattern
```javascript
// reducer
const initialState = { items: [] }

export const itemReducer = (state = initialState, action) => {
  switch(action.type) {
    case 'SET_ITEMS':
      return { ...state, items: action.payload }
    default:
      return state
  }
}

// dispatch
dispatch({ type: 'SET_ITEMS', payload: data })
```

### Estrutura de Pastas
- src/screens/ - Telas completas
- src/components/ - Componentes reutilizáveis
- src/redux/ - Reducers e actions
- src/services/ - HTTP API calls
- src/styles/ - StyleSheet

### NÃO FAZER
❌ Queries do banco no mobile
❌ Lógica de negócio pesada no componente
❌ State management sem Redux
"""
    
    return "Unknown stack"


def get_validation_instructions(stacks_affected: List[Stack]) -> str:
    """
    Retorna instruções de validação para não misturar stacks.
    """
    
    instruction = "## ⚠️ ATENÇÃO: Múltiplos Stacks Afetados\n\n"
    
    if len(stacks_affected) == 1:
        instruction = f"## Stack Único Afetado\n\n"
        instruction += f"Apenas **{STACK_DETAILS[stacks_affected[0]]['name']}** será alterado.\n\n"
        return instruction
    
    instruction += f"Esta demanda afeta **{len(stacks_affected)}** stacks diferentes:\n\n"
    
    for stack in stacks_affected:
        details = STACK_DETAILS[stack]
        instruction += f"- **{details['name']}** ({details['language']}, {details['framework']})\n"
    
    instruction += """
### Restrições:
1. ✅ GERAR código correto para CADA stack conforme suas convenções
2. ✅ API: Use Dapper, NÃO Entity Framework
3. ✅ Frontend: Use Vue/Pinia, NÃO estado local avulso
4. ✅ Mobile: Use React Native Redux, NÃO lógica no componente
5. ❌ NUNCA misture tecnologias (Entity Framework em Dapper, etc)
6. ❌ NUNCA gere código para stack não mencionado

### Formato:
Cada arquivo deve começar com:
# File: src/path/to/file.ext
```language
// código aqui
```

Que será interpretado APENAS para o repositório correto.
"""
    
    return instruction


# ============================================================================
# EXPORTAR FUNÇÕES PÚBLICAS
# ============================================================================

__all__ = [
    'Stack',
    'detect_stacks_from_demand',
    'get_primary_stack',
    'get_affected_stacks',
    'get_stack_appropriate_context',
    'get_validation_instructions',
]
