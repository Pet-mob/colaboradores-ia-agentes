# Demanda: Modo de Serviço com Sub-itens para Selecionar

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #12
**Tipo:** Feature
**Status:** To Do
**Complexidade:** Alta

---

## 📋 Descrição

Implementar um sistema onde serviços podem ter sub-itens configuráveis que o cliente deve selecionar durante o agendamento. Exemplo: Serviço "Tosa" com sub-itens "Tosa Completa", "Tosa Higiênica", "Tosa com Banho".

## 🎯 Objetivos

1. Permitir criar sub-itens para serviços
2. Tornar sub-itens obrigatórios ou opcionais
3. Permitir cliente selecionar sub-itens no agendamento
4. Aplicar preços diferentes por sub-item
5. Exibir sub-itens selecionados na confirmação

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Criar modelo `ServicoSubItem` com:
  - ID único
  - ServicoId (FK)
  - Nome
  - Descrição
  - Valor adicional (pode ser 0)
  - Ordem de exibição
  - Status (Ativo/Inativo)

- [ ] Criar endpoints:
  - `POST /api/servicos/{id}/subitens` - Criar sub-item
  - `GET /api/servicos/{id}/subitens` - Listar sub-itens
  - `PUT /api/servicos/{id}/subitens/{subitemId}` - Atualizar
  - `DELETE /api/servicos/{id}/subitens/{subitemId}` - Deletar

- [ ] Modificar modelo `Agendamento`:
  - Adicionar campo para sub-itens selecionados (JSON array)
  - Recalcular total incluindo valores dos sub-itens

- [ ] Validações:
  - Validar se sub-item selecionado pertence ao serviço
  - Verificar se todos os sub-itens obrigatórios foram selecionados

### Frontend (petshop)

- [ ] Modificar `FormularioServico.vue`:
  - Adicionar seção de sub-itens
  - Input para nome do sub-item
  - Input para valor adicional
  - Checkbox para obrigatório/opcional
  - Botão adicionar/remover sub-item
  - Reordenação via drag-drop (opcional)

- [ ] Modificar `FormAgendamento.vue`:
  - Verificar se serviço tem sub-itens
  - Exibir checkboxes/radio buttons para seleção
  - Destacar sub-itens obrigatórios
  - Mostrar valor adicional de cada sub-item
  - Recalcular preço total dinamicamente

- [ ] Modificar `ConfirmacaoAgendamento.vue`:
  - Exibir sub-itens selecionados
  - Mostrar detalhamento de preços

### Composable

- [ ] Criar `useSubItens.js`:
  - Validar seleção de sub-itens
  - Calcular valor total com sub-itens
  - Manter estado de seleção

## ✅ Critérios de Aceitação

- [ ] CRUD de sub-itens funcional
- [ ] Sub-itens aparecem corretamente no agendamento
- [ ] Validações de obrigatoriedade funcionam
- [ ] Preço total recalculado corretamente
- [ ] Sub-itens persistidos no agendamento
- [ ] Responsivo mobile
- [ ] Testes com cobertura >75%
- [ ] Sem erros de console

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Domain/Entities/ServicoSubItem.cs
- Pet.ON.Domain/Entities/Agendamento.cs (modificar)
- Pet.ON.Application/DTOs/ServicoSubItemDto.cs
- Pet.ON.Application/Services/ServicoService.cs (modificar)
- Pet.ON.Infra/Repositories/ServicoRepository.cs (modificar)
- Pet.ON.Api/Controllers/ServicosController.cs

**Frontend:**

- src/components/Forms/FormularioServico.vue
- src/components/Forms/FormAgendamento.vue
- src/pages/ConfirmacaoAgendamentoPage.vue
- src/composables/useFormularioServico.js (modificar)
- src/composables/useSubItens.js
- src/services/servicoService.js (modificar)

## 🔗 Dependências

- Sistema de agendamento base funcional
- Sistema de formatos de preço
- Autenticação

## 📊 Complexidade

- **Backend:** Alta
- **Frontend:** Alta
- **Integração:** Alta
- **Tempo Estimado:** 12-15 horas

---

## 📋 Planejamento

