# Demanda #23: Função - Sugestões na Página Inicial

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** To Do  
**Tags:** app, v1  
**Versão:** v1

---

## 📋 Descrição

Implementar sistema de recomendação/sugestões inteligente na página inicial do aplicativo. O sistema deve sugerir petshops baseado em histórico de compras, localização, preferências do usuário e tendências populares para aumentar engajamento e conversão.

### Objetivo
- Aumentar descoberta de novos petshops
- Melhorar retenção com conteúdo relevante
- Aumentar taxa de conversão
- Personalizar experiência do usuário

---

## 🎯 Critérios de Aceitação

- [ ] Carrossel/seção de "Sugestões para você" na página inicial
- [ ] Sugestões baseadas em histórico de agendamentos
- [ ] Sugestões baseadas em localização (lojas próximas)
- [ ] Sugestões baseadas em serviços populares
- [ ] Diferentes algoritmos de recomendação
- [ ] Mínimo 5 sugestões por sessão
- [ ] Cache de sugestões (não fazer request a cada reload)
- [ ] Atualização de sugestões periódica
- [ ] Clique em sugestão leva a detalhes da loja

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela inicial/Dashboard
- Novo componente de Carrossel de Sugestões
- Serviço de Recomendações (novo)
- Store de Recomendações (novo)

### Algoritmos de Recomendação
1. **Baseado em Histórico**: Petshops similares aos já visitados
2. **Baseado em Localização**: Lojas próximas (usando geolocalização)
3. **Baseado em Serviços**: Serviços mais procurados
4. **Tendências**: Lojas top-rated ou mais visitadas
5. **Colaborativo**: Baseado em usuários similares

### APIs Necessárias
- GET `/api/sugestoes/para-voce`
- GET `/api/sugestoes/proximas`
- GET `/api/sugestoes/tendencias`
- POST `/api/sugestoes/feedback`

### Estrutura de Dados
```json
{
  "sugestoes": [
    {
      "lojaId": "123",
      "nomeLoja": "Pet Shop XYZ",
      "rating": 4.8,
      "distancia": 2.5,
      "servicoDestaque": "Banho e Tosa",
      "motivo": "Baseada em seu histórico",
      "imagem": "url"
    }
  ]
}
```

---

## 📊 Estimativa

- **Esforço:** Grande (5-7 dias)
- **Complexidade:** Alta
- **Prioridade:** Alta (v1)

---

## 🔗 Dependências

- Histórico de agendamentos implementado
- API de recomendações no backend
- Geolocalização funcionando
- Rating/feedback de lojas

---

## 📝 Notas de Implementação

- Usar algoritmo de cache para não fazer requests frequentes
- Implementar fallback se não tiver histórico
- Considerar ML/algoritmo mais sofisticado no futuro
- Testar com usuários novos (sem histórico)
- Implementar analytics para medir efetividade

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._