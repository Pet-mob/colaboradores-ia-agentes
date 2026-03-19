# Demanda #24: Função - Ordenação de Petshops

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** To Do  
**Tags:** app, v1  
**Versão:** v1

---

## 📋 Descrição

Implementar opções de ordenação na tela de busca de petshops. Usuários devem conseguir ordenar resultados por critérios como distância, avaliação, preço ou popularidade para encontrar facilmente o petshop ideal.

### Objetivo
- Melhorar UX da busca
- Facilitar descoberta de melhores opções
- Aumentar conversão
- Reduzir tempo de decisão

---

## 🎯 Critérios de Aceitação

- [ ] Seletor de ordenação visível na tela de busca
- [ ] Ordenação por distância (mais próximo primeiro)
- [ ] Ordenação por avaliação (melhor avaliado primeiro)
- [ ] Ordenação por preço (mais barato/caro)
- [ ] Ordenação por popularidade (mais visitado)
- [ ] Ordenação padrão configurable
- [ ] Seleção persiste durante sessão
- [ ] UI intuitiva com ícones/labels claros
- [ ] Ordenação funciona com filtros existentes

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Busca (`screens/Buscar.js`)
- Componente de Card de Loja
- Serviço de Lojas
- Store de Busca

### Ordenações Implementadas
```javascript
const sortOptions = [
  { id: 'distancia', label: 'Mais Próximo', field: 'distancia', order: 'asc' },
  { id: 'avaliacao', label: 'Melhor Avaliado', field: 'rating', order: 'desc' },
  { id: 'preco', label: 'Menos Caro', field: 'precoMedio', order: 'asc' },
  { id: 'popularidade', label: 'Mais Popular', field: 'numeroAgendamentos', order: 'desc' },
  { id: 'novo', label: 'Mais Recente', field: 'dataCadastro', order: 'desc' }
];
```

### Query Parameters
- GET `/api/lojas?ordem=distancia&direcao=asc`

---

## 📊 Estimativa

- **Esforço:** Médio (2-3 dias)
- **Complexidade:** Média
- **Prioridade:** Média (v1)

---

## 🔗 Dependências

- Tela de busca implementada
- Dados de distância, avaliação e preço disponíveis

---

## 📝 Notas de Implementação

- UI pode usar dropdown ou botões toggle
- Armazenar preferência no localStorage para próximas sessões
- Indicar qual ordenação está ativa
- Considerar performance com muitos resultados

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._