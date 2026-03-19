# Demanda #48: Bug - Botões um Sobre o Outro

**Projeto:** Pet.ON.App  
**Tipo:** Bug  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Alta

---

## 📋 Descrição

Há problema de sobreposição visual onde botões se sobrepõem (aparecem um encima do outro), tornando impossível clicar em alguns ou crear confusão visual. Problema de layout/CSS.

### Impacto
- Botões inacessíveis
- Cliques não funcionam como esperado
- Péssima UX
- Interface confusa

---

## 🎯 Critérios de Aceitação

- [ ] Botões alinhados sem sobreposição
- [ ] Espaçamento adequado entre botões
- [ ] Todos botões clicáveis
- [ ] Responsive em diferentes tamanhos
- [ ] Orden de z-index correta
- [ ] Sem corte de texto dos botões
- [ ] Hover/press states visíveis
- [ ] Testes em iOS e Android
- [ ] Visual aprovado

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Depende de qual tela está com problema
- Possíveis: Agendamento, ConsultaAgendamento, configurações
- Qualquer tela com múltiplos botões

### Possíveis Causas
- Position absolute mal posicionado
- Flex layout com conflitos
- z-index inadequado
- Margin/Padding negativo
- Transform scale skew
- Viewport units incorretos

### Solução Padrão
```javascript
// Botões devem estar em container com flex
<View style={styles.buttonContainer}>
  <TouchableOpacity style={styles.button}>
    <Text>Botão 1</Text>
  </TouchableOpacity>
  
  <TouchableOpacity style={styles.button}>
    <Text>Botão 2</Text>
  </TouchableOpacity>
</View>

// Styles
buttonContainer: {
  flexDirection: 'row', // ou 'column'
  justifyContent: 'space-between',
  gap: 10
},
button: {
  flex: 1,
  padding: 15
}
```

---

## 📊 Estimativa

- **Esforço:** Pequeno (0.5-1 dia)
- **Complexidade:** Baixa
- **Prioridade:** Alta

---

## 🔗 Dependências

- Nenhuma

---

## 📝 Checklist de Resolução

- [ ] Reproduzir bug em qual tela?
- [ ] Fazer print/screenshot do problema
- [ ] Revisar CSS/flexbox layout
- [ ] Testar em múltiplos devices
- [ ] Ajustar spacing/alignment
- [ ] Validar z-index
- [ ] Testar cliques em todos botões

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._