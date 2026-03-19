# Demanda: Selo de Qualidade da Loja

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #15
**Tipo:** Feature
**Status:** To Do
**Complexidade:** Média

---

## 📋 Descrição

Implementar um sistema de selo/badge de qualidade para lojas com base em critérios como taxa de confirmação de agendamentos, avaliações, tempo de resposta e histórico sem problemas. O selo deve ser visível na loja pública e no dashboard.

## 🎯 Objetivos

1. Definir critérios de qualidade
2. Calcular score de qualidade automaticamente
3. Exibir seal/badge em loja pública
4. Mostrar rating na loja pública
5. Dashboard com métricas de qualidade

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Criar modelo `QualidadeLoja`:
  - LojaId (FK)
  - Taxa confirmação (%) agendamentos
  - Avaliação média (1-5 stars)
  - Tempo médio de resposta (horas)
  - Número de reclamações
  - Score total (0-100)
  - Nível (Bronze, Prata, Ouro, Platina)
  - Data última atualização

- [ ] Criar endpoints:
  - `GET /api/lojas/{id}/qualidade` - Obter score
  - `GET /api/loja/minha-qualidade` - Para lojista
  - `POST /api/lojas/{id}/avaliacoes` - Criar avaliação (cliente)

- [ ] Implementar cálculo automático:
  - Job background que recalcula scores diariamente
  - Trigger ao confirmar agendamento
  - Trigger ao criar avaliação
  - Fórmula: (taxa_confirmacao*40% + avaliacoes_media*30% + tempo_resposta*20% + historico*10%)

- [ ] Validações:
  - Apenas cliente pode avaliar
  - Apenas após agendamento realizado
  - Score entre 1-5

### Frontend (petshop)

- [ ] Dashboard do Lojista:
  - Seção "Qualidade da Sua Loja"
  - Exibir score total e nível
  - Cards para cada métrica
  - Gráfico de evolução de score
  - Dicas para melhorar score

- [ ] Página Pública da Loja:
  - Exibir seal/badge grande (topo)
  - Stars de avaliação
  - Link para ver avaliações
  - Histórico de mudanças de nível

- [ ] Sistema de Avaliações:
  - Modal de avaliação (antes ou depois de agendamento)
  - Input 1-5 stars
  - Textarea para comentário (opcional)
  - Feed de avaliações recentes

- [ ] Composable `useQualidadeLoja.js`:
  - Carregar dados de qualidade
  - Formatar dados
  - Cache apropriado

## ✅ Critérios de Aceitação

- [ ] Score calculado corretamente
- [ ] Selos exibidos apropriadamente
- [ ] Avaliações persistidas
- [ ] Dashboard mostra métricas corretas
- [ ] Página pública exibe qualidade
- [ ] Job de recalculo funciona
- [ ] Responsivo mobile
- [ ] Testes com cobertura >75%
- [ ] Sem erros de console

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Domain/Entities/QualidadeLoja.cs
- Pet.ON.Domain/Entities/AvaliacaoCliente.cs
- Pet.ON.Application/DTOs/QualidadeLojaDto.cs
- Pet.ON.Application/Services/QualidadeService.cs
- Pet.ON.Infra/Repositories/QualidadeRepository.cs
- Pet.ON.Api/Controllers/QualidadeController.cs
- Pet.ON.Service/Jobs/RecalcularQualidadeLojaJob.cs
- appsettings.json (configurar job)

**Frontend:**

- src/pages/DashboardPage.vue (modificar - adicionar qualidade)
- src/pages/LojaPublicaPage.vue (modificar)
- src/components/QualidadeCard.vue
- src/components/AvaliacaoModal.vue
- src/components/DisplayQualidade.vue
- src/components/GraficoQualidade.vue
- src/composables/useQualidadeLoja.js
- src/composables/useAvaliacoes.js
- src/services/qualidadeService.js

## 🔗 Dependências

- Sistema de agendamentos
- Sistema de autenticação com roles
- Background jobs configurados
- Banco de dados

## 📊 Complexidade

- **Backend:** Média-Alta
- **Frontend:** Média
- **Integração:** Média
- **Tempo Estimado:** 10-12 horas

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
