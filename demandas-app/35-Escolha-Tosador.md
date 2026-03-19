# Demanda #35: Função - Escolha de Tosador (validação pendente)

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** To Do  
**Tags:** app, v1  
**Versão:** v1

---

## 📋 Descrição

Implementar funcionalidade que permite usuário escolher/preferir um tosador específico ao agendar serviço de banho e tosa. Sistema deve exibir disponibilidade de tosadores e permitir preferência de profissional.

### Objetivo
- Melhorar UX permitindo preferência
- Aumentar fidelidade (usuário com tosador preferido)
- Otimizar agendamentos por profissional
- Personalizar serviço

---

## 🎯 Critérios de Aceitação

- [ ] Tela de agendamento mostra lista de tosadores
- [ ] Tosador segue com foto e rating
- [ ] Usuário pode preferir tosador ou "qualquer um"
- [ ] Tosadores têm horários disponíveis (API)
- [ ] Disponibilidade por tosador é respeitada
- [ ] Rating/avaliação do tosador exibido
- [ ] Histórico de tosadores já utilizados
- [ ] Opção "Tosador preferido" ou "Qualquer um"
- [ ] Validação de disponibilidade no backend
- [ ] Notação visual clara de preferência no agendamento

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Tela de Agendamento (`screens/Agendamento.js`)
- Novo Componente de Seleção de Tosador
- Serviço de Agendamentos
- Serviço de Tosadores

### APIs Necessárias
- GET `/api/petshops/{id}/tosadores` - Listar tosadores
- GET `/api/tosadores/{id}/disponibilidade?data=2026-03-25` - Horários disponíveis
- GET `/api/tosadores/{id}` - Detalhes (foto, rating)
- POST `/api/agendamentos` - Com campo tosadorId

### Fluxo
1. Usuário seleciona serviço de tosa
2. Sistema lista tosadores do petshop
3. Usuário escolhe tosador ou "qualquer um"
4. Sistema filtra horários disponíveis para ese tosador
5. Usuário confirma agendamento com tosador selecionado

### Estrutura de Dados
```json
{
  "agendamento": {
    "tosadorId": "t123",
    "tosadorPreferido": true,
    "qualquerTosador": false
  },
  "tosador": {
    "id": "t123",
    "nome": "João Silva",
    "foto": "url",
    "rating": 4.9,
    "numeroAvaliacoes": 145,
    "especialidades": ["Tosa Higiênica", "Tosa Criativa"]
  }
}
```

---

## 📊 Estimativa

- **Esforço:** Grande (4-5 dias)
- **Complexidade:** Média-Alta
- **Prioridade:** Média (v1)

---

## 🔗 Dependências

- Backend com dados de tosadores
- Disponibilidade por tosador
- Rating/avaliação de tosadores

---

## 📝 Notas de Implementação

- Validar que tosador selecionado trabalha naquele petshop
- Considerar histórico de tosador preferido do usuário
- Testar race conditions (múltiplos usuários selecionando mesmo tosador)
- Performance com muitos tosadores
- UI responsiva com múltiplas opções

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._