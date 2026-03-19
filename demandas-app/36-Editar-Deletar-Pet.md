# Demanda #36: Função - Editar/Deletar Pet

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Alta

---

## 📋 Descrição

Implementar funcionalidade que permite usuário editar informações do pet (nome, raça, idade, foto, etc) ou deletar um pet do perfil. Muito importante para correção de dados ou remoção de pets falecidos/vendidos.

### Objetivo
- Permitir atualização de dados
- Melhorar controle do usuário
- Manter dados atualizados
- Manter histórico refletindo realidade

---

## 🎯 Critérios de Aceitação

- [ ] Usuário consegue acessar lista de seus pets
- [ ] Cada pet tem opção "Editar"
- [ ] Editar abre formulário com dados preenchidos
- [ ] Todos os campos são editáveis (nome, raça, idade, foto)
- [ ] Alterações são salvas
- [ ] Feedback visual após salvar
- [ ] Cada pet tem opção "Deletar"
- [ ] Deletar solicita confirmação
- [ ] Pet deletado remove agendamentos futuros (ou notifica)
- [ ] Histórico/agendamentos passados mantêm referência ao pet
- [ ] Foto pode ser atualizada
- [ ] Validação de campos mantida

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Dados dos Pets (`screens/DadosPets.js`)
- Formulário de Pet (reutilizar de cadastro)
- Serviço de Pets
- Store de Pets

### APIs Necessárias
- GET `/api/pets/{id}` - Obter dados do pet
- PUT `/api/pets/{id}` - Atualizar pet
- DELETE `/api/pets/{id}` - Deletar pet

### Fluxo de Edição
1. Usuário abre lista de pets
2. Seleciona pet e clica "Editar"
3. Formulário abre com dados preenchidos
4. Edita informações desejadas
5. Clica "Salvar"
6. API é chamada com PUT
7. Feedback de sucesso
8. Retorna para lista

### Fluxo de Deleção
1. Usuário clica "Deletar" no pet
2. Modal de confirmação: "Tem certeza que deseja deletar?"
3. Se confirmado, DELETE `/api/pets/{id}`
4. Pet removido da lista
5. Agendamentos futuros cancelados ou transferidos

---

## 📊 Estimativa

- **Esforço:** Médio (2-3 dias)
- **Complexidade:** Média
- **Prioridade:** Alta

---

## 🔗 Dependências

- Tela de cadastro de pet funcionando
- API de pets funcionando

---

## 📝 Checklist de Resolução

- [ ] Implementar tela de listagem de pets
- [ ] Layout de cada pet com opções (editar/deletar)
- [ ] Formulário de edição com dados preenchidos
- [ ] API PUT para atualizar
- [ ] API DELETE com confirmação
- [ ] Tratar agendamentos futuros
- [ ] Feedback visual (loading/sucesso)
- [ ] Testar edição de foto
- [ ] Testar deleção com agendamentos
