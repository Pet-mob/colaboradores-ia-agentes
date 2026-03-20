#!/usr/bin/env python3
"""
Teste rápido do novo code_generator.py com padrão melhorado
"""
from tools.code_generator import extract_code_blocks

# Simula output do Developer Agent com o novo formato
dev_output = """
# File: src/Controllers/ShoppingController.cs
```csharp
[ApiController]
[Route("api/[controller]")]
public class ShoppingController : ControllerBase
{
    [HttpGet]
    public IActionResult GetCartItems()
    {
        return Ok(new { items = new[] { } });
    }
}
```

Documentation about the shopping feature.

# File: src/Services/CartService.cs
```csharp
public class CartService
{
    public async Task<Cart> GetCart(int userId)
    {
        return await _repository.GetCartAsync(userId);
    }
}
```

Some more explanation here.

```typescript
// Generate Vue component too
export default {
  name: 'ShoppingCart',
  data() {
    return { items: [] }
  }
}
```

"""

print("=" * 70)
print("Testando extract_code_blocks() melhorado")
print("=" * 70)

blocks = extract_code_blocks(dev_output)

print(f"\n[✓] Blocos extraídos: {len(blocks)}")
for i, (filepath, lang, code) in enumerate(blocks, 1):
    code_size = len(code)
    lines = code.count('\n')
    print(f"\n[{i}] Arquivo: {filepath}")
    print(f"    Linguagem: {lang}")
    print(f"    Tamanho: {code_size} chars, {lines} linhas")
    if len(code) > 100:
        print(f"    Preview (primeiras 100 chars): {code[:100]}...")

print("\n" + "=" * 70)
if len(blocks) == 3:
    print("✅ SUCESSO! 3 blocos de código extraídos corretamente")
else:
    print(f"❌ ERRO! Esperava 3 blocos, obteve {len(blocks)}")
print("=" * 70)
