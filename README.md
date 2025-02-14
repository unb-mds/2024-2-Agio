![GitHub License](https://img.shields.io/github/license/unb-mds/2024-2-Agio)
![GitHub Issues](https://img.shields.io/github/issues/unb-mds/2024-2-Agio)
![GitHub Contributors](https://img.shields.io/github/contributors/unb-mds/2024-2-Agio)
![Test Status](https://github.com/unb-mds/2024-2-Agio/actions/workflows/django-ci.yml/badge.svg)
![Lint Critical Status](https://github.com/unb-mds/2024-2-Agio/actions/workflows/lint-critical.yml/badge.svg)
![Lint Style Status](https://github.com/unb-mds/2024-2-Agio/actions/workflows/lint-style.yml/badge.svg)
# ♦ **2024.2 - AGIO** 📂 <!-- omit from toc -->

<br>

### 📌 *Conheça o website:* https://agio-inventory-system.vercel.app/ <!-- omit from toc -->

---

<br>

## ***Sumário*** <!-- omit from toc -->
- [1. Escopo da Aplicação 💡](#1-escopo-da-aplicação-)
- [2. Requisitos para Configuração do Ambiente 📋](#2-requisitos-para-configuração-do-ambiente-)
- [3. Etapas para a Execução do Ambiente 🔧](#3-etapas-para-a-execução-do-ambiente-)
- [4. Como Contribuir com o Projeto? 💻](#4-como-contribuir-com-o-projeto-)
- [5. Política de Segurança e Releases 🔑](#5-política-de-segurança-e-releases-)
- [6. Equipe de Desenvolvimento 👥](#6-equipe-de-desenvolvimento-)

<br>

## 1. Escopo da Aplicação 💡
O *Agio*, ou Aplicação de Gestão de Inventário Otimizada, é um sistema open source web simples da disciplina de Métodos de Desenvolvimento de Software, da Universidade de Brasília. Desenvolvido com o objetivo de servir como um controle de inventário de uma corporação de pequeno a médio porte, é capaz de fornecer ao usuário uma maneira de gerenciar os itens presentes no inventário, adicionando e removendo os componentes de acordo com sua necessidade e monitorando-os de forma prática, simples e segura.

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

No GIF abaixo, é possível conferir uma demonstração rápida das funções básicas da aplicação:


![Demonstração das Funções Básicas](DOCS/assets/app_summary.gif)

<br>

## 2. Requisitos para Configuração do Ambiente 📋
1. Python; [[LINK]](https://www.python.org/downloads/)
2. Docker Engine (ou Docker Desktop); [[LINK]](https://www.docker.com/products/docker-desktop/)

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

5. Baixe o Docker Desktop (Docker Engine, no linux) no [site oficial do docker](https://www.docker.com/products/docker-desktop/);

<br>

6. Crie um arquivo ".env" e insira as variáveis do projeto (requisite-as com os desenvolvedores);

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

12. Acesse, no navegador, o IP no qual a porta foi aberta. Padrão: ***XXX.X.X.X:8000***

<br>

13. E pronto! Assim o ambiente do projeto estará pronto para execução.

<br>

## 4. Como Contribuir com o Projeto? 💻

### 🔹 Antes de Começar <!-- omit from toc -->
- Leia a documentação do projeto no [README](README.md)  
- Certifique-se de que sua ideia ou problema ainda não foi reportado.

### 🔹 Reportando Problemas <!-- omit from toc -->

Ao encontrar um problema, abra uma issue no repositório seguindo o modelo:  
- **Descrição:** Explique o problema de forma clara e objetiva.  
- **Reprodução:** Liste os passos para reproduzir o problema.  
- **Resultado Esperado:** O que deveria acontecer?  
- **Resultado Atual:** O que realmente aconteceu?  
- **Extras:** Inclua capturas de tela ou logs, se aplicável. 

### 🔹 Solicitando Funcionalidades <!-- omit from toc -->

Se desejar sugerir uma nova funcionalidade, abra uma issue com:  
- **Descrição:** Explique detalhadamente sua proposta.  
- **Motivação:** Por que a funcionalidade é importante?  
- **Exemplo de Uso:** Descreva como a funcionalidade seria usada.  

### 🔹 Contribuindo com o Código <!-- omit from toc -->

Para contribuir com código, siga estas etapas:  

1. Faça um fork deste repositório.  
2. Crie uma branch para sua funcionalidade ou correção.  
3. Implemente suas alterações.  
4. Envie as alterações e crie um pull request.  


### 🔹 Mais Informações <!-- omit from toc -->

Para mais informações sobre estrutura de commits e tecnologias utilizadas, consulte o arquivo [CONTRIBUTING](CONTRIBUTING.md).

<br>

## 5. Política de Segurança e Releases 🔑

As releases que atualmente possuem as verificações necessárias de segurança estão descritas na tabela abaixo.

| Version | Safety Features          |
| ------- | ------------------ |
| 1.0.0   | ✅ |

Para mais informações relacionadas a segurança e a notas de vulnerabilidades, consulte o arquivo [SECURITY](SECURITY.md).

<br>

## 6. Equipe de Desenvolvimento 👥

| Scrum Master | Product Owner | Front-End Developer | Back-End Developer | Front-End Developer | Architect |
|:-------------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| [![](https://avatars.githubusercontent.com/caio-venancio)](https://github.com/caio-venancio) | [![](https://avatars.githubusercontent.com/eduardodpms)](https://github.com/eduardodpms) | [![](https://avatars.githubusercontent.com/EnzoEmir)](https://github.com/EnzoEmir) | [![](https://avatars.githubusercontent.com/JMPNascimento)](https://github.com/JMPNascimento) | [![](https://avatars.githubusercontent.com/MM4k)](https://github.com/MM4k) | [![](https://avatars.githubusercontent.com/VictorPontual)](https://github.com/VictorPontual) |
| [Caio Venâncio](https://github.com/caio-venancio) | [Eduardo de Pina](https://github.com/eduardodpms) | [Enzo Emir](https://github.com/EnzoEmir) | [João Maurício](https://github.com/JMPNascimento) | [Marcelo Makoto](https://github.com/MM4k) | [Victor Pontual](https://github.com/VictorPontual) |