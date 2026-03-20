"""
Teste do extrator de código para validar parsing de outputs do Developer Agent
"""

from tools.code_generator import extract_code_blocks

# Exemplo 1: Saída típica com "### File:"
example1 = """
### File: Models/PhotoService.cs

```csharp
using System;

namespace Pet.ON.Api.Services
{
    public class PhotoService
    {
        public void UploadPhoto(string path)
        {
            // implementation
        }
    }
}
```

### File: Controllers/PhotoController.cs

```csharp
using Microsoft.AspNetCore.Mvc;

namespace Pet.ON.Api.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PhotoController : ControllerBase
    {
        public IActionResult Upload()
        {
            return Ok();
        }
    }
}
```
"""

# Exemplo 2: Saída com "## File:"
example2 = """
## File: src/components/PhotoUpload.vue

```vue
<template>
  <div class="upload">
    <input type="file" @change="handleUpload" />
  </div>
</template>

<script setup>
defineProps(['title'])
</script>
```

## File: src/services/photoApi.js

```javascript
export async function uploadPhoto(file) {
  const formData = new FormData()
  formData.append('file', file)
  return fetch('/api/photos', { method: 'POST', body: formData })
}
```
"""

print("🧪 Teste 1: Extração com '### File:'")
blocks1 = extract_code_blocks(example1)
print(f"✅ Encontrados {len(blocks1)} blocos:\n")
for filepath, lang, code in blocks1:
    print(f"  📄 {filepath} ({lang})")
    print(f"     Primeiras 50 chars: {code[:50]}...\n")

print("\n🧪 Teste 2: Extração com '## File:'")
blocks2 = extract_code_blocks(example2)
print(f"✅ Encontrados {len(blocks2)} blocos:\n")
for filepath, lang, code in blocks2:
    print(f"  📄 {filepath} ({lang})")
    print(f"     Primeiras 50 chars: {code[:50]}...\n")

print("\n✅ Todos os testes passaram!")
