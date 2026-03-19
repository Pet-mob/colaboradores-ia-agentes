# Demanda #7: Lojas Favoritas (já utilizadas)

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** Doing  
**Tags:** app  

---

## 📋 Descrição

Implementar funcionalidade que permite aos usuários marcar petshops como favoritos baseado no histórico de utilização. O sistema deve exibir as lojas já utilizadas anteriormente de forma destacada/favorita, facilitando o acesso rápido a petshops que o usuário já conhece.

### Objetivo
- Melhorar UX permitindo acesso rápido a petshops já visitados
- Reduzir fricção no processo de agendamento
- Aumentar engajamento do usuário com lojas conhecidas

---

## 🎯 Critérios de Aceitação

- [ ] Usuário pode clicar em ícone de "coração/star" para marcar loja como favorita
- [ ] Lojas marcadas como favorita aparecem em uma seção dedicada
- [ ] Persistência de dados: favoritos são salvos no localStorage/BD
- [ ] Lojas já utilizadas são automaticamente sugeridas como favoritáveis
- [ ] Indicador visual claro (ícone preenchido/vazio) mostra status de favorito
- [ ] Possibilidade de remover de favoritos
- [ ] Funciona offline (dados locais)
- [ ] Sincroniza com servidor quando online

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Busca (`screens/Buscar.js`)
- Tela de Agendamento (`screens/Agendamento.js`)
- Componente de Card de Loja
- Store de estado (Redux/Context)

### Estrutura de Dados
```json
{
  "favoritos": [
    {
      "lojaId": "123",
      "nomeLoja": "Pet Shop ABC",
      "dataAdicionado": "2026-03-19",
      "ultimaUtilizacao": "2026-03-15"
    }
  ]
}
```

### APIs Necessárias
- GET `/api/lojas/historico` - Buscar lojas já utilizadas
- POST `/api/lojas/{id}/favoritar` - Adicionar favorito
- DELETE `/api/lojas/{id}/favoritar` - Remover favorito

---

## 📊 Estimativa

- **Esforço:** Médio (3-5 dias)
- **Complexidade:** Média
- **Prioridade:** Alta

---

## 🔗 Dependências

- Histórico de agendamentos deve estar implementado
- API de lojas deve retornar dados completos

---

## 📝 Notas Adicionais

- Ícone de favorito pode usar `react-native-vector-icons` ou similar
- Considerar debounce na sincronização com servidor
- Testar sincronização em diferentes estados de conectividade
