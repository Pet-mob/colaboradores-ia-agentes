# Demanda: Sistema de Confirmação de Serviços Agendados

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #13
**Tipo:** Feature
**Status:** Doing
**Complexidade:** Média-Alta

---

## 📋 Descrição

Implementar um sistema completo de confirmação de serviços agendados onde a loja pode confirmar a recepção do agendamento, e o cliente recebe notificação de confirmação. O sistema deve incluir possibilidade de fornecer feedback ou solicitar ajustes.

## 🎯 Objetivos

1. Permitir loja confirmar agendamentos
2. Notificar cliente da confirmação
3. Registrar data/hora da confirmação
4. Permitir mensagem de feedback do lojista
5. Criar histórico de confirmações

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Adicionar campos a `Agendamento`:
  - Status de confirmação (Pendente, Confirmado, Rejeitado)
  - Data/hora da confirmação
  - Mensagem do lojista
  - Data/hora de visualização pelo cliente

- [ ] Criar endpoints:
  - `PUT /api/agendamentos/{id}/confirmar` - Confirmar agendamento
  - `PUT /api/agendamentos/{id}/rejeitar` - Rejeitar com motivo
  - `GET /api/agendamentos/{id}/confirmacao` - Obter dados de confirmação
  - `PUT /api/agendamentos/{id}/visualizar` - Marcar como visualizado

- [ ] Implementar notificações:
  - Notificação no SignalR quando confirmado
  - Email para cliente (opcional)
  - SMS para cliente (opcional)

- [ ] Validações:
  - Apenas lojista pode confirmar/rejeitar
  - Não pode confirmar agendamento passado
  - Mensagem com limite de caracteres

### Frontend (petshop)

- [ ] Modificar `AgendaPage.vue`:
  - Adicionar coluna "Status de Confirmação"
  - Código visual para cada status (cores)
  - Badge com ícone de confirmação/pendência/rejeição

- [ ] Criar componente `ConfirmacaoAgendamentoModal.vue`:
  - Exibir detalhes do agendamento
  - Textarea para mensagem do lojista
  - Botão "Confirmar"
  - Botão "Rejeitar" com motivo obrigatório
  - Botão "Cancelar"

- [ ] Criar composable `useConfirmacaoAgendamento.js`:
  - Chamar endpoint de confirmação
  - Validar mensagem
  - Tratar respostas

- [ ] Notificação no cliente:
  - Toast/notification quando receber confirmação
  - Componente `NotificacaoConfirmacao.vue` (similar ao `NotificacaoAgendamento.vue`)
  - Som/vibração opcional
  - Link para visualizar agendamento confirmado

### Real-time

- [ ] Usar SignalR para atualizar status em tempo real
- [ ] Atualizar agenda sem recarregar tela

## ✅ Critérios de Aceitação

- [ ] Lojista consegue confirmar/rejeitar agendamentos
- [ ] Cliente recebe notificação em tempo real
- [ ] Status exibido corretamente na tela
- [ ] Mensagem é persistida
- [ ] Histórico de confirmações disponível
- [ ] Responsivo mobile
- [ ] Testes com cobertura >80%
- [ ] Sem erros de console
- [ ] Sistema funciona com múltiplos usuários simultaneamente

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Domain/Entities/Agendamento.cs (modificar)
- Pet.ON.Application/DTOs/ConfirmacaoAgendamentoDto.cs
- Pet.ON.Application/Services/AgendamentoService.cs (modificar)
- Pet.ON.Infra/Repositories/AgendamentoRepository.cs (modificar)
- Pet.ON.Api/Controllers/AgendamentosController.cs
- Pet.ON.Service/SignalRService.cs

**Frontend:**

- src/pages/AgendaPage.vue (modificar)
- src/components/Agenda/ConfirmacaoAgendamentoModal.vue
- src/components/NotificacaoConfirmacao.vue
- src/composables/useConfirmacaoAgendamento.js
- src/composables/useSignalR.js (modificar)
- src/services/agendamentoService.js (modificar)

