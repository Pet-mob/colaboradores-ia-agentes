# Demanda #40: Bug - Teclado Impede Visão Durante Digitação

**Projeto:** Pet.ON.App  
**Tipo:** Bug  
**Status:** Doing  
**Tags:** app  
**Prioridade:** Alta

---

## 📋 Descrição

Quando usuário toca em campos de input, teclado virtual aparece e não empurra formulário para cima, obstruindo a visualização do campo que está sendo digitado. Especialmente problemático em telefones com telas pequenas.

### Impacto
- Péssima UX
- Usuários não conseguem ver o que digitam
- Formulários mais difíceis de preencher
- Afeta cadastro e login

---

## 🎯 Critérios de Aceitação

- [ ] Teclado virtual não obstrui campo de input
- [ ] Formulário sobe automaticamente quando teclado aparece
- [ ] Campo digitado fica visível no topo da tela
- [ ] Funciona em iOS (react-native-keyboard-aware)
- [ ] Funciona em Android
- [ ] Scroll automático para mostrar input
- [ ] Comportamento suave (não "salta")
- [ ] Sem overflow/corte de conteúdo
- [ ] Testes em diferentes tamanhos de tela

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Todas as telas com formulários
- Tela de Cadastro (`screens/Cadastro.js`)
- Tela de Login
- Tela de Agendamento
- Wrapper de Inputs

### Solução Recomendada
Usar `react-native-keyboard-aware-scroll-view` ou `KeyboardAvoidingView` do React Native.

```javascript
import { KeyboardAvoidingView } from 'react-native';
// OU
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';

// Envolver formulário
<KeyboardAwareScrollView>
  <TextInput />
  <TextInput />
</KeyboardAwareScrollView>
```

### Componente Existente
Parece haver `KeyboardAvoidingWrapper.js` - verificar implementação.

### Testando
- Tocar em campos (especialmente últimos)
- Observar se teclado obstrui ou se forma empurra para cima
- Testar em iPhone SE (tela pequena)
- Testar em Android com teclado grande

---

## 📊 Estimativa

- **Esforço:** Médio (1-2 dias)
- **Complexidade:** Média
- **Prioridade:** Alta

---

## 🔗 Dependências

- Implementação de KeyboardAwareScrollView

---

## 📝 Checklist de Resolução

- [ ] Verificar implementação de KeyboardAvoidingWrapper
- [ ] Instalar biblioteca (se necessário)
- [ ] Envolver formulários com componente
- [ ] Validar comportamento em iOS
- [ ] Validar comportamento em Android
- [ ] Testar em múltiplos devices
- [ ] Testar com teclado landscape
- [ ] Remover KeyboardAvoidingView nativo se conflita
