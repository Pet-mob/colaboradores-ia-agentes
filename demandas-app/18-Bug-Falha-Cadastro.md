# Demanda #18: Bug - Falha de Cadastro de Usuário

**Projeto:** Pet.ON.App  
**Tipo:** Bug  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Crítica

---

## 📋 Descrição

Usuários enfrentam falhas ao tentar se cadastrar na plataforma. O fluxo de registro não está completando corretamente, impedindo novos usuários de acessar a aplicação. Isso representa um bloqueio crítico de onboarding.

### Impacto
- Novos usuários não conseguem se registrar
- Churn de usuários no onboarding
- Redução de base de usuários
- Bloqueio crítico

---

## 🎯 Critérios de Aceitação

- [ ] Formulário de cadastro abre corretamente
- [ ] Campos obrigatórios são validados
- [ ] Senha é aceita e validada corretamente
- [ ] Email é validado sem erros falsos
- [ ] Telefone é formatado e validado
- [ ] Dados são salvos no servidor
- [ ] Usuário recebe confirmação (email/SMS)
- [ ] Usuário consegue fazer login após cadastro
- [ ] Mensagens de erro são claras

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Cadastro (`screens/Cadastro.js`)
- Tela de Registrar Novo Usuário (`screens/RegistrarNovoUsuario.js`)
- Serviço de Autenticação
- Validação de email e telefone

### Possíveis Causas
- Erro na validação de email/telefone
- Falha na chamada da API de registro
- Problema de conectividade
- Inconsistência entre frontend e backend
- Database constraints violados
- Token JWT não gerado corretamente

### APIs Envolvidas
- POST `/api/auth/registrar` 
- POST `/api/auth/validar-email`
- POST `/api/auth/validar-telefone`

---

## 📊 Estimativa

- **Esforço:** Grande (2-3 dias)
- **Complexidade:** Alta
- **Prioridade:** Crítica

---

## 🔗 Dependências

- Acesso a logs da API
- Acesso ao banco de dados
- Coordenação com Backend

---

## 📝 Checklist de Resolução

- [ ] Acessar erro logs do servidor
- [ ] Testar cada campo de validação
- [ ] Verificar resposta da API
- [ ] Testar fluxo end-to-end
- [ ] Validar confirmação de email
- [ ] Testar login após cadastro
- [ ] Confirmar em ambientes (dev/staging/prod)
