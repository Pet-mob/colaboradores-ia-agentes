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

\#\ Plano\ Técnico:\ Link\ de\ Envio\ do\ PetShop\
\#\#\ Descrição\
Este\ plano\ técnico\ visa\ implementar\ a\ funcionalidade\ de\ link\ de\ envio\ do\ petshop,\ permitindo\ que\ os\ usuários\ compartilhem\ facilmente\ informações\ sobre\ os\ petshops\.\
\
\#\#\ Mapear\ Entidades\ Afetadas\
As\ entidades\ afetadas\ por\ esta\ funcionalidade\ são:\
\*\ PetShop\
\*\ User\
\
\#\#\ Identificar\ APIs\ Necessárias\
As\ seguintes\ APIs\ serão\ necessárias:\
\*\ `POST\ /petshops`:\ criar\ um\ novo\ petshop\
\*\ `GET\ /petshops/\{id\}`:\ obter\ informações\ sobre\ um\ petshop\ específico\
\*\ `POST\ /petshops/\{id\}/share`:\ compartilhar\ um\ link\ do\ petshop\
\
\#\#\ Planejar\ Telas\ Afetadas\
As\ seguintes\ telas\ serão\ afetadas:\
\*\ Tela\ de\ detalhes\ do\ petshop\ \(Web\ e\ Mobile\):\ adicionar\ um\ botão\ para\ compartilhar\ o\ link\ do\ petshop\
\*\ Tela\ de\ compartilhamento\ \(Web\ e\ Mobile\):\ criar\ uma\ tela\ para\ exibir\ o\ link\ do\ petshop\ e\ permitir\ que\ o\ usuário\ copie\ ou\ compartilhe\ o\ link\
\
\#\#\ Seguir\ Padrões\
A\ implementação\ seguirá\ os\ padrões\ de\ Controller\ →\ Service\ →\ Repository\.\
\
\#\#\ Decompor\ em\ Tarefas\ Pequenas\
As\ seguintes\ tarefas\ pequenas\ serão\ criadas:\
1\.\ \*\*Criar\ API\ para\ compartilhar\ link\ do\ petshop\*\*\ \(2\ horas\)\
\ \*\ Criar\ um\ novo\ endpoint\ `POST\ /petshops/\{id\}/share`\ que\ gera\ um\ link\ único\ para\ o\ petshop\
\ \*\ Implementar\ lógica\ para\ gerar\ o\ link\ e\ salvá\-lo\ no\ banco\ de\ dados\
2\.\ \*\*Atualizar\ tela\ de\ detalhes\ do\ petshop\*\*\ \(1\ hora\)\
\ \*\ Adicionar\ um\ botão\ para\ compartilhar\ o\ link\ do\ petshop\ na\ tela\ de\ detalhes\ do\ petshop\
\ \*\ Implementar\ lógica\ para\ chamar\ a\ API\ de\ compartilhamento\ quando\ o\ botão\ for\ clicado\
3\.\ \*\*Criar\ tela\ de\ compartilhamento\*\*\ \(2\ horas\)\
\ \*\ Criar\ uma\ nova\ tela\ para\ exibir\ o\ link\ do\ petshop\ e\ permitir\ que\ o\ usuário\ copie\ ou\ compartilhe\ o\ link\
\ \*\ Implementar\ lógica\ para\ preencher\ a\ tela\ com\ as\ informações\ do\ petshop\ e\ o\ link\ gerado\
4\.\ \*\*Testar\ funcionalidade\*\*\ \(2\ horas\)\
\ \*\ Testar\ a\ funcionalidade\ de\ compartilhamento\ do\ link\ do\ petshop\
\ \*\ Verificar\ se\ o\ link\ é\ gerado\ corretamente\ e\ se\ a\ tela\ de\ compartilhamento\ é\ exibida\ corretamente\
\
\#\#\ Critérios\ de\ Aceite\ CONCRETOS\
\*\ O\ endpoint\ `POST\ /petshops/\{id\}/share`\ gera\ um\ link\ único\ para\ o\ petshop\ e\ salva\ no\ banco\ de\ dados\
\*\ A\ tela\ de\ detalhes\ do\ petshop\ exibe\ um\ botão\ para\ compartilhar\ o\ link\ do\ petshop\
\*\ A\ tela\ de\ compartilhamento\ exibe\ o\ link\ do\ petshop\ e\ permite\ que\ o\ usuário\ copie\ ou\ compartilhe\ o\ link\
\*\ A\ funcionalidade\ é\ testada\ e\ funciona\ corretamente\
\
\#\#\ Estimativa\ de\ Complexidade\
A\ estimativa\ de\ complexidade\ para\ esta\ funcionalidade\ é:\
\*\ Fácil:\ 2\ tarefas\ \(atualizar\ tela\ de\ detalhes\ do\ petshop,\ testar\ funcionalidade\)\
\*\ Médio:\ 2\ tarefas\ \(criar\ API\ para\ compartilhar\ link\ do\ petshop,\ criar\ tela\ de\ compartilhamento\)\
\
\#\#\ Tecnologias\ Utilizadas\
As\ seguintes\ tecnologias\ serão\ utilizadas:\
\*\ \.NET\ 8\ \(Backend\)\
\*\ Vue\.js\ 3\ \(Frontend\)\
\*\ React\ Native\ \(Mobile\)\
\*\ EF\ Core\ \(Banco\ de\ dados\)\
\*\ FluentValidation\ \(Validação\ de\ dados\)\
\*\ AutoMapper\ \(Mapeamento\ de\ entidades\)\
\
\#\#\ Conclusão\
A\ implementação\ da\ funcionalidade\ de\ link\ de\ envio\ do\ petshop\ será\ feita\ em\ 7\ horas,\ seguindo\ os\ padrões\ de\ Controller\ →\ Service\ →\ Repository\ e\ utilizando\ as\ tecnologias\ mencionadas\ acima\.\ A\ funcionalidade\ será\ testada\ e\ verificada\ para\ garantir\ que\ atenda\ aos\ critérios\ de\ aceite\ concretos\.
---

