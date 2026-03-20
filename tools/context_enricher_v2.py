"""
Context Enricher V2 - Injeta contexto MASSIVO nos prompts dos agents
Usa o knowledge_base_v2.py para enriquecer 20-50x
"""

import re
from pathlib import Path
from typing import Tuple

try:
    from tools.project_knowledge_base_v2 import (
        get_context_for_agent,
        get_full_knowledge_base,
    )
except ImportError:
    print("⚠️ Aviso: project_knowledge_base_v2 não encontrado, usando fallback")
    
    def get_context_for_agent(agent_type: str) -> str:
        return f"Context for {agent_type}"
    
    def get_full_knowledge_base():
        return {}


def enrich_planner_prompt(
    original_prompt: str, demand_name: str = ""
) -> Tuple[str, dict]:
    """
    Enriquece prompt do Planner Agent com contexto de projeto
    """
    
    context = get_context_for_agent("planner")
    
    enriched = original_prompt + """

================================================================================
📚 CONTEXTO DO PROJETO - INFORMAÇÕES CRÍTICAS PARA PLANEJAMENTO
================================================================================

""" + context + """

================================================================================
⚠️ INSTRUÇÃO DE PLANEJAMENTO EXPANDIDA
================================================================================

1. **Mapear Entidades Afetadas** - User, Pet, PetShop, Service, Appointment, etc
2. **Identificar APIs Necessárias** - Quais endpoints usar?
3. **Planejar Telas Afetadas** - Web (Vue.js) e Mobile (React Native)
4. **Seguir Padrões** - Controller → Service → Repository
5. **Decompor em Tarefas Pequenas** - 1-2 horas cada
6. **Critérios de Aceite CONCRETOS** - comportamento esperado

================================================================================
"""
    
    stats = {
        "original_length": len(original_prompt),
        "enriched_length": len(enriched),
        "multiplier": round(len(enriched) / len(original_prompt), 1),
        "context_source": "knowledge_base_v2",
    }
    
    return enriched, stats


def enrich_developer_prompt(
    original_prompt: str, demand_name: str = "", stack: str = "backend"
) -> Tuple[str, dict]:
    """
    Enriquece prompt do Developer Agent com contexto técnico detalhado
    """
    
    context = get_context_for_agent("developer")
    stack_specific = _get_stack_specific_context(stack)
    
    enriched = original_prompt + """

================================================================================
🔧 CONTEXTO TÉCNICO DETALHADO PARA IMPLEMENTAÇÃO
================================================================================

""" + context + """
""" + stack_specific + """

================================================================================
📋 CHECKLIST DE CÓDIGO ESPERADO
================================================================================

FORMATO OBRIGATÓRIO para cada arquivo:

# File: src/path/to/FileName.ext
```language
// seu código aqui
```

✓ Imports/exports completos
✓ Tipo em TypeScript (interfaces, types)
✓ Tratamento de erro com try-catch
✓ Validações de entrada
✓ Seguir padrões (Controller → Service → Repository)
✓ Conectar com APIs existentes
✓ Comentários nas partes não óbvias

================================================================================
"""
    
    stats = {
        "original_length": len(original_prompt),
        "enriched_length": len(enriched),
        "multiplier": round(len(enriched) / len(original_prompt), 1),
        "stack": stack,
        "context_source": "knowledge_base_v2",
    }
    
    return enriched, stats


