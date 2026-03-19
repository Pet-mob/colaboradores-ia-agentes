# Demanda: Sistema de Confirmação de Serviços Agendados

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #13
**Tipo:** Feature
**Status:** Doing
**Complexidade:** Média-Alta

---

## 📋 Descrição

Implementar um sistema completo de confirmação de serviços agendados onde a loja pode confirmar a recepção do agendamento, e o cliente recebe notificação de confirmação. O sistema deve incluir possibilidade de fornecer feedback ou solicitar ajustes.

## 🎯 Objetivos

1. Permitir loja confirmar agendamentos
2. Notificar cliente da confirmação
3. Registrar data/hora da confirmação
4. Permitir mensagem de feedback do lojista
5. Criar histórico de confirmações

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Adicionar campos a `Agendamento`:
  - Status de confirmação (Pendente, Confirmado, Rejeitado)
  - Data/hora da confirmação
  - Mensagem do lojista
  - Data/hora de visualização pelo cliente

- [ ] Criar endpoints:
  - `PUT /api/agendamentos/{id}/confirmar` - Confirmar agendamento
  - `PUT /api/agendamentos/{id}/rejeitar` - Rejeitar com motivo
  - `GET /api/agendamentos/{id}/confirmacao` - Obter dados de confirmação
  - `PUT /api/agendamentos/{id}/visualizar` - Marcar como visualizado

- [ ] Implementar notificações:
  - Notificação no SignalR quando confirmado
  - Email para cliente (opcional)
  - SMS para cliente (opcional)

- [ ] Validações:
  - Apenas lojista pode confirmar/rejeitar
  - Não pode confirmar agendamento passado
  - Mensagem com limite de caracteres

### Frontend (petshop)

- [ ] Modificar `AgendaPage.vue`:
  - Adicionar coluna "Status de Confirmação"
  - Código visual para cada status (cores)
  - Badge com ícone de confirmação/pendência/rejeição

- [ ] Criar componente `ConfirmacaoAgendamentoModal.vue`:
  - Exibir detalhes do agendamento
  - Textarea para mensagem do lojista
  - Botão "Confirmar"
  - Botão "Rejeitar" com motivo obrigatório
  - Botão "Cancelar"

- [ ] Criar composable `useConfirmacaoAgendamento.js`:
  - Chamar endpoint de confirmação
  - Validar mensagem
  - Tratar respostas

- [ ] Notificação no cliente:
  - Toast/notification quando receber confirmação
  - Componente `NotificacaoConfirmacao.vue` (similar ao `NotificacaoAgendamento.vue`)
  - Som/vibração opcional
  - Link para visualizar agendamento confirmado

### Real-time

- [ ] Usar SignalR para atualizar status em tempo real
- [ ] Atualizar agenda sem recarregar tela

## ✅ Critérios de Aceitação

- [ ] Lojista consegue confirmar/rejeitar agendamentos
- [ ] Cliente recebe notificação em tempo real
- [ ] Status exibido corretamente na tela
- [ ] Mensagem é persistida
- [ ] Histórico de confirmações disponível
- [ ] Responsivo mobile
- [ ] Testes com cobertura >80%
- [ ] Sem erros de console
- [ ] Sistema funciona com múltiplos usuários simultaneamente

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Domain/Entities/Agendamento.cs (modificar)
- Pet.ON.Application/DTOs/ConfirmacaoAgendamentoDto.cs
- Pet.ON.Application/Services/AgendamentoService.cs (modificar)
- Pet.ON.Infra/Repositories/AgendamentoRepository.cs (modificar)
- Pet.ON.Api/Controllers/AgendamentosController.cs
- Pet.ON.Service/SignalRService.cs

**Frontend:**

- src/pages/AgendaPage.vue (modificar)
- src/components/Agenda/ConfirmacaoAgendamentoModal.vue
- src/components/NotificacaoConfirmacao.vue
- src/composables/useConfirmacaoAgendamento.js
- src/composables/useSignalR.js (modificar)
- src/services/agendamentoService.js (modificar)

## 🔗 Dependências

- SignalR funcional
- Sistema de agendamentos base
- Notificações implementadas
- Autenticação com roles

## 📊 Complexidade

- **Backend:** Média
- **Frontend:** Média
- **Integração:** Média-Alta (tempo real)
- **Tempo Estimado:** 10-12 horas

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
