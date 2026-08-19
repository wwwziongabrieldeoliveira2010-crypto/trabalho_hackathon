# 🌱 Sistema Residencial de Sustentabilidade

## ▶️ Como executar o projeto

### 1. Baixe ou clone o projeto

Clone o repositório utilizando o Git:

```bash
git clone https://github.com/wwwziongabrieldeoliveira2010-crypto/trabalho_hackathon.git
```

Depois entre na pasta do projeto:

```bash
cd trabalho_hackathon
```

### 2. Instale o Python

Certifique-se de que o **Python** esteja instalado no computador.

Para verificar:

```bash
python --version
```

### 3. Instale o MySQL

O sistema utiliza o **MySQL** para armazenar os dados da aplicação.

Certifique-se de que o servidor MySQL esteja instalado e em execução.

### 4. Instale o conector do MySQL

No terminal, execute:

```bash
pip install mysql-connector-python
```

### 5. Configure a conexão com o banco

Abra o arquivo:

```text
banco.py
```

Configure os dados de acesso ao seu MySQL:

```python
mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha"
)
```

Utilize os dados da sua instalação do MySQL.

### 6. Execute o sistema

Depois de configurar o banco, execute:

```bash
python main.py
```

O sistema será iniciado e o menu principal ficará disponível para o usuário.

### 7. Utilize o menu

A partir do menu, o usuário poderá acessar as funcionalidades disponíveis no sistema, como:

* Cadastro de residência;
* Cadastro de consumo de água;
* Cadastro de consumo de energia;
* Cadastro de resíduos;
* Consulta de dados;
* Atualização de informações;
* Análise de consumo;
* Exclusão de registros;
* Visualização das movimentações.

---

## 👨‍💻 Créditos

**Projeto desenvolvido para Hackathon**

**Desenvolvedor:** Zion Gabriel, Pedro Felipe, Maria Julia e Cecilia

**Tecnologias utilizadas:**

* Python
* MySQL
* MySQL Connector
* Git
* GitHub

**Repositório:**
[GitHub — trabalho_hackathon](https://github.com/wwwziongabrieldeoliveira2010-crypto/trabalho_hackathon?utm_source=chatgpt.com)

Projeto desenvolvido com finalidade **educacional**, com foco em tecnologia, sustentabilidade e desenvolvimento de sistemas.