def enrich_qa_prompt(original_prompt: str, demand_name: str = "") -> Tuple[str, dict]:
    """
    Enriquece prompt do QA Agent com contexto de testes
    """
    
    context = get_context_for_agent("qa")
    
    enriched = original_prompt + """

================================================================================
🧪 CONTEXTO DE TESTES DETALHADO
================================================================================

""" + context + """

================================================================================
📊 MATRIZ DE TESTES ESPERADA
================================================================================

1. **Testes Funcionais** - Fluxo principal funciona corretamente
2. **Edge Cases** - Campos vazios/nulos, valores inválidos, duplicatas
3. **Validação** - Frontend + Backend FluentValidation
4. **Segurança** - Auth, Autorização, SQL Injection, CORS
5. **Performance** - N+1 queries, Caching, Paginação
6. **Integração** - Controller → Service → Repository
7. **Relacionamentos** - Cascata de delete, Soft delete, Integridade referencial

✅ APROVADO - 100% padrões, validações, testes, sem N+1
⚠️ RESSALVAS - 90%+ correto, pequenos problemas edge
❌ REPROVADO - Validações faltando, vulnerabilidades, N+1 críticas

================================================================================
"""
    
    stats = {
        "original_length": len(original_prompt),
        "enriched_length": len(enriched),
        "multiplier": round(len(enriched) / len(original_prompt), 1),
        "context_source": "knowledge_base_v2",
    }
    
    return enriched, stats


def _get_stack_specific_context(stack: str) -> str:
    """Retorna contexto específico por stack"""
    
    if stack.lower().startswith("backend") or stack.lower().startswith("pet.on.api"):
        return """
## BACKEND (.NET) - Padrão Controller/Service/Repository

```csharp
// Controller
[ApiController]
[Route("api/[controller]")]
public class ResourceController : ControllerBase
{
    private readonly IResourceService _service;
    public ResourceController(IResourceService service) => _service = service;
    
    [HttpGet]
    public async Task<ActionResult<IEnumerable<ResourceViewModel>>> GetAll()
    {
        var resources = await _service.GetAllAsync();
        return Ok(resources);
    }
}

// Service
public class ResourceService : IResourceService
{
    private readonly IResourceRepository _repository;
    public ResourceService(IResourceRepository repository) => _repository = repository;
    
    public async Task<IEnumerable<ResourceViewModel>> GetAllAsync()
    {
        return await _repository.GetAllAsync();
    }
}
```
"""
    
    elif stack.lower().startswith("frontend") or stack.lower().startswith("petshop.webapp"):
        return """
## FRONTEND (Vue.js 3) - Padrão Component/Store

```vue
<script setup lang="ts">
import { ref } from 'vue'
import { useStore } from '@/stores/mainStore'

const store = useStore()
const items = ref([])

const handleAction = async () => {
  items.value = await store.fetchResources()
}
</script>

<template>
  <div>
    <h1>Resources</h1>
    <button @click="handleAction">Load</button>
  </div>
</template>
```

Padrão Pinia Store: defineStore('name', () => { ... })
```
"""
    
    else:  # mobile
        return """
## MOBILE (React Native) - Padrão Screen/Redux

```typescript
import { FC, useEffect, useState } from 'react'
import { View, FlatList, StyleSheet } from 'react-native'
import { useAppSelector } from '@/store/hooks'

const ResourceListScreen: FC = () => {
  const resources = useAppSelector(state => state.resources.items)
  const [loading, setLoading] = useState(false)
  
  useEffect(() => {
    loadResources()
  }, [])
  
  const loadResources = async () => {
    setLoading(true)
    // fetch
    setLoading(false)
  }
  
  return (
    <View style={styles.container}>
      <FlatList data={resources} renderItem={({item}) => <Card item={item} />} />
    </View>
  )
}

const styles = StyleSheet.create({ container: { flex: 1 } })
export default ResourceListScreen
```
"""


def estimate_enrichment_size(prompt_length: int, agent_type: str) -> dict:
    """Estima o tamanho final do prompt enriquecido"""
    
    base_context_sizes = {
        "planner": 3500,
        "developer": 6500,
        "qa": 4500,
    }
    
    base_size = base_context_sizes.get(agent_type, 4500)
    enriched_size = prompt_length + base_size
    
    return {
        "original": prompt_length,
        "base_context": base_size,
        "total_enriched": enriched_size,
        "multiplier": round(enriched_size / prompt_length, 1),
        "context_percent": f"{round((base_size / enriched_size) * 100)}%",
    }


if __name__ == "__main__":
    print("✅ Context Enricher V2 carregado com sucesso!")
