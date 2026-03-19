# Demanda #25: Função - Cadastro de Endereço

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** To Do  
**Tags:** app, v1  
**Versão:** v1

---

## 📋 Descrição

Implementar fluxo completo de cadastro e gerenciamento de endereços do usuário. Sistema deve permitir adicionar múltiplos endereços, definir principal, editar e deletar, com validação de CEP e autocomplete de rua.

### Objetivo
- Facilitar seleção de local para agendamentos
- Suportar múltiplos endereços
- Melhorar UX de checkout
- Dados estruturados para cálculo de distâncias

---

## 🎯 Critérios de Aceitação

- [ ] Usuário pode adicionar novo endereço
- [ ] Campos: CEP, Rua, Número, Complemento, Cidade, Estado
- [ ] Validação de CEP com busca de dados (ViaCEP)
- [ ] Autocomplete de rua baseado em CEP
- [ ] Usuário pode definir um endereço como "principal"
- [ ] Usuário pode editar endereço existente
- [ ] Usuário pode deletar endereço
- [ ] Mínimo 1 endereço obrigatório
- [ ] Endereços persistem no servidor
- [ ] Validação de campos obrigatórios
- [ ] Seleção de endereço durante agendamento

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Nova Tela de Endereços (`screens/Enderecos.js`)
- Formulário de Endereço (componente)
- Serviço de Endereços
- Store de Endereços

### Integrações Externas
- ViaCEP API para busca de endereço via CEP
- Google Maps API (opcional) para autocomplete avançado

### Estrutura de Dados
```json
{
  "enderecos": [
    {
      "id": "123",
      "cep": "03134-000",
      "rua": "Rua da Paz",
      "numero": "100",
      "complemento": "Apto 42",
      "cidade": "São Paulo",
      "estado": "SP",
      "principal": true,
      "latitude": -23.5505,
      "longitude": -46.6333
    }
  ]
}
```

### APIs Necessárias
- GET `/api/enderecos` - Listar endereços
- POST `/api/enderecos` - Criar endereço
- PUT `/api/enderecos/{id}` - Atualizar endereço
- DELETE `/api/enderecos/{id}` - Deletar endereço
- PUT `/api/enderecos/{id}/principal` - Definir como principal

---

## 📊 Estimativa

- **Esforço:** Grande (4-5 dias)
- **Complexidade:** Média-Alta
- **Prioridade:** Média (v1)

---

## 🔗 Dependências

- Integração com ViaCEP
- Backend de endereços implementado
- Autenticação de usuário

---

## 📝 Notas de Implementação

- Usar ViaCEP para validação gratuita
- Considerar Google Places para melhor UX
- Armazenar coordenadas para cálculo posterior de distância
- Validar formato de CEP brasileiro
- Tratar erros de conexão com API externa

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._