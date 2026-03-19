# Demanda: Função - Criar Aba do Fale Conosco

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #51
**Tipo:** Feature
**Status:** Doing
**Complexidade:** Média

---

## 📋 Descrição

Implementar uma nova aba/seção de "Fale Conosco" (ou "Contato", "Suporte") onde clientes possam entrar em contato com a loja para dúvidas, sugestões ou problemas. A loja receberá as mensagens e poderá responder.

## 🎯 Objetivos

1. Permitir clientes enviar mensagens de contato
2. Registrar mensagens com timestamp
3. Notificar lojista de novo contato
4. Permitir lojista responder
5. Histórico de conversa para cliente e lojista

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Criar modelo `MensagemContato`:
  - ID único
  - LojaId (FK)
  - ClienteId ou Email (para contatos anônimos)
  - Nome do remetente
  - Assunto
  - Mensagem
  - Status (Não Lido, Lido, Respondido)
  - Data de criação
  - Respostas (relação 1:N)

- [ ] Criar modelo `RespostaMensagem`:
  - ID único
  - MensagemContatoId (FK)
  - Remetente (Lojista/Sistema)
  - Texto da resposta
  - Data
  - Lido (boolean)

- [ ] Endpoints:
  - `POST /api/lojas/{lojaId}/contato` - Enviar mensagem
  - `GET /api/loja/contatos` - Listar contatos recebidos (lojista)
  - `GET /api/loja/contatos/{id}` - Detalhes com respostas
  - `POST /api/loja/contatos/{id}/responder` - Responder mensagem
  - `PUT /api/loja/contatos/{id}/marcar-lido` - Marcar como lido
  - `DELETE /api/loja/contatos/{id}` - Deletar

- [ ] Notificações:
  - SignalR para notificar lojista de novo contato
  - Email opcional para lojista
  - Email para cliente com resposta (opcional)

- [ ] Validações:
  - Nome obrigatório
  - Assunto entre 5-100 caracteres
  - Mensagem entre 10-5000 caracteres
  - Email válido se fornecido
  - Rate limiting para evitar spam

### Frontend (petshop)

**Para Clientes (Customer View):**

- [ ] Criar rota e página `ContatoPage.vue`:
  - Se logado: Mostrar contatos anteriores
  - Se não logado: Mostrar apenas form

- [ ] Componente `FormContatoLoja.vue`:
  - Input Nome (pré-preenchido se logado)
  - Input Email (pré-preenchido se logado)
  - Input Assunto
  - Textarea Mensagem extensa
  - Botão Enviar
  - Feedback de sucesso/erro
  - Spinner durante envio

- [ ] Componente `ListaContatosCliente.vue`:
  - Lista de contatos enviados
  - Mostrar resposta se houver
  - Status (Respondido/Pendente)
  - Data de envio

**Para Lojistas (Admin View):**

- [ ] Nova aba em Configurações: "Mensagens de Contato"

- [ ] Componente `ListaContatosLoja.vue`:
  - Tabela com todos contatos
  - Filtros: Status (Não Lido, Lido, Respondido)
  - Busca por nome/assunto
  - Badges de status
  - Badge de quantidade não lida
  - Click para abrir detalhes

- [ ] Componente `DetalheContatoModal.vue`:
  - Exibir mensagem do cliente
  - Histórico de respostas
  - Textarea para nova resposta
  - Botão Responder
  - Botão Marcar como Respondido
  - Botão Deletar

- [ ] Notificação real-time:
  - Toast quando novo contato chega
  - Som (opcional)
  - Atualizar contador de não lidas
  - SignalR integration

### Composables

- [ ] `useContato.js`:
  - Enviar mensagem
  - Listar contatos
  - Responder
  - Marcar como lido

## ✅ Critérios de Aceitação

- [ ] Cliente consegue enviar mensagem
- [ ] Lojista recebe notificação
- [ ] Lojista consegue responder
- [ ] Cliente vê resposta
- [ ] Histórico mantido
- [ ] Validações funcionam
- [ ] Responsivo mobile
- [ ] Testes com cobertura >75%
- [ ] Sem erros de console
- [ ] Rate limiting funciona

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Domain/Entities/MensagemContato.cs
- Pet.ON.Domain/Entities/RespostaMensagem.cs
- Pet.ON.Application/DTOs/MensagemContatoDto.cs
- Pet.ON.Application/Services/ContatoService.cs
- Pet.ON.Infra/Repositories/ContatoRepository.cs
- Pet.ON.Api/Controllers/ContatoController.cs
- Pet.ON.Service/SignalRService.cs (modificar)
- Migration: AddMensagensContato.cs

**Frontend:**

- src/pages/ContatoPage.vue
- src/pages/Configuracoes/ContatosLoja.vue
- src/components/Forms/FormContatoLoja.vue
- src/components/ListaContatosCliente.vue
- src/components/ListaContatosLoja.vue
- src/components/DetalheContatoModal.vue
- src/composables/useContato.js
- src/services/contatoService.js
- src/router/index.js (adicionar rota)
- src/router/indexConfiguracoes.js (adicionar aba)

## 🔗 Dependências

- Autenticação base
- SignalR funcional
- Sistema de notificações
- Email service (opcional)

## 📊 Complexidade

- **Backend:** Média
- **Frontend:** Média
- **Integração:** Média
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
