# Demanda: Link de Envio do PetShop

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #14
**Tipo:** Feature
**Status:** To Do
**Complexidade:** Baixa-Média

---

## 📋 Descrição

Gerar um link único e compartilhável para cada loja que permite clientes acessarem a plataforma diretamente ao perfil da loja sem necessidade de busca. O link deve ser fácil de copiar e compartilhar (redes sociais, WhatsApp, etc).

## 🎯 Objetivos

1. Gerar slug único para cada loja
2. Criar URL acessível com slug
3. Permitir copiar link facilmente
4. Rastrear acessos ao link (analytics)
5. QR Code opcional

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Adicionar campo `Slug` ao modelo `Loja`:
  - Gerado automaticamente a partir do CNPJ ou nome
  - Permitir customização
  - Validar unicidade

- [ ] Criar endpoints:
  - `GET /api/lojas/por-slug/{slug}` - Obter loja por slug
  - `GET /api/loja/meu-link` - Obter link da loja do usuário
  - `PUT /api/loja/slug` - Atualizar slug customizado

- [ ] Implementar rastreamento:
  - Registrar cada acesso ao link
  - Armazenar IP, User-Agent, referência
  - Criar endpoint de analytics: `GET /api/loja/analise-link`

### Frontend (petshop)

- [ ] Criar seção em Configurações:
  - Exibir link da loja
  - Botão "Copiar link" com feedback visual
  - Campo para customizar slug
  - Pré-visualização de URL
  - Botão gerar QR Code (opcional)
  - Analytics simples (visualizações, últimos acessos)

- [ ] Criar página pública `LojaPublica.vue`:
  - Acessível por `/loja/{slug}`
  - Exibir informações da loja
  - Listagem de serviços
  - CTA para agendar
  - Design atrativo (landing page)

- [ ] Composable `useLojaLink.js`:
  - Gerar slug
  - Validar slug
  - Copiar para clipboard
  - Gerar QR Code

## ✅ Critérios de Aceitação

- [ ] Link funcional e acessível
- [ ] Slug validado e único
- [ ] Cópia de link funciona em todos navegadores
- [ ] Página pública responsiva
- [ ] Analytics básico funcional
- [ ] QR Code correto (se implementado)
- [ ] Sem erros de console
- [ ] Performance adequada

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Domain/Entities/Loja.cs (modificar)
- Pet.ON.Domain/Entities/AcessoLoja.cs (novo - rastreamento)
- Pet.ON.Application/DTOs/LojaPublicaDto.cs
- Pet.ON.Application/Services/LojaService.cs (modificar)
- Pet.ON.Infra/Repositories/LojaRepository.cs (modificar)
- Pet.ON.Api/Controllers/LojaPublicaController.cs (novo)

**Frontend:**

- src/pages/Configuracoes/LinkLoja.vue
- src/pages/LojaPublicaPage.vue
- src/components/LinkLojaBanner.vue
- src/composables/useLojaLink.js
- src/services/lojaService.js (modificar)
- src/router/index.js (adicionar rota pública)

## 🔗 Dependências

- Sistema de loja base
- Autenticação
- URL base da aplicação configurada

## 📊 Complexidade

- **Backend:** Baixa-Média
- **Frontend:** Média
- **Integração:** Baixa
- **Tempo Estimado:** 6-8 horas

---

## 📋 Planejamento

_Aguardando processamento pelo Planner Agent..._

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
