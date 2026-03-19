# Demanda #29: Ajuste - Formato de Horário

**Projeto:** Pet.ON.App  
**Tipo:** Ajuste/Bug  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Média

---

## 📋 Descrição

Ajustar formato de exibição de horários no aplicativo. Horários podem estar exibidos em formato 24h quando deveriam ser 12h (ou vice-versa), causando confusão ao usuário.

### Objetivo
- Padronizar exibição de horários em todo app
- Usar formato consistente com localidade brasileira
- Evitar confusão de usuários

---

## 🎯 Critérios de Aceitação

- [ ] Horários exibidos em formato 24h (conforme padrão brasileiro)
- [ ] Formato consistente em todas as telas
- [ ] Telas afetadas: Agendamento, Consulta, Histórico, Confirmação
- [ ] Toast/notificações usam mesmo formato
- [ ] Email/SMS confirmação usa mesmo formato
- [ ] Separador de hora/minuto é ":" (ex: 14:30)
- [ ] Sem AM/PM (padrão brasileiro 24h)
- [ ] Leitura fácil: HH:MM

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Agendamento (`screens/Agendamento.js`)
- Tela de Consulta Agendamento (`screens/ConsultaAgendamento.js`)
- Componente de Horário
- Serviço de Formatação
- Notificações Toast

### Formatação Padronizada
```javascript
// Usar biblioteca date-fns ou similar
import { format } from 'date-fns';
import { ptBR } from 'date-fns/locale';

const hora = new Date('2026-03-25T14:30:00');
format(hora, 'HH:mm', { locale: ptBR }); // "14:30"
```

### Locais de Atualização
- Telas de agendamento
- Notificações
- Confirmações
- Histórico
- Emails enviados
- SMS/Whatsapp

---

## 📊 Estimativa

- **Esforço:** Pequeno (1 dia)
- **Complexidade:** Baixa
- **Prioridade:** Média

---

## 🔗 Dependências

- Nenhuma

---

## 📝 Checklist de Resolução

- [ ] Definir padrão: HH:MM formato 24h
- [ ] Atualizar componentes de exibição
- [ ] Usar date-fns para padronização
- [ ] Testar em todas as telas
- [ ] Verificar emails/SMS
- [ ] Validar em diferentes devices
