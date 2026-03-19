# Demanda #39: Bug - Duplicação de Cadastro

**Projeto:** Pet.ON.App  
**Tipo:** Bug  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Alta

---

## 📋 Descrição

Há um problema onde usuários conseguem criar múltiplas contas com mesmo email/CPF. Sistema não está validando unicidade de email durante o cadastro, permitindo duplicação de registros.

### Impacto
- Duplicação de registros
- Inconsistência de dados
- Possibilidade de fraude
- Problemas com comunicação (múltiplos emails)

---

## 🎯 Critérios de Aceitação

- [ ] Validação de email único antes de aceitar cadastro
- [ ] Mensagem de erro clara: "Email já cadastrado"
- [ ] Validação ocorre no frontend (feedback rápido)
- [ ] Validação ocorre no backend (segurança)
- [ ] Email é case-insensitive na busca
- [ ] Whitespace é trimmed antes de validar
- [ ] CPF também é único (se coletado)
- [ ] Sugestão: "Fazer login" se email já existe
- [ ] Sem duplicatas no banco de dados
- [ ] Constraint ao nível do DB (unique index)

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Cadastro (`screens/Cadastro.js`)
- Validação de Cadastro
- Serviço de Autenticação
- Banco de Dados

### Validação Frontend
```javascript
const [email, setEmail] = useState('');
const [erro, setErro] = useState('');

const validarEmail = async (email) => {
  if (!email) return;
  const valido = await api.get(`/api/auth/verificar-email?email=${email}`);
  setErro(valido.existe ? "Email já cadastrado" : "");
};
```

### Constraint no Database
```sql
ALTER TABLE usuarios ADD CONSTRAINT UQ_Email UNIQUE (email);
ALTER TABLE usuarios ADD INDEX idx_email (email);
```

### API
- GET `/api/auth/verificar-email?email=user@email.com` - Verifica se email existe
- POST `/api/auth/registrar` - Com validação adicional

---

## 📊 Estimativa

- **Esforço:** Médio (1-2 dias)
- **Complexidade:** Média
- **Prioridade:** Alta

---

## 🔗 Dependências

- Acesso ao banco de dados
- API capaz de verificar email

---

## 📝 Checklist de Resolução

- [ ] Adicionar validação frontend
- [ ] Criar endpoint de verificação de email
- [ ] Adicionar constraint UNIQUE no DB
- [ ] Testar cadastro com email duplicado
- [ ] Testar com variações (maiúsculas, espaços)
- [ ] Limpeza manual de duplicatas existentes
- [ ] Validar mensagem de erro
- [ ] Testar race condition (duplo submit rápido)
