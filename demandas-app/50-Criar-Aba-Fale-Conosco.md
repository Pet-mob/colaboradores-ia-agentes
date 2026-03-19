# Demanda #50: Função - Criar Aba do Fale Conosco

**Projeto:** Pet.ON.App  
**Tipo:** Feature  
**Status:** Doing  
**Tags:** app  
**Responsável:** Nathan Nery <nbnery@gmail.com>  
**Prioridade:** Alta

---

## 📋 Descrição

Criar nova aba "Fale Conosco" (ou "Contato" / "Suporte") no menu inferior. Esta aba deve permitir usuários entrar em contato com o suporte/empresa através de formulário, chat, email ou telefone.

### Objetivo
- Facilitando suporte ao usuário
- Canal de comunicação direto
- Melhorar satisfação do cliente
- Coletar feedback importante

---

## 🎯 Critérios de Aceitação

- [ ] Nova aba visível no menu inferior
- [ ] Ícone apropriado e intuitivo
- [ ] Tela de contato carrega corretamente
- [ ] Formulário com campos: nome, email, assunto, mensagem
- [ ] Validação de campos obrigatórios
- [ ] Opções de contato: email, telefone, whatsapp ou chat
- [ ] Informações de contato atualizadas (empresa)
- [ ] Envio de mensagem funciona (integração)
- [ ] Confirmação após envio
- [ ] Histórico de tickets/mensagens (opcional)
- [ ] Integração com sistema de tickets (backend)

---

## 💻 Detalhes Técnicos

### Componentes Afetados
- Menu Inferior (`components/menuInferior.js`)
- Nova Tela de Contato (`screens/ContatoEmpresa.js` ou `screens/FaleConosco.js`)
- Novo Componente de Formulário de Contato
- Serviço de Contato (novo)
- Navegação (adicionar rota)

### Opções de Contato
```json
{
  "contato": {
    "telefone": "(11) 1234-5678",
    "whatsapp": "(11) 91234-5678",
    "email": "suporte@petonapp.com.br",
    "horarioAtendimento": "Seg-Sex: 9h-18h"
  }
}
```

### Formulário de Contato
- **Nome**: Text input, obrigatório
- **Email**: Email input, obrigatório, validado
- **Assunto**: Dropdown com categorias (Bug, Sugestão, Reclamação, Faturamento, etc)
- **Mensagem**: Text area, obrigatório, mínimo 10 caracteres
- **Arquivo**: Opcional (screenshot, documento)

### APIs Necessárias
- POST `/api/suporte/tickets` - Criar novo ticket
- GET `/api/suporte/categorias` - Listar categorias de assunto
- Envio por email/integração com sistema de tickets

### Fluxo
1. Usuário abre menu inferior
2. Clica em nova aba "Fale Conosco"
3. Tela abre com formulário e opções de contato
4. Usuário preenche formulário ou clica em whatsapp/email
5. Se formulário: envia e recebe confirmação
6. Se whatsapp/email: abre app nativo

---

## 📊 Estimativa

- **Esforço:** Grande (3-4 dias)
- **Complexidade:** Média
- **Prioridade:** Alta

---

## 🔗 Dependências

- Menu inferior implementado
- Sistema de navegação
- Backend de suporte/tickets
- Informações de contato definidas
- Integração de email ou sistema de tickets

---

## 📝 Notas de Implementação

- Usar `react-native-share` para integração com whatsapp
- Validar email com regex apropriado
- Considerar IA/chatbot para respostas automáticas
- Analytics para rastrear tickets
- Compartilhar ID do ticket com usuário
- Considerar FAQ/artigos antes de contato

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._