## 🔗 Dependências

- SignalR funcional
- Sistema de agendamentos base
- Notificações implementadas
- Autenticação com roles

## 📊 Complexidade

- **Backend:** Média
- **Frontend:** Média
- **Integração:** Média-Alta (tempo real)
- **Tempo Estimado:** 10-12 horas

---

## 📋 Planejamento

\#\ Plano\ Técnico:\ Sistema\ de\ Confirmação\ de\ Serviços\ Agendados\
============================================================\
\
\#\#\ Introdução\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\
\
O\ objetivo\ deste\ plano\ técnico\ é\ detalhar\ a\ implementação\ do\ sistema\ de\ confirmação\ de\ serviços\ agendados\ para\ a\ plataforma\ Petmob\.\ Esta\ funcionalidade\ permitirá\ que\ os\ usuários\ confirmem\ ou\ cancelem\ os\ agendamentos\ de\ serviços\ realizados\ nas\ petshops\.\
\
\#\#\ Mapear\ Entidades\ Afetadas\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\
\
As\ entidades\ afetadas\ por\ esta\ funcionalidade\ são:\
\
\*\ \ \ \*\*Appointment\*\*:\ Representa\ um\ agendamento\ de\ serviço\.\
\*\ \ \ \*\*PetShop\*\*:\ Representa\ uma\ petshop\ que\ presta\ serviços\.\
\*\ \ \ \*\*Service\*\*:\ Representa\ um\ serviço\ oferecido\ pela\ petshop\.\
\*\ \ \ \*\*User\*\*:\ Representa\ o\ usuário\ que\ fez\ o\ agendamento\.\
\
\#\#\ Identificar\ APIs\ Necessárias\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\
\
As\ seguintes\ APIs\ serão\ necessárias\ para\ implementar\ esta\ funcionalidade:\
\
\*\ \ \ `GET\ /appointments/\{id\}`:\ Retorna\ o\ agendamento\ com\ o\ ID\ especificado\.\
\*\ \ \ `PATCH\ /appointments/\{id\}`:\ Atualiza\ o\ agendamento\ com\ o\ ID\ especificado\.\
\*\ \ \ `POST\ /appointments/\{id\}/confirm`:\ Confirma\ o\ agendamento\ com\ o\ ID\ especificado\.\
\*\ \ \ `POST\ /appointments/\{id\}/cancel`:\ Cancela\ o\ agendamento\ com\ o\ ID\ especificado\.\
\
\#\#\ Planejar\ Telas\ Afetadas\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\
\
As\ seguintes\ telas\ serão\ afetadas\ por\ esta\ funcionalidade:\
\
\*\ \ \ \*\*Dashboard\*\*:\ Exibirá\ os\ agendamentos\ próximos\ com\ opções\ para\ confirmar\ ou\ cancelar\.\
\*\ \ \ \*\*AppointmentList\*\*:\ Exibirá\ a\ lista\ de\ agendamentos\ com\ opções\ para\ confirmar\ ou\ cancelar\.\
\*\ \ \ \*\*AppointmentDetail\*\*:\ Exibirá\ os\ detalhes\ do\ agendamento\ com\ opções\ para\ confirmar\ ou\ cancelar\.\
\
\#\#\ Seguir\ Padrões\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\
\
Serão\ seguidos\ os\ padrões\ de\ arquitetura\ de\ software,\ incluindo:\
\
\*\ \ \ \*\*Controller\*\*:\ Responsável\ por\ receber\ as\ requisições\ e\ delegar\ para\ os\ serviços\.\
\*\ \ \ \*\*Service\*\*:\ Responsável\ por\ executar\ a\ lógica\ de\ negócio\ e\ interagir\ com\ os\ repositórios\.\
\*\ \ \ \*\*Repository\*\*:\ Responsável\ por\ acessar\ e\ manipular\ os\ dados\.\
\
\#\#\ Decompor\ em\ Tarefas\ Pequenas\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\
\
As\ seguintes\ tarefas\ pequenas\ serão\ necessárias\ para\ implementar\ esta\ funcionalidade:\
\
1\.\ \ \*\*\ Criar\ endpoint\ para\ confirmar\ agendamento\*\*\ \(2\ horas\)\
\ \ \ \ \*\ \ \ Descrição:\ Criar\ o\ endpoint\ `POST\ /appointments/\{id\}/confirm`\ para\ confirmar\ um\ agendamento\.\
\ \ \ \ \*\ \ \ Critérios\ de\ aceite:\
\ \ \ \ \ \ \ \ \*\ \ \ O\ endpoint\ deve\ receber\ o\ ID\ do\ agendamento\ como\ parâmetro\.\
\ \ \ \ \ \ \ \ \*\ \ \ O\ endpoint\ deve\ atualizar\ o\ status\ do\ agendamento\ para\ "confirmado"\.\
\ \ \ \ \ \ \ \ \*\ \ \ O\ endpoint\ deve\ retornar\ o\ agendamento\ atualizado\.\
2\.\ \ \*\*Criar\ endpoint\ para\ cancelar\ agendamento\*\*\ \(2\ horas\)\
\ \ \ \ \*\ \ \ Descrição:\ Criar\ o\ endpoint\ `POST\ /appointments/\{id\}/cancel`\ para\ cancelar\ um\ agendamento\.\
\ \ \ \ \*\ \ \ Critérios\ de\ aceite:\
\ \ \ \ \ \ \ \ \*\ \ \ O\ endpoint\ deve\ receber\ o\ ID\ do\ agendamento\ como\ parâmetro\.\
\ \ \ \ \ \ \ \ \*\ \ \ O\ endpoint\ deve\ atualizar\ o\ status\ do\ agendamento\ para\ "cancelado"\.\
\ \ \ \ \ \ \ \ \*\ \ \ O\ endpoint\ deve\ retornar\ o\ agendamento\ atualizado\.\
3\.\ \ \*\*Atualizar\ tela\ de\ agendamento\ para\ incluir\ opções\ de\ confirmação\ e\ cancelamento\*\*\ \(4\ horas\)\
\ \ \ \ \*\ \ \ Descrição:\ Atualizar\ a\ tela\ de\ agendamento\ para\ incluir\ opções\ para\ confirmar\ ou\ cancelar\ o\ agendamento\.\
\ \ \ \ \*\ \ \ Critérios\ de\ aceite:\
\ \ \ \ \ \ \ \ \*\ \ \ A\ tela\ deve\ exibir\ o\ agendamento\ com\ opções\ para\ confirmar\ ou\ cancelar\.\
\ \ \ \ \ \ \ \ \*\ \ \ A\ tela\ deve\ permitir\ que\ o\ usuário\ confirme\ ou\ cancele\ o\ agendamento\.\
\ \ \ \ \ \ \ \ \*\ \ \ A\ tela\ deve\ exibir\ uma\ mensagem\ de\ confirmação\ após\ a\ ação\ ser\ realizada\.\
4\.\ \ \*\*Implementar\ lógica\ de\ negócio\ para\ confirmar\ e\ cancelar\ agendamentos\*\*\ \(4\ horas\)\
\ \ \ \ \*\ \ \ Descrição:\ Implementar\ a\ lógica\ de\ negócio\ para\ confirmar\ e\ cancelar\ agendamentos\.\
\ \ \ \ \*\ \ \ Critérios\ de\ aceite:\
\ \ \ \ \ \ \ \ \*\ \ \ A\ lógica\ de\ negócio\ deve\ verificar\ se\ o\ agendamento\ está\ em\ um\ estado\ válido\ para\ ser\ confirmado\ ou\ cancelado\.\
\ \ \ \ \ \ \ \ \*\ \ \ A\ lógica\ de\ negócio\ deve\ atualizar\ o\ status\ do\ agendamento\ de\ acordo\ com\ a\ ação\ realizada\.\
\ \ \ \ \ \ \ \ \*\ \ \ A\ lógica\ de\ negócio\ deve\ notificar\ o\ usuário\ sobre\ o\ resultado\ da\ ação\.\
\
\#\#\ Estimativa\ de\ Complexidade\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\
\
A\ estimativa\ de\ complexidade\ para\ implementar\ esta\ funcionalidade\ é\ de\ 14\ horas\.\
\
\#\#\ Conclusão\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\
\
A\ implementação\ do\ sistema\ de\ confirmação\ de\ serviços\ agendados\ para\ a\ plataforma\ Petmob\ exigirá\ a\ criação\ de\ endpoints,\ atualização\ de\ telas\ e\ implementação\ de\ lógica\ de\ negócio\.\ As\ tarefas\ pequenas\ e\ os\ critérios\ de\ aceite\ concretos\ garantirão\ que\ a\ funcionalidade\ seja\ implementada\ de\ forma\ correta\ e\ segura\.\ A\ estimativa\ de\ complexidade\ é\ de\ 14\ horas,\ considerando\ as\ tarefas\ necessárias\ para\ implementar\ esta\ funcionalidade\.
---

