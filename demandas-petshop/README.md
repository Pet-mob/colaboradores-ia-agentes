# 📋 Demandas - PetShop

Biblioteca de demandas estruturadas para treinar agentes de IA no desenvolvimento do projeto PetShop.

## 📁 Estrutura

```
demandas-petshop/
├── README.md (este arquivo)
├── 006-criar-promocao-geral.md
├── 008-foto-capa-padrao-loja.md
├── 012-modo-servico-subitens.md
├── 013-sistema-confirmacao-servicos.md
├── 014-link-envio-petshop.md
├── 015-selo-qualidade-loja.md
├── 017-ajuste-criacao-servico.md
├── 020-mostrar-porte-servicos.md
├── 021-criacao-porte-tipo-todos.md
├── 022-ajuste-hover-grafico.md
├── 044-bug-dados-incorretos.md
├── 045-ajuste-nomes-modelos-servico.md
├── 046-bug-apresentacao-servico.md
├── 051-aba-fale-conosco.md
├── 052-bug-responsivo-login.md
├── 053-bug-responsivo-agendamento.md
├── 054-bug-servicos-nao-deletaveis.md
└── 055-funcao-confirmacao-informacoes.md
```

## 📊 Resumo das Demandas

| ID  | Título                       | Tipo    | Complexidade | Status |
| --- | ---------------------------- | ------- | ------------ | ------ |
| #6  | Criar Promoção Geral         | Feature | Média        | To Do  |
| #8  | Foto de Capa Padrão          | Feature | Baixa        | To Do  |
| #12 | Serviço com Sub-itens        | Feature | Alta         | To Do  |
| #13 | Sistema de Confirmação       | Feature | Média-Alta   | Doing  |
| #14 | Link de Envio                | Feature | Baixa-Média  | To Do  |
| #15 | Selo de Qualidade            | Feature | Média        | To Do  |
| #17 | Ajuste: Criação de Serviço   | Ajuste  | Média        | To Do  |
| #20 | Mostrar Porte nos Serviços   | Feature | Média        | Doing  |
| #21 | Porte Tipo "Todos"           | Feature | Baixa-Média  | Doing  |
| #22 | Ajuste: Hover do Gráfico     | Ajuste  | Baixa        | To Do  |
| #44 | Bug: Dados Incorretos        | Bug     | Investigação | Doing  |
| #45 | Ajuste: Nomes de Modelos     | Ajuste  | Baixa-Média  | Doing  |
| #46 | Bug: Apresentação Serviço    | Bug     | Investigação | Doing  |
| #51 | Aba: Fale Conosco            | Feature | Média        | Doing  |
| #52 | Bug: Responsivo Login        | Bug     | Baixa        | To Do  |
| #53 | Bug: Responsivo Agendamento  | Bug     | Baixa-Média  | To Do  |
| #54 | Bug: Serviços Não Deletáveis | Bug     | Baixa-Média  | To Do  |
| #55 | Confirmação com Informações  | Feature | Média        | To Do  |

## 🎯 Como Usar

### Para o Agente

1. **Selecionar uma demanda:** Escolher um arquivo .md da lista acima
2. **Ler a demanda completa:** Revisar descrição, requisitos e critérios
3. **Implementar:** Seguir especificações de Backend, Frontend e Integração
4. **Testar:** Realizar testes conforme critérios de aceitação
5. **Relatar:** Atualizar seções de Implementação e Revisão

### Estrutura Padrão de Cada Demanda

Cada arquivo segue um padrão:

```markdown
# Demanda: [Título]

**Projeto:** PetShop.WebApp ou Pet.ON.Api Backend
**ID:** #[número]
**Tipo:** Feature | Bug | Ajuste/Refatoração
**Status:** To Do | Doing | Done
**Complexidade:** Baixa | Baixa-Média | Média | Média-Alta | Alta

---

## 📋 Descrição

Explicação clara do que fazer

## 🎯 Objetivos

Lista de objetivos principais

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- Lista de implementações necessárias

### Frontend (petshop)

- Lista de implementações necessárias

### Composables/Services

- Lógica reutilizável

## ✅ Critérios de Aceitação

Checklist de validação

## 📦 Arquivos/Componentes Afetados

Quais arquivos modificar/criar

## 🔗 Dependências

O que precisa estar funcionando antes

## 📊 Complexidade

Estimativas de tempo e dificuldade

---

## 💻 Implementação

_Aguardando processamento_

---

## ✅ Revisão de Qualidade

_Aguardando processamento_
```

## 🏗️ Stack do Projeto

### Frontend

- **Framework:** Vue 3
- **Build:** Vue CLI + Vite
- **Roteamento:** Vue Router 4
- **State:** Pinia
- **Testes:** Vitest + @vue/test-utils
- **Styling:** CSS + SCSS
- **Icons:** Lucide Vue
- **Charts:** Chart.js + Vue-Chartjs
- **Real-time:** SignalR

### Backend

- **Framework:** .NET 6+
- **Arquitetura:** Clean Architecture (Domain, Application, Infra, API)
- **ORM:** Entity Framework Core
- **Autenticação:** JWT + SignalR
- **API:** REST
- **Testes:** NUnit/xUnit

## 📝 Notas Importantes

### Para Features

- Especificar campos do DTO
- Documentar endpoints da API
- Listar componentes Vue no frontend
- Incluir validações obrigatórias
- Mencionar integrações com sistemas existentes (SignalR, autenticação)

### Para Bugs

- Explicar o que está errado
- Listar possíveis causas
- Incluir checklist de investigação
- Documentar como reproduzir
- Definir comportamento esperado

### Para Ajustes

- Ser específico sobre o que melhorar
- Listar todos os lugares afetados
- Considerar impacto em UX
- Validar compatibilidade mobile

## 🔄 Processo de Atualização

1. **Ao iniciar uma demanda:** Documentar status em `Status: Doing`
2. **Durante implementação:** Atualizar seção "Implementação" com progresso
3. **Ao completar:** Marcar `Status: Done` e documentar período de testes
4. **Após QA:** Documentar resultados na seção "Revisão de Qualidade"

## 📞 Suporte

Para esclarecer detalhes de uma demanda:

1. Revisar seções de "Requisitos" e "Critérios de Aceitação"
2. Consultar contexto do projeto (arquivos ARCHITECTURE.md, documentação)
3. Verificar dependências listadas
4. Se necessário, investigar código existente

## 🚀 Próximas Etapas

Após completar uma demanda:

- [ ] Executar todos os testes
- [ ] Revisar código para qualidade
- [ ] Validar critérios de aceitação
- [ ] Documentar decisões de implementação
- [ ] Solicitar revisão conforme necessário

---

**Última Atualização:** Março 2026
**Total de Demandas:** 18
**Status:** Pronto para treinamento de agentes
