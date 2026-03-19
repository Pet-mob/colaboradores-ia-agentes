# Demanda #30: Ajuste - Mensagem de Login/Senha Errada

**Projeto:** Pet.ON.App  
**Tipo:** Ajuste/UX  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Média

---

## 📋 Descrição

Melhorar mensagem de erro exibida quando usuário tenta fazer login com email/senha incorretos. A mensagem atual pode ser vaga, confusa ou não seguir padrão de UX esperado.

### Objetivo
- Mensagem clara e útil ao usuário
- Evitar exposição de informações de segurança
- Padronizar mensagens de erro em todo app
- Melhorar UX

---

## 🎯 Critérios de Aceitação

- [ ] Mensagem de erro clara e amigável
- [ ] Não expõe se email existe ou não no sistema
- [ ] Sugere ação (tentar novamente, recuperar senha)
- [ ] Mensagem padronizada em toda aplicação
- [ ] Cores e styling consistentes
- [ ] Accessible (tamanho fonte, contraste)
- [ ] Link para "Esqueci a Senha" visível
- [ ] Permite novo(s) tenta(s) sem recarregar
- [ ] Toast ou modal (conforme padrão)

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Login (`screens/Login.js`)
- Componente de Erro/Toast
- Serviço de Autenticação

### Mensagem Recomendada
```
"Email ou senha incorretos. Tente novamente ou recupere sua senha."
```

### UX Pattern
```javascript
// Ao receber erro 401/403
showErrorToast("Email ou senha incorretos");
// Limpar campo de senha
// Manter foco no input
// Mostrar link para "Esqueci a senha"
```

### Evitar
- "Usuário não encontrado" (expõe emails válidos)
- "Senha incorreta" (expõe que email exista)
- Mensagens técnicas ("Auth error 401")

---

## 📊 Estimativa

- **Esforço:** Pequeno (0.5-1 dia)
- **Complexidade:** Baixa
- **Prioridade:** Média

---

## 🔗 Dependências

- Nenhuma

---

## 📝 Checklist de Resolução

- [ ] Definir mensagem padrão
- [ ] Atualizr componente de erro
- [ ] Testar tela de login
- [ ] Validar accessibility
- [ ] Verificar consistency com outras mensagens

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._