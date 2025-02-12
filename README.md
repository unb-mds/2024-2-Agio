# 📚 2024/2 - AGIO 📂 <!-- omit from toc -->
![GitHub License](https://img.shields.io/github/license/unb-mds/2024-2-Agio)
![GitHub Issues](https://img.shields.io/github/issues/unb-mds/2024-2-Agio)
![GitHub Contributors](https://img.shields.io/github/contributors/unb-mds/2024-2-Agio)

---

<br>
Workflows:

![Test Status](https://github.com/unb-mds/2024-2-Agio/actions/workflows/django-ci.yml/badge.svg)
![Lint Critical Status](https://github.com/unb-mds/2024-2-Agio/actions/workflows/lint-critical.yml/badge.svg)
![Lint Style Status](https://github.com/unb-mds/2024-2-Agio/actions/workflows/lint-style.yml/badge.svg)


## ***Sumário*** <!-- omit from toc -->
- [1. Resumo 💡](#1-resumo-)
- [2. Escopo da Aplicação 💼](#2-escopo-da-aplicação-)
- [3. Pré-requisitos 📋](#3-pré-requisitos-)
- [4. Etapas para a Execução do Ambiente 🔧](#4-etapas-para-a-execução-do-ambiente-)
- [5. Equipe de Desenvolvimento 👥](#5-equipe-de-desenvolvimento-)

<br>


## 1. Resumo 💡
O *Agio* (Aplicação de Gestão de Inventário Otimizada) é um projeto open source da disciplina de Métodos de Desenvolvimento de Software, da Universidade de Brasília. O nosso objetivo é trabalhar nas diferentes áreas que envolvem o ciclo de vida de um software, afim de desenvolver uma aplicação de gerenciamento/gestão de inventário(s).

<br>


## 2. Escopo da Aplicação 💼
O *Agio*, ou Aplicação de Gestão de Inventário Otimizada, é um sistema web simples desenvolvido com o objetivo de servir como um controle de inventário de uma corporação de pequeno a médio porte. Dessa forma, o usuário será capaz de manter um controle dos itens presentes no inventário, adicionando e removendo os componentes de acordo com sua necessidade e monitorando-os de forma prática, simples e segura.

Ao utilizar os serviços do nosso projeto, um usuário encontrará uma série de funcionalidades, dentre elas:

*   Criação do superusuário, o qual controla quem pode acessar/editar o inventário;
*   Login e Logout de usuários, com controle de acesso às páginas;
*   Registro das informações de usuário e de inventário em um banco de dados;
*   Acesso ao inventário, permitindo visualização dos itens nele presentes;
*   Adição, remoção e edição dos itens em um inventário;
*   Visualização em sequência personalizada dos itens do inventário;
*   Exportação dos componentes de um inventário para um arquivo *.CSV*;
*   Entre outras, a serem implementadas.


<br>

## 3. Pré-requisitos 📋
1. Python; [[LINK]](https://www.python.org/downloads/)
2. Docker Engine (ou Docker desktop); [[LINK]](https://www.docker.com/products/docker-desktop/)

<br>


## 4. Etapas para a Execução do Ambiente 🔧

1. Clone o repositório;
    ```Bash
    git clone https://github.com/unb-mds/2024-2-Squad04

2. Navegue até o diretório do projeto;
    ```Bash
    cd PROJECT

3. Crie um ambiente virtual e ative-o;
    ```Bash
    python -m venv .venv
    .venv/scripts/activate

4. Instale as dependências;
    ```Bash
    pip install -r requirements.txt

5. Baixe o Docker Desktop (Docker Engine, no linux) no [site oficial do docker](https://www.docker.com/products/docker-desktop/);

<br>

1. Crie um arquivo ".env" na pasta /PROJECT, e insira as variáveis do projeto (requisitá-las com os desenvolvedores);

<br>

7. Execute o container do docker-compose.yml;
    ```Bash
    docker compose up -d

8. Navegue até a raiz do projeto;
    ```Bash
    cd src 

9. Gere os arquivos de migração; 
    ```Bash
    python manage.py makemigrations

10. Aplique as migrações do banco de dados;
    ```Bash
    python manage.py migrate

11. Inicie o servidor de desenvolvimento;
    ```Bash
    python manage.py runserver

E pronto! Assim o ambiente do projeto está pronto para execução.

<br>


## 5. Equipe de Desenvolvimento 👥

| Scrum Master | Product Owner | Front-End Developer | Back-End Developer | Front-End Developer | Architect |
|:-------------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| [![](https://avatars.githubusercontent.com/caio-venancio)](https://github.com/caio-venancio) | [![](https://avatars.githubusercontent.com/eduardodpms)](https://github.com/eduardodpms) | [![](https://avatars.githubusercontent.com/EnzoEmir)](https://github.com/EnzoEmir) | [![](https://avatars.githubusercontent.com/JMPNascimento)](https://github.com/JMPNascimento) | [![](https://avatars.githubusercontent.com/MM4k)](https://github.com/MM4k) | [![](https://avatars.githubusercontent.com/VictorPontual)](https://github.com/VictorPontual) |
| [Caio Venâncio](https://github.com/caio-venancio) | [Eduardo de Pina](https://github.com/eduardodpms) | [Enzo Emir](https://github.com/EnzoEmir) | [João Maurício](https://github.com/JMPNascimento) | [Marcelo Makoto](https://github.com/MM4k) | [Victor Pontual](https://github.com/VictorPontual) |