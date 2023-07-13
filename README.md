# API para testar um dos modelos de linguagem natural do Google

Essa é uma API desenvolvida em python usando o framework flask. O objetivo é testar o envio de perguntas ao modelo text-bison@001 do Google utilizando o SDK do Vertex AI para python.

A API recebe uma requisição em formato json:

```json
{
    "text": "O que é um modelo de linguagem?"
}
```
Esse é só um exemplo de prompt, você pode escrever o que quiser no campo text.

## Setup

### Pré-requisitos

Crie um arquivo ".env" e coloque as variaveis de ambiente:

```python
GOOGLE_APPLICATION_CREDENTIALS='<caminho para a sua chave de api da conta de serviço>'
PROJECT_ID='<Id do projeto no google cloud>'
```

Crie um ambiente virtual:

No Linux
```
python3 -m venv venv
source /venv/bin/activate
```

No windows
```
python -m venv venv
.\venv\bin\activate
```

Por fim instale as dependências:

```
pip install -r requirements.txt
```
