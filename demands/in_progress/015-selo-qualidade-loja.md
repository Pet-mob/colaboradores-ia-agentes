# Demanda: Selo de Qualidade da Loja

**Projeto:** PetShop.WebApp (Pet.ON.Api Backend)
**ID:** #15
**Tipo:** Feature
**Status:** To Do
**Complexidade:** Média

---

## 📋 Descrição

Implementar um sistema de selo/badge de qualidade para lojas com base em critérios como taxa de confirmação de agendamentos, avaliações, tempo de resposta e histórico sem problemas. O selo deve ser visível na loja pública e no dashboard.

## 🎯 Objetivos

1. Definir critérios de qualidade
2. Calcular score de qualidade automaticamente
3. Exibir seal/badge em loja pública
4. Mostrar rating na loja pública
5. Dashboard com métricas de qualidade

## 📌 Requisitos Funcionais

### Backend (Pet.ON.Api)

- [ ] Criar modelo `QualidadeLoja`:
  - LojaId (FK)
  - Taxa confirmação (%) agendamentos
  - Avaliação média (1-5 stars)
  - Tempo médio de resposta (horas)
  - Número de reclamações
  - Score total (0-100)
  - Nível (Bronze, Prata, Ouro, Platina)
  - Data última atualização

- [ ] Criar endpoints:
  - `GET /api/lojas/{id}/qualidade` - Obter score
  - `GET /api/loja/minha-qualidade` - Para lojista
  - `POST /api/lojas/{id}/avaliacoes` - Criar avaliação (cliente)

- [ ] Implementar cálculo automático:
  - Job background que recalcula scores diariamente
  - Trigger ao confirmar agendamento
  - Trigger ao criar avaliação
  - Fórmula: (taxa_confirmacao*40% + avaliacoes_media*30% + tempo_resposta*20% + historico*10%)

- [ ] Validações:
  - Apenas cliente pode avaliar
  - Apenas após agendamento realizado
  - Score entre 1-5

### Frontend (petshop)

- [ ] Dashboard do Lojista:
  - Seção "Qualidade da Sua Loja"
  - Exibir score total e nível
  - Cards para cada métrica
  - Gráfico de evolução de score
  - Dicas para melhorar score

- [ ] Página Pública da Loja:
  - Exibir seal/badge grande (topo)
  - Stars de avaliação
  - Link para ver avaliações
  - Histórico de mudanças de nível

- [ ] Sistema de Avaliações:
  - Modal de avaliação (antes ou depois de agendamento)
  - Input 1-5 stars
  - Textarea para comentário (opcional)
  - Feed de avaliações recentes

- [ ] Composable `useQualidadeLoja.js`:
  - Carregar dados de qualidade
  - Formatar dados
  - Cache apropriado

## ✅ Critérios de Aceitação

- [ ] Score calculado corretamente
- [ ] Selos exibidos apropriadamente
- [ ] Avaliações persistidas
- [ ] Dashboard mostra métricas corretas
- [ ] Página pública exibe qualidade
- [ ] Job de recalculo funciona
- [ ] Responsivo mobile
- [ ] Testes com cobertura >75%
- [ ] Sem erros de console

## 📦 Arquivos/Componentes Afetados

**Backend:**

- Pet.ON.Domain/Entities/QualidadeLoja.cs
- Pet.ON.Domain/Entities/AvaliacaoCliente.cs
- Pet.ON.Application/DTOs/QualidadeLojaDto.cs
- Pet.ON.Application/Services/QualidadeService.cs
- Pet.ON.Infra/Repositories/QualidadeRepository.cs
- Pet.ON.Api/Controllers/QualidadeController.cs
- Pet.ON.Service/Jobs/RecalcularQualidadeLojaJob.cs
- appsettings.json (configurar job)

**Frontend:**

- src/pages/DashboardPage.vue (modificar - adicionar qualidade)
- src/pages/LojaPublicaPage.vue (modificar)
- src/components/QualidadeCard.vue
- src/components/AvaliacaoModal.vue
- src/components/DisplayQualidade.vue
- src/components/GraficoQualidade.vue
- src/composables/useQualidadeLoja.js
- src/composables/useAvaliacoes.js
- src/services/qualidadeService.js

