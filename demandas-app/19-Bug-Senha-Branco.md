# Demanda #19: Bug - Senha em Branco

**Projeto:** Pet.ON.App  
**Tipo:** Bug  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Alta

---

## 📋 Descrição

Usuários conseguem cadastrar ou alterar sua senha para um valor em branco, o que causa problemas de segurança e login. O sistema não está validando corretamente a obrigatoriedade do campo senha.

### Impacto
- Falha de segurança (senhas vazias)
- Usuários não conseguem fazer login
- Necessidade de reset de senha
- Problema crítico de autenticação

---

## 🎯 Critérios de Aceitação

- [ ] Campo de senha rejeita valores em branco
- [ ] Mensagem de erro clara quando senha está vazia
- [ ] Validação funciona em cadastro e alteração
- [ ] Requisitos mínimos de senha são verificados (comprimento, caracteres)
- [ ] Botão de envio fica desabilitado se senha for inválida
- [ ] Frontend e Backend validam igualmente
- [ ] Usuários com senha vazia não conseguem logar

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Cadastro (`screens/Cadastro.js`)
- Tela de Dados da Conta (`screens/DadosConta.js`)
- Tela de Registrar Novo Usuário (`screens/RegistrarNovoUsuario.js`)
- Validação de Senha

### Validação de Senha Necessária
```javascript
// Requisitos
- Mínimo 8 caracteres
- Pelo menos 1 letra maiúscula
- Pelo menos 1 letra minúscula
- Pelo menos 1 número
- Pelo menos 1 caractere especial (!@#$%^&*)
```

### Pontos de Validação
1. **Frontend**: Validação em tempo real
2. **Backend**: Validação obrigatória antes de salvar
3. **Database**: Constraint NOT NULL e validação

---

## 📊 Estimativa

- **Esforço:** Pequeno (1-2 dias)
- **Complexidade:** Baixa
- **Prioridade:** Alta

---

## 🔗 Dependências

- Nenhuma

---

## 📝 Checklist de Resolução

- [ ] Adicionar validação no campo de senha (frontend)
- [ ] Adicionar feedback visual de validação
- [ ] Adicionar validação Backend
- [ ] Testar cadastro com senha vazia
- [ ] Testar alteração com senha vazia
- [ ] Testar com senhas fracas
- [ ] Testar com senhas válidas
- [ ] Confirmar mensagens de erro
