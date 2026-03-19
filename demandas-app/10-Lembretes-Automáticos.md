# Demanda #10: Lembretes Automáticos

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** To Do  
**Tags:** app, v1  
**Versão:** v1

---

## 📋 Descrição

Implementar sistema de lembretes automáticos para agendamentos futuros. O aplicativo deve notificar o usuário em momentos estratégicos (ex: 24h antes, 1h antes) sobre seus agendamentos marcados para melhorar taxa de comparecimento.

### Objetivo
- Reduzir taxa de no-shows
- Melhorar experiência do usuário com lembretes periódicos
- Aumentar fidelidade com petshops
- Engajar usuário ao manter agendamentos em mente

---

## 🎯 Critérios de Aceitação

- [ ] Notificação push 24 horas antes do agendamento
- [ ] Notificação push 1 hora antes do agendamento
- [ ] Lembretes configuráveis por usuário (decidir quais receber)
- [ ] Notificação contém: data, hora, nome do petshop, serviço agendado
- [ ] Link na notificação para abrir detalhes do agendamento
- [ ] Desativar lembretes quando agendamento é cancelado
- [ ] Suportar múltiplos agendamentos simultâneos
- [ ] Funciona mesmo com app fechado

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Notificação Toast (`components/notificacaoToastCustomizado.js`)
- Serviço de Notificações (novo)
- Tela de Agendamento (`screens/Agendamento.js`)
- Store de Notificações (novo)

### Tecnologias
- Expo Notifications ou similar para push notifications
- Background Task Scheduler
- AsyncStorage para persistir preferências

### Fluxo de Implementação
1. Ao criar agendamento, salvar timestamps de lembretes
2. Usar background job para verificar agendamentos próximos
3. Dispara notificação push via serviço de notificações
4. Usuário recebe notificação com opções para confirmar/descartar

### Estrutura de Dados
```json
{
  "agendamento": {
    "id": "123",
    "dataAgendamento": "2026-03-25T14:00:00",
    "lembretes": [
      {
        "tipo": "24h_antes",
        "dataAgendamento": "2026-03-24T14:00:00",
        "enviado": false
      },
      {
        "tipo": "1h_antes",
        "dataAgendamento": "2026-03-25T13:00:00",
        "enviado": false
      }
    ]
  }
}
```

---

## 📊 Estimativa

- **Esforço:** Grande (5-8 dias)
- **Complexidade:** Alta
- **Prioridade:** Alta (v1)

---

## 🔗 Dependências

- Sistema de agendamentos implementado
- Permissões de notificação configuradas
- Backend para gerenciar fila de notificações

---

## 📝 Notas de Implementação

- Usar background tasks para garantir notificações em tempo certo
- Testar em diferentes devices (iOS/Android)
- Implementar rate limiting para não sobrecarregar com notificações
- Considerar timezone do usuário

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._