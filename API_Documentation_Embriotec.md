# 📘 Documentação da API

---

## 📦 Endpoints: `/api/data`

### ➕ POST `/api/data/itens`

#### Descrição
Cria um novo item com o nome fornecido no corpo da requisição.

#### Método HTTP
`POST`

#### Requisição
```json
{
  "name": "Nome do item"
}
```

#### Resposta (201 Created)
```json
{
  "message": "Item criado com sucesso",
  "item": {
    "id": 1,
    "name": "Nome do item"
  }
}
```

#### Códigos de status
- `201 Created`: Item criado com sucesso
- `400 Bad Request`: Dados inválidos

---

### 📥 GET `/api/data`

#### Descrição
Retorna uma lista com todos os itens registrados no banco de dados.

#### Método HTTP
`GET`

#### Resposta (200 OK)
```json
{
  "message": "Dados recuperados com sucesso",
  "data": [
    {
      "id": 1,
      "name": "Item 1",
      "created_at": "2024-04-01T14:23:45"
    }
  ]
}
```

#### Códigos de status
- `200 OK`: Sucesso na recuperação dos dados

---

### ♻️ PUT `/api/data/<item_id>`

#### Descrição
Atualiza o nome de um item específico com base no seu ID.

#### Método HTTP
`PUT`

#### Parâmetros de URL
- `item_id` (int): ID do item

#### Requisição
```json
{
  "name": "Nome atualizado"
}
```

#### Resposta (200 OK)
```json
{
  "message": "Item atualizado com sucesso",
  "item": {
    "id": 2,
    "name": "Nome atualizado"
  }
}
```

#### Códigos de status
- `200 OK`: Sucesso
- `404 Not Found`: Item não encontrado

---

### 🗑️ DELETE `/api/data/delete/<item_id>`

#### Descrição
Remove um item específico do banco de dados com base no seu ID.

#### Método HTTP
`DELETE`

#### Parâmetros de URL
- `item_id` (int): ID do item

#### Resposta (200 OK)
```json
{
  "message": "Item deletado com sucesso"
}
```

#### Códigos de status
- `200 OK`: Sucesso
- `404 Not Found`: Item não encontrado

---

## 🌱 Endpoints: `/api/parametros`

### ➕ POST `/api/parametros`

#### Descrição
Adiciona um novo registro de parâmetros ambientais.

#### Método HTTP
`POST`

#### Requisição
```json
{
  "lote": 101,
  "temperatura": 25.3,
  "umidade": 60.5,
  "pressao": 1013.2,
  "luminosidade": 320.8
}
```

#### Resposta (201 Created)
```json
{
  "message": "Parâmetro adicionado com sucesso",
  "parametro": {
    "id": 5,
    "lote": 101,
    "temperatura": 25.3,
    "umidade": 60.5,
    "pressao": 1013.2,
    "luminosidade": 320.8
  }
}
```

#### Códigos de status
- `201 Created`: Sucesso
- `400 Bad Request`: Dados ausentes ou inválidos

---

### 📥 GET `/api/parametros`

#### Descrição
Retorna todos os registros de parâmetros ambientais.

#### Método HTTP
`GET`

#### Resposta (200 OK)
```json
{
  "message": "Parâmetros recuperados com sucesso",
  "data": [
    {
      "id": 1,
      "lote": "A1",
      "temperatura": 23.5,
      "umidade": 55.0,
      "pressao": 1012,
      "luminosidade": 300,
      "created_at": "2024-04-01T14:23:45"
    }
  ]
}
```

#### Códigos de status
- `200 OK`: Sucesso
- `500 Internal Server Error`: Falha ao consultar o banco

---

### ♻️ PUT `/api/parametros/<parametro_id>`

#### Descrição
Atualiza campos de um parâmetro ambiental específico.

#### Método HTTP
`PUT`

#### Parâmetros de URL
- `parametro_id` (int): ID do parâmetro

#### Requisição
```json
{
  "lote": 101,
  "temperatura": 26.0,
  "umidade": 58.5,
  "pressao": 1014.0,
  "luminosidade": 310.2
}
```

#### Resposta (200 OK)
```json
{
  "message": "Parâmetro atualizado com sucesso",
  "parametro": {
    "id": 5,
    "lote": 101
  }
}
```

#### Códigos de status
- `200 OK`: Sucesso
- `404 Not Found`: Parâmetro não encontrado

---

### 🗑️ DELETE `/api/parametros/<parametro_id>`

#### Descrição
Remove um parâmetro ambiental específico com base no seu ID.

#### Método HTTP
`DELETE`

#### Parâmetros de URL
- `parametro_id` (int): ID do parâmetro

#### Resposta (200 OK)
```json
{
  "message": "Parâmetro deletado com sucesso"
}
```

#### Códigos de status
- `200 OK`: Sucesso
- `404 Not Found`: Parâmetro não encontrado

---

## 🌆 Rota Inicial `/`

### GET `/`

#### Descrição
Rota principal da API, retorna uma mensagem de boas-vindas e a hora atual do servidor.

#### Método HTTP
`GET`

#### Resposta (200 OK)
```
Bem-vindo à API Outside - Embriotec 
Hora atual: 15:45:20 04-04-2025
```

#### Códigos de status
- `200 OK`: Sucesso