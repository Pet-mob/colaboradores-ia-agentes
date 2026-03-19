# Demanda: Bug - Serviços que Não Podem Ser Deletados

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #54
**Tipo:** Bug
**Status:** To Do
**Complexidade:** Baixa-Média
**Tags:** petshop, v1

---

## 📋 Descrição

Há um bug onde certos serviços não podem ser deletados, mas sem mensagem clara do motivo. Ou a funcionalidade de deletar está quebrada para alguns casos. Precisa investigar e corrigir.

## 🎯 Objetivos

1. Investigar por que alguns serviços não podem ser deletados
2. Implementar validações corretas
3. Mostrar mensagem clara do motivo
4. Permitir deleção quando apropriado
5. Impedir deleção quando não apropriado com feedback claro

## 📌 Requisitos Investigativos

### Possíveis Causas

- [ ] **Agendamentos ativos/futuros:**
  - Serviço não pode ter agendamentos pendentes
  - Solução: Deletar agendamentos ou arquivar serviço

- [ ] **Histórico/auditoria:**
  - Serviço referenciado em histórico
  - Solução: Soft delete (marcar como inativo) em vez de hard delete

- [ ] **Bug na constraint:**
  - FK constraint errado
  - Solução: Corrigir migration e banco

- [ ] **Falta de validação:**
  - Sem checar antes de deletar
  - Solução: Adicionar validações

- [ ] **Permissões:**
  - Usuário não tem permissão
  - Solução: Verificar autenticação/autorização

### Checklist de Investigação

- [ ] **Frontend:**
  - Botão de deletar está desabilitado?
  - Mensagem de erro aparece?
  - Qual é a mensagem?
  - Qual o status HTTP retornado?

- [ ] **Backend:**
  - Endpoint retorna erro 400/403/500?
  - Valida antes de deletar?
  - FK constraints no banco?
  - Há agendamentos referenciando serviço?

- [ ] **Banco de Dados:**
  - Constraints de chave estrangeira?
  - Há registros órfãos?
  - Histórico de deletados?

## 📋 Passos de Resolução

### Investigação

- [ ] **Reproduzir:**
  - Qual serviço exato não pode deletar?
  - Qual é a mensagem de erro?
  - Sempre falha ou intermitentemente?
  - Afeta todos serviços ou específicos?

- [ ] **Logs:**
  - Backend logs
  - Network tab (response HTTP)
  - Console errors

### Implementação da Solução

**Se for agendamentos pendentes:**

```
POST /api/servicos/{id}/deletar
{
  "deletarAgendamentos": true/false
}
```

**Se for histórico:**

- Implementar soft delete (flag IsActive)
- Esconder serviços inativos de listagens
- Manter em histórico

**Se for apenas falta de validação:**

- Adicionar validações no backend
- Mensagens claras no frontend
- Feedback visual

### No Frontend

- [ ] Mostrar modal de confirmação antes de deletar
- [ ] Explicar por que não pode deletar se houver motivo
- [ ] Oferecer alternativas (arquivar em vez de deletar)
- [ ] Toast de sucesso/erro

## ✅ Critérios de Aceitação

- [ ] Serviços deletáveis são deletados
- [ ] Serviços não deletáveis mostram motivo claro
- [ ] Sem erros de console
- [ ] Comportamento consistente
- [ ] Testes cobrindo cenários
- [ ] Mensagens de erro úteis
- [ ] Sem perda de dados

## 📦 Arquivos Potencialmente Afetados

**Backend:**

- Pet.ON.Api/Controllers/ServicosController.cs
- Pet.ON.Application/Services/ServicoService.cs
- Pet.ON.Infra/Repositories/ServicoRepository.cs

**Frontend:**

- src/pages/Configuracoes/ServicosPage.vue
- src/components/ListaServicos.vue
- src/composables/useServico.js
- src/services/servicoService.js

## 📊 Complexidade

- **Investigação:** Média
- **Correção:** Baixa-Média
- **Teste:** Baixa
- **Tempo Estimado:** 3-5 horas

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

**Primeira Ação:** Investigar e reproduzir exatamente o bug.

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
