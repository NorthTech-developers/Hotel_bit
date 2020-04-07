from .forms import NewsletterForm
from asyncio.sslproto import ssl
import smtplib
from django.http import request


def Newsletter(request):    
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():			
            form.save()
            # configuracion de servicio smtp para emails
            usuario = request.POST['email_newsletter']
            smtp_server = 'smtp.gmail.com'
            port = 465

            sender = 'daniferpro3@gmail.com'
            password = 'daniferpro2016'

            reciever = usuario

            message = """\
                
                Muchas Gracias """ + str(usuario) + """ por Suscribirse al nuestro Newsletter.

                """ + """
                Atravez e este medio estaremos en contacto con tigo, enviandote Boletines
                Con descuentos y cupones Pormocionales
                No Olvides Registrate en Nuestra Web
                Puede Hacerlo aqui-> http://127.0.0.1:8000/usuario/login

                Encantados de poder contar contigo. Hotel BIT 2020
                """

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
                server.login(sender, password)
                server.sendmail(sender, reciever, message, )

			
    
    else:
        form = NewsletterForm

        
            


