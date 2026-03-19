# Demanda: Mostrar Porte nos Serviços

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #20
**Tipo:** Feature
**Status:** Doing
**Complexidade:** Média

---

## 📋 Descrição

Implementar a exibição de porte/tamanho de animal nos serviços. Mostrar claramente quais portes (Pequeno, Médio, Grande, etc) cada serviço atendo, permitindo filtros e exibição visual clara.

## 🎯 Objetivos

1. Associar serviços a portes específicos
2. Exibir portes na listagem de serviços
3. Permitir filtrar por porte
4. Aplicar preços diferentes por porte (se necessário)
5. Exibir claramente no agendamento

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Estrutura de Portes:
  - Criar ou reutilizar modelo `Porte` (Pequeno, Médio, Grande, Gigante, Todos)
  - Cada porte com ID único

- [ ] Relação Serviço-Porte:
  - Tabela junction `ServicoPorte` com:
    - ServicoId
    - PorteId
    - Preço específico (opcional, deixar em branco = usar preço do serviço)
    - Status

- [ ] Endpoints:
  - `GET /api/portes` - Listar todos os portes
  - `GET /api/servicos/{id}/portes` - Listar portes de um serviço
  - `POST /api/servicos/{id}/portes` - Adicionar porte ao serviço
  - `DELETE /api/servicos/{id}/portes/{porteId}` - Remover porte
  - `GET /api/servicos?porte={porteId}` - Filtrar serviços por porte

- [ ] Validações:
  - Não permitir deletar todos os portes de um serviço
  - Validar preço específico se fornecido

### Frontend (petshop)

- [ ] Formulário de Serviço:
  - Adicionar seção "Portes Atendidos"
  - Checkboxes para selecionar portes
  - Input de preço específico por porte (opcional)
  - Layout claro com ícones de tamanho

- [ ] Listagem de Serviços:
  - Badges/tags mostrando portes (ex: "P | M | G")
  - Cores diferentes por porte (opcional)
  - Hover para ver detalhes

- [ ] Agendamento:
  - Selectionar porte do pet
  - Filtrar serviços disponíveis para aquele porte
  - Exibir preço correto (geral ou específico)
  - Mostrar aviso se serviço não atende aquele porte

- [ ] Composables:
  - `usePortes.js` - Carregar lista de portes
  - `useServicoPorte.js` - Gerenciar relação serviço-porte
  - `useFiltroPorte.js` - Filtrar serviços por porte

## ✅ Critérios de Aceitação

- [ ] Portes associados corretamente a serviços
- [ ] Filtro por porte funciona
- [ ] Preço específico aplicado corretamente
- [ ] Seleção de porte no agendamento obrigatória
- [ ] Exibição visual clara de portes
- [ ] Responsivo mobile
- [ ] Testes com cobertura >80%
- [ ] Sem erros de console

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Domain/Entities/Porte.cs (existente ou novo)
- Pet.ON.Domain/Entities/ServicoPorte.cs (novo)
- Pet.ON.Application/DTOs/ServicoPorteDto.cs
- Pet.ON.Application/Services/ServicoService.cs
- Pet.ON.Infra/Repositories/ServicoRepository.cs
- Pet.ON.Api/Controllers/ServicosController.cs
- Migration: AddServicoPorte.cs

**Frontend:**

- src/components/Forms/FormularioServico.vue (modificar)
- src/components/SelectPorte.vue
- src/pages/AgendaPage.vue (modificar para filtro)
- src/pages/AgendaPage.vue (filtro por porte)
- src/composables/usePortes.js
- src/composables/useServicoPorte.js
- src/composables/useFiltroPorte.js
- src/components/BadgePorte.vue

## 🔗 Dependências

- Sistema de serviços base
- Sistema de agendamentos
- Lista de portes definida

## 📊 Complexidade

- **Backend:** Média
- **Frontend:** Média
- **Integração:** Média
- **Tempo Estimado:** 8-10 horas

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
