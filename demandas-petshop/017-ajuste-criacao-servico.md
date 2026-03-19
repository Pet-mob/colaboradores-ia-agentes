# Demanda: Ajuste - Criação de Serviço

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #17
**Tipo:** Ajuste/Bug
**Status:** To Do
**Complexidade:** Média

---

## 📋 Descrição

Revisar e ajustar o formulário de criação de serviço. Melhorias na validação, UX, adição de novos campos e correção de bugs reportados no processo de criação.

## 🎯 Objetivos

1. Melhorar validações de entrada
2. Aprimorar UX do formulário
3. Adicionar campos faltantes
4. Corrigir bugs conhecidos
5. Melhorar feedback ao usuário

## 📌 Requisitos Funcionais

### Campos a Revisar/Adicionar

- [ ] Nome do serviço (validar tamanho e caracteres especiais)
- [ ] Descrição (validar tamanho máximo)
- [ ] Preço (validar formato, mínimo/máximo)
- [ ] Duração (em minutos, validar)
- [ ] Categoria (dropdown com opções)
- [ ] Portaria? (Pode ser aplicado a que portes/tamanhos)
- [ ] Imagem do serviço (upload)
- [ ] Status (Ativo/Inativo)
- [ ] Período de agendamento (opcional)
- [ ] Disponibilidade por dia da semana

### Validações Implementar

- [ ] Nome não pode estar vazio
- [ ] Nome deve ter entre 3 e 100 caracteres
- [ ] Descrição máximo 500 caracteres
- [ ] Preço deve ser > 0
- [ ] Duração deve ser múltiplo de 15 minutos
- [ ] Categoria selecionada obrigatória
- [ ] Imagem com validação de tipo e tamanho
- [ ] Alertar se descrição vazia
- [ ] Validar disponibilidade de agendamento (não pode estar toda desativada)

### UX Improvements

- [ ] Salvar rascunho automaticamente (localStorage)
- [ ] Botão "Previewizar" serviço
- [ ] Tooltips explicativos em campos
- [ ] Indicador de campos obrigatórios vs opcionais
- [ ] Feedback visual em tempo real de validação
- [ ] Mensagens de erro claras e construtivas
- [ ] Confirmação antes de sair se houver mudanças não salvas

### Backend Adjustments

- [ ] Revisar DTOs e validações
- [ ] Adicionar validações em nível API
- [ ] Melhorar mensagens de erro
- [ ] Adicionar logs apropriados
- [ ] Validar permissões corretamente

## ✅ Critérios de Aceitação

- [ ] Todas as validações funcionam
- [ ] Formulário salva rascunho
- [ ] Mensagens de erro claras
- [ ] Previewização funciona
- [ ] Responsivo mobile
- [ ] Sem erros de console
- [ ] Performance adequada
- [ ] Testes para novas validações
- [ ] Documentação de campos atualizada

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Application/DTOs/ServicoCreateDto.cs
- Pet.ON.Application/Services/ServicoService.cs
- Pet.ON.Api/Controllers/ServicosController.cs
- Pet.ON.Api/Validators/ServicoValidator.cs

**Frontend:**

- src/components/Forms/FormularioServico.vue
- src/composables/useFormularioServico.js
- src/composables/useDebounce.js (para validação em tempo real)
- src/services/servicoService.js
- src/**tests**/unit/components/FormularioServico.spec.js (novo/atualizar)

## 🔗 Dependências

- Sistema de serviços base
- Sistema de categorias
- Sistema de portaria/tamanhos
- Autenticação

## 📊 Complexidade

- **Backend:** Média
- **Frontend:** Média
- **Integração:** Baixa
- **Tempo Estimado:** 6-8 horas

---

## 💻 Implementação

_Aguardando processamento pelo Developer Agent..._

---

## ✅ Revisão de Qualidade

_Aguardando processamento pelo QA Agent..._
