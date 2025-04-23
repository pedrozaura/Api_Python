Para executar o Serviço, subir a API, Se faz necessario banco de dados Postgres, e seguir o passo a passo do arquivo SequenciaInicializacao.txt

ou seguir essas instruções abaixo:

**** Novo Comando para subir o Serviço devido a alteração para o RepositorioGithub

D:\RepositorioGithub\Api_Python\venv\Scripts\activate

para finalizar "  deactivate  "

python API_Full.py


Para rodar a atualização do banco de dados criando a nova estrutura montada no codigo.

para criar as tabelas novas:

flask --app API_Full.py db init

Para atualizar o banco com a criação

flask --app API_Full.py db upgrade


Espero que tenha uma experiencia fantastica ao usar esse serviço. 

Link de acesso a Documentação da API: https://documenter.getpostman.com/view/9137178/2sAYdfpqzL
