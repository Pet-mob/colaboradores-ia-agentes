# Demanda #26: Função - Cálculo de Distâncias

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** To Do  
**Tags:** app, v1  
**Versão:** v1

---

## 📋 Descrição

Implementar cálculo automático de distância entre a localização do usuário e os petshops. O sistema deve usar geolocalização e coordenadas para calcular e exibir distância, facilitando a escolha baseada em proximidade.

### Objetivo
- Mostrar distância entre usuário e petshop
- Permitir ordenação e filtragem por distância
- Melhorar UX da busca
- Integração com mapas (futuro)

---

## 🎯 Critérios de Aceitação

- [ ] Aplicativo solicita permissão de geolocalização
- [ ] Distância exibida em km (com 1 casa decimal)
- [ ] Cálculo correto usando fórmula Haversine
- [ ] Distância atualizada periodicamente
- [ ] Funciona offline (usa última localização conhecida)
- [ ] Ordenação por distância funciona corretamente
- [ ] Exibição clara na card do petshop
- [ ] Performance adequada com múltiplas lojas
- [ ] Precisão mínima de 100 metros

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Serviço de Geolocalização (novo/melhorado)
- Tela de Busca (`screens/Buscar.js`)
- Card de Loja
- Service de Cálculo de Distância

### Tecnologias
- Expo Location (ou similar) para geolocalização
- Fórmula Haversine para cálculo de distância

### Implementação da Fórmula Haversine
```javascript
function calcularDistancia(lat1, lon1, lat2, lon2) {
  const R = 6371; // Raio da terra em km
  const dLat = (lat2 - lat1) * Math.PI / 180;
  const dLon = (lon2 - lon1) * Math.PI / 180;
  const a = 
    Math.sin(dLat/2) * Math.sin(dLat/2) +
    Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
    Math.sin(dLon/2) * Math.sin(dLon/2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  return R * c;
}
```

### Fluxo
1. Solicitar permissão de localização
2. Obter coordenadas do usuário
3. Para cada loja, calcular distância
4. Armazenar em cache
5. Atualizar periodicamente ou quando usuário se move
6. Usar na ordenação e filtros

---

## 📊 Estimativa

- **Esforço:** Médio (3-4 dias)
- **Complexidade:** Média
- **Prioridade:** Média (v1)

---

## 🔗 Dependências

- Permissão de localização do device
- Coordenadas de cada petshop no banco de dados
- Feature de Cadastro de Endereço (complementar)

---

## 📝 Notas de Implementação

- Testar precisão em diferentes devices
- Considerar cache para não fazer requests frequentes
- Implementar fallback se localização não estiver disponível
- Respeitar privacidade do usuário
- Documentar permissões necessárias em README

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._