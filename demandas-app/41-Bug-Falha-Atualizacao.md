# Demanda #41: Bug - Falha de Atualização

**Projeto:** Pet.ON.App  
**Tipo:** Bug  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Alta

---

## 📋 Descrição

Há falha ao atualizar dados de usuário ou pets. Mudanças não são salvas, aparecem como sucesso mas dados revertém, ou geram erro genérico sem mensagem clara.

### Impacto
- Dados não atualizam
- Usuários perdem confiança
- Problemas com perfil/pets inconsistentes
- Bloqueio de funcionalidade crítica

---

## 🎯 Critérios de Aceitação

- [ ] Atualizações de usuário são salvas corretamente
- [ ] Atualizações de pets são salvas corretamente
- [ ] Atualizações de endereço são salvas corretamente
- [ ] Feedback visual de loading durante atualização
- [ ] Mensagem de sucesso/erro clara
- [ ] Dados persistem após refresh
- [ ] Validação no servidor antes de salvar
- [ ] Rollback se falhar (volta dados anteriores)
- [ ] Log de erro no console para debug

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Dados da Conta (`screens/DadosConta.js`)
- Tela de Dados dos Pets (`screens/DadosPets.js`)
- Serviços de atualização
- Store/State Management

### Possíveis Causas
- Erro na request HTTP (network)
- API retorna erro mas aplicativo mostra sucesso
- Estado local não sincroniza com servidor
- Validação no servidor rejeitando dados
- Timeout na requisição
- Token expirado durante requisição
- Erro no response parsing

### Debugging
1. Verificar Network Tab (DevTools)
2. Ver status code da resposta
3. Ver corpo do erro (error message)
4. Verificar se dados foram salvos no servidor
5. Verificar cache local vs BD

### Implementação Correta
```javascript
const atualizarUsuario = async (dados) => {
  try {
    setCarregando(true);
    const resposta = await api.put('/api/usuarios/me', dados);
    
    if (resposta.status === 200) {
      // Salvar localmente
      dispatch(setUsuario(resposta.data));
      showSuccessToast("Dados atualizados com sucesso");
    }
  } catch (erro) {
    showErrorToast(erro.response?.data?.mensagem || "Erro ao atualizar");
    // NÃO aceitar mudanças - reverter estado
  } finally {
    setCarregando(false);
  }
};
```

---

## 📊 Estimativa

- **Esforço:** Médio-Grande (2-3 dias)
- **Complexidade:** Média-Alta
- **Prioridade:** Alta

---

## 🔗 Dependências

- Acesso a logs da API
- Acesso ao backend para debug

---

## 📝 Checklist de Resolução

- [ ]Reproduzir falha (qual dados não atualiza?)
- [ ] Verificar Network Tab para status de erro
- [ ] Verificar backend logs
- [ ] Testar validação no servidor
- [ ] Verificar token/autenticação
- [ ] Testar fluxo end-to-end
- [ ] Adicionar error boundary
- [ ] Implementar retry logic
- [ ] Validar em production
