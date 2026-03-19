# Demanda: Função - Confirmação com Informações

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #55
**Tipo:** Feature
**Status:** To Do
**Complexidade:** Média

---

## 📋 Descrição

Implementar componentes/modals de confirmação melhorados que exibem informações contextuais relevantes antes do usuário confirmar uma ação. Ex: ao deletar um serviço, mostrar quantos agendamentos futuros serão afetados.

## 🎯 Objetivos

1. Criar componente genérico de confirmação com informações
2. Exibir dados relevantes antes da confirmação
3. Melhorar segurança (usuário ciente das consequências)
4. Melhorar UX com feedback visual
5. Reutilizável em múltiplos contextos

## 📌 Requisitos Funcionais

### Componente `ConfirmacaoComInformacoes.vue`

**Props:**

- [ ] `titulo` - Título do modal
- [ ] `mensagem` - Mensagem principal
- [ ] `informacoes` - Object com dados a exibir
- [ ] `botaoPrimario` - Texto do botão confirmar
- [ ] `botaoSecundario` - Texto do botão cancelar
- [ ] `tipo` - Type (success, warning, danger, info)
- [ ] `carregando` - Estado de carregamento
- [ ] `desabilitado` - Desabilitar confirmar

**Emits:**

- [ ] `confirmar`
- [ ] `cancelar`

**Slot:**

- [ ] Slot padrão para informações customizadas

### Casos de Uso

#### 1. Deletar Serviço

```
Tem certeza que deseja deletar "Tosa Completa"?

⚠️ Isso afetará:
- 3 agendamentos futuros
- 15 clientes serão notificados
- Ação não poderá ser desfeita
```

#### 2. Cancelar Agendamento

```
Tem certeza que deseja cancelar este agendamento?

📅 Detalhes:
- Cliente: João Silva
- Serviço: Banho e Tosa
- Data: 20/05/2026 14:00
- Pet: Rex (Golden Retriever)
```

#### 3. Arquivar Promoção

```
Deseja arquivar a promoção "Black Friday"?

📊 Dados:
- Status: Ativa
- Clientes beneficiados: 45
- Desconto oferecido: 30%
```

### Backend (Pet.ON.Api)

Para suportar esses modalS, pode ser necessário:

- [ ] Endpoints que retornem info de impacto de deleção
- [ ] Ex: `GET /api/servicos/{id}/impacto-delecao`
  - Retorna quantidade agendamentos, clientes afetados, etc

### Frontend (petshop)

**Componente Base:**

- [ ] `src/components/ConfirmacaoComInformacoes.vue`
  - Template com layout bem estruturado
  - Suporte a diferentes tipos (warning, danger)
  - Icons adequados
  - Animação/transição
  - Responsive

**Composable Helper:**

- [ ] `useConfirmacao.js`
  - Wrapper que mostra/esconde modal
  - Handle de confirmar/cancelar
  - State management

**Integrações:**

1. **Deletar Serviço:**
   - Modificar em: ListaServicos.vue ou ServicosPage.vue
   - Chamar `useConfirmacao` antes de deletar
   - Mostrar informações de impacto

2. **Cancelar Agendamento:**
   - Modificar em: AgendaPage.vue
   - Mostrar detalhes do agendamento
   - Confirmar antes de cancelar

3. **Outros (Promoções, Configurações):**
   - Aplicar padrão em outros lugares necessários

## ✅ Critérios de Aceitação

- [ ] Componente criado e funcional
- [ ] Exibe informações contextuais
- [ ] Responsivo mobile
- [ ] Acessível (keyboard nav, screen reader)
- [ ] Animações suaves
- [ ] Integrado em pelo menos 3 casos de uso
- [ ] Testes cobrendo componente
- [ ] Documentado para outros devs
- [ ] Sem erros de console

## 📦 Arquivos/Componentes Afetados

**Frontend:**

- src/components/ConfirmacaoComInformacoes.vue (novo)
- src/composables/useConfirmacao.js (novo)
- src/pages/Configuracoes/ServicosPage.vue (modificar)
- src/pages/AgendaPage.vue (modificar)
- src/services/\* (adicionar endpoints de info de impacto se necessário)

**Backend (opcional):**

- Pet.ON.Api/Controllers/ServicosController.cs
- Pet.ON.Application/Services/ServicoService.cs

## 🔗 Dependências

- Vue 3
- Sistema de modals base (se houver)
- Design system e icons

## 📊 Complexidade

- **Frontend:** Média
- **Backend:** Baixa (opcional)
- **Integração:** Média (integrar em vários lugares)
- **Tempo Estimado:** 6-8 horas

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
