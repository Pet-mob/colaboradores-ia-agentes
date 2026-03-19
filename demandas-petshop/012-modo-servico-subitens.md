# Demanda: Modo de Serviço com Sub-itens para Selecionar

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #12
**Tipo:** Feature
**Status:** To Do
**Complexidade:** Alta

---

## 📋 Descrição

Implementar um sistema onde serviços podem ter sub-itens configuráveis que o cliente deve selecionar durante o agendamento. Exemplo: Serviço "Tosa" com sub-itens "Tosa Completa", "Tosa Higiênica", "Tosa com Banho".

## 🎯 Objetivos

1. Permitir criar sub-itens para serviços
2. Tornar sub-itens obrigatórios ou opcionais
3. Permitir cliente selecionar sub-itens no agendamento
4. Aplicar preços diferentes por sub-item
5. Exibir sub-itens selecionados na confirmação

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Criar modelo `ServicoSubItem` com:
  - ID único
  - ServicoId (FK)
  - Nome
  - Descrição
  - Valor adicional (pode ser 0)
  - Ordem de exibição
  - Status (Ativo/Inativo)

- [ ] Criar endpoints:
  - `POST /api/servicos/{id}/subitens` - Criar sub-item
  - `GET /api/servicos/{id}/subitens` - Listar sub-itens
  - `PUT /api/servicos/{id}/subitens/{subitemId}` - Atualizar
  - `DELETE /api/servicos/{id}/subitens/{subitemId}` - Deletar

- [ ] Modificar modelo `Agendamento`:
  - Adicionar campo para sub-itens selecionados (JSON array)
  - Recalcular total incluindo valores dos sub-itens

- [ ] Validações:
  - Validar se sub-item selecionado pertence ao serviço
  - Verificar se todos os sub-itens obrigatórios foram selecionados

### Frontend (petshop)

- [ ] Modificar `FormularioServico.vue`:
  - Adicionar seção de sub-itens
  - Input para nome do sub-item
  - Input para valor adicional
  - Checkbox para obrigatório/opcional
  - Botão adicionar/remover sub-item
  - Reordenação via drag-drop (opcional)

- [ ] Modificar `FormAgendamento.vue`:
  - Verificar se serviço tem sub-itens
  - Exibir checkboxes/radio buttons para seleção
  - Destacar sub-itens obrigatórios
  - Mostrar valor adicional de cada sub-item
  - Recalcular preço total dinamicamente

- [ ] Modificar `ConfirmacaoAgendamento.vue`:
  - Exibir sub-itens selecionados
  - Mostrar detalhamento de preços

### Composable

- [ ] Criar `useSubItens.js`:
  - Validar seleção de sub-itens
  - Calcular valor total com sub-itens
  - Manter estado de seleção

## ✅ Critérios de Aceitação

- [ ] CRUD de sub-itens funcional
- [ ] Sub-itens aparecem corretamente no agendamento
- [ ] Validações de obrigatoriedade funcionam
- [ ] Preço total recalculado corretamente
- [ ] Sub-itens persistidos no agendamento
- [ ] Responsivo mobile
- [ ] Testes com cobertura >75%
- [ ] Sem erros de console

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Domain/Entities/ServicoSubItem.cs
- Pet.ON.Domain/Entities/Agendamento.cs (modificar)
- Pet.ON.Application/DTOs/ServicoSubItemDto.cs
- Pet.ON.Application/Services/ServicoService.cs (modificar)
- Pet.ON.Infra/Repositories/ServicoRepository.cs (modificar)
- Pet.ON.Api/Controllers/ServicosController.cs

**Frontend:**

- src/components/Forms/FormularioServico.vue
- src/components/Forms/FormAgendamento.vue
- src/pages/ConfirmacaoAgendamentoPage.vue
- src/composables/useFormularioServico.js (modificar)
- src/composables/useSubItens.js
- src/services/servicoService.js (modificar)

## 🔗 Dependências

- Sistema de agendamento base funcional
- Sistema de formatos de preço
- Autenticação

## 📊 Complexidade

- **Backend:** Alta
- **Frontend:** Alta
- **Integração:** Alta
- **Tempo Estimado:** 12-15 horas

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
