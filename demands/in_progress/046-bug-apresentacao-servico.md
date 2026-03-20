# Demanda: Bug - Apresentação do Serviço Agendado

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #46
**Tipo:** Bug
**Status:** Doing
**Complexidade:** Investigação Necessária

---

## 📋 Descrição

Há um problema na forma como o serviço agendado é apresentado/exibido ao cliente ou lojista. As informações podem estar incompletas, formatadas incorretamente, ou em ordem errada.

## 🎯 Objetivos

1. Identificar o problema exato de apresentação
2. Garantir exibição correta em todos os contextos
3. Melhorar legibilidade e formatação
4. Consistência entre telas
5. Testes para evitar regressão

## 📌 Requisitos Investigativos

### Contextos de Exibição

- [ ] **Tela de Agendamento (antes de confirmar)**
- [ ] **Página de Confirmação Pós-Agendamento**
- [ ] **Agenda do Lojista (listagem)**
- [ ] **Detalhes de Agendamento**
- [ ] **Notificação do Cliente**
- [ ] **Email/SMS de confirmação**

### Possíveis Problemas

- [ ] Informações faltando (preço, duração, porte?)
- [ ] Formatação incorreta (valores monetários, datas, horas)
- [ ] Ordem confusa de informações
- [ ] Truncamento de texto longo
- [ ] Cores/estilos inconsistentes
- [ ] Responsividade quebrada
- [ ] Dados não carregando/lazy loading lento
- [ ] Ícones/imagens do serviço não aparecendo
- [ ] Sub-itens não exibindo
- [ ] Descrição do serviço formatada errada (quebras de linha)

### Checklist de Investigação

- [ ] **Frontend:**
  - Componentes responsáveis pela exibição: `agendamento-card.vue`, `detalhes-agendamento.vue`, etc
  - Estado de dados chegando corretamente
  - Template renderizando correto
  - CSS causando problema visual
  - Responsividade (testar mobile)

- [ ] **Backend:**
  - DTO incluindo todos campos necessários
  - Formatação de valores (decimal, data, hora)
  - Lazy loading de dados relacionados
  - Paginação causando dados incompletos

- [ ] **API Response:**
  - Analisar JSON retornado
  - Verificar tipos de dados
  - Completude de informações

## 📋 Passos de Resolução

- [ ] **Reproduzir:**
  - Em qual tela exato?
  - Com qual tipo de serviço?
  - Com qual navegador/device?
  - Consistente ou intermitente?

- [ ] **Documentar Problema:**
  - Screenshots da apresentação errada
  - Screenshots da apresentação esperada
  - Descrever diferenças

- [ ] **Corrigir:**
  - Ajustar template/componente se frontend
  - Ajustar DTO se backend
  - Verificar CSS
  - Testar em todos contextos

- [ ] **Validar:**
  - Testes em múltiplos tamanhos de tela
  - Testes com diferentes tipos de serviço
  - Testes com múltiplos idiomas (se aplicável)

## ✅ Critérios de Aceitação

- [ ] Apresentação clara e consistente
- [ ] Todas informações relevantes visíveis
- [ ] Formatação correta (moeda, data)
- [ ] Responsivo em todos devices
- [ ] Sem erros de console
- [ ] Testes cobrindo apresentação
- [ ] Documentado comportamento esperado

## 📦 Arquivos Potencialmente Afetados

**Frontend:**

- src/pages/ConfirmacaoAgendamentoPage.vue
- src/pages/AgendaPage.vue
- src/components/Agenda/\* (cards, modals)
- src/services (formatação de dados)

**Backend:**

- Pet.ON.Application/DTOs/AgendamentoDto.cs
- Pet.ON.Application/Services/AgendamentoService.cs

## 📊 Complexidade

- **Investigação:** Média
- **Correção:** Depende da causa
- **Teste:** Média
- **Tempo Estimado:** 3-6 horas

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

**Primeira Ação:** Investigar e descrever exatamente qual é o problema de apresentação.

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
