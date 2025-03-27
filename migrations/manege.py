from flask_migrate import MigrateCommand
from flask_script import Manager
from app import app, db  # Certifique-se de importar a instância correta do Flask e do SQLAlchemy

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
