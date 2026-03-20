# Demanda: Bug - Design Responsivo Mobile (Tela de Agendamento)

**Projeto:** PetShop.WebApp
**ID:** #53
**Tipo:** Bug
**Status:** To Do
**Complexidade:** Baixa-Média
**Tags:** petshop, v1

---

## 📋 Descrição

A tela/fluxo de agendamento não está exibindo corretamente em dispositivos mobile. Há problemas de layout do formulário, datas/horários, seleção de serviços ou confirmação em telas pequenas.

## 🎯 Objetivos

1. Garantir layout responsivo em todos tamanhos de tela
2. Melhorar experiência de preenchimento do formulário
3. Facilitar seleção de data/hora em mobile
4. Melhorar legibilidade e usabilidade
5. Testar em múltiplos devices

## 📌 Requisitos Funcionais

### Problemas Comuns em Mobile (Agendamento)

- [ ] **Seletor de Data/Hora:**
  - Calendário muito grande
  - Inputs de hora ilegíveis
  - Teclado numérico não funciona
  - Masking de data confuso

- [ ] **Seleção de Serviço:**
  - Cards de serviço muito grandes
  - Imagens transbordando
  - Texto truncado
  - Filtros difíceis de usar

- [ ] **Formulário:**
  - Inputs trans bordando tela
  - Labels sobrepostos
  - Múltiplas colunas não se adaptam
  - Validação não clara

- [ ] **Resumo/Confirmação:**
  - Informações não caem na tela
  - Botão de confirmar fora da vista
  - Scroll excessivo

- [ ] **Responsividade:**
  - Landscape não funciona
  - Scroll horizontal
  - Elementos fixed causando problemas
  - Safe area em notch/devices especiais

### Checklist de Teste Mobile

- [ ] iPhone 5/SE (320px)
- [ ] iPhone 12 (390px)
- [ ] iPhone 12 Pro Max (428px)
- [ ] Samsung A10 (360px)
- [ ] Samsung S20 (360px)
- [ ] iPad Mini em portrait (768px)
- [ ] iPad em landscape (1024px)
- [ ] Todos em landscape orientation

### Possíveis Soluções

**Date Picker:**

- [ ] Usar input type="date" nativo em mobile
- [ ] Fallback para date picker library
- [ ] Mostrar calendário menos "pesado" em mobile

**Seleção de Serviço:**

- [ ] Cards em 1 coluna em mobile
- [ ] Imagens scaled corretamente
- [ ] Botões de seleção claros (radio/checkbox)

**Formulário:**

- [ ] Stack vertical em mobile
- [ ] Full width inputs
- [ ] Font-size >= 16px
- [ ] Apenas inputs necessários em mobile

**Layout:**

- [ ] Flexbox/grid responsivo
- [ ] Scroll vertical apenas
- [ ] Sticky header/footer se necessário

## ✅ Critérios de Aceitação

- [ ] Layout funciona em 320px+
- [ ] Formulário preenchível sem scroll horizontal
- [ ] Date picker funcional em mobile
- [ ] Resumo exibido corretamente
- [ ] Botão de confirmar sempre acessível
- [ ] Funciona em landscape
- [ ] Sem overflow
- [ ] Testes em múltiplos devices
- [ ] Sem erros de console

## 📦 Arquivos/Componentes Afetados

**Frontend:**

- src/pages/AgendaPage.vue
- src/components/Forms/FormAgendamento.vue
- src/pages/ConfirmacaoAgendamentoPage.vue
- src/components/Cards/ServicoCard.vue
- src/style/responsive.css
- src/components/DatePicker.vue (se existir)

## 🔗 Dependências

- CSS responsivo base
- Date picker library (se usado)
- Design system

## 📊 Complexidade

- **Investigação:** Baixa-Média
- **Correção:** Baixa-Média
- **Teste:** Média-Alta (múltiplos devices)
- **Tempo Estimado:** 4-6 horas

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
