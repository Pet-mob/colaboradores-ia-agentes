# Demanda: Criação de Porte do Tipo "Todos"

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #21
**Tipo:** Feature
**Status:** Doing
**Complexidade:** Baixa-Média

---

## 📋 Descrição

Criar um tipo especial de porte chamado "Todos" para serviços que podem ser agendados para qualquer tamanho de animal. Isso simplifica a configuração de serviços que não discriminam por porte.

## 🎯 Objetivos

1. Criar tipo especial de porte (ID=0 ou especial) para "Todos"
2. Permitir selecionar como único porte
3. Exibir "Todos os portes" na interface
4. Lógica de filtro apropriada
5. Não forçar seleção de porte se serviço atende "Todos"

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Modificar modelo `Porte`:
  - Adicionar novo porte com ID especial (0 ou flag IsAll)
  - Nome = "Todos"
  - Descrição = "Atende todos os portes"

- [ ] Lógica em endpoints:
  - Se porte "Todos" selecionado, remover outros
  - Se outro porte adicionado com "Todos" ativo, remover "Todos"
  - Na filtragem, "Todos" deve retornar quando filtrado por qualquer porte

- [ ] Validação:
  - Ao criar relação ServicoPorte com "Todos", validar
  - Garantir que não há conflito de portes

### Frontend (petshop)

- [ ] Formulário de Serviço:
  - Option "Atende todos os portes" em destaque
  - Se selecionado, desabilitar seleção de portes individuais
  - Se pessoal porte selecionado, desabilitar "Todos"

- [ ] Listagem:
  - Exibir "Todos os portes" ou badge especial
  - Não mostrar lista de portes individuais

- [ ] Agendamento:
  - Se serviço atende "Todos", não forçar seleção de porte
  - Se porte "Todos", usar preço geral

## ✅ Critérios de Aceitação

- [ ] Porte "Todos" criado e funcional
- [ ] Serviços com "Todos" funcionam corretamente
- [ ] Filtros funcionam com "Todos"
- [ ] Validações funcionam
- [ ] Exibição clara na interface
- [ ] Sem erros de console
- [ ] Testes passando

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Domain/Entities/Porte.cs (modificar)
- Pet.ON.Application/Services/ServicoService.cs
- Migration: AddPorteTodos.cs
- Seed data: adicionar porte "Todos"

**Frontend:**

- src/components/Forms/FormularioServico.vue
- src/composables/usePortes.js
- src/components/BadgePorte.vue

## 🔗 Dependências

- Demanda #20 (Mostrar Porte nos Serviços) - deve estar implementada ou ser implementada junto
- Sistema de serviços

## 📊 Complexidade

- **Backend:** Baixa-Média
- **Frontend:** Baixa
- **Integração:** Baixa
- **Tempo Estimado:** 3-4 horas

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