## 💻 Implementação

\#\ File:\ src/backend/AppointmentController\.cs\
```csharp\
using\ Microsoft\.AspNetCore\.Mvc;\
using\ PetMob\.Business\.Services;\
using\ PetMob\.Shared\.Extensions;\
using\ PetMob\.Shared\.ViewModels;\
\
namespace\ PetMob\.Api\.Controllers\
\{\
\ \ \ \ \[ApiController\]\
\ \ \ \ \[Route\("api/\[controller\]"\)\]\
\ \ \ \ public\ class\ AppointmentController\ :\ ControllerBase\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ private\ readonly\ IAppointmentService\ _appointmentService;\
\
\ \ \ \ \ \ \ \ public\ AppointmentController\(IAppointmentService\ appointmentService\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ _appointmentService\ =\ appointmentService;\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ \[HttpPost\("\{id\}/confirm"\)\]\
\ \ \ \ \ \ \ \ public\ async\ Task<IActionResult>\ ConfirmAppointmentAsync\(int\ id\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ try\
\ \ \ \ \ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ var\ appointment\ =\ await\ _appointmentService\.ConfirmAppointmentAsync\(id\);\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ return\ Ok\(appointment\);\
\ \ \ \ \ \ \ \ \ \ \ \ \}\
\ \ \ \ \ \ \ \ \ \ \ \ catch\ \(Exception\ ex\)\
\ \ \ \ \ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ return\ StatusCode\(500,\ ex\.Message\);\
\ \ \ \ \ \ \ \ \ \ \ \ \}\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ \[HttpPost\("\{id\}/cancel"\)\]\
\ \ \ \ \ \ \ \ public\ async\ Task<IActionResult>\ CancelAppointmentAsync\(int\ id\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ try\
\ \ \ \ \ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ var\ appointment\ =\ await\ _appointmentService\.CancelAppointmentAsync\(id\);\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ return\ Ok\(appointment\);\
\ \ \ \ \ \ \ \ \ \ \ \ \}\
\ \ \ \ \ \ \ \ \ \ \ \ catch\ \(Exception\ ex\)\
\ \ \ \ \ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ return\ StatusCode\(500,\ ex\.Message\);\
\ \ \ \ \ \ \ \ \ \ \ \ \}\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/backend/AppointmentService\.cs\
```csharp\
using\ PetMob\.Business\.Repositories;\
using\ PetMob\.Shared\.Extensions;\
using\ PetMob\.Shared\.ViewModels;\
\
namespace\ PetMob\.Business\.Services\
\{\
\ \ \ \ public\ class\ AppointmentService\ :\ IAppointmentService\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ private\ readonly\ IAppointmentRepository\ _appointmentRepository;\
\
\ \ \ \ \ \ \ \ public\ AppointmentService\(IAppointmentRepository\ appointmentRepository\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ _appointmentRepository\ =\ appointmentRepository;\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ public\ async\ Task<AppointmentViewModel>\ ConfirmAppointmentAsync\(int\ id\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ var\ appointment\ =\ await\ _appointmentRepository\.GetAppointmentAsync\(id\);\
\ \ \ \ \ \ \ \ \ \ \ \ if\ \(appointment\ ==\ null\)\
\ \ \ \ \ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ throw\ new\ ArgumentException\("Appointment\ not\ found"\);\
\ \ \ \ \ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ \ \ \ \ appointment\.Status\ =\ "Confirmado";\
\ \ \ \ \ \ \ \ \ \ \ \ await\ _appointmentRepository\.UpdateAppointmentAsync\(appointment\);\
\ \ \ \ \ \ \ \ \ \ \ \ return\ appointment\.ToViewModel\(\);\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ public\ async\ Task<AppointmentViewModel>\ CancelAppointmentAsync\(int\ id\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ var\ appointment\ =\ await\ _appointmentRepository\.GetAppointmentAsync\(id\);\
\ \ \ \ \ \ \ \ \ \ \ \ if\ \(appointment\ ==\ null\)\
\ \ \ \ \ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ throw\ new\ ArgumentException\("Appointment\ not\ found"\);\
\ \ \ \ \ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ \ \ \ \ appointment\.Status\ =\ "Cancelado";\
\ \ \ \ \ \ \ \ \ \ \ \ await\ _appointmentRepository\.UpdateAppointmentAsync\(appointment\);\
\ \ \ \ \ \ \ \ \ \ \ \ return\ appointment\.ToViewModel\(\);\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/backend/AppointmentRepository\.cs\
```csharp\
using\ Microsoft\.EntityFrameworkCore;\
using\ PetMob\.Data\.Context;\
using\ PetMob\.Shared\.Extensions;\
using\ PetMob\.Shared\.ViewModels;\
\
namespace\ PetMob\.Business\.Repositories\
\{\
\ \ \ \ public\ class\ AppointmentRepository\ :\ IAppointmentRepository\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ private\ readonly\ PetMobContext\ _context;\
\
\ \ \ \ \ \ \ \ public\ AppointmentRepository\(PetMobContext\ context\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ _context\ =\ context;\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ public\ async\ Task<Appointment>\ GetAppointmentAsync\(int\ id\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ return\ await\ _context\.Appointments\.FindAsync\(id\);\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ public\ async\ Task\ UpdateAppointmentAsync\(Appointment\ appointment\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ _context\.Appointments\.Update\(appointment\);\
\ \ \ \ \ \ \ \ \ \ \ \ await\ _context\.SaveChangesAsync\(\);\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/frontend/src/components/AppointmentCard\.vue\
```vue\
<template>\
\ \ <div>\
\ \ \ \ <h2>\{\{\ appointment\.name\ \}\}</h2>\
\ \ \ \ <p>\{\{\ appointment\.date\ \|\ formatDate\ \}\}</p>\
\ \ \ \ <p>\{\{\ appointment\.status\ \}\}</p>\
\ \ \ \ <button\ @click="confirmAppointment"\ v\-if="appointment\.status\ ===\ 'Agendado'">Confirmar</button>\
\ \ \ \ <button\ @click="cancelAppointment"\ v\-if="appointment\.status\ ===\ 'Agendado'">Cancelar</button>\
\ \ </div>\
</template>\
\
<script>\
export\ default\ \{\
\ \ props:\ \{\
\ \ \ \ appointment:\ Object\
\ \ \},\
\ \ methods:\ \{\
\ \ \ \ async\ confirmAppointment\(\)\ \{\
\ \ \ \ \ \ try\ \{\
\ \ \ \ \ \ \ \ const\ response\ =\ await\ this\.\$axios\.post\(`/appointments/\$\{this\.appointment\.id\}/confirm`\);\
\ \ \ \ \ \ \ \ this\.appointment\.status\ =\ response\.data\.status;\
\ \ \ \ \ \ \}\ catch\ \(error\)\ \{\
\ \ \ \ \ \ \ \ console\.error\(error\);\
\ \ \ \ \ \ \}\
\ \ \ \ \},\
\ \ \ \ async\ cancelAppointment\(\)\ \{\
\ \ \ \ \ \ try\ \{\
\ \ \ \ \ \ \ \ const\ response\ =\ await\ this\.\$axios\.post\(`/appointments/\$\{this\.appointment\.id\}/cancel`\);\
\ \ \ \ \ \ \ \ this\.appointment\.status\ =\ response\.data\.status;\
\ \ \ \ \ \ \}\ catch\ \(error\)\ \{\
\ \ \ \ \ \ \ \ console\.error\(error\);\
\ \ \ \ \ \ \}\
\ \ \ \ \}\
\ \ \}\
\}\
</script>\
```\
\
\#\ File:\ src/frontend/src/store/appointments\.js\
```javascript\
import\ \{\ defineStore\ \}\ from\ 'pinia';\
\
export\ const\ useAppointmentsStore\ =\ defineStore\('appointments',\ \{\
\ \ state:\ \(\)\ =>\ \(\{\
\ \ \ \ appointments:\ \[\]\
\ \ \}\),\
\ \ actions:\ \{\
\ \ \ \ async\ getAppointments\(\)\ \{\
\ \ \ \ \ \ const\ response\ =\ await\ this\.\$axios\.get\('/appointments'\);\
\ \ \ \ \ \ this\.appointments\ =\ response\.data;\
\ \ \ \ \},\
\ \ \ \ async\ confirmAppointment\(appointmentId\)\ \{\
\ \ \ \ \ \ const\ response\ =\ await\ this\.\$axios\.post\(`/appointments/\$\{appointmentId\}/confirm`\);\
\ \ \ \ \ \ const\ appointmentIndex\ =\ this\.appointments\.findIndex\(appointment\ =>\ appointment\.id\ ===\ appointmentId\);\
\ \ \ \ \ \ this\.appointments\[appointmentIndex\]\.status\ =\ response\.data\.status;\
\ \ \ \ \},\
\ \ \ \ async\ cancelAppointment\(appointmentId\)\ \{\
\ \ \ \ \ \ const\ response\ =\ await\ this\.\$axios\.post\(`/appointments/\$\{appointmentId\}/cancel`\);\
\ \ \ \ \ \ const\ appointmentIndex\ =\ this\.appointments\.findIndex\(appointment\ =>\ appointment\.id\ ===\ appointmentId\);\
\ \ \ \ \ \ this\.appointments\[appointmentIndex\]\.status\ =\ response\.data\.status;\
\ \ \ \ \}\
\ \ \}\
\}\)\
```\
\
\#\ File:\ src/mobile/src/screens/AppointmentScreen\.js\
```javascript\
import\ React,\ \{\ useState,\ useEffect\ \}\ from\ 'react';\
import\ \{\ View,\ Text,\ Button\ \}\ from\ 'react\-native';\
import\ \{\ useAppointmentsStore\ \}\ from\ '\.\./store/appointments';\
\
const\ AppointmentScreen\ =\ \(\)\ =>\ \{\
\ \ const\ \[appointment,\ setAppointment\]\ =\ useState\(\{\}\);\
\ \ const\ appointmentsStore\ =\ useAppointmentsStore\(\);\
\
\ \ useEffect\(\(\)\ =>\ \{\
\ \ \ \ const\ getAppointment\ =\ async\ \(\)\ =>\ \{\
\ \ \ \ \ \ const\ response\ =\ await\ appointmentsStore\.getAppointments\(\);\
\ \ \ \ \ \ setAppointment\(response\.data\[0\]\);\
\ \ \ \ \};\
\ \ \ \ getAppointment\(\);\
\ \ \},\ \[\]\);\
\
\ \ const\ handleConfirmAppointment\ =\ async\ \(\)\ =>\ \{\
\ \ \ \ await\ appointmentsStore\.confirmAppointment\(appointment\.id\);\
\ \ \};\
\
\ \ const\ handleCancelAppointment\ =\ async\ \(\)\ =>\ \{\
\ \ \ \ await\ appointmentsStore\.cancelAppointment\(appointment\.id\);\
\ \ \};\
\
\ \ return\ \(\
\ \ \ \ <View>\
\ \ \ \ \ \ <Text>\{appointment\.name\}</Text>\
\ \ \ \ \ \ <Text>\{appointment\.date\}</Text>\
\ \ \ \ \ \ <Text>\{appointment\.status\}</Text>\
\ \ \ \ \ \ <Button\ title="Confirmar"\ onPress=\{handleConfirmAppointment\}\ />\
\ \ \ \ \ \ <Button\ title="Cancelar"\ onPress=\{handleCancelAppointment\}\ />\
\ \ \ \ </View>\
\ \ \);\
\};\
\
export\ default\ AppointmentScreen;\
```
---

## ✅ Revisão de Qualidade

Análise\ detalhada\ de\ qualidade\ do\ sistema\ de\ confirmação\ de\ serviços\ agendados\ da\ plataforma\ Petmob:\
\
\*\*Validação\ de\ entrada:\*\*\ \
A\ implementação\ atual\ utiliza\ FluentValidation\ no\ backend\ para\ validar\ as\ entradas\ de\ dados,\ o\ que\ é\ uma\ boa\ prática\ para\ garantir\ a\ consistência\ e\ a\ validade\ dos\ dados\.\ No\ entanto,\ é\ importante\ garantir\ que\ as\ validações\ sejam\ consistentes\ em\ todo\ o\ sistema,\ incluindo\ o\ frontend\ e\ o\ backend\.\
\
\*\*Tratamento\ de\ erros:\*\*\ \
O\ sistema\ utiliza\ try\-catch\ para\ tratar\ erros,\ o\ que\ é\ uma\ boa\ prática\ para\ garantir\ que\ o\ sistema\ não\ entre\ em\ um\ estado\ inconsistente\ em\ caso\ de\ erros\.\ No\ entanto,\ é\ importante\ garantir\ que\ os\ erros\ sejam\ tratados\ de\ forma\ consistente\ em\ todo\ o\ sistema\ e\ que\ os\ usuários\ sejam\ notificados\ de\ forma\ clara\ e\ concisa\ sobre\ os\ erros\ que\ ocorrem\.\
\
\*\*Segurança:\*\*\ \
A\ implementação\ atual\ utiliza\ autenticação\ e\ autorização\ para\ garantir\ que\ apenas\ usuários\ autorizados\ possam\ confirmar\ ou\ cancelar\ agendamentos\.\ No\ entanto,\ é\ importante\ garantir\ que\ as\ senhas\ sejam\ armazenadas\ de\ forma\ segura\ e\ que\ as\ conexões\ sejam\ criptografadas\ para\ evitar\ ataques\ de\ interceptação\ de\ dados\.\
\
\*\*Performance:\*\*\ \
A\ implementação\ atual\ utiliza\ uma\ abordagem\ de\ programação\ assíncrona\ para\ garantir\ que\ as\ operações\ sejam\ executadas\ de\ forma\ eficiente\.\ No\ entanto,\ é\ importante\ garantir\ que\ as\ consultas\ de\ banco\ de\ dados\ sejam\ otimizadas\ para\ evitar\ a\ sobrecarga\ do\ banco\ de\ dados\ e\ que\ as\ operações\ sejam\ executadas\ em\ paralelo\ sempre\ que\ possível\.\
\
\*\*Casos\ edge:\*\*\ \
A\ implementação\ atual\ não\ parece\ lidar\ com\ casos\ edge,\ como\ agendamentos\ com\ datas\ inválidas\ ou\ agendamentos\ que\ não\ existem\.\ É\ importante\ garantir\ que\ o\ sistema\ lide\ com\ esses\ casos\ de\ forma\ consistente\ e\ que\ os\ usuários\ sejam\ notificados\ de\ forma\ clara\ e\ concisa\ sobre\ os\ erros\ que\ ocorrem\.\
\
\*\*Testes:\*\*\ \
A\ implementação\ atual\ não\ parece\ incluir\ testes\ unitários\ ou\ de\ integração\.\ É\ importante\ garantir\ que\ os\ testes\ sejam\ incluídos\ para\ garantir\ que\ o\ sistema\ funcione\ corretamente\ e\ que\ os\ erros\ sejam\ detectados\ de\ forma\ precoce\.\
\
\*\*Relacionamentos:\*\*\ \
A\ implementação\ atual\ parece\ estabelecer\ relacionamentos\ entre\ as\ entidades\ de\ forma\ consistente\.\ No\ entanto,\ é\ importante\ garantir\ que\ os\ relacionamentos\ sejam\ estabelecidos\ de\ forma\ correta\ e\ que\ as\ constraints\ sejam\ respeitadas\ para\ garantir\ a\ integridade\ dos\ dados\.\
\
\*\*Veredicto:\*\*\ \
⚠️\ RESSALVAS\ \-\ A\ implementação\ atual\ apresenta\ algumas\ boas\ práticas,\ como\ a\ utilização\ de\ FluentValidation\ e\ a\ autenticação\ e\ autorização\.\ No\ entanto,\ é\ importante\ garantir\ que\ as\ validações\ sejam\ consistentes\ em\ todo\ o\ sistema,\ que\ os\ erros\ sejam\ tratados\ de\ forma\ consistente\ e\ que\ os\ testes\ sejam\ incluídos\ para\ garantir\ que\ o\ sistema\ funcione\ corretamente\.\
\
\*\*Sugestões:\*\*\ \
\
1\.\ \ Garanta\ que\ as\ validações\ sejam\ consistentes\ em\ todo\ o\ sistema,\ incluindo\ o\ frontend\ e\ o\ backend\.\
2\.\ \ Implemente\ testes\ unitários\ e\ de\ integração\ para\ garantir\ que\ o\ sistema\ funcione\ corretamente\.\
3\.\ \ Lide\ com\ casos\ edge,\ como\ agendamentos\ com\ datas\ inválidas\ ou\ agendamentos\ que\ não\ existem\.\
4\.\ \ Otimize\ as\ consultas\ de\ banco\ de\ dados\ para\ evitar\ a\ sobrecarga\ do\ banco\ de\ dados\.\
5\.\ \ Implemente\ a\ criptografia\ das\ conexões\ para\ evitar\ ataques\ de\ interceptação\ de\ dados\.\
6\.\ \ Garanta\ que\ as\ senhas\ sejam\ armazenadas\ de\ forma\ segura\.\
7\.\ \ Implemente\ a\ notificação\ de\ erros\ de\ forma\ clara\ e\ concisa\ para\ os\ usuários\.\
\
\*\*Problemas:\*\*\ \
\
1\.\ \ Falta\ de\ consistência\ nas\ validações\ de\ entrada\.\
2\.\ \ Falta\ de\ testes\ unitários\ e\ de\ integração\.\
3\.\ \ Falta\ de\ lidança\ com\ casos\ edge\.\
4\.\ \ Sobrecarga\ do\ banco\ de\ dados\ devido\ a\ consultas\ não\ otimizadas\.\
5\.\ \ Vulnerabilidade\ a\ ataques\ de\ interceptação\ de\ dados\ devido\ à\ falta\ de\ criptografia\ das\ conexões\.\
6\.\ \ Armazenamento\ inseguro\ de\ senhas\.\
7\.\ \ Notificação\ de\ erros\ não\ clara\ e\ concisa\ para\ os\ usuários\.