# Demanda #42: Função - Inserir Endereço e Cálculo de Distâncias

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** To Do  
**Tags:** app, v1  
**Versão:** v1

---

## 📋 Descrição

Feature combinada que integra cadastro de endereço com cálculo automático de distâcias até petshops. Sistema deve mostrar petshops mais próximos do endereço selecionado e permitir ordenação por proximidade.

### Objetivo
- Mostrar petshops mais próximos
- Facilitar seleção baseada em localização
- Melhorar UX de busca
- Feature essencial de localização

---

## 🎯 Critérios de Aceitação

- [ ] Usuário pode selecionar ou adicionar endereço
- [ ] Sistema calcula distância para cada petshop
- [ ] Petshops ordenados por distância (padrão)
- [ ] Distância exibida em km
- [ ] Pode filtrar por raio (ex: 5km, 10km)
- [ ] Mapa visual (opcional mas desejável)
- [ ] Busca filtra apenas petshops viáveis
- [ ] Performance adequada (cálculo rápido)
- [ ] Atualização de endereço reflete imediatamente
- [ ] Fallback se localização não disponível

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Demanda #25 (Cadastro de Endereço)
- Demanda #26 (Cálculo de Distâncias)
- Tela de Busca (`screens/Buscar.js`)
- Componente de Filtro de Localização
- Serviço de Busca

### Fluxo de Integração
1. Usuário abre tela de busca
2. Sistema usa endereço principal do usuário
3. Para cada petshop:
   - Calcula distância (Haversine)
   - Armazena em cache
4. Exibe petshops ordenados por distância
5. Usuário pode trocar endereço (abre seletor)
6. Distâncias recalculam automaticamente

### API
- GET `/api/lojas?enderecoId=123` - Buscar lojas com distâncias

### Cache
```javascript
{
  "enderecoId": "e123",
  "lojas": [
    {
      "lojaId": "l1",
      "distancia": 2.5,
      "calculadoEm": "2026-03-19T10:00:00"
    }
  ],
  "validoPor": 3600000 // 1 hora
}
```

---

## 📊 Estimativa

- **Esforço:** Grande (5-7 dias)
- **Complexidade:** Alta
- **Prioridade:** Alta (v1)

---

## 🔗 Dependências

- Demanda #25: Cadastro de Endereço
- Demanda #26: Cálculo de Distâncias
- Coordenadas de petshops no BD

---

## 📝 Notas de Implementação

- Reutilizar componentes das features anteriores
- Cache agressivo para performance
- Considerar background updates
- Testar com geolocalização desativada
- Performance com muitos petshops (1000+)

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._