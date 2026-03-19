# Demanda #34: Função - Integração de Fotos do Pet Shop

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Alta

---

## 📋 Descrição

Implementar integração que permite carregar e exibir fotos do pet shop (ambientes, pet groomers, facilidades) na tela de detalhes e busca. Fotos aumentam confiança e ajudam usuário a escolher melhor o petshop.

### Objetivo
- Aumentar confiança do usuário
- Melhorar decisão de compra
- Exibir qualidades (limpeza, profissionalismo)
- Aumentar conversão
- Diferenciar petshops

---

## 🎯 Critérios de Aceitação

- [ ] Upload de múltiplas fotos por petshop
- [ ] Fotos exibidas em galeria/carrossel
- [ ] Fotos aparecem na busca (destaque)
- [ ] Fotos aparecem em detalhes do petshop
- [ ] Otimização de imagem (compressão, cache)
- [ ] Loading placeholder enquanto carrega
- [ ] Modal/view de foto em tamanho maior
- [ ] Fallback se sem fotos (ícone padrão)
- [ ] Suporta JPEG, PNG, WebP
- [ ] Máximo de fotos: 10 por petshop
- [ ] Tamanho máximo: 5MB por foto

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Card de Petshop (busca)
- Tela de Detalhes do Petshop (novo/existente)
- Componente `ExpoImageWithPlaceholder.js` (melhorar)
- Galeria/Carrossel (novo elemento)
- Serviço de Upload
- Store de Petshops

### Upload de Imagem
- Usar Expo ImagePicker
- Validar tipo e tamanho
- Comprimir antes de enviá Endpoint: POST `/api/petshops/{id}/fotos`
- Retorna URL da imagem armazenada (AWS S3 ou similar)

### Exibição
```javascript
<Carrossel>
  {fotos.map(foto => (
    <GaleriaFoto 
      url={foto.url}
      onPress={() => abrirModalFoto(foto)}
    />
  ))}
</Carrossel>
```

### Estrutura de Dados
```json
{
  "petshop": {
    "id": "123",
    "fotos": [
      {
        "id": "f1",
        "url": "s3://bucket/petshop-123/foto1.jpg",
        "dataUpload": "2026-03-15",
        "ordem": 1
      }
    ]
  }
}
```

---

## 📊 Estimativa

- **Esforço:** Grande (4-5 dias)
- **Complexidade:** Média-Alta
- **Prioridade:** Alta

---

## 🔗 Dependências

- Storage em nuvem (AWS S3 ou similar)
- API de upload
- Detalhes do petshop renderizando

---

## 📝 Notas de Implementação

- Usar ExpoImagePicker para seleção
- Implementar compressão (ImageResizer ou similar)
- Cache local de imagens
- Tratamento de erros de upload
- UX agradável com preview

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._