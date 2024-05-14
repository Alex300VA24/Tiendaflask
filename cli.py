from flask.cli import FlaskGroup
from app import inicializar_app
from config import config


configuracion = config['development']

app = inicializar_app(configuracion)
cli = FlaskGroup(app)



if __name__ =='__main__':
    cli()