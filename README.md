# TST - Cadernos

Módulo do projeto MAPA responsável por montar as fichas das propostas dos seguros agrículas e produzir seus metadados.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Tabela de Conteúdo
- [TST - Cadernos](#tst---cadernos)
  - [Tabela de Conteúdo](#tabela-de-conteúdo)
  - [Instalação](#instalação)
  - [Execução](#execução)
  - [_Features_](#features)
  - [Funcionamento do Módulo](#funcionamento-do-módulo)
    - [Consumo de Dados Externos](#consumo-de-dados-externos)
    - [Geração de Figuras](#geração-de-figuras)
    - [Montagem das Fichas](#montagem-das-fichas)
    - [Exportação de Fichas e Metadados](#exportação-de-fichas-e-metadados)
  - [Outputs](#outputs)
  - [Tratativas de Erros Conhecidos](#tratativas-de-erros-conhecidos)
  - [Roadmap](#roadmap)


## Instalação 

Esse módulo possui suas dependências gerenciadas pelo módulo [pipenv](https://pipenv.pypa.io/en/latest/) através dos arquivos Pipfile e Pipfile.lock. 

Para instalar o _pipenv_, é necessário ter o _Python_ já instalado (versão 3.11) e digitar no terminal:

```shell
pip install pipenv
```

Logo após, basta entrar na pasta do projeto e digitar no terminal:

```shell
pipenv install --deploy
```


## Execução

Para a execução, é necessário criar um arquivo na raiz da pasta chamado ".env" similar ao .env.sample preenchido com as credenciais de acesso ao banco e ao SSH do servidor-alvo. Logo após, basta executar de acordo com o formato que melhor couber a partir dos seguintes:

```shell
python main.py
```

## _Features_

 - [ ] Navegação no site do tribunal
 - [ ] _Download_ dos cadernos
 - [ ] Leitura dos cadernos
 - [ ] Gerenciamento de sistema de arquivos
 - [ ] Salvamento dos números de processos em planilhas separadas por data
 - [ ] Relatório de duplicatas



## Funcionamento do Módulo

![Diagrama de Fluxo de Dados](docs/images/diagram-full.png)

### Consumo de Dados Externos

![Diagrama de Fluxo do Consumo de Dados Externos](docs/images/diagram-externals.png)

### Geração de Figuras

![Diagrama de Fluxo da Geração de Figuras](docs/images/diagram-figures.png)

### Montagem das Fichas

![Diagrama de Fluxo da Montagem da Ficha](docs/images/diagram-assembly.png)

### Exportação de Fichas e Metadados

![Diagrama de Fluxo da Exportação de Fichas e Metadados](docs/images/diagram-export.png)


## Outputs



## Tratativas de Erros Conhecidos

:construction: Área em Construção

| Tipo de Erro | Causa | Tratativa Aplicada |
| --- | --- | --- |
| --- | --- | --- |


## Roadmap

 - [x] Implementar _log_ de texto e de interface com o usuário;
 - [x] Retirar credenciais _hardcoded_ com o banco e SSH;
 - [x] Implementar rastreamento de IDs;
 - [x] Executar módulo no servidor;
 - [ ] :construction: Realizar tratativas de exceções;
 - [ ] :construction: Dockerizar a aplicação;
 - [ ] Implementar CI e CD (?);
 - [ ] Implementar testes e controle de qualidade (SonarQube);
 - [ ] Estruturar arquitetura limpa;
 - [ ] Implementar mensageria para integração com demais módulos;
 - [ ] Subir para o MAPA.