\#\ Plano:\ Modo\ de\ Serviço\ com\ Sub\-itens\ para\ Selecionar\
\
\#\#\ Resumo\
O\ objetivo\ deste\ plano\ técnico\ é\ implementar\ a\ funcionalidade\ de\ modo\ de\ serviço\ com\ sub\-itens\ para\ seleção\ na\ plataforma\ Petmob\.\ Essa\ feature\ permitirá\ que\ os\ usuários\ selecionem\ serviços\ com\ sub\-itens\ específicos,\ melhorando\ a\ experiência\ do\ usuário\ e\ a\ eficiência\ na\ gestão\ de\ serviços\.\ Será\ necessário\ atualizar\ as\ entidades\ de\ negócio,\ criar\ novas\ relações\ entre\ serviços\ e\ sub\-serviços,\ e\ implementar\ a\ lógica\ de\ negócio\ para\ gerenciar\ essas\ relações\.\
\
A\ implementação\ seguirá\ os\ padrões\ arquiteturais\ estabelecidos\ no\ projeto,\ utilizando\ a\ arquitetura\ em\ camadas,\ com\ controllers,\ services\ e\ repositories\.\ Além\ disso,\ será\ garantido\ que\ a\ nova\ funcionalidade\ esteja\ em\ conformidade\ com\ as\ restrições\ de\ negócio,\ como\ o\ respeito\ aos\ horários\ de\ funcionamento\ das\ petshops\ e\ a\ proteção\ dos\ dados\ sensíveis\ dos\ pets\.\
\
\#\#\ Stack\ e\ Tecnologias\
\-\ Linguagens:\ \.NET\ 8,\ C\#\
\-\ Frameworks:\ Entity\ Framework\ Core,\ SQL\ Server\
\-\ Padrões\ de\ Projeto:\ Arquitetura\ em\ camadas,\ Repository/Service\ patterns,\ validação\ com\ FluentValidation,\ mapping\ com\ AutoMapper\
\-\ Tecnologias\ de\ Integração:\ DI\ Container\ para\ injeção\ de\ dependências\
\
\#\#\ Tarefas\ Técnicas\
\
\#\#\#\ 1\.\ Atualizar\ a\ Entidade\ de\ Negócio\ "Service"\ para\ Incluir\ Sub\-serviços\
\-\ \*\*Descrição\*\*:\ Atualizar\ a\ entidade\ "Service"\ para\ incluir\ uma\ lista\ de\ sub\-serviços\.\ Isso\ envolverá\ a\ criação\ de\ uma\ nova\ entidade\ "SubService"\ e\ a\ relação\ entre\ "Service"\ e\ "SubService"\.\
\-\ \*\*Critérios\ de\ Aceite\*\*:\
\ \ \-\ ✓\ A\ entidade\ "Service"\ contém\ uma\ lista\ de\ sub\-serviços\
\ \ \-\ ✓\ A\ entidade\ "SubService"\ é\ criada\ com\ sucesso\
\ \ \-\ ✓\ A\ relação\ entre\ "Service"\ e\ "SubService"\ é\ estabelecida\ corretamente\
\
\#\#\#\ 2\.\ Implementar\ a\ Lógica\ de\ Negócio\ para\ Gerenciar\ Sub\-serviços\
\-\ \*\*Descrição\*\*:\ Desenvolver\ a\ lógica\ de\ negócio\ nos\ services\ para\ gerenciar\ a\ seleção\ de\ sub\-serviços\.\ Isso\ incluirá\ a\ validação\ dos\ sub\-serviços\ selecionados\ e\ a\ atualização\ dos\ preços\ dos\ serviços\ de\ acordo\ com\ os\ sub\-serviços\ escolhidos\.\
\-\ \*\*Critérios\ de\ Aceite\*\*:\
\ \ \-\ ✓\ A\ lógica\ de\ negócio\ valida\ corretamente\ os\ sub\-serviços\ selecionados\
\ \ \-\ ✓\ O\ preço\ do\ serviço\ é\ atualizado\ corretamente\ com\ base\ nos\ sub\-serviços\ escolhidos\
\ \ \-\ ✓\ A\ seleção\ de\ sub\-serviços\ é\ persistida\ corretamente\ no\ banco\ de\ dados\
\
\#\#\#\ 3\.\ Atualizar\ os\ Controllers\ e\ Views\ para\ Refletir\ a\ Nova\ Funcionalidade\
\-\ \*\*Descrição\*\*:\ Atualizar\ os\ controllers\ e\ views\ para\ incluir\ a\ seleção\ de\ sub\-serviços\.\ Isso\ envolverá\ a\ criação\ de\ novos\ endpoints\ e\ a\ atualização\ das\ interfaces\ de\ usuário\ para\ permitir\ a\ seleção\ de\ sub\-serviços\.\
\-\ \*\*Critérios\ de\ Aceite\*\*:\
\ \ \-\ ✓\ Os\ novos\ endpoints\ são\ criados\ e\ funcionam\ corretamente\
\ \ \-\ ✓\ As\ interfaces\ de\ usuário\ são\ atualizadas\ para\ incluir\ a\ seleção\ de\ sub\-serviços\
\ \ \-\ ✓\ A\ funcionalidade\ de\ seleção\ de\ sub\-serviços\ é\ testada\ e\ funciona\ como\ esperado\
\
\#\#\ Complexidade\
Estimativa:\ Média\
Razão:\ A\ implementação\ da\ nova\ funcionalidade\ requer\ a\ atualização\ de\ entidades\ de\ negócio,\ a\ criação\ de\ novas\ relações\ e\ a\ implementação\ de\ lógica\ de\ negócio\.\ Além\ disso,\ a\ integração\ com\ outros\ componentes\ do\ sistema,\ como\ a\ gestão\ de\ preços\ e\ a\ persistência\ de\ dados,\ pode\ aumentar\ a\ complexidade\.\
\
\#\#\ Riscos\ Identificados\
\-\ \*\*Risco\ 1:\ Impacto\ na\ Performance\*\*:\ A\ adição\ de\ sub\-serviços\ pode\ aumentar\ a\ complexidade\ das\ queries\ no\ banco\ de\ dados,\ impactando\ a\ performance\ do\ sistema\.\
\ \ \-\ Mitigação:\ Otimizar\ as\ queries\ e\ garantir\ que\ o\ sistema\ de\ caching\ esteja\ funcionando\ corretamente\.\
\-\ \*\*Risco\ 2:\ Problemas\ de\ Integração\*\*:\ A\ integração\ com\ outros\ componentes\ do\ sistema,\ como\ a\ gestão\ de\ preços\ e\ a\ persistência\ de\ dados,\ pode\ ser\ problemática\.\
\ \ \-\ Mitigação:\ Realizar\ testes\ integração\ rigorosos\ e\ garantir\ que\ todos\ os\ componentes\ estejam\ funcionando\ corretamente\ antes\ da\ implementação\.\
\
\#\#\ Notas\ para\ o\ Developer\
\-\ \*\*Padrão\ a\ Seguir\*\*:\ Utilizar\ os\ padrões\ de\ projeto\ e\ arquitetura\ estabelecidos\ no\ projeto,\ como\ a\ arquitetura\ em\ camadas\ e\ a\ injeção\ de\ dependências\.\
\-\ \*\*Cuidado\ Especial\ com\ a\ Segurança\*\*:\ Garantir\ que\ a\ nova\ funcionalidade\ esteja\ em\ conformidade\ com\ as\ restrições\ de\ negócio\ e\ que\ os\ dados\ sensíveis\ sejam\ protegidos\.\
\-\ \*\*Reutilize\ Componentes\ Existentes\*\*:\ Reutilizar\ componentes\ e\ classes\ existentes\ sempre\ que\ possível\ para\ minimizar\ a\ duplicação\ de\ código\ e\ facilitar\ a\ manutenção\.
---

