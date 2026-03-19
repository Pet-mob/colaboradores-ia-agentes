# Demanda #33: Ajuste - Retirar Validação de Exigências de Senha

**Projeto:** Pet.ON.App  
**Tipo:** Ajuste  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Média

---

## 📋 Descrição

Remover ou reduzir as exigências/validações de criação de senha muito rigorosas. Validação pode estar pedindo requisitos demais (maiúsculas, minúsculas, números, caracteres especiais) tornando difícil para usuários criarem senhas memoráveis.

### Objetivo
- Melhorar UX de cadastro
- Simplificar criação de senha
- Manter segurança básica
- Reduzir fricção no onboarding

---

## 🎯 Critérios de Aceitação

- [ ] Requisito mínimo: 6-8 caracteres
- [ ] Sem exigência de maiúsculas
- [ ] Sem exigência de números
- [ ] Sem exigência de caracteres especiais
- [ ] Validação em tempo real mostra requisitos
- [ ] Mensagem clara de requisitos mínimos
- [ ] Usuário consegue ver requisito que falta
- [ ] Feedback visual positivo quando válida
- [ ] Segurança mínima mantida

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Cadastro (`screens/Cadastro.js`)
- Tela de Registrar Novo Usuário (`screens/RegistrarNovoUsuario.js`)
- Validação de Senha
- Componente de Input de Senha

### Validação Simplificada
```javascript
// Novo requisito
const validarSenha = (senha) => {
  if (senha.length < 6) return false; // Mínimo 6 caracteres
  return true;
};

// Antigo provavelmente similar a:
// - 8+ caracteres
// - 1 maiúscula
// - 1 minúscula
// - 1 número
// - 1 caractere especial
```

### Feedback Visual
- Campo vazio: "Crie uma senha"
- 1-5 caracteres: "Mínimo 6 caracteres"
- 6+ caracteres: "✓ Válido"

---

## 📊 Estimativa

- **Esforço:** Pequeno (1 dia)
- **Complexidade:** Baixa
- **Prioridade:** Média

---

## 🔗 Dependências

- Aprovação de segurança
- Validação backend também reduzida

---

## 📝 Checklist de Resolução

- [ ] Definir novos requisitos com segurança/produto
- [ ] Atualizar validação frontend
- [ ] Atualizar validação backend
- [ ] Atualizar mensagens de validação
- [ ] Testar fluxo de cadastro
- [ ] Validar UX/clareza
