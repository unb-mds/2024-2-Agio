# 📚AGIO📚
<!-- ###### Aplicação de Gestão de Inventário Otimizada -->
![Lint Critical Status](https://github.com/unb-mds/2024-2-Agio/actions/workflows/lint-critical.yml/badge.svg)
![Lint Style Status](https://github.com/unb-mds/2024-2-Agio/actions/workflows/lint-style.yml/badge.svg)

<br>

##  2024-2-Squad04 

## ***Sumário*** <!-- omit from toc -->
- [1. Descrição 💡](#1-descrição-)
- [2. Pré-requisitos 📋](#2-pré-requisitos-)
- [3. Etapas para a Execução do Ambiente 🔧](#3-etapas-para-a-execução-do-ambiente-)
- [4. Novas Planilhas do Banco](#4-novas-planilhas-no-banco-)
- [5. Equipe 👥](#4-equipe-)

<br>

## 1. Descrição 💡
Esse é um projeto da disciplina de Métodos de Desenvolvimento de Software, da Universidade de Brasília. O nosso objetivo é trabalhar nas diferentes áreas que envolvem o ciclo de vida de um software, afim de desenvolver uma aplicação de gerenciamento/gestão de inventário(s).

<br>

## 2. Pré-requisitos 📋
1. Python; [[LINK]](https://www.python.org/downloads/)
2. Docker Engine (ou Docker desktop); [[LINK]](https://www.docker.com/products/docker-desktop/)
3. Django Models; [[LINK]](https://docs.djangoproject.com/en/5.1/topics/db/models/) 
<br>

## 3. Etapas para a Execução do Ambiente 🔧

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

5. Baixe a Docker Desktop (Docker Engine, linux) no [site oficial do docker](https://www.docker.com/products/docker-desktop/);

<br>

6. Crie um arquivo ".env" na pasta /PROJECT, e insira as variáveis do projeto(requisitar elas com os desenvolvedores);

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

E pronto! Assim está pronto para a execução do ambiente do projeto.

<br>

## 4. Novas Planilhas no Banco 🏦

1. Crie ou modifique uma planilha seguindo o models;

<br>

2. Navegue até a raiz do projeto;
    ```Bash
     cd .\PROJECT\src\ 

3. Gere os arquivos de migração; 
    ```Bash
    python manage.py makemigrations

4. Aplique as migrações do banco de dados;
    ```Bash
    python manage.py migrate

<br>

## 5. Equipe 👥

| Scrum Master | Product Owner | Front-End Developer | Back-End Developer | Front-End Developer | Architect |
|:-------------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| [![](https://avatars.githubusercontent.com/caio-venancio)](https://github.com/caio-venancio) | [![](https://avatars.githubusercontent.com/eduardodpms)](https://github.com/eduardodpms) | [![](https://avatars.githubusercontent.com/EnzoEmir)](https://github.com/EnzoEmir) | [![](https://avatars.githubusercontent.com/JMPNascimento)](https://github.com/JMPNascimento) | [![](https://avatars.githubusercontent.com/MM4k)](https://github.com/MM4k) | [![](https://avatars.githubusercontent.com/VictorPontual)](https://github.com/VictorPontual) |
| [Caio Venâncio](https://github.com/caio-venancio) | [Eduardo de Pina](https://github.com/eduardodpms) | [Enzo Emir](https://github.com/EnzoEmir) | [João Maurício](https://github.com/JMPNascimento) | [Marcelo Makoto](https://github.com/MM4k) | [Victor Pontual](https://github.com/VictorPontual) |