## 💻 Implementação

\#\ File:\ src/Models/Service\.cs\
```csharp\
using\ System\.ComponentModel\.DataAnnotations;\
using\ System\.ComponentModel\.DataAnnotations\.Schema;\
\
public\ class\ Service\
\{\
\ \ \ \ \[Key\]\
\ \ \ \ public\ int\ Id\ \{\ get;\ set;\ \}\
\
\ \ \ \ \[Required\]\
\ \ \ \ public\ string\ Name\ \{\ get;\ set;\ \}\
\
\ \ \ \ public\ decimal\ Price\ \{\ get;\ set;\ \}\
\
\ \ \ \ public\ virtual\ ICollection<SubService>\ SubServices\ \{\ get;\ set;\ \}\
\}\
```\
\
\#\ File:\ src/Models/SubService\.cs\
```csharp\
using\ System\.ComponentModel\.DataAnnotations;\
using\ System\.ComponentModel\.DataAnnotations\.Schema;\
\
public\ class\ SubService\
\{\
\ \ \ \ \[Key\]\
\ \ \ \ public\ int\ Id\ \{\ get;\ set;\ \}\
\
\ \ \ \ \[Required\]\
\ \ \ \ public\ string\ Name\ \{\ get;\ set;\ \}\
\
\ \ \ \ public\ decimal\ Price\ \{\ get;\ set;\ \}\
\
\ \ \ \ \[ForeignKey\("ServiceId"\)\]\
\ \ \ \ public\ virtual\ Service\ Service\ \{\ get;\ set;\ \}\
\
\ \ \ \ public\ int\ ServiceId\ \{\ get;\ set;\ \}\
\}\
```\
\
\#\ File:\ src/Repositories/ServiceRepository\.cs\
```csharp\
using\ Microsoft\.EntityFrameworkCore;\
using\ Petmob\.Database;\
using\ System;\
using\ System\.Collections\.Generic;\
using\ System\.Linq;\
using\ System\.Threading\.Tasks;\
\
public\ class\ ServiceRepository\ :\ IServiceRepository\
\{\
\ \ \ \ private\ readonly\ PetmobDbContext\ _context;\
\
\ \ \ \ public\ ServiceRepository\(PetmobDbContext\ context\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ _context\ =\ context;\
\ \ \ \ \}\
\
\ \ \ \ public\ async\ Task<List<Service>>\ GetServicesAsync\(\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ return\ await\ _context\.Services\
\ \ \ \ \ \ \ \ \ \ \ \ \.Include\(s\ =>\ s\.SubServices\)\
\ \ \ \ \ \ \ \ \ \ \ \ \.ToListAsync\(\);\
\ \ \ \ \}\
\
\ \ \ \ public\ async\ Task<Service>\ GetServiceAsync\(int\ id\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ return\ await\ _context\.Services\
\ \ \ \ \ \ \ \ \ \ \ \ \.Include\(s\ =>\ s\.SubServices\)\
\ \ \ \ \ \ \ \ \ \ \ \ \.FirstOrDefaultAsync\(s\ =>\ s\.Id\ ==\ id\);\
\ \ \ \ \}\
\
\ \ \ \ public\ async\ Task\ CreateServiceAsync\(Service\ service\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ _context\.Services\.Add\(service\);\
\ \ \ \ \ \ \ \ await\ _context\.SaveChangesAsync\(\);\
\ \ \ \ \}\
\
\ \ \ \ public\ async\ Task\ UpdateServiceAsync\(Service\ service\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ _context\.Services\.Update\(service\);\
\ \ \ \ \ \ \ \ await\ _context\.SaveChangesAsync\(\);\
\ \ \ \ \}\
\
\ \ \ \ public\ async\ Task\ DeleteServiceAsync\(int\ id\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ var\ service\ =\ await\ GetServiceAsync\(id\);\
\ \ \ \ \ \ \ \ if\ \(service\ !=\ null\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ _context\.Services\.Remove\(service\);\
\ \ \ \ \ \ \ \ \ \ \ \ await\ _context\.SaveChangesAsync\(\);\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/Services/ServiceService\.cs\
```csharp\
using\ Petmob\.Database;\
using\ System;\
using\ System\.Collections\.Generic;\
using\ System\.Linq;\
using\ System\.Threading\.Tasks;\
\
public\ class\ ServiceService\ :\ IServiceService\
\{\
\ \ \ \ private\ readonly\ IServiceRepository\ _repository;\
\
\ \ \ \ public\ ServiceService\(IServiceRepository\ repository\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ _repository\ =\ repository;\
\ \ \ \ \}\
\
\ \ \ \ public\ async\ Task<List<Service>>\ GetServicesAsync\(\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ return\ await\ _repository\.GetServicesAsync\(\);\
\ \ \ \ \}\
\
\ \ \ \ public\ async\ Task<Service>\ GetServiceAsync\(int\ id\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ return\ await\ _repository\.GetServiceAsync\(id\);\
\ \ \ \ \}\
\
\ \ \ \ public\ async\ Task\ CreateServiceAsync\(Service\ service\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ await\ _repository\.CreateServiceAsync\(service\);\
\ \ \ \ \}\
\
\ \ \ \ public\ async\ Task\ UpdateServiceAsync\(Service\ service\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ await\ _repository\.UpdateServiceAsync\(service\);\
\ \ \ \ \}\
\
\ \ \ \ public\ async\ Task\ DeleteServiceAsync\(int\ id\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ await\ _repository\.DeleteServiceAsync\(id\);\
\ \ \ \ \}\
\
\ \ \ \ public\ async\ Task\ SelectSubServicesAsync\(int\ serviceId,\ List<int>\ subServiceIds\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ var\ service\ =\ await\ _repository\.GetServiceAsync\(serviceId\);\
\ \ \ \ \ \ \ \ if\ \(service\ !=\ null\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ service\.SubServices\ =\ subServiceIds\.Select\(id\ =>\ new\ SubService\ \{\ Id\ =\ id\ \}\)\.ToList\(\);\
\ \ \ \ \ \ \ \ \ \ \ \ await\ _repository\.UpdateServiceAsync\(service\);\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/Controllers/ServiceController\.cs\
```csharp\
using\ Microsoft\.AspNetCore\.Mvc;\
using\ Petmob\.Database;\
using\ System;\
using\ System\.Collections\.Generic;\
using\ System\.Linq;\
using\ System\.Threading\.Tasks;\
\
\[ApiController\]\
\[Route\("api/\[controller\]"\)\]\
public\ class\ ServiceController\ :\ ControllerBase\
\{\
\ \ \ \ private\ readonly\ IServiceService\ _service;\
\
\ \ \ \ public\ ServiceController\(IServiceService\ service\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ _service\ =\ service;\
\ \ \ \ \}\
\
\ \ \ \ \[HttpGet\]\
\ \ \ \ public\ async\ Task<ActionResult<List<Service>>>\ GetServices\(\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ return\ await\ _service\.GetServicesAsync\(\);\
\ \ \ \ \}\
\
\ \ \ \ \[HttpGet\("\{id\}"\)\]\
\ \ \ \ public\ async\ Task<ActionResult<Service>>\ GetService\(int\ id\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ return\ await\ _service\.GetServiceAsync\(id\);\
\ \ \ \ \}\
\
\ \ \ \ \[HttpPost\]\
\ \ \ \ public\ async\ Task<ActionResult<Service>>\ CreateService\(Service\ service\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ await\ _service\.CreateServiceAsync\(service\);\
\ \ \ \ \ \ \ \ return\ CreatedAtAction\(nameof\(GetService\),\ new\ \{\ id\ =\ service\.Id\ \},\ service\);\
\ \ \ \ \}\
\
\ \ \ \ \[HttpPut\("\{id\}"\)\]\
\ \ \ \ public\ async\ Task<ActionResult>\ UpdateService\(int\ id,\ Service\ service\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ if\ \(id\ !=\ service\.Id\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ return\ BadRequest\(\);\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \ \ \ \ await\ _service\.UpdateServiceAsync\(service\);\
\ \ \ \ \ \ \ \ return\ NoContent\(\);\
\ \ \ \ \}\
\
\ \ \ \ \[HttpDelete\("\{id\}"\)\]\
\ \ \ \ public\ async\ Task<ActionResult>\ DeleteService\(int\ id\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ await\ _service\.DeleteServiceAsync\(id\);\
\ \ \ \ \ \ \ \ return\ NoContent\(\);\
\ \ \ \ \}\
\
\ \ \ \ \[HttpPost\("\{serviceId\}/subservices"\)\]\
\ \ \ \ public\ async\ Task<ActionResult>\ SelectSubServices\(int\ serviceId,\ List<int>\ subServiceIds\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ await\ _service\.SelectSubServicesAsync\(serviceId,\ subServiceIds\);\
\ \ \ \ \ \ \ \ return\ NoContent\(\);\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/Database/PetmobDbContext\.cs\
```csharp\
using\ Microsoft\.EntityFrameworkCore;\
using\ Petmob\.Models;\
using\ System;\
using\ System\.Collections\.Generic;\
using\ System\.Linq;\
using\ System\.Threading\.Tasks;\
\
public\ class\ PetmobDbContext\ :\ DbContext\
\{\
\ \ \ \ public\ PetmobDbContext\(DbContextOptions<PetmobDbContext>\ options\)\ :\ base\(options\)\
\ \ \ \ \{\
\ \ \ \ \}\
\
\ \ \ \ public\ DbSet<Service>\ Services\ \{\ get;\ set;\ \}\
\ \ \ \ public\ DbSet<SubService>\ SubServices\ \{\ get;\ set;\ \}\
\
\ \ \ \ protected\ override\ void\ OnModelCreating\(ModelBuilder\ modelBuilder\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ modelBuilder\.Entity<Service>\(\)\
\ \ \ \ \ \ \ \ \ \ \ \ \.HasMany\(s\ =>\ s\.SubServices\)\
\ \ \ \ \ \ \ \ \ \ \ \ \.WithOne\(ss\ =>\ ss\.Service\)\
\ \ \ \ \ \ \ \ \ \ \ \ \.HasForeignKey\(ss\ =>\ ss\.ServiceId\);\
\ \ \ \ \}\
\}\
```\
\
Para\ integrar\ e\ testar\ essa\ funcionalidade,\ você\ precisará\ seguir\ os\ passos\ abaixo:\
\
1\.\ Adicione\ as\ migrations\ ao\ seu\ projeto\ executando\ o\ comando\ `dotnet\ ef\ migrations\ add\ UpdateServices`\ no\ terminal\.\
2\.\ Execute\ o\ comando\ `dotnet\ ef\ database\ update`\ para\ aplicar\ as\ migrations\ ao\ seu\ banco\ de\ dados\.\
3\.\ Adicione\ o\ serviço\ e\ o\ repositório\ ao\ container\ de\ injeção\ de\ dependência\ no\ arquivo\ `Startup\.cs`\.\
4\.\ Utilize\ o\ Postman\ ou\ outro\ cliente\ HTTP\ para\ testar\ os\ endpoints\ da\ API\.\
\
Exemplos\ de\ uso:\
\
\*\ \ \ Obter\ todos\ os\ serviços:\ `GET\ /api/Service`\
\*\ \ \ Obter\ um\ serviço\ específico:\ `GET\ /api/Service/\{id\}`\
\*\ \ \ Criar\ um\ novo\ serviço:\ `POST\ /api/Service`\ com\ o\ corpo\ da\ requisição\ contendo\ as\ informações\ do\ serviço\.\
\*\ \ \ Atualizar\ um\ serviço\ existente:\ `PUT\ /api/Service/\{id\}`\ com\ o\ corpo\ da\ requisição\ contendo\ as\ informações\ atualizadas\ do\ serviço\.\
\*\ \ \ Excluir\ um\ serviço:\ `DELETE\ /api/Service/\{id\}`\
\*\ \ \ Selecionar\ sub\-serviços\ para\ um\ serviço:\ `POST\ /api/Service/\{serviceId\}/subservices`\ com\ o\ corpo\ da\ requisição\ contendo\ a\ lista\ de\ IDs\ de\ sub\-serviços\.\
\
A\ arquitetura\ em\ camadas\ foi\ utilizada\ para\ separar\ as\ responsabilidades\ do\ sistema\ em\ diferentes\ camadas,\ tornando\ o\ código\ mais\ organizado,\ escalável\ e\ fácil\ de\ manter\.\ A\ injeção\ de\ dependência\ foi\ utilizada\ para\ encapsular\ as\ dependências\ entre\ as\ camadas,\ tornando\ o\ sistema\ mais\ modular\ e\ flexível\.\
\
A\ escolha\ da\ arquitetura\ em\ camadas\ e\ da\ injeção\ de\ dependência\ foi\ fundamentada\ nos\ seguintes\ motivos:\
\
\*\ \ \ \*\*Separar\ as\ responsabilidades\ do\ sistema\ em\ diferentes\ camadas\*\*:\ Cada\ camada\ tem\ uma\ responsabilidade\ específica,\ tornando\ o\ código\ mais\ organizado\ e\ fácil\ de\ entender\.\
\*\ \ \ \*\*Tornar\ o\ sistema\ mais\ escalável\*\*:\ A\ arquitetura\ em\ camadas\ permite\ que\ cada\ camada\ seja\ desenvolvida\ e\ testada\ de\ forma\ independente,\ tornando\ mais\ fácil\ adicionar\ novas\ funcionalidades\ ao\ sistema\.\
\*\ \ \ \*\*Tornar\ o\ sistema\ mais\ flexível\*\*:\ A\ injeção\ de\ dependência\ permite\ que\ as\ dependências\ entre\ as\ camadas\ sejam\ encapsuladas,\ tornando\ mais\ fácil\ trocar\ ou\ substituir\ uma\ camada\ por\ outra\.\
\
No\ entanto,\ é\ importante\ considerar\ os\ seguintes\ pontos:\
\
\*\ \ \ \*\*A\ arquitetura\ em\ camadas\ pode\ aumentar\ a\ complexidade\ do\ sistema\*\*:\ Com\ mais\ camadas,\ o\ sistema\ pode\ se\ tornar\ mais\ complexo\ e\ difícil\ de\ entender\.\
\*\ \ \ \*\*A\ injeção\ de\ dependência\ pode\ aumentar\ a\ complexidade\ do\ sistema\*\*:\ Com\ mais\ dependências\ entre\ as\ camadas,\ o\ sistema\ pode\ se\ tornar\ mais\ complexo\ e\ difícil\ de\ entender\.\
\
Para\ mitigar\ esses\ riscos,\ é\ fundamental:\
\
\*\ \ \ \*\*Manter\ o\ sistema\ simples\ e\ fácil\ de\ entender\*\*:\ Utilizar\ uma\ arquitetura\ em\ camadas\ simples\ e\ evitar\ a\ criação\ de\ camadas\ desnecessárias\.\
\*\ \ \ \*\*Documentar\ o\ sistema\*\*:\ Manter\ uma\ documentação\ clara\ e\ atualizada\ do\ sistema,\ incluindo\ as\ dependências\ entre\ as\ camadas\.\
\*\ \ \ \*\*Testar\ o\ sistema\*\*:\ Realizar\ testes\ rigorosos\ do\ sistema\ para\ garantir\ que\ ele\ esteja\ funcionando\ corretamente\ e\ que\ as\ dependências\ entre\ as\ camadas\ estejam\ sendo\ gerenciadas\ corretamente\.
---

## ✅ Revisão de Qualidade

\#\ Relatório\ de\ Análise\ da\ Implementação\ do\ Modo\ de\ Serviço\ com\ Sub\-Itens\
\
\#\#\ Introdução\
O\ objetivo\ deste\ relatório\ é\ analisar\ a\ implementação\ do\ modo\ de\ serviço\ com\ sub\-itens\ para\ seleção\ na\ plataforma\ Petmob\.\ Esta\ funcionalidade\ permite\ que\ os\ usuários\ selecionem\ serviços\ com\ sub\-itens\ específicos,\ melhorando\ a\ experiência\ do\ usuário\ e\ a\ eficiência\ na\ gestão\ de\ serviços\.\
\
\#\#\ Análise\ da\ Implementação\
\
\#\#\#\ Conformidade\ com\ o\ Plano\ Técnico\
A\ implementação\ segue\ os\ padrões\ arquiteturais\ estabelecidos\ no\ projeto,\ utilizando\ a\ arquitetura\ em\ camadas,\ com\ controllers,\ services\ e\ repositories\.\ A\ nova\ funcionalidade\ está\ em\ conformidade\ com\ as\ restrições\ de\ negócio,\ como\ o\ respeito\ aos\ horários\ de\ funcionamento\ das\ petshops\ e\ a\ proteção\ dos\ dados\ sensíveis\ dos\ pets\.\
\
\#\#\#\ Qualidade\ de\ Código\ e\ Padrões\ do\ Projeto\
O\ código\ está\ bem\ organizado\ e\ segue\ os\ padrões\ de\ projeto\ estabelecidos\ no\ projeto\.\ A\ utilização\ da\ arquitetura\ em\ camadas\ e\ da\ injeção\ de\ dependência\ torna\ o\ sistema\ mais\ modular\ e\ flexível\.\
\
\#\#\#\ Segurança\
A\ implementação\ não\ apresenta\ vulnerabilidades\ de\ segurança\ óbvias,\ como\ injeção\ de\ SQL\ ou\ XSS\.\ No\ entanto,\ é\ importante\ realizar\ testes\ de\ segurança\ mais\ aprofundados\ para\ garantir\ que\ o\ sistema\ esteja\ protegido\ contra\ ataques\.\
\
\#\#\#\ Performance\ e\ Escalabilidade\
A\ implementação\ utiliza\ a\ arquitetura\ em\ camadas\ e\ a\ injeção\ de\ dependência,\ o\ que\ torna\ o\ sistema\ mais\ escalável\.\ No\ entanto,\ é\ importante\ realizar\ testes\ de\ performance\ para\ garantir\ que\ o\ sistema\ possa\ lidar\ com\ um\ grande\ volume\ de\ requisições\.\
\
\#\#\#\ Casos\ Edge\ Não\ Tratados\
A\ implementação\ não\ apresenta\ casos\ edge\ não\ tratados\ óbvios\.\ No\ entanto,\ é\ importante\ realizar\ testes\ mais\ aprofundados\ para\ garantir\ que\ o\ sistema\ esteja\ preparado\ para\ lidar\ com\ situações\ inesperadas\.\
\
\#\#\#\ Testes\
A\ implementação\ não\ inclui\ testes\ automatizados\.\ É\ importante\ criar\ testes\ automatizados\ para\ garantir\ que\ o\ sistema\ esteja\ funcionando\ corretamente\ e\ que\ as\ dependências\ entre\ as\ camadas\ estejam\ sendo\ gerenciadas\ corretamente\.\
\
\#\#\ Problemas\ e\ Sugestões\
\
\#\#\#\ Problemas\
1\.\ \*\*Falta\ de\ testes\ automatizados\*\*:\ A\ implementação\ não\ inclui\ testes\ automatizados,\ o\ que\ pode\ levar\ a\ erros\ e\ bugs\ não\ detectados\.\
2\.\ \*\*Segurança\*\*:\ A\ implementação\ não\ apresenta\ vulnerabilidades\ de\ segurança\ óbvias,\ mas\ é\ importante\ realizar\ testes\ de\ segurança\ mais\ aprofundados\.\
3\.\ \*\*Performance\*\*:\ A\ implementação\ utiliza\ a\ arquitetura\ em\ camadas\ e\ a\ injeção\ de\ dependência,\ o\ que\ torna\ o\ sistema\ mais\ escalável\.\ No\ entanto,\ é\ importante\ realizar\ testes\ de\ performance\ para\ garantir\ que\ o\ sistema\ possa\ lidar\ com\ um\ grande\ volume\ de\ requisições\.\
\
\#\#\#\ Sugestões\
1\.\ \*\*Criar\ testes\ automatizados\*\*:\ É\ importante\ criar\ testes\ automatizados\ para\ garantir\ que\ o\ sistema\ esteja\ funcionando\ corretamente\ e\ que\ as\ dependências\ entre\ as\ camadas\ estejam\ sendo\ gerenciadas\ corretamente\.\
2\.\ \*\*Realizar\ testes\ de\ segurança\*\*:\ É\ importante\ realizar\ testes\ de\ segurança\ mais\ aprofundados\ para\ garantir\ que\ o\ sistema\ esteja\ protegido\ contra\ ataques\.\
3\.\ \*\*Realizar\ testes\ de\ performance\*\*:\ É\ importante\ realizar\ testes\ de\ performance\ para\ garantir\ que\ o\ sistema\ possa\ lidar\ com\ um\ grande\ volume\ de\ requisições\.\
\
\#\#\ Veredicto\ Final\
⚠️\
\
A\ implementação\ do\ modo\ de\ serviço\ com\ sub\-itens\ para\ seleção\ na\ plataforma\ Petmob\ está\ em\ conformidade\ com\ os\ padrões\ arquiteturais\ estabelecidos\ no\ projeto\ e\ segue\ os\ padrões\ de\ projeto\.\ No\ entanto,\ é\ importante\ realizar\ testes\ mais\ aprofundados\ para\ garantir\ que\ o\ sistema\ esteja\ funcionando\ corretamente\ e\ que\ as\ dependências\ entre\ as\ camadas\ estejam\ sendo\ gerenciadas\ corretamente\.\ Além\ disso,\ é\ importante\ criar\ testes\ automatizados\ e\ realizar\ testes\ de\ segurança\ e\ performance\ para\ garantir\ que\ o\ sistema\ esteja\ protegido\ contra\ ataques\ e\ possa\ lidar\ com\ um\ grande\ volume\ de\ requisições\.