# **TaskSage - Sistema de Gerenciamento de Tarefas e Projetos**
O TaskSage é um exemplo didático de um sistema de gerenciamento de tarefas e projetos, projetado para ensinar os fundamentos de bancos de dados e padronizaçāo de projeto. 

## **Estrutura do Repositório:**

1. **Configuração do Banco de Dados**:
   - [config.py](https://github.com/DemetriosCoutinho/task-sage/blob/main/src/database/config.py): Este arquivo contém funções para ler as configurações do banco de dados a partir de um arquivo `config.ini`.

2. **Modelos de Banco de Dados**:
   - [models.py](https://github.com/DemetriosCoutinho/task-sage/blob/main/src/database/models.py): Define a estrutura das tabelas do banco de dados, incluindo tabelas para projetos, tarefas e usuários.

3. **Consultas ao Banco de Dados**:
   - [queries.py](https://github.com/DemetriosCoutinho/task-sage/blob/main/src/database/queries.py): Contém funções para realizar operações CRUD (Criar, Ler, Atualizar e Deletar) no banco de dados, bem como funções para autenticação de usuários.

4. **Interface do Usuário**:
   - [menu.py](https://github.com/DemetriosCoutinho/task-sage/blob/main/src/ui/menu.py): Este arquivo gerencia a interface do usuário, permitindo que os usuários (administradores e visualizadores) interajam com o sistema através de um menu.

5. **Configuração Inicial**:
   - [initial_setup.py](https://github.com/DemetriosCoutinho/task-sage/blob/main/src/utilities/initial_setup.py): Script para configurar o sistema pela primeira vez, criando tabelas e adicionando usuários padrão.

6. **Ponto de Entrada**:
   - [main.py](https://github.com/DemetriosCoutinho/task-sage/blob/main/src/main.py): É o ponto de entrada do sistema. Ele gerencia o login do usuário e direciona para o menu apropriado com base no tipo de usuário.


## **Instalação e Execução do TaskSage**

### **1. Clonando o Repositório**:
Primeiro, clone o repositório para sua máquina local usando o Git:
```
git clone https://github.com/DemetriosCoutinho/task-sage.git
cd task-sage
```

### **2. Criando um Ambiente Virtual**:
O ambiente virtual é uma maneira de isolar as dependências do projeto para evitar conflitos com outros projetos. Aqui está como criar um:

**Para Linux/Mac**:
```
python3 -m venv venv
source venv/bin/activate
```

**Para Windows**:
```
python -m venv venv
.\venv\Scripts\activate
```

Após executar esses comandos, seu terminal ou prompt de comando deve indicar que o ambiente virtual está ativo, geralmente prefixando o prompt com `(venv)`.

### **3. Instalando as Dependências**:
Com o ambiente virtual ativado, instale as dependências necessárias usando o pip:
```
pip install -r requirements.txt
```

### **4. Configuração Inicial**:
Antes de executar o projeto pela primeira vez, é necessário configurar o banco de dados e adicionar alguns usuários padrão. Altere o `execute_initial_setup` para yes no arquivo de configuraçāo `config.ini`. Basta fazer isso uma vez, depois altere para `no`.
```
[DEFAULT]
execute_initial_setup = yes
```

### **5. Executando o Projeto**:
Agora, você pode executar o projeto:
```
python src/main.py
```
### **5.1. Executando o Projeto**:
Se aparecer um erro de módulo nāo encontrado, execute o seguinte comando.
```
export PYTHONPATH=.:$PYTHONPATH
```
Siga as instruções na tela para fazer login e interagir com o sistema.

### **6. Desativando o Ambiente Virtual**:
Depois de terminar de trabalhar no projeto, você pode desativar o ambiente virtual:
```
deactivate
```

