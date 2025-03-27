import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configuração do banco de dados SQL Server
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://sa:pwd@123ABC@147.79.104.68:1433/BUMBA?driver=ODBC+Driver+17+for+SQL+Server"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelo de dados
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Parametro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lote = db.Column(db.Integer, nullable=False)
    temperatura = db.Column(db.Float, nullable=False)
    umidade = db.Column(db.Float, nullable=False)
    pressao = db.Column(db.Float, nullable=False)
    luminosidade = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Testa conexão com banco antes de iniciar
with app.app_context():
    try:
        db.create_all()
        print("Conectado ao banco de dados com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")

# Rota padrão
@app.route('/')
def home():
    now = datetime.datetime.now()
    return f"Bem-vindo à API Outside - Embriotec\nHora atual: {now.strftime('%H:%M:%S %d-%m-%Y')}"

# Rota para obter dados
@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        items = Item.query.all()
        items_list = [{"id": item.id, "name": item.name, "created_at": item.created_at} for item in items]
        return jsonify({"message": "Dados recuperados com sucesso", "data": items_list}), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao recuperar dados: {e}"}), 500

# Rota para criar item
@app.route('/api/data/itens', methods=['POST'])
def post_data():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Dados inválidos"}), 400
    try:
        new_item = Item(name=data["name"])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Item criado com sucesso", "item": {"id": new_item.id, "name": new_item.name}}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Erro ao inserir dados: {e}"}), 500

# Rota para atualizar item
@app.route('/api/data/<int:item_id>', methods=['PUT'])
def update_data(item_id):
    data = request.json
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item não encontrado"}), 404
    try:
        if "name" in data:
            item.name = data["name"]
        db.session.commit()
        return jsonify({"message": "Item atualizado com sucesso", "item": {"id": item.id, "name": item.name}}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Erro ao atualizar dados: {e}"}), 500

# Rota para deletar item
@app.route('/api/data/delete/<int:item_id>', methods=['DELETE'])
def delete_data(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item não encontrado"}), 404
    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Item deletado com sucesso"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Erro ao deletar dados: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
