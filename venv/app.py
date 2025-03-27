import datetime
from flask import Flask, jsonify, request


app = Flask(__name__)

# Rota padrão
@app.route('/')
def home():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S %d-%m-%Y")    
    return "Bem-vindo à API Outside - Embryotec \n Hora atual: " + current_time  


# Rota para obter dados
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Esta é uma resposta JSON da API Ocorreu sucesso na requisição',
        'status': 'success'
    }
    return jsonify(data)

# Rota para enviar dados
@app.route('/api/data', methods=['POST'])
def post_data():
    content = request.json
    return jsonify({"received": content}), 201



if __name__ == '__main__':
    app.run(debug=True)