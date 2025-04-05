import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
    
app = Flask(__name__)

# Configuração do banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:q27pptz8@localhost/embriotec'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy
db = SQLAlchemy(app)

# Inicializa o Flask-Migrate
migrate = Migrate(app, db)  

# Modelo de exemplo para uma tabela no banco de dados
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Item {self.name}>"
    
class Parametro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lote = db.Column(db.Integer, nullable=False)
    temperatura = db.Column(db.Float, nullable=False)
    umidade = db.Column(db.Float, nullable=False)
    pressao = db.Column(db.Float, nullable=False)
    luminosidade = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Parametro Lote={self.lote}, Temperatura={self.temperatura}, Umidade={self.umidade}, Pressao={self.pressao}, Luminosidade={self.luminosidade}>"    

# Cria as tabelas no banco de dados (executar apenas uma vez)
with app.app_context():
    db.create_all()

# Rota padrão
@app.route('/')
def home():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S %d-%m-%Y")
    return "Bem-vindo à API Outside - Embriotec \n Hora atual: " + current_time

# Rota para obter dados
@app.route('/api/data', methods=['GET'])
def get_data():
    items = Item.query.all()
    items_list = [{"id": item.id, "name": item.name, "created_at": item.created_at} for item in items]
    return jsonify({"message": "Dados recuperados com sucesso", "data": items_list}), 200

# Rota para enviar dados (POST)
# Feito kkkk
@app.route('/api/data/itens', methods=['POST'])
def post_data():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    new_item = Item(name=data["name"])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item criado com sucesso", "item": {"id": new_item.id, "name": new_item.name}}), 201

# Rota para atualizar dados (PUT)
#feito kkkk
@app.route('/api/data/<int:item_id>', methods=['PUT'])
def update_data(item_id):
    data = request.json
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item não encontrado"}), 404

    if "name" in data:
        item.name = data["name"]
    db.session.commit()
    return jsonify({"message": "Item atualizado com sucesso", "item": {"id": item.id, "name": item.name}}), 200

# Rota para deletar dados (DELETE)
#Feito kkkk
@app.route('/api/data/delete/<int:item_id>', methods=['DELETE'])
def delete_data(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item não encontrado"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deletado com sucesso"}), 200

# feito kkkk
@app.route('/api/parametros', methods=['POST'])
def add_parametro():
    data = request.json
   # Verifica se o corpo da requisição está vazio
    if not data:
        return jsonify({"error": "O corpo da requisição está vazio"}), 400

    # Lista de campos obrigatórios
    campos_obrigatorios = ["lote", "temperatura", "umidade", "pressao", "luminosidade"]
    campos_faltantes = [campo for campo in campos_obrigatorios if campo not in data]

    # Verifica se há campos faltantes
    if campos_faltantes:
        return jsonify({
            "error": "Campos obrigatórios faltando",
            "campos_faltantes": campos_faltantes
        }), 400

    # Verifica se os valores dos campos são válidos
    try:
        lote = int(data["lote"])
        temperatura = float(data["temperatura"])
        umidade = float(data["umidade"])
        pressao = float(data["pressao"])
        luminosidade = float(data["luminosidade"])
    except (ValueError, TypeError):
        return jsonify({
            "error": "Valores inválidos",
            "detalhes": "Certifique-se de que 'lote' é um número inteiro e os demais campos são números decimais."
        }), 400

    novo_parametro = Parametro(
        lote=data["lote"],
        temperatura=data["temperatura"],
        umidade=data["umidade"],
        pressao=data["pressao"],
        luminosidade=data["luminosidade"]
    )
   # Gravar os dados no banco de dados e commit
    db.session.add(novo_parametro)
    db.session.commit()
   
   # Retorna a resposta de sucesso
    return jsonify({
        "message": "Parâmetro adicionado com sucesso",
        "parametro": {
            "id": novo_parametro.id,
            "lote": novo_parametro.lote,
            "temperatura": novo_parametro.temperatura,
            "umidade": novo_parametro.umidade,
            "pressao": novo_parametro.pressao,
            "luminosidade": novo_parametro.luminosidade
        }
    }), 201

# FEito kkkk
@app.route('/api/parametros', methods=['GET'])
def get_parametros():
    parametros = Parametro.query.all()
    parametros_list = [{
        "id": p.id,
        "lote": p.lote,
        "temperatura": p.temperatura,
        "umidade": p.umidade,
        "pressao": p.pressao,
        "luminosidade": p.luminosidade,
        "created_at": p.created_at
    } for p in parametros]
    return jsonify({"message": "Parâmetros recuperados com sucesso", "data": parametros_list}), 200

#Feito kkkk
@app.route('/api/parametros/<int:parametro_id>', methods=['PUT'])
def update_parametro(parametro_id):
    data = request.json
    parametro = Parametro.query.get(parametro_id)
    if not parametro:
        return jsonify({"error": "Parâmetro não encontrado"}), 404

    if "lote" in data:
        parametro.lote = data["lote"]
    if "temperatura" in data:
        parametro.temperatura = data["temperatura"]
    if "umidade" in data:
        parametro.umidade = data["umidade"]
    if "pressao" in data:
        parametro.pressao = data["pressao"]
    if "luminosidade" in data:
        parametro.luminosidade = data["luminosidade"]

    db.session.commit()
    return jsonify({"message": "Parâmetro atualizado com sucesso", "parametro": {"id": parametro.id, "lote": parametro.lote}}), 200

@app.route('/api/parametros/<int:parametro_id>', methods=['DELETE'])
def delete_parametro(parametro_id):
    parametro = Parametro.query.get(parametro_id)
    if not parametro:
        return jsonify({"error": "Parâmetro não encontrado"}), 404

    db.session.delete(parametro)
    db.session.commit()
    return jsonify({"message": "Parâmetro deletado com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)