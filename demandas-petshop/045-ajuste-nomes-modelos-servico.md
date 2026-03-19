# Demanda: Ajuste - Alterar os Nomes dos "Modelos de Serviço"

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #45
**Tipo:** Ajuste/Refatoração
**Status:** Doing
**Complexidade:** Baixa-Média

---

## 📋 Descrição

Renomear/desambiguar a terminologia usada para "Modelos de Serviço". Pode ser que o termo atual esteja confuso (conflitando com outros conceitos) ou não represente bem a funcionalidade.

## 🎯 Objetivos

1. Clarificar terminologia
2. Dessambiguar conceitos
3. Atualizar em todos os lugares (frontend, backend, docs)
4. Evitar confusão futura
5. Melhorar UX e compreensão

## 📌 Requisitos Funcionais

### Investigação Inicial

**Contexto Necessário:**

- [ ] Qual é o termo atual exato? ("Modelos de Serviço", "Templates", "Categorias"?)
- [ ] O que representa? (Padrões de serviço? Categorias? Templates reutilizáveis?)
- [ ] Qual é a confusão causada?
- [ ] Qual é o novo termo proposto?

### Exemplos Possíveis

Se for categorias/tipos de serviço:

- Termo atual: "Modelos"
- Novo termo: "Categorias de Serviço" ou "Tipos de Serviço"

Se for templates reutilizáveis:

- Termo atual: "Modelos"
- Novo termo: "Templates de Serviço" ou "Serviços Padrão"

Se for templates de agendamento:

- Termo atual: "Modelos"
- Novo termo: "Horários Padrão" ou "Slots Padrão"

### Mudanças Backend

- [ ] Renomear classe/entidade se aplicável
- [ ] Renomear variáveis e propriedades
- [ ] Renomear endpoints de API se necessário
- [ ] Atualizar documentação de API
- [ ] Atualizar comentários e logs
- [ ] Migration no banco se houver campo

### Mudanças Frontend

- [ ] Renomear componentes se clareza
- [ ] Atualizar labels e placeholders
- [ ] Atualizar mensagens de erro
- [ ] Atualizar tooltips
- [ ] Atualizar títulos de páginas
- [ ] Atualizar variáveis em composables

### Documentação

- [ ] Atualizar README
- [ ] Atualizar comentários de código
- [ ] Atualizar documentação de API
- [ ] Atualizar documentação de features
- [ ] Atualizar exemplos

## ✅ Critérios de Aceitação

- [ ] Novo termo consistente em todo código
- [ ] Frontend refletindo novo termo
- [ ] Backend refletindo novo termo
- [ ] Documentação atualizada
- [ ] Sem quebra de funcionalidade
- [ ] Mensagens de erro claras
- [ ] Sem erros de console
- [ ] Testes passando

## 📦 Arquivos Potencialmente Afetados

Será determinado após definir exatamente o que renomear, mas tipicamente:

**Backend:**

- Arquivos de entidades/modelos
- Services
- Controllers
- DTOs
- Migrations
- appsettings

**Frontend:**

- Componentes de listagem
- Formulários
- Composables
- Services client
- Router (labels)

## 📊 Complexidade

- **Investigação:** Baixa
- **Backend:** Baixa-Média (busca e replace)
- **Frontend:** Baixa-Média (busca e replace)
- **Testes:** Baixa
- **Tempo Estimado:** 3-5 horas

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

**Primeira Ação:** Confirmar qual é o termo atual e qual é o novo termo proposto.

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