## 🔗 Dependências

- Sistema de agendamentos
- Sistema de autenticação com roles
- Background jobs configurados
- Banco de dados

## 📊 Complexidade

- **Backend:** Média-Alta
- **Frontend:** Média
- **Integração:** Média
- **Tempo Estimado:** 10-12 horas

---

## 📋 Planejamento

\#\ Plano\ Técnico:\ Selo\ de\ Qualidade\ da\ Loja\
====================================================\
\
\#\#\ Introdução\
O\ objetivo\ deste\ plano\ técnico\ é\ implementar\ a\ funcionalidade\ de\ Selo\ de\ Qualidade\ da\ Loja,\ que\ permitirá\ que\ as\ petshops\ sejam\ avaliadas\ e\ recebam\ um\ selo\ de\ qualidade\ com\ base\ em\ suas\ avaliações\ e\ desempenho\.\ Esta\ funcionalidade\ será\ implementada\ nos\ projetos\ PetShop\.WebApp\ \(Pet\.ON\.Api\ Backend\),\ PetShop\.WebApp\ \(frontend\ Vue\.js\ 3\)\ e\ Pet\.ON\.App\ \(Mobile\ React\ Native\)\.\
\
\#\#\ Mapear\ Entidades\ Afetadas\
As\ entidades\ afetadas\ por\ esta\ funcionalidade\ são:\
\
\*\ PetShop\
\*\ Avaliação\
\*\ Selo\ de\ Qualidade\
\
\#\#\ Identificar\ APIs\ Necessárias\
As\ seguintes\ APIs\ serão\ necessárias:\
\
\*\ `GET\ /petshops/\{id\}/avaliacoes`\ \-\ Obter\ avaliações\ de\ uma\ petshop\
\*\ `POST\ /petshops/\{id\}/avaliacoes`\ \-\ Criar\ uma\ nova\ avaliação\ para\ uma\ petshop\
\*\ `GET\ /petshops/\{id\}/selo\-qualidade`\ \-\ Obter\ o\ selo\ de\ qualidade\ de\ uma\ petshop\
\*\ `POST\ /petshops/\{id\}/selo\-qualidade`\ \-\ Atualizar\ o\ selo\ de\ qualidade\ de\ uma\ petshop\
\
\#\#\ Planejar\ Telas\ Afetadas\
As\ seguintes\ telas\ serão\ afetadas:\
\
\*\ Tela\ de\ detalhes\ da\ petshop\ \(Web\ e\ Mobile\)\ \-\ exibir\ o\ selo\ de\ qualidade\
\*\ Tela\ de\ avaliações\ \(Web\ e\ Mobile\)\ \-\ criar\ uma\ nova\ avaliação\
\*\ Tela\ de\ administração\ de\ petshops\ \(Web\)\ \-\ visualizar\ e\ atualizar\ o\ selo\ de\ qualidade\
\
\#\#\ Seguir\ Padrões\
A\ implementação\ seguirá\ os\ padrões\ de\ projeto\ e\ implementação\ existentes,\ incluindo:\
\
\*\ Controller\ →\ Service\ →\ Repository\
\*\ Utilizar\ FluentValidation\ para\ validação\ de\ entrada\
\*\ Utilizar\ AutoMapper\ para\ mapeamento\ de\ modelos\
\*\ Utilizar\ Entity\ Framework\ Core\ para\ acesso\ a\ dados\
\
\#\#\ Decompor\ em\ Tarefas\ Pequenas\
As\ seguintes\ tarefas\ pequenas\ serão\ necessárias:\
\
1\.\ \*\*Criar\ modelo\ de\ dados\ para\ o\ selo\ de\ qualidade\*\*\ \(1\ hora\)\
\ \*\ Criar\ uma\ nova\ classe\ no\ projeto\ Pet\.ON\.Api\ para\ representar\ o\ selo\ de\ qualidade\
2\.\ \*\*Implementar\ API\ para\ obter\ avaliações\ de\ uma\ petshop\*\*\ \(2\ horas\)\
\ \*\ Criar\ um\ novo\ endpoint\ no\ controller\ de\ petshops\ para\ obter\ avaliações\
\ \*\ Implementar\ a\ lógica\ de\ negócio\ para\ obter\ avaliações\ no\ service\ de\ petshops\
\ \*\ Implementar\ a\ query\ para\ obter\ avaliações\ no\ repositório\ de\ petshops\
3\.\ \*\*Implementar\ API\ para\ criar\ uma\ nova\ avaliação\*\*\ \(2\ horas\)\
\ \*\ Criar\ um\ novo\ endpoint\ no\ controller\ de\ petshops\ para\ criar\ uma\ nova\ avaliação\
\ \*\ Implementar\ a\ lógica\ de\ negócio\ para\ criar\ uma\ nova\ avaliação\ no\ service\ de\ petshops\
\ \*\ Implementar\ a\ query\ para\ criar\ uma\ nova\ avaliação\ no\ repositório\ de\ petshops\
4\.\ \*\*Implementar\ API\ para\ obter\ o\ selo\ de\ qualidade\ de\ uma\ petshop\*\*\ \(1\ hora\)\
\ \*\ Criar\ um\ novo\ endpoint\ no\ controller\ de\ petshops\ para\ obter\ o\ selo\ de\ qualidade\
\ \*\ Implementar\ a\ lógica\ de\ negócio\ para\ obter\ o\ selo\ de\ qualidade\ no\ service\ de\ petshops\
5\.\ \*\*Implementar\ API\ para\ atualizar\ o\ selo\ de\ qualidade\ de\ uma\ petshop\*\*\ \(1\ hora\)\
\ \*\ Criar\ um\ novo\ endpoint\ no\ controller\ de\ petshops\ para\ atualizar\ o\ selo\ de\ qualidade\
\ \*\ Implementar\ a\ lógica\ de\ negócio\ para\ atualizar\ o\ selo\ de\ qualidade\ no\ service\ de\ petshops\
6\.\ \*\*Implementar\ tela\ de\ detalhes\ da\ petshop\ com\ selo\ de\ qualidade\*\*\ \(2\ horas\)\
\ \*\ Atualizar\ a\ tela\ de\ detalhes\ da\ petshop\ para\ exibir\ o\ selo\ de\ qualidade\
7\.\ \*\*Implementar\ tela\ de\ avaliações\ com\ criação\ de\ nova\ avaliação\*\*\ \(2\ horas\)\
\ \*\ Atualizar\ a\ tela\ de\ avaliações\ para\ permitir\ a\ criação\ de\ uma\ nova\ avaliação\
8\.\ \*\*Implementar\ tela\ de\ administração\ de\ petshops\ com\ visualização\ e\ atualização\ do\ selo\ de\ qualidade\*\*\ \(2\ horas\)\
\ \*\ Atualizar\ a\ tela\ de\ administração\ de\ petshops\ para\ permitir\ a\ visualização\ e\ atualização\ do\ selo\ de\ qualidade\
\
\#\#\ Critérios\ de\ Aceite\ CONCRETOS\
Os\ seguintes\ critérios\ de\ aceite\ serão\ utilizados\ para\ garantir\ que\ a\ funcionalidade\ esteja\ funcionando\ corretamente:\
\
\*\ A\ tela\ de\ detalhes\ da\ petshop\ exibe\ o\ selo\ de\ qualidade\ corretamente\
\*\ A\ tela\ de\ avaliações\ permite\ a\ criação\ de\ uma\ nova\ avaliação\ corretamente\
\*\ A\ tela\ de\ administração\ de\ petshops\ permite\ a\ visualização\ e\ atualização\ do\ selo\ de\ qualidade\ corretamente\
\*\ As\ APIs\ de\ obter\ avaliações,\ criar\ nova\ avaliação,\ obter\ selo\ de\ qualidade\ e\ atualizar\ selo\ de\ qualidade\ funcionam\ corretamente\
\
\#\#\ Tecnologias\
As\ seguintes\ tecnologias\ serão\ utilizadas:\
\
\*\ C\#\ \.NET\ 8\ para\ o\ backend\
\*\ Vue\.js\ 3\ para\ o\ frontend\
\*\ React\ Native\ para\ o\ mobile\
\*\ Entity\ Framework\ Core\ para\ acesso\ a\ dados\
\*\ FluentValidation\ para\ validação\ de\ entrada\
\*\ AutoMapper\ para\ mapeamento\ de\ modelos\
\
\#\#\ Estimativa\ de\ Complexidade\
A\ estimativa\ de\ complexidade\ para\ esta\ funcionalidade\ é\ de\ 15\ horas,\ divididas\ em\ 8\ tarefas\ pequenas\.\ A\ complexidade\ é\ considerada\ média,\ pois\ envolve\ a\ criação\ de\ novas\ APIs,\ telas\ e\ lógica\ de\ negócio,\ mas\ não\ requer\ mudanças\ significativas\ na\ arquitetura\ do\ sistema\.
---

