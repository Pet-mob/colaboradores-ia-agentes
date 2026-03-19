# Demanda #38: Função - Cadastro de Senha

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Alta

---

## 📋 Descrição

Implementar fluxo de cadastro/criação de senha quando usuário se registra sem senha (ex: login social) ou precisa definir/resetar senha. Deve incluir validação, confirmação e feedback claro.

### Objetivo
- Permitir usuário definir/alterar senha com segurança
- Melhorar fluxo de cadastro
- Validação forte
- UX clara

---

## 🎯 Critérios de Aceitação

- [ ] Tela de cadastro de senha acessível
- [ ] Campo de senha com validação em tempo real
- [ ] Campo de confirmação de senha
- [ ] Validação: mínimo 6 caracteres (conforme demanda #33)
- [ ] Mensagens de validação claras
- [ ] Botão mostra/esconde senha
- [ ] Força da senha indicada visualmente
- [ ] Botão "Salvar" desabilitado até válido
- [ ] Tratamento de erros
- [ ] Sucesso e redirecionamento

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Cadastro (`screens/Cadastro.js`)
- Tela de Registrar Novo Usuário (`screens/RegistrarNovoUsuario.js`)
- Componente de Input de Senha (novo/melhorado)
- Validação de Senha

### UI Components
- Input de Senha (com ícone show/hide)
- Input de Confirmação
- Indicador de Força
- Mensagens de Validação

### Validação
```javascript
const validar = (senha) => {
  const erros = [];
  if (!senha) erros.push("Senha obrigatória");
  if (senha.length < 6) erros.push("Mínimo 6 caracteres");
  return { valido: erros.length === 0, erros };
};
```

### API
- PUT `/api/usuarios/senha` - Atualizar senha
- POST `/api/usuarios/verificar-senha-temporaria` - Para reset flow

---

## 📊 Estimativa

- **Esforço:** Médio (2-3 dias)
- **Complexidade:** Média
- **Prioridade:** Alta

---

## 🔗 Dependências

- Validação de senha definida (demanda #33)
- API de atualização de senha

---

## 📝 Checklist de Resolução

- [ ] Criar/melhorar componente de Input de Senha
- [ ] Adicionar toggle show/hide
- [ ] Implementar validação em tempo real
- [ ] Adicionar campo de confirmação
- [ ] Indicador visual de força
- [ ] API PUT para atualizar
- [ ] Mensagens de erro claras
- [ ] Sucesso com feedback visual
- [ ] Testar fluxo completo
