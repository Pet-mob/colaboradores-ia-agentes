# Demanda #49: Bug - Fotos dos Pets Repetidas

**Projeto:** Pet.ON.App  
**Tipo:** Bug  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Média

---

## 📋 Descrição

Há problema onde fotos de pets estão sendo repetidas ou exibidas de forma incorreta. Mesma foto aparece para múltiplos pets, ou foto antiga aparece mesmo após trocar.

### Impacto
- Confusão do usuário qual é o pet correto
- Problema de cache ou referência
- Dados inconsistentes

---

## 🎯 Critérios de Aceitação

- [ ] Cada pet exibe sua própria foto corretamente
- [ ] Trocar foto de um pet não afeta outros
- [ ] Cache não persiste foto antiga
- [ ] Foto atualiza imediatamente após upload
- [ ] Reset completo de cache functions corretamente
- [ ] Não há duplicação de fotos no servidor
- [ ] Foto certa exibe em todos as telas (perfil, agendamento, histórico)

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Dados dos Pets (`screens/DadosPets.js`)
- Componente `ExpoImageWithPlaceholder.js`
- Serviço de Cache de Imagens
- Store de Pets

### Possíveis Causas
- Cache global não diferencia por pet ID
- URL da imagem duplicada para múltiplos pets
- Component reuse sem key prop (React list rendering)
- Imagem em cache sem invalidação
- Referência incorreta no BD

### Debugging
```javascript
// Verificar se cada pet tem foto URL única
pets.map(pet => {
  console.log(`Pet ${pet.id}: ${pet.fotoUrl}`);
});

// Verificar se componente renderiza com key
{pets.map(pet => (
  <PetCard key={pet.id} pet={pet} /> // Importante: key={pet.id}
))}
```

### Cache Adequado
```javascript
// Cache por pet ID, não global
const cacheKey = `pet_${petId}_foto`;
const foto = await getCacheOuFetch(cacheKey, petId);

// Invalidar ao alterar
await clearCache(`pet_${petId}_foto`);
```

---

## 📊 Estimativa

- **Esforço:** Médio (1-2 dias)
- **Complexidade:** Média
- **Prioridade:** Média

---

## 🔗 Dependências

- Sistema de fotos implementado

---

## 📝 Checklist de Resolução

- [ ] Reproduzir bug (qual pet específico?)
- [ ] Verificar URLs no BD
- [ ] Checar implementação de cache
- [ ] Validar key props em listas
- [ ] Testar update de foto
- [ ] Validar em diferentes telas
- [ ] Limpar cache durante testes