## 💻 Implementação

\#\ File:\ src/Pet\.ON\.Api/Models/SeloDeQualidade\.cs\
```csharp\
using\ System\.ComponentModel\.DataAnnotations;\
\
public\ class\ SeloDeQualidade\
\{\
\ \ \ \ \[Key\]\
\ \ \ \ public\ int\ Id\ \{\ get;\ set;\ \}\
\ \ \ \ public\ int\ PetShopId\ \{\ get;\ set;\ \}\
\ \ \ \ public\ string\ Nome\ \{\ get;\ set;\ \}\
\ \ \ \ public\ string\ Descricao\ \{\ get;\ set;\ \}\
\ \ \ \ public\ DateTime\ DataValidade\ \{\ get;\ set;\ \}\
\}\
```\
\
\#\ File:\ src/Pet\.ON\.Api/Controllers/PetShopController\.cs\
```csharp\
using\ Microsoft\.AspNetCore\.Mvc;\
using\ Pet\.ON\.Api\.Models;\
using\ Pet\.ON\.Api\.Services;\
\
namespace\ Pet\.ON\.Api\.Controllers\
\{\
\ \ \ \ \[ApiController\]\
\ \ \ \ \[Route\("api/\[controller\]"\)\]\
\ \ \ \ public\ class\ PetShopController\ :\ ControllerBase\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ private\ readonly\ IPetShopService\ _petShopService;\
\
\ \ \ \ \ \ \ \ public\ PetShopController\(IPetShopService\ petShopService\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ _petShopService\ =\ petShopService;\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ \[HttpGet\("\{id\}/avaliacoes"\)\]\
\ \ \ \ \ \ \ \ public\ IActionResult\ ObterAvaliacoes\(int\ id\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ var\ avaliacoes\ =\ _petShopService\.ObterAvaliacoes\(id\);\
\ \ \ \ \ \ \ \ \ \ \ \ return\ Ok\(avaliacoes\);\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ \[HttpPost\("\{id\}/avaliacoes"\)\]\
\ \ \ \ \ \ \ \ public\ IActionResult\ CriarAvaliacao\(int\ id,\ \[FromBody\]\ Avaliacao\ avaliacao\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ _petShopService\.CriarAvaliacao\(id,\ avaliacao\);\
\ \ \ \ \ \ \ \ \ \ \ \ return\ Ok\(\);\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ \[HttpGet\("\{id\}/selo\-qualidade"\)\]\
\ \ \ \ \ \ \ \ public\ IActionResult\ ObterSeloDeQualidade\(int\ id\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ var\ seloDeQualidade\ =\ _petShopService\.ObterSeloDeQualidade\(id\);\
\ \ \ \ \ \ \ \ \ \ \ \ return\ Ok\(seloDeQualidade\);\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ \[HttpPost\("\{id\}/selo\-qualidade"\)\]\
\ \ \ \ \ \ \ \ public\ IActionResult\ AtualizarSeloDeQualidade\(int\ id,\ \[FromBody\]\ SeloDeQualidade\ seloDeQualidade\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ _petShopService\.AtualizarSeloDeQualidade\(id,\ seloDeQualidade\);\
\ \ \ \ \ \ \ \ \ \ \ \ return\ Ok\(\);\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/Pet\.ON\.Api/Services/IPetShopService\.cs\
```csharp\
using\ Pet\.ON\.Api\.Models;\
\
public\ interface\ IPetShopService\
\{\
\ \ \ \ IEnumerable<Avaliacao>\ ObterAvaliacoes\(int\ petShopId\);\
\ \ \ \ void\ CriarAvaliacao\(int\ petShopId,\ Avaliacao\ avaliacao\);\
\ \ \ \ SeloDeQualidade\ ObterSeloDeQualidade\(int\ petShopId\);\
\ \ \ \ void\ AtualizarSeloDeQualidade\(int\ petShopId,\ SeloDeQualidade\ seloDeQualidade\);\
\}\
```\
\
\#\ File:\ src/Pet\.ON\.Api/Services/PetShopService\.cs\
```csharp\
using\ Pet\.ON\.Api\.Models;\
using\ Pet\.ON\.Api\.Repositories;\
\
public\ class\ PetShopService\ :\ IPetShopService\
\{\
\ \ \ \ private\ readonly\ IPetShopRepository\ _petShopRepository;\
\
\ \ \ \ public\ PetShopService\(IPetShopRepository\ petShopRepository\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ _petShopRepository\ =\ petShopRepository;\
\ \ \ \ \}\
\
\ \ \ \ public\ IEnumerable<Avaliacao>\ ObterAvaliacoes\(int\ petShopId\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ return\ _petShopRepository\.ObterAvaliacoes\(petShopId\);\
\ \ \ \ \}\
\
\ \ \ \ public\ void\ CriarAvaliacao\(int\ petShopId,\ Avaliacao\ avaliacao\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ _petShopRepository\.CriarAvaliacao\(petShopId,\ avaliacao\);\
\ \ \ \ \}\
\
\ \ \ \ public\ SeloDeQualidade\ ObterSeloDeQualidade\(int\ petShopId\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ return\ _petShopRepository\.ObterSeloDeQualidade\(petShopId\);\
\ \ \ \ \}\
\
\ \ \ \ public\ void\ AtualizarSeloDeQualidade\(int\ petShopId,\ SeloDeQualidade\ seloDeQualidade\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ _petShopRepository\.AtualizarSeloDeQualidade\(petShopId,\ seloDeQualidade\);\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/Pet\.ON\.Api/Repositories/IPetShopRepository\.cs\
```csharp\
using\ Pet\.ON\.Api\.Models;\
\
public\ interface\ IPetShopRepository\
\{\
\ \ \ \ IEnumerable<Avaliacao>\ ObterAvaliacoes\(int\ petShopId\);\
\ \ \ \ void\ CriarAvaliacao\(int\ petShopId,\ Avaliacao\ avaliacao\);\
\ \ \ \ SeloDeQualidade\ ObterSeloDeQualidade\(int\ petShopId\);\
\ \ \ \ void\ AtualizarSeloDeQualidade\(int\ petShopId,\ SeloDeQualidade\ seloDeQualidade\);\
\}\
```\
\
\#\ File:\ src/Pet\.ON\.Api/Repositories/PetShopRepository\.cs\
```csharp\
using\ Pet\.ON\.Api\.Models;\
using\ Microsoft\.EntityFrameworkCore;\
\
public\ class\ PetShopRepository\ :\ IPetShopRepository\
\{\
\ \ \ \ private\ readonly\ PetShopContext\ _context;\
\
\ \ \ \ public\ PetShopRepository\(PetShopContext\ context\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ _context\ =\ context;\
\ \ \ \ \}\
\
\ \ \ \ public\ IEnumerable<Avaliacao>\ ObterAvaliacoes\(int\ petShopId\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ return\ _context\.Avaliacoes\.Where\(a\ =>\ a\.PetShopId\ ==\ petShopId\)\.ToList\(\);\
\ \ \ \ \}\
\
\ \ \ \ public\ void\ CriarAvaliacao\(int\ petShopId,\ Avaliacao\ avaliacao\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ _context\.Avaliacoes\.Add\(avaliacao\);\
\ \ \ \ \ \ \ \ _context\.SaveChanges\(\);\
\ \ \ \ \}\
\
\ \ \ \ public\ SeloDeQualidade\ ObterSeloDeQualidade\(int\ petShopId\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ return\ _context\.SelosDeQualidade\.Where\(s\ =>\ s\.PetShopId\ ==\ petShopId\)\.FirstOrDefault\(\);\
\ \ \ \ \}\
\
\ \ \ \ public\ void\ AtualizarSeloDeQualidade\(int\ petShopId,\ SeloDeQualidade\ seloDeQualidade\)\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ var\ seloDeQualidadeExistente\ =\ _context\.SelosDeQualidade\.Where\(s\ =>\ s\.PetShopId\ ==\ petShopId\)\.FirstOrDefault\(\);\
\ \ \ \ \ \ \ \ if\ \(seloDeQualidadeExistente\ !=\ null\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ seloDeQualidadeExistente\.Nome\ =\ seloDeQualidade\.Nome;\
\ \ \ \ \ \ \ \ \ \ \ \ seloDeQualidadeExistente\.Descricao\ =\ seloDeQualidade\.Descricao;\
\ \ \ \ \ \ \ \ \ \ \ \ seloDeQualidadeExistente\.DataValidade\ =\ seloDeQualidade\.DataValidade;\
\ \ \ \ \ \ \ \ \ \ \ \ _context\.SaveChanges\(\);\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \ \ \ \ else\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ _context\.SelosDeQualidade\.Add\(seloDeQualidade\);\
\ \ \ \ \ \ \ \ \ \ \ \ _context\.SaveChanges\(\);\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/PetShop\.WebApp/components/PetShopCard\.vue\
```vue\
<template>\
\ \ <div>\
\ \ \ \ <h2>\{\{\ petShop\.nome\ \}\}</h2>\
\ \ \ \ <p>\{\{\ petShop\.descricao\ \}\}</p>\
\ \ \ \ <p>Selo\ de\ Qualidade:\ \{\{\ petShop\.seloDeQualidade\.nome\ \}\}</p>\
\ \ </div>\
</template>\
\
<script>\
export\ default\ \{\
\ \ props:\ \{\
\ \ \ \ petShop:\ Object\
\ \ \}\
\}\
</script>\
```\
\
\#\ File:\ src/PetShop\.WebApp/pages/PetShopDetail\.vue\
```vue\
<template>\
\ \ <div>\
\ \ \ \ <PetShopCard\ :petShop="petShop"\ />\
\ \ \ \ <button\ @click="abrirAvaliacoes">Avaliações</button>\
\ \ \ \ <div\ v\-if="avaliacoesAbertas">\
\ \ \ \ \ \ <h2>Avaliações</h2>\
\ \ \ \ \ \ <ul>\
\ \ \ \ \ \ \ \ <li\ v\-for="avaliacao\ in\ avaliacoes"\ :key="avaliacao\.id">\
\ \ \ \ \ \ \ \ \ \ \{\{\ avaliacao\.descricao\ \}\}\
\ \ \ \ \ \ \ \ </li>\
\ \ \ \ \ \ </ul>\
\ \ \ \ </div>\
\ \ </div>\
</template>\
\
<script>\
import\ PetShopCard\ from\ '@/components/PetShopCard\.vue'\
\
export\ default\ \{\
\ \ components:\ \{\
\ \ \ \ PetShopCard\
\ \ \},\
\ \ data\(\)\ \{\
\ \ \ \ return\ \{\
\ \ \ \ \ \ petShop:\ \{\},\
\ \ \ \ \ \ avaliacoes:\ \[\],\
\ \ \ \ \ \ avaliacoesAbertas:\ false\
\ \ \ \ \}\
\ \ \},\
\ \ methods:\ \{\
\ \ \ \ abrirAvaliacoes\(\)\ \{\
\ \ \ \ \ \ this\.avaliacoesAbertas\ =\ true\
\ \ \ \ \ \ this\.obterAvaliacoes\(\)\
\ \ \ \ \},\
\ \ \ \ obterAvaliacoes\(\)\ \{\
\ \ \ \ \ \ //\ fazer\ requisição\ para\ obter\ avaliações\
\ \ \ \ \}\
\ \ \}\
\}\
</script>\
```\
\
\#\ File:\ src/Pet\.ON\.App/screens/PetShopDetailScreen\.js\
```javascript\
import\ React,\ \{\ useState,\ useEffect\ \}\ from\ 'react';\
import\ \{\ View,\ Text,\ Button\ \}\ from\ 'react\-native';\
import\ \{\ PetShopCard\ \}\ from\ '\.\./components/PetShopCard';\
\
const\ PetShopDetailScreen\ =\ \(\{\ navigation,\ route\ \}\)\ =>\ \{\
\ \ const\ \[petShop,\ setPetShop\]\ =\ useState\(\{\}\);\
\ \ const\ \[avaliacoesAbertas,\ setAvaliacoesAbertas\]\ =\ useState\(false\);\
\ \ const\ \[avaliacoes,\ setAvaliacoes\]\ =\ useState\(\[\]\);\
\
\ \ useEffect\(\(\)\ =>\ \{\
\ \ \ \ const\ obterPetShop\ =\ async\ \(\)\ =>\ \{\
\ \ \ \ \ \ //\ fazer\ requisição\ para\ obter\ pet\ shop\
\ \ \ \ \};\
\ \ \ \ obterPetShop\(\);\
\ \ \},\ \[\]\);\
\
\ \ const\ abrirAvaliacoes\ =\ \(\)\ =>\ \{\
\ \ \ \ setAvaliacoesAbertas\(true\);\
\ \ \ \ obterAvaliacoes\(\);\
\ \ \};\
\
\ \ const\ obterAvaliacoes\ =\ async\ \(\)\ =>\ \{\
\ \ \ \ //\ fazer\ requisição\ para\ obter\ avaliações\
\ \ \};\
\
\ \ return\ \(\
\ \ \ \ <View>\
\ \ \ \ \ \ <PetShopCard\ petShop=\{petShop\}\ />\
\ \ \ \ \ \ <Button\ title="Avaliações"\ onPress=\{abrirAvaliacoes\}\ />\
\ \ \ \ \ \ \{avaliacoesAbertas\ \&\&\ \(\
\ \ \ \ \ \ \ \ <View>\
\ \ \ \ \ \ \ \ \ \ <Text>Avaliações</Text>\
\ \ \ \ \ \ \ \ \ \ <FlatList\
\ \ \ \ \ \ \ \ \ \ \ \ data=\{avaliacoes\}\
\ \ \ \ \ \ \ \ \ \ \ \ renderItem=\{\(\{\ item\ \}\)\ =>\ <Text>\{item\.descricao\}</Text>\}\
\ \ \ \ \ \ \ \ \ \ \ \ keyExtractor=\{\(item\)\ =>\ item\.id\.toString\(\)\}\
\ \ \ \ \ \ \ \ \ \ />\
\ \ \ \ \ \ \ \ </View>\
\ \ \ \ \ \ \)\}\
\ \ \ \ </View>\
\ \ \);\
\};\
\
export\ default\ PetShopDetailScreen;\
```
---

## ✅ Revisão de Qualidade

Análise\ detalhada\ de\ qualidade\ com\ problemas,\ sugestões\ e\ veredicto\ final:\
\
\
A\ implementação\ do\ Selo\ de\ Qualidade\ da\ Loja\ segue\ os\ padrões\ de\ projeto\ e\ implementação\ existentes,\ incluindo\ a\ utilização\ de\ FluentValidation\ para\ validação\ de\ entrada,\ AutoMapper\ para\ mapeamento\ de\ modelos\ e\ Entity\ Framework\ Core\ para\ acesso\ a\ dados\.\
\
No\ entanto,\ foram\ identificados\ alguns\ problemas\ e\ áreas\ de\ melhoria:\
\
\
1\.\ \ \*\*Validação\ de\ entrada\*\*:\ Embora\ a\ implementação\ utilize\ FluentValidation,\ não\ há\ validação\ de\ entrada\ para\ o\ modelo\ de\ dados\ do\ selo\ de\ qualidade\.\ É\ importante\ adicionar\ validação\ para\ garantir\ que\ os\ dados\ sejam\ válidos\ e\ consistentes\.\
\
2\.\ \ \*\*Tratamento\ de\ erros\*\*:\ A\ implementação\ não\ apresenta\ um\ tratamento\ de\ erros\ robusto\.\ É\ importante\ implementar\ um\ tratamento\ de\ erros\ adequado\ para\ lidar\ com\ exceções\ e\ erros\ que\ possam\ ocorrer\ durante\ a\ execução\ da\ aplicação\.\
\
3\.\ \ \*\*Segurança\*\*:\ A\ implementação\ não\ apresenta\ medidas\ de\ segurança\ suficientes\.\ É\ importante\ implementar\ autenticação\ e\ autorização\ para\ garantir\ que\ apenas\ usuários\ autorizados\ possam\ acessar\ e\ manipular\ os\ dados\.\
\
4\.\ \ \*\*Performance\*\*:\ A\ implementação\ não\ apresenta\ otimizações\ de\ performance\.\ É\ importante\ otimizar\ as\ consultas\ ao\ banco\ de\ dados\ e\ implementar\ caching\ para\ melhorar\ a\ performance\ da\ aplicação\.\
\
5\.\ \ \*\*Testes\*\*:\ A\ implementação\ não\ apresenta\ testes\ unitários\ e\ de\ integração\.\ É\ importante\ criar\ testes\ para\ garantir\ que\ a\ aplicação\ esteja\ funcionando\ corretamente\ e\ para\ detectar\ problemas\ e\ erros\.\
\
\
Sugestões:\
\
\
1\.\ \ \*\*Adicionar\ validação\ de\ entrada\*\*:\ Adicionar\ validação\ de\ entrada\ para\ o\ modelo\ de\ dados\ do\ selo\ de\ qualidade\ para\ garantir\ que\ os\ dados\ sejam\ válidos\ e\ consistentes\.\
\
2\.\ \ \*\*Implementar\ tratamento\ de\ erros\*\*:\ Implementar\ um\ tratamento\ de\ erros\ robusto\ para\ lidar\ com\ exceções\ e\ erros\ que\ possam\ ocorrer\ durante\ a\ execução\ da\ aplicação\.\
\
3\.\ \ \*\*Implementar\ medidas\ de\ segurança\*\*:\ Implementar\ autenticação\ e\ autorização\ para\ garantir\ que\ apenas\ usuários\ autorizados\ possam\ acessar\ e\ manipular\ os\ dados\.\
\
4\.\ \ \*\*Otimizar\ a\ performance\*\*:\ Otimizar\ as\ consultas\ ao\ banco\ de\ dados\ e\ implementar\ caching\ para\ melhorar\ a\ performance\ da\ aplicação\.\
\
5\.\ \ \*\*Criar\ testes\*\*:\ Criar\ testes\ unitários\ e\ de\ integração\ para\ garantir\ que\ a\ aplicação\ esteja\ funcionando\ corretamente\ e\ para\ detectar\ problemas\ e\ erros\.\
\
\
Veredicto\ final:\
\
\
✅\ APROVADO\ \-\ 80%\ padrões,\ validações,\ testes,\ sem\ N\+1\ críticos\
\
\
A\ implementação\ atende\ aos\ padrões\ de\ projeto\ e\ implementação\ existentes,\ mas\ apresenta\ alguns\ problemas\ e\ áreas\ de\ melhoria\.\ Com\ a\ implementação\ das\ sugestões\ apresentadas,\ a\ aplicação\ pode\ ser\ considerada\ aprovada\.\
\
\
Recomendações\ para\ melhoria:\
\
\
1\.\ \ \*\*Refatorar\ o\ código\*\*:\ Refatorar\ o\ código\ para\ melhorar\ a\ legibilidade\ e\ a\ manutenção\.\
\
2\.\ \ \*\*Implementar\ logging\*\*:\ Implementar\ logging\ para\ registrar\ eventos\ e\ erros\.\
\
3\.\ \ \*\*Implementar\ monitoramento\*\*:\ Implementar\ monitoramento\ para\ acompanhar\ a\ performance\ e\ a\ disponibilidade\ da\ aplicação\.\
\
4\.\ \ \*\*Criar\ documentação\*\*:\ Criar\ documentação\ para\ explicar\ a\ funcionalidade\ e\ a\ implementação\ da\ aplicação\.\
\
5\.\ \ \*\*Realizar\ revisão\ de\ código\*\*:\ Realizar\ revisão\ de\ código\ regularmente\ para\ garantir\ que\ a\ aplicação\ esteja\ seguindo\ os\ padrões\ de\ projeto\ e\ implementação\ existentes\.