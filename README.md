
# IA: Criando um Database de Contexto para seus Prompts

Vou mostrar como desenvolver um sistema para otimizar o uso de **prompts** em aplicações de inteligência artificial, utilizando um banco de dados de contexto. Este projeto utiliza **Python** e plataformas de gerenciamento de banco de dados. Destaca-se pelo uso do **DuckDB** como banco de dados vetorial, o que ajuda a gerenciar grandes volumes de dados de forma eficiente, enquanto a biblioteca **Langchain** é integrada para explorar as capacidades do modelo de linguagem **ChatGPT-4**

Por meio desta integração, o projeto incorpora técnicas avançadas, como **embeddings** e **Retrieval-Augmented Generation (RAG)**, demonstrando uma aplicação prática e sofisticada dos conceitos teóricos abordados. Esta combinação de ferramentas e técnicas não apenas eleva a precisão e eficiência das aplicações de **IA**, mas também exemplifica a prática de ***Few-Shot Prompting***, na qual um prompt é apresentado com alguns exemplos que contribuem para o entendimento do que está sendo solicitado.

<!--
# Apresentação em vídeo
<p align="center">
  <a href="https://youtu.be/xxxxxxxxx" target="_blank"><img src="deploy/thumbnail/ContextDB_Youtube.png" alt="Vídeo de apresentação"></a>
</p>
-->

### Requisitos

+ ![Git](https://img.shields.io/badge/Git-2.25.1%2B-E3E3E3)

+ ![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04%2B-E3E3E3)

+ ![Python](https://img.shields.io/badge/Python-3.8%2B-E3E3E3)

+ ![ChatGPT4](https://img.shields.io/badge/ChatGPT-4-E3E3E3)


### Deploy da aplicação

##### Clonando o repositório:

```bash
git clone https://github.com/Renatoelho/ContextDB.git contextDB
```

##### Preparando o ambiente:

+ Acessando o diretório clonado
```bash
cd contextDB/app/
```

+ Criando o ambiente virtual
```bash
python3 -m venv .venv
```

+ Ativando o ambiente virtual
```bash
source .venv/bin/activate
```

+ Instalando as dependências
```bash
pip install pip setuptools wheel && pip install -r requirements.txt
```

+ Testando a aplicação
```bash
python3 ./app.py
```

***Observação***: para testar a aplicação com outras mensagens é só mudar o texto da vaiável ```atendimento``` no arquivo ```app.py```.


# Referências
<!--
NiFi System Administrator’s Guide, ***Apache NiFi***. Disponível em: <https://nifi.apache.org/docs/nifi-docs/html/administration-guide.html>. Acesso em: 28 mar. 2024.
-->