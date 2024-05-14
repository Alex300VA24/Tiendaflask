from threading import Thread
from flask_mail import Message
from flask import current_app, render_template

"""
def confirmacion_compra(mail, usuario, curso):
    try:
        message = Message('Confirmación de compra del curso',
                          sender=current_app.config['MAIL_USERNAME'],
                          recipients=['dazabache@unitru.edu.pe'])
        message.html = render_template(
            'emails/confirmacion_compra.html', usuario=usuario, curso=curso)
        mail.send(message)
    except Exception as ex:
        raise Exception(ex)"""

# Para mandar el correo al cliente
def confirmacion_compra(app, mail, usuario, curso):
    try:
        message = Message('Confirmación de compra del curso',
                          sender=current_app.config['MAIL_USERNAME'],
                          recipients=['dazabache@unitru.edu.pe'])
        message.html = render_template(
            'emails/confirmacion_compra.html', usuario=usuario, curso=curso)
        thread = Thread(target=envio_email_async, args=[app, mail, message])
        thread.start()
    except Exception as ex:
        raise Exception(ex)

def envio_email_async(app, mail, message):
    with app.app_context():
        mail.send(message)