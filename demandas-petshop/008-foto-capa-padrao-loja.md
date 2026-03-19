# Demanda: Foto de Capa Padrão para Loja

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #8
**Tipo:** Feature
**Status:** To Do
**Complexidade:** Baixa

---

## 📋 Descrição

Implementar funcionalidade para definir uma foto de capa padrão para loja que seja exibida quando nenhuma foto customizada foi enviada. A foto deve ser gerenciável por administrador.

## 🎯 Objetivos

1. Permitir upload de foto de capa padrão
2. Armazenar foto no sistema
3. Exibir foto padrão quando loja não tiver foto customizada
4. Permitir atualização de foto padrão

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Criar endpoint `POST /api/loja/capa-padrao` para upload
- [ ] Criar endpoint `GET /api/loja/capa-padrao` para obter foto
- [ ] Criar endpoint `PUT /api/loja/capa-padrao` para atualizar
- [ ] Armazenar arquivo em Storage (local ou Azure Blob)
- [ ] Validar tipo de arquivo (imagem)
- [ ] Validar tamanho máximo (5MB)

### Frontend (petshop)

- [ ] Criar seção em Configurações para upload de capa padrão
- [ ] Componente input file com preview
- [ ] Mostrar foto atual
- [ ] Botão para remover/substituir
- [ ] Feedback visual durante upload (spinner)
- [ ] Mensagem de sucesso/erro

### Exibição

- [ ] Usar foto padrão em dashboard se loja não tiver foto
- [ ] Usar foto padrão em perfil público da loja
- [ ] Cache apropriado da imagem

## ✅ Critérios de Aceitação

- [ ] Upload funcional
- [ ] Validações de tipo e tamanho
- [ ] Foto aparece corretamente em todas as telas
- [ ] Compatível mobile
- [ ] Tratamento de erros
- [ ] Performance de carregamento adequada
- [ ] Sem erros de console

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Api/Controllers/LojaController.cs
- Pet.ON.Application/Services/LojaService.cs
- Pet.ON.Application/DTOs/UploadDto.cs
- Pet.ON.Infra/Services/StorageService.cs
- appsettings.json (configuração de storage)

**Frontend:**

- src/pages/Configuracoes/CapaLojaSettings.vue
- src/components/Forms/UploadFotoCapaForm.vue
- src/composables/useUploadFoto.js
- src/services/lojaService.js
- src/pages/DashboardPage.vue

## 🔗 Dependências

- Sistema de autenticação
- Storage configurado (local ou Azure)
- Permissões de administrador

## 📊 Complexidade

- **Backend:** Baixa-Média
- **Frontend:** Baixa
- **Integração:** Baixa
- **Tempo Estimado:** 4-5 horas

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
