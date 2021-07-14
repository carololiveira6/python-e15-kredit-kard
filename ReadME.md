## **Table of Contents**
- [E15 - Kredit Kard](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1f8j0bs3e0) 
  - [Objetivos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1f8j0bs3e1)
- [Diagrama de Relação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1f8j0bs3e2)
- [Comandos CLI](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1f8j1cnbr3) 
  - [user create ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1f8j1cnbr4)
    - [Entradas e saídas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1f8j1cnbr5)
  - [admin create](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1f8j1odkf6) 
    - [Entradas e saídas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1f8j1odkf7)
- [Extra](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1f8j1p5gb8) 
  - [users_credit_cards create ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1f8j1pvgd9)
    - [Entradas e saídas](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1f8j2b3bta)
- [Entregáveis ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1egvoav555j)
  - [Repositório ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação ](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/5a_e_01_kredit_kard.html&ref=master#mcetoc_1eh146n6m3)
# **E15 - Kredit Kard**
Nessa entrega você irá criar uma aplicação que irá fazer a criação de usuários rodando apenas um comando no terminal.


## **Objetivos**
Praticar a criação de comandos CLI, codificação de senha, migrações, relacionamentos e leitura de documentação (que nesse caso será a biblioteca [Faker](https://faker.readthedocs.io/en/stable/)).


# **Diagrama de Relação**
![](Aspose.Words.f0830dd4-f2c4-40b2-953e-9d3799ec7329.001.png)


# **Comandos CLI**
## **user create <quantidade>**
- Esse comando deve fazer a criação de **users** seguindo a quantidade passada, **TODOS** esses usuários devem ser instanciados com o atribuo **is\_admin** igual a **falso**. 
- O **login** e a **password** devem ser gerados aleatoriamente utilizando a biblioteca [Faker](https://faker.readthedocs.io/en/stable/).
- A **password** deve conter: caracteres especiais, letras em maiúsculo, letras em minúsculo e dígitos.


### **Entradas e saídas**

|**Comando rodado no terminal**|
| :-: |
|![](Aspose.Words.f0830dd4-f2c4-40b2-953e-9d3799ec7329.001.png)|


|**Usuários criados no banco de dados**|
| :-: |
|![](Aspose.Words.f0830dd4-f2c4-40b2-953e-9d3799ec7329.001.png)|

## **admin create**
- Esse comando deve fazer a criação de apenas um **user** que vai ser **admin** no bando de dados. 
- O **login** e a **password** devem ser gerados aleatoriamente utilizando a biblioteca [Faker](https://faker.readthedocs.io/en/stable/).
- A **password** deve conter: caracteres especiais, letras em maiúsculo, letras em minúsculo e dígitos.
- Deve **retornar no terminal** o **login** e a **password** do admin criado.


### **Entradas e saídas**

|**Comando rodado no terminal**|
| :-: |
|![](Aspose.Words.f0830dd4-f2c4-40b2-953e-9d3799ec7329.001.png)|


|**Usuários criados no banco de dados**|
| :-: |
|![](Aspose.Words.f0830dd4-f2c4-40b2-953e-9d3799ec7329.001.png)|


-----
# **Extra**
## **users\_credit\_cards create <quantidade>**
Esse comando CLI deverá fazer:

- A criação de **users** seguindo a quantidade passada, **TODOS** essas instancias de usuários devem ter o atributo **is\_admin** igual a falso.
- O **login** e a **password** devem ser gerados aleatoriamente utilizando a biblioteca [Faker](https://faker.readthedocs.io/en/stable/).
- A **password** deve conter: caracteres especiais, letras em maiúsculo, letras em minúsculo e dígitos.
- A criação de **credit card** para cada usuário, com a devida relação 1:N feita corretamente.
- Cada **user** poderá ter de entre 0 e 2 **credit card** relacionados.
- A criação do **credit card** também deverá ser feita utilizando a biblioteca [Faker](https://faker.readthedocs.io/en/stable/index.html). 
- Lembrando que o **security\_code** deve ter **3 de tamanho**.


### **Entradas e saídas**

|**Comando rodado no terminal**|
| :-: |
|![](Aspose.Words.f0830dd4-f2c4-40b2-953e-9d3799ec7329.001.png)|


|**Usuários criados no banco de dados**|
| :-: |
|![](Aspose.Words.f0830dd4-f2c4-40b2-953e-9d3799ec7329.001.png)|


|**Cartões criados no banco de dados**|
| :-: |
|![](Aspose.Words.f0830dd4-f2c4-40b2-953e-9d3799ec7329.001.png)|


**Nota**: Perceba que nem todos os usuários têm cartão de crédito e perceba também que existe usuário com 1 ou 2 cartões.

-----
# **Entregáveis** 
## **Repositório** 
- Link do **repositório** do **GitLab** 
- **Código-fonte:** 
  - Pasta app. 
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como **reporter**. 
### -----
# **Critérios de aceitação** 

|**Pts** |**Dado** |**Quando** |**É esperado** |
| :-: | :-: | :-: | :-: |
|2|Comando CLI:<br>**user create <quantidade>**|Executado|Fazer a criação dos usuários no banco de dados|
|2|Comando CLI:<br>**admin create**|Executado|Fazer a criação do usuário admin no banco de dados|
|2|Database|Verificado|Estar da forma que foi pedida|
|1|Projeto|Verificado|Que exista o arquivo **.env.example**|
|1|Projeto|Verificado|Que exista o arquivo **requirements.txt**|
|1|Projeto|Verificado|Que exista a pasta **migrations** com as suas migrações|
|1|Projeto|Verificado|Que exista o arquivo .gitignore|
|2|Comando CLI:<br>**users\_credit\_cards create <quantidade>**|Executado|Fazer a criação dos usuários e dos cartões de crédito no banco de dados|


**Divirta-se! 😄**


