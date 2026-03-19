# Demanda #28: Bug - Validação de Opções de Data/Horário

**Projeto:** Pet.ON.App  
**Tipo:** Bug  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Alta

---

## 📋 Descrição

Há problema na validação de datas e horários disponíveis para agendamento. O sistema pode estar permitindo seleção de datas passadas, horários já ocupados ou indisponíveis, causando erro ao confirmar agendamento.

### Impacto
- Usuários recebem erro após esperar para confirmar
- Péssima experiência
- Problemas de agendamentos inválidos no sistema

---

## 🎯 Critérios de Aceitação

- [ ] Não é possível selecionar datas passadas
- [ ] Data mínima é hoje ou amanhã (configurável)
- [ ] Horários indisponíveis são bloqueados visualmente
- [ ] Horários já agendados não aparecem
- [ ] Validação funciona de acordo com horário de funcionamento da loja
- [ ] Horários ocupados mostram indicador visual claro
- [ ] Ao confirmar, validação no backend confirma disponibilidade
- [ ] Mensagem de erro se horário já foi agendado por outro usuário
- [ ] Resposta da API retorna lista correta de horários disponíveis

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Agendamento (`screens/Agendamento.js`)
- Componente de Seletor de Data/Hora
- Serviço de Agendamentos
- Validação de Disponibilidade

### Validações Necessárias
```javascript
// Frontend
- Data >= hoje
- Hora >= agora (se for hoje)
- Hora funciona dentro horário da loja
- Horário já selecionado por outro usuário

// Backend
- Validação idêntica
- Verificação contra DB
```

### APIs Necessárias
- GET `/api/lojas/{id}/horarios-disponiveis?data=2026-03-25`
- POST `/api/agendamentos` (com validação de disponibilidade)

---

## 📊 Estimativa

- **Esforço:** Médio (2-3 dias)
- **Complexidade:** Média
- **Prioridade:** Alta

---

## 🔗 Dependências

- API de horários disponíveis
- Dados de funcionamento das lojas

---

## 📝 Checklist de Resolução

- [ ] Verificar lógica de validação de data
- [ ] Testar com datas passadas
- [ ] Testar com horários indisponíveis
- [ ] Verificar API retorna horários corretos
- [ ] Testar case de dupla reserva (race condition)
- [ ] Validar timezone/horário local
- [ ] Testar com diferentes lojas

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._