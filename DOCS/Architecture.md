# **Sistema de Gestão de Inventário**

## **1. Descrição do Sistema**  
O sistema de gestão de inventário é uma plataforma robusta projetada para facilitar o gerenciamento de estoques em tempo real. Ele permite que empresas monitorem, organizem e atualizem seus itens de forma eficiente, com suporte a notificações dinâmicas e relatórios.

---

## **2. Arquitetura Geral do Sistema**  

O sistema segue uma arquitetura modular e escalável, dividida em quatro camadas principais:  

1. **Frontend:** Responsável pela interação do usuário.  
2. **Backend:** Gerencia regras de negócios, APIs REST e lógica de WebSocket.  
3. **Banco de Dados:** Armazena dados estruturados e históricos de ações.  
4. **Serviços Externos:** Integrações opcionais, como provedores de autenticação ou relatórios analíticos.  

### **Diagrama de Arquitetura Geral Inicial** 
```plaintext
+---------------------+       http request        +--------------------+
|     Frontend        | <--------------------->   |     Backend        |
|  (HTML, JS, CSS)    |                           | (Django + REST API)|
+---------------------+        HTTP/REST          +--------------------+
                                   |                                |
                                   | Database Queries               | External Services
                                   V                                V
                         +---------------------+                 +--------------------+
                         |    Banco de Dados   |                 |  Integrações       |
                         |     (PostgreSQL)    |                 | (Auth, Analytics)  |
                         +---------------------+                 +--------------------+
```

## **3. Principais Componentes e Papéis**  

### **3.1 Frontend**  
- Desenvolvido com JS, HTML5 e CSS.  
- Exibe informações do estoque em dashboards e tabelas.  
- Responsável por:  
  - Entrada de dados de usuários.  
  - Consumo das APIs REST.  
  - Renderização de notificações em tempo real.  

### **3.2 Backend**  
#### **Funções:**  
- Processamento de regras de negócios.  
- Controle de acesso e autenticação (JWT).  
- Comunicação com o banco de dados e envio de atualizações via WebSocket.  

#### **Tecnologias:**  
- Django como framework principal.  
- Django REST Framework (DRF) para criação de APIs.    

### **3.3 Banco de Dados**  
#### **PostgreSQL**  
- Estrutura para armazenar informações como:  
  - Itens do inventário (nome, categoria, quantidade, etc.).  
  - Usuários e permissões.  
  - Logs de alterações no estoque.  
- Otimizado para buscas frequentes e relatórios.  

### **3.4 Serviços Externos ou Integrações**  
- **Autenticação:** Suporte a Single Sign-On (SSO) com provedores externos.  
- **Relatórios Analíticos:** Integração com serviços de BI para análise avançada.  

---

## **4. Fluxo de Dados e Interações entre Componentes**

### **Fluxo de Interações**

1. **Homepage:**  
   - O usuário acessa a página inicial do sistema.

2. **Login:**  
   - O usuário realiza o login através da interface de login.

3. **Seleção de Inventário:**  
   - Após o login, o usuário escolhe o inventário com o qual deseja interagir.

4. **Dashboard de Inventário:**  
   - O sistema exibe o dashboard com os itens do inventário selecionado, mostrando informações detalhadas sobre o estoque.

### **Fluxo em Diagrama**  
```plaintext
Homepage --> Login --> Seleção de Inventário --> Dashboard (Itens do Inventário)
```

### **Fluxo de Dados e Interações entre Componentes**

O fluxo de dados pode ser descrito da seguinte forma:

1. **Usuário:**  
   - Navega entre as páginas: homepage, login, seleção de inventário e dashboard.

2. **Frontend:**  
   - O frontend lida com a navegação entre as páginas e as interações com o usuário. Ele envia as solicitações de login e de seleção de inventário para o backend via APIs REST.

3. **Backend:**  
   - O backend recebe as solicitações de login e de seleção de inventário e processa as regras de negócios, como autenticação de usuário e recuperação dos dados do inventário. O backend também faz consultas no banco de dados PostgreSQL para fornecer os dados necessários para o dashboard.

4. **Banco de Dados:**  
   - O banco de dados armazena e fornece os dados necessários para exibir os itens do inventário no dashboard, como nome, categoria e quantidade de itens.

5. **Serviços Externos:**  
   - Dependendo da configuração do sistema, pode haver integrações externas para autenticação (SSO) ou análise de dados (relatórios).

Esse fluxo representa a navegação típica do usuário, com interações entre o frontend, backend e o banco de dados. O diagrama de fluxo de dados pode ser representado de forma simplificada como abaixo:

```plaintext
Usuário --> Frontend ------->  Backend --> Banco de Dados
   |            ^                 |            ^
   |            |                 |            |
Notificações <--- http request <--|            |
``` 
---

## **5. Estrutura de Diretórios**

```plaintext
├── apps
│   ├── dashboard
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── homepage
│   |   ├── admin.py
│   |   ├── apps.py
│   |   ├── models.py
│   |   ├── tests.py
│   |   └── views.py
│   └── login
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── manage.py
├── mysite
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   ├── base.css
│   ├── dashboard
│   │   └── dashboard.css
│   └── homepage
│       └── homepage.css
├── templates
│   ├── base.html
│   ├── dashboard
│   │   └── dashboard.html
│   └── homepage
│       └── homepage.html
└── REQUIREMENTS.txt
```

---

## **6. Segurança**  
- Criptografia de senhas com o módulo `pbkdf2` do Django.  
- Validação de entrada nos endpoints REST com DRF.  
- Permissões definidas com base em grupos de usuários.  

---

## **7. Testes**  

| Tipo               | Descrição                                               | Ferramenta         |  
|---------------------|---------------------------------------------------------|--------------------|  
| Teste Unitário      | Verifica funções individuais (ex.: validação de dados). | pytest-django      |  
| Teste de Integração | Garante o funcionamento entre módulos (ex.: views e API). | Django Test Framework |  
| Teste End-to-End    | Simula fluxo de usuário no frontend e backend.          | Selenium/Playwright|  

---

## **8. Glossário**  
- **CSRF:** Proteção contra falsificação de requisições.  
- **JWT:** Token usado para autenticação e autorização de usuários.
