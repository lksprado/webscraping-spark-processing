# webscraping-spark-processing

Este projeto é um caso de teste para posição de Engenheiro de Dados:

Consiste em obter dados através de webscraping, transformar através do pyspark e salvar o arquivo em parquet.

## Abordagem
Estrutura:
``` 
.
├── app
│   ├── extract.py
│   └── transform.py
├── app.log
├── main.py
├── poetry.lock
├── populacao_paises.csv
├── populacao_paises_processado.parquet
│   ├── part-00000-431b9d8a-abbf-413b-91dc-9396340f6043-c000.snappy.parquet
│   └── _SUCCESS
├── pyproject.toml
├── README.md
└── tests
    └── test_extract.py
```


1. O script `app/extract.py` contém os códigos que fazem a requisição do HTML página web,
o parseamento das informações requisitadas e salva em um arquivo csv;

2. O script `app/transform.py` contém a classe que faz a leitura do csv, transforma os dados e salva em parquet;

3. O script `main.py` contém o código executor de todo o projeto;

4. O arquivo `populacao_paises.csv` contém os dados brutos da extração web

5. A pasta `populacao_paises_processado.parquet` contém o output no formato parquet


O projeto contém aplicação de conceitos e boas práticas de escrita de código, dentre eles:
- Teste unitário
- Compilação automatizada do código python seguindo PEP8
- Logging
- Modularização
- OOP

## Utilização
1. Clone o repositório: \
``` gh repo clone lksprado/webscraping-spark-processing ```

2. Instale as dependências: \
``` poetry install ```

3. Ative o ambiente virtual: \
``` poetry shell ```

4. Rode o script main:
``` python main.py ```