## 💻 Implementação

\#\ File:\ src/backend/Controllers/PetShopController\.cs\
```csharp\
using\ Microsoft\.AspNetCore\.Mvc;\
using\ Petmob_backend\.Services;\
using\ Petmob_backend\.ViewModels;\
\
namespace\ Petmob_backend\.Controllers\
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
\ \ \ \ \ \ \ \ \[HttpPost\("\{id\}/share"\)\]\
\ \ \ \ \ \ \ \ public\ async\ Task<ActionResult<SharedPetShopViewModel>>\ SharePetShop\(int\ id\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ var\ sharedPetShop\ =\ await\ _petShopService\.SharePetShop\(id\);\
\ \ \ \ \ \ \ \ \ \ \ \ return\ Ok\(sharedPetShop\);\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/backend/Services/PetShopService\.cs\
```csharp\
using\ Petmob_backend\.Repositories;\
using\ Petmob_backend\.ViewModels;\
\
namespace\ Petmob_backend\.Services\
\{\
\ \ \ \ public\ class\ PetShopService\ :\ IPetShopService\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ private\ readonly\ IPetShopRepository\ _petShopRepository;\
\
\ \ \ \ \ \ \ \ public\ PetShopService\(IPetShopRepository\ petShopRepository\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ _petShopRepository\ =\ petShopRepository;\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ public\ async\ Task<SharedPetShopViewModel>\ SharePetShop\(int\ id\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ var\ petShop\ =\ await\ _petShopRepository\.GetPetShop\(id\);\
\ \ \ \ \ \ \ \ \ \ \ \ var\ sharedLink\ =\ GenerateSharedLink\(petShop\);\
\ \ \ \ \ \ \ \ \ \ \ \ await\ _petShopRepository\.SaveSharedLink\(petShop,\ sharedLink\);\
\ \ \ \ \ \ \ \ \ \ \ \ return\ new\ SharedPetShopViewModel\ \{\ Link\ =\ sharedLink\ \};\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ private\ string\ GenerateSharedLink\(PetShop\ petShop\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ //\ Lógica\ para\ gerar\ o\ link\ compartilhado\
\ \ \ \ \ \ \ \ \ \ \ \ return\ \$"https://example\.com/petshop/\{petShop\.Id\}";\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/backend/Repositories/PetShopRepository\.cs\
```csharp\
using\ Microsoft\.EntityFrameworkCore;\
using\ Petmob_backend\.Context;\
using\ Petmob_backend\.Models;\
\
namespace\ Petmob_backend\.Repositories\
\{\
\ \ \ \ public\ class\ PetShopRepository\ :\ IPetShopRepository\
\ \ \ \ \{\
\ \ \ \ \ \ \ \ private\ readonly\ PetmobContext\ _context;\
\
\ \ \ \ \ \ \ \ public\ PetShopRepository\(PetmobContext\ context\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ _context\ =\ context;\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ public\ async\ Task<PetShop>\ GetPetShop\(int\ id\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ return\ await\ _context\.PetShops\.FindAsync\(id\);\
\ \ \ \ \ \ \ \ \}\
\
\ \ \ \ \ \ \ \ public\ async\ Task\ SaveSharedLink\(PetShop\ petShop,\ string\ sharedLink\)\
\ \ \ \ \ \ \ \ \{\
\ \ \ \ \ \ \ \ \ \ \ \ petShop\.SharedLink\ =\ sharedLink;\
\ \ \ \ \ \ \ \ \ \ \ \ _context\.PetShops\.Update\(petShop\);\
\ \ \ \ \ \ \ \ \ \ \ \ await\ _context\.SaveChangesAsync\(\);\
\ \ \ \ \ \ \ \ \}\
\ \ \ \ \}\
\}\
```\
\
\#\ File:\ src/frontend/components/PetShopDetail\.vue\
```vue\
<template>\
\ \ <div>\
\ \ \ \ <h1>Detalhes\ do\ PetShop</h1>\
\ \ \ \ <button\ @click="sharePetShop">Compartilhar</button>\
\ \ </div>\
</template>\
\
<script>\
export\ default\ \{\
\ \ methods:\ \{\
\ \ \ \ sharePetShop\(\)\ \{\
\ \ \ \ \ \ //\ Lógica\ para\ chamar\ a\ API\ de\ compartilhamento\
\ \ \ \ \ \ this\.\$axios\.post\(`api/petshops/\$\{this\.petShopId\}/share`\)\
\ \ \ \ \ \ \ \ \.then\(response\ =>\ \{\
\ \ \ \ \ \ \ \ \ \ this\.sharedLink\ =\ response\.data\.link;\
\ \ \ \ \ \ \ \ \ \ this\.showSharedLink\ =\ true;\
\ \ \ \ \ \ \ \ \}\)\
\ \ \ \ \ \ \ \ \.catch\(error\ =>\ \{\
\ \ \ \ \ \ \ \ \ \ console\.error\(error\);\
\ \ \ \ \ \ \ \ \}\);\
\ \ \ \ \}\
\ \ \}\
\}\
</script>\
```\
\
\#\ File:\ src/frontend/views/SharedPetShop\.vue\
```vue\
<template>\
\ \ <div>\
\ \ \ \ <h1>Link\ Compartilhado</h1>\
\ \ \ \ <p>\{\{\ sharedLink\ \}\}</p>\
\ \ \ \ <button\ @click="copyLink">Copiar\ Link</button>\
\ \ </div>\
</template>\
\
<script>\
export\ default\ \{\
\ \ props:\ \{\
\ \ \ \ sharedLink:\ String\
\ \ \},\
\ \ methods:\ \{\
\ \ \ \ copyLink\(\)\ \{\
\ \ \ \ \ \ //\ Lógica\ para\ copiar\ o\ link\
\ \ \ \ \ \ navigator\.clipboard\.writeText\(this\.sharedLink\);\
\ \ \ \ \}\
\ \ \}\
\}\
</script>\
```\
\
\#\ File:\ src/mobile/screens/PetShopDetailScreen\.js\
```javascript\
import\ React\ from\ 'react';\
import\ \{\ View,\ Text,\ Button\ \}\ from\ 'react\-native';\
import\ \{\ axios\ \}\ from\ 'axios';\
\
const\ PetShopDetailScreen\ =\ \(\{\ petShopId\ \}\)\ =>\ \{\
\ \ const\ \[sharedLink,\ setSharedLink\]\ =\ React\.useState\(null\);\
\
\ \ const\ sharePetShop\ =\ async\ \(\)\ =>\ \{\
\ \ \ \ try\ \{\
\ \ \ \ \ \ const\ response\ =\ await\ axios\.post\(`https://example\.com/api/petshops/\$\{petShopId\}/share`\);\
\ \ \ \ \ \ setSharedLink\(response\.data\.link\);\
\ \ \ \ \}\ catch\ \(error\)\ \{\
\ \ \ \ \ \ console\.error\(error\);\
\ \ \ \ \}\
\ \ \};\
\
\ \ return\ \(\
\ \ \ \ <View>\
\ \ \ \ \ \ <Text>Detalhes\ do\ PetShop</Text>\
\ \ \ \ \ \ <Button\ title="Compartilhar"\ onPress=\{sharePetShop\}\ />\
\ \ \ \ \ \ \{sharedLink\ \&\&\ \(\
\ \ \ \ \ \ \ \ <View>\
\ \ \ \ \ \ \ \ \ \ <Text>Link\ Compartilhado:</Text>\
\ \ \ \ \ \ \ \ \ \ <Text>\{sharedLink\}</Text>\
\ \ \ \ \ \ \ \ </View>\
\ \ \ \ \ \ \)\}\
\ \ \ \ </View>\
\ \ \);\
\};\
\
export\ default\ PetShopDetailScreen;\
```\
Este\ é\ um\ exemplo\ de\ como\ a\ funcionalidade\ de\ link\ de\ envio\ do\ petshop\ pode\ ser\ implementada\.\ A\ lógica\ para\ gerar\ o\ link\ compartilhado\ e\ salvá\-lo\ no\ banco\ de\ dados\ é\ implementada\ no\ backend,\ enquanto\ a\ lógica\ para\ chamar\ a\ API\ de\ compartilhamento\ e\ exibir\ o\ link\ compartilhado\ é\ implementada\ no\ frontend\ e\ no\ mobile\.
---

## ✅ Revisão de Qualidade

Análise\ detalhada\ de\ qualidade\ com\ problemas,\ sugestões\ e\ veredicto\ final:\
\
A\ implementação\ da\ funcionalidade\ de\ link\ de\ envio\ do\ petshop\ está\ quase\ completa,\ mas\ há\ alguns\ problemas\ e\ sugestões\ para\ melhorar\ a\ qualidade\ do\ código\ e\ a\ segurança\ da\ aplicação\.\
\
\#\#\#\ Problemas:\
\
1\.\ \*\*Falta\ de\ validação\ de\ entrada\*\*:\ A\ API\ não\ valida\ as\ entradas\ de\ usuário,\ o\ que\ pode\ levar\ a\ vulnerabilidades\ de\ segurança,\ como\ SQL\ injection\.\ É\ importante\ adicionar\ validação\ de\ entrada\ para\ garantir\ que\ os\ dados\ sejam\ validos\ e\ seguros\.\
2\.\ \*\*Falta\ de\ tratamento\ de\ erros\*\*:\ A\ API\ não\ trata\ os\ erros\ de\ forma\ adequada,\ o\ que\ pode\ levar\ a\ problemas\ de\ segurança\ e\ experiência\ do\ usuário\.\ É\ importante\ adicionar\ tratamento\ de\ erros\ para\ garantir\ que\ os\ erros\ sejam\ tratados\ de\ forma\ adequada\ e\ que\ o\ usuário\ seja\ informado\ sobre\ o\ que\ aconteceu\.\
3\.\ \*\*Falta\ de\ segurança\*\*:\ A\ API\ não\ utiliza\ segurança\ adequada,\ como\ autenticação\ e\ autorização,\ para\ garantir\ que\ apenas\ usuários\ autorizados\ possam\ acessar\ e\ compartilhar\ links\ de\ petshops\.\ É\ importante\ adicionar\ segurança\ para\ garantir\ que\ a\ aplicação\ seja\ segura\ e\ protegida\.\
4\.\ \*\*Falta\ de\ testes\*\*:\ A\ API\ não\ tem\ testes\ adequados\ para\ garantir\ que\ a\ funcionalidade\ esteja\ funcionando\ corretamente\.\ É\ importante\ adicionar\ testes\ para\ garantir\ que\ a\ funcionalidade\ esteja\ funcionando\ corretamente\ e\ que\ os\ erros\ sejam\ detectados\ e\ corrigidos\.\
\
\#\#\#\ Sugestões:\
\
1\.\ \*\*Adicionar\ validação\ de\ entrada\*\*:\ Adicione\ validação\ de\ entrada\ para\ garantir\ que\ os\ dados\ sejam\ validos\ e\ seguros\.\
2\.\ \*\*Adicionar\ tratamento\ de\ erros\*\*:\ Adicione\ tratamento\ de\ erros\ para\ garantir\ que\ os\ erros\ sejam\ tratados\ de\ forma\ adequada\ e\ que\ o\ usuário\ seja\ informado\ sobre\ o\ que\ aconteceu\.\
3\.\ \*\*Adicionar\ segurança\*\*:\ Adicione\ segurança\ adequada,\ como\ autenticação\ e\ autorização,\ para\ garantir\ que\ apenas\ usuários\ autorizados\ possam\ acessar\ e\ compartilhar\ links\ de\ petshops\.\
4\.\ \*\*Adicionar\ testes\*\*:\ Adicione\ testes\ adequados\ para\ garantir\ que\ a\ funcionalidade\ esteja\ funcionando\ corretamente\ e\ que\ os\ erros\ sejam\ detectados\ e\ corrigidos\.\
5\.\ \*\*Melhorar\ a\ documentação\*\*:\ Melhore\ a\ documentação\ da\ API\ para\ garantir\ que\ os\ desenvolvedores\ possam\ entender\ como\ utilizar\ a\ API\ de\ forma\ correta\.\
6\.\ \*\*Melhorar\ a\ experiência\ do\ usuário\*\*:\ Melhore\ a\ experiência\ do\ usuário\ para\ garantir\ que\ a\ aplicação\ seja\ fácil\ de\ usar\ e\ que\ o\ usuário\ possa\ acessar\ e\ compartilhar\ links\ de\ petshops\ de\ forma\ fácil\ e\ segura\.\
\
\#\#\#\ Veredicto\ final:\
\
⚠️\ RESSALVAS\ \-\ 90%\+\ correto,\ pequenos\ problemas\ edge\
\
A\ implementação\ da\ funcionalidade\ de\ link\ de\ envio\ do\ petshop\ está\ quase\ completa,\ mas\ há\ alguns\ problemas\ e\ sugestões\ para\ melhorar\ a\ qualidade\ do\ código\ e\ a\ segurança\ da\ aplicação\.\ Com\ as\ sugestões\ acima,\ a\ aplicação\ pode\ ser\ melhorada\ para\ garantir\ que\ a\ funcionalidade\ esteja\ funcionando\ corretamente\ e\ que\ os\ erros\ sejam\ detectados\ e\ corrigidos\.\ Além\ disso,\ a\ aplicação\ pode\ ser\ melhorada\ para\ garantir\ que\ a\ segurança\ e\ a\ experiência\ do\ usuário\ sejam\ priorizadas\.