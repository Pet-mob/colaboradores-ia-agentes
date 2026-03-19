# Demanda: Criar Promoção Geral

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #6
**Tipo:** Feature
**Status:** To Do
**Complexidade:** Média

---

## 📋 Descrição

Implementar um sistema de promoção geral que permita criar, gerenciar e visualizar promoções aplicáveis em toda a plataforma. As promoções devem ser configuráveis por percentual de desconto e período de validade.

## 🎯 Objetivos

1. Criar estrutura de dados para promoções (Domain)
2. Implementar endpoints de CRUD para promoções (API)
3. Criar tela de gerenciamento de promoções (Frontend)
4. Aplicar descontos em serviços quando uma promoção está ativa

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Criar modelo `Promocao` no Domain com:
  - Identificador único (GUID)
  - Nome/Descrição
  - Percentual de desconto (0-100%)
  - Data início e fim
  - Status (Ativa/Inativa)
  - Timestamp de criação/atualização
- [ ] Criar endpoints REST:
  - `POST /api/promocoes` - Criar nova promoção
  - `GET /api/promocoes` - Listar todas
  - `GET /api/promocoes/{id}` - Obter detalhes
  - `PUT /api/promocoes/{id}` - Atualizar
  - `DELETE /api/promocoes/{id}` - Deletar
  - `GET /api/promocoes/ativas` - Listar ativas

- [ ] Implementar validações:
  - Percentual entre 0 e 100
  - Data fim maior que data início
  - Apenas um administrador pode criar

- [ ] Criar repository e service layer

### Frontend (petshop)

- [ ] Criar página `PromocoesList.vue`:
  - Tabela com todas as promoções
  - Filtros por status (Ativa/Inativa)
  - Busca por nome
  - Ações: Editar, Deletar, Visualizar

- [ ] Criar form `PromocaoForm.vue`:
  - Campo nome/descrição
  - Campo percentual com validação
  - Seletor de datas (início/fim)
  - Toggle para ativar/inativar
  - Botão salvar/cancelar

- [ ] Criar composable `usePromocao.js`:
  - Chamadas HTTP para endpoints
  - Validações de entrada
  - Tratamento de erros

### Integração Serviços

- [ ] Aplicar desconto em listagem de serviços
- [ ] Mostrar badge "Em Promoção" em serviços com desconto

## ✅ Critérios de Aceitação

- [ ] CRUD funcional de promoções
- [ ] Validações implementadas
- [ ] Tela responsiva mobile
- [ ] Testes unitários (cobertura >80%)
- [ ] Sem erros de console
- [ ] Funciona com múltiplas promoções simultâneas

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Domain/Entities/Promocao.cs
- Pet.ON.Application/DTOs/PromocaoDto.cs
- Pet.ON.Application/Services/PromocaoService.cs
- Pet.ON.Infra/Repositories/PromocaoRepository.cs
- Pet.ON.Api/Controllers/PromocoesController.cs

**Frontend:**

- src/pages/Configuracoes/PromocoesList.vue
- src/components/Forms/PromocaoForm.vue
- src/composables/usePromocao.js
- src/services/promocaoService.js
- src/router/indexConfiguracoes.js
- src/**tests**/unit/composables/usePromocao.spec.js

## 🔗 Dependências

- Sistema de autenticação funcional
- Database setup
- Permissões de administrador

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
