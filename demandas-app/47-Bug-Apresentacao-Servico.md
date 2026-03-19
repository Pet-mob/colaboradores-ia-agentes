# Demanda #47: Bug - Apresentação do Serviço Agendado

**Projeto:** Pet.ON.App  
**Tipo:** Bug  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Média

---

## 📋 Descrição

Há problema na exibição/apresentação do serviço agendado. O serviço pode estar truncado, mal posicionado, com informações faltando ou com styling incorreto quando exibido em diferentes telas.

### Impacto
- Usuário não vê informações importantes
- Confusão sobre qual serviço foi agendado
- Problemas ao tentar cancelar/consultar

---

## 🎯 Critérios de Aceitação

- [ ] Serviço agendado exibido de forma clara
- [ ] Nome do serviço não truncado
- [ ] Descrição do serviço visível (se houver)
- [ ] Preço do serviço exibido
- [ ] Duração/tempo estimado do serviço
- [ ] Sem corte visual em diferentes devices
- [ ] Responsive em telas pequenas
- [ ] Ícone descritivo do serviço
- [ ] Informação destacada/fácil leitura
- [ ] Consistente com card de serviço na seleção

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Consulta de Agendamento (`screens/ConsultaAgendamento.js`)
- Tela de Detalhe de Agendamento
- Componente de Serviço Card
- Apresentação em histórico

### Possíveis Causas
- CSS: overflow hidden, text truncate
- Flex layout incorreto
- Fonte muito grande para espaço
- Padding/Margin inadequado
- Wrapping de texto desabilitado
- Dados não carregando completamente

### Dados de Serviço
```json
{
  "servico": {
    "id": "s123",
    "nome": "Banho e Tosa Completa",
    "descricao": "Limpeza completa com tosa padrão",
    "duracao": 90,
    "preco": 85.00,
    "icone": "scissors"
  }
}
```

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

- [ ] Reproduzir bug em qual tela específica?
- [ ] Revisar CSS/styling de apresentação
- [ ] Testar em múltiplos devices
- [ ] Validar dados carregam completamente
- [ ] Melhorar layout se necessário
- [ ] Adicionar ellipsis com tooltip se necessário
