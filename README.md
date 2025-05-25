# NyxKit

## Visão geral

Este projeto foi desenvolvido como um modelo inicial para a criação de APIs utilizando FastAPI

Ele é especialmente indicado para projetos pessoais, iniciativas voltadas ao aprendizado ou aplicações que não demandam alta escalabilidade

Seu principal objetivo é ser extremamente simples, permitindo que o desenvolvedor foque na construção da sua solução, sem se preocupar com configurações complexas ou estruturas excessivamente robustas

A estrutura do projeto segue a arquitetura baseada em funcionalidades (Feature-Based Architecture), utilizando o UV como gerenciador de dependências, Uvicorn como servidor ASGI, SQLModel como ORM e FastAPI para a construção dos endpoints

### Watchmen

uma mini-biblioteca experimental incluída no projeto. 

Construída sobre o SQLAlchemy, ela tem como objetivo detectar diferenças entre as Models do projeto e a estrutura real do banco de dados, facilitando a automação de migrações

## Iniciando

``~ git clone https://github.com/ThiagoVRabethge/NyxKit``

``~ cd NyxKit``

``~ uv sync``

``~ .venv\Scripts\activate``

``py -m uvicorn main:app --reload``

## Variáveis de ambiente

``SECRET=``

``ALGORITHM=``

``DIALECTICS=``

## Próximas funcionalidades

1. Início via linha de comando

2. Sistema de Logs

3. seeds

4. recuperação de senha/dois fatores/restante de auth
