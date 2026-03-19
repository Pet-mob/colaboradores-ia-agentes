# Demanda: Ajuste - Hover do Mouse sobre Gráfico

**Projeto:** PetShop.WebApp
**ID:** #22
**Tipo:** Ajuste/UX
**Status:** To Do
**Complexidade:** Baixa

---

## 📋 Descrição

Melhorar a experiência de interação com o gráfico de serviços no dashboard. Aprimorar o tooltip/popup que aparece ao passar o mouse sobre as barras, linhas ou pontos do gráfico.

## 🎯 Objetivos

1. Melhorar visibilidade do tooltip
2. Mostrar informações relevantes
3. Melhorar espaçamento e positioning
4. Adicionar animações suave
5. Garantir funcionalidade mobile (touch)

## 📌 Requisitos Funcionais

### Melhorias de Tooltip

- [ ] **Conteúdo do Tooltip:**
  - Nome do serviço
  - Quantidade de agendamentos
  - Valor total gerado (se aplicável)
  - Data/período
  - Percentual da semana/mês

- [ ] **Estilo Visual:**
  - Fundo com boa contrast
  - Sombra para profundidade
  - Fonte legível
  - Cores consistentes com design system
  - Borda ou arredondamento

- [ ] **Posicionamento:**
  - Auto-ajustar se perto das bordas
  - Não sobrepor dados importantes
  - Aparecer acima/abaixo dependendo do espaço
  - Acompanhar movimento do mouse suavemente

- [ ] **Animação:**
  - Fade-in suave (100-200ms)
  - Transição de posição fluida
  - Fade-out ao sair (opcional)

- [ ] **Responsividade:**
  - Em mobile, usar click/tap em vez de hover
  - Tamanho ajustado para tela pequena
  - Não cobrir área importante

- [ ] **Performance:**
  - Não causar lag ao mouse over
  - Usar throttle se necessário
  - Rerender otimizado

### Componente Afetado

- [ ] Arquivo: `GraficoServicos.vue`
  - Revisar library de gráfico (Chart.js)
  - Configurar opções de tooltip
  - Adicionar handlers de evento

## ✅ Critérios de Aceitação

- [ ] Tooltip aparece ao passar mouse
- [ ] Informações claras e legíveis
- [ ] Posicionamento inteligente
- [ ] Animações suaves
- [ ] Funciona em mobile (touch)
- [ ] Sem lag/stuttering
- [ ] Sem erros de console
- [ ] Testes de comportamento

## 📦 Arquivos/Componentes Afetados

**Frontend:**

- src/components/GraficoServicos.vue
- src/assets/estilos-grafico.css (novo ou modificar)

## 🔗 Dependências

- Chart.js (já instalado)
- Vue 3
- Composable useThrottle (já existe)

## 📊 Complexidade

- **Frontend:** Baixa
- **Integração:** Baixa
- **Tempo Estimado:** 2-3 horas

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
