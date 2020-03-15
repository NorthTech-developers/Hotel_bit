from django.shortcuts import redirect, render
import random
from django.contrib.auth.models import User
from .models import Habitacion, Reserva_habitacion, Habitaciones, Reserva
from datetime import date, datetime, timedelta
from _datetime import timedelta
from .models import Reserva, Reservas_habitacion, Tipo_alojamiento



# Create your views here.

def reservar(request):
    
    return render(request, 'reservar.html', {})

def editar_reserva(request): 

    a = datetime.now()
    hoy = int(a.strftime('%d%m%Y'))
    habitacion = Habitaciones.objects.all()
    

    if request.POST.get('Numero_Personas'):
        numero_personas = int(request.POST.get('Numero_Personas'))
        habitacion = habitacion.filter(capacidad__gt=numero_personas)
        
        fecha_egreso_sucia = request.POST.get('Fecha_egreso')
        fecha_egreso_limpia = str(fecha_egreso_sucia).replace('-', '') # sustituimos el simbolo - por nada quedando un str de numeros
        fecha_egreso = datetime.strptime(fecha_egreso_sucia, '%Y-%m-%d') #Transformación del string a tipo Date Objects
        fecha_egreso = fecha_egreso.date()

        fecha_ingreso_sucia = request.POST.get('Fecha_ingreso')
        fecha_ingreso_limpia = str(fecha_ingreso_sucia).replace('-', '') # sustituimos el simbolo - por nada quedando un str de numeros
        fecha_ingreso = datetime.strptime(fecha_ingreso_sucia, '%Y-%m-%d') #Transformación del string a tipo Date Objects
        fecha_ingreso = fecha_ingreso.date()
        
        dias_reserva =  fecha_egreso - fecha_ingreso
    else:
        dias_reserva = "Completar Formulario"

       
    return render(request, 'editar_reserva.html', 
                    { 'habitacion':habitacion, 
                      'dias_reserva': dias_reserva, 
                      'fecha_ingreso': fecha_ingreso, 
                      'fecha_egreso': fecha_egreso , 
                      'fecha_entrada' : fecha_ingreso_sucia, 
                      'fecha_salida' : fecha_egreso_sucia,
                      'cantidad_personas' : numero_personas
                      
                    })


def habitacion_detail(request): 
	#Función para ver en datalle la habitación seleccionada
	#Creamos las variables que recogen todas las habitaciones en base de datos, reservas,
	# y reservas de habitaciones
	habitacion_detail = Habitaciones.objects.get(descripcion=request.POST['nombre_habitacion'])
	reserva = Reserva.objects.all()
	reservas_habitacion = Reservas_habitacion.objects.all()
	#Creamos la variable que hará que cargue dicho html
	template = 'hotel/detail.html'

	#Si la habitacion ya esta reservada aparecerá el siguiente html.	
	for reserva in reservas_habitacion:
		if habitacion_detail == reserva.reserva_habitacion:
			template = 'hotel/detail2.html'

	if request.method == 'POST':
		#Aquí recogemos los campos del formulario de la reserva de habitacion y lo tratamos
		precio = 0
		fecha_entrada = request.POST['fecha_entrada']
		fecha_entrada = datetime.strptime(fecha_entrada, '%Y-%m-%d')
		fecha_entrada = fecha_entrada.date()
		fecha_salida = request.POST['fecha_salida']
		fecha_salida = datetime.strptime(fecha_salida, '%Y-%m-%d')
		fecha_salida = fecha_salida.date()
		ocupantes = request.POST['ocupantes']
		habitacion = habitacion_detail
		reserva = datetime.today()
		tipo_pension = request.POST['pension']
		precio_pension = 0
		if tipo_pension == 'completa':
			precio_pension = 150.00
		elif tipo_pension == 'media':
			precio_pension = 100.00
		elif tipo_pension == 'desayuno':
			precio_pension = 60.00
		elif tipo_pension == 'nada':
			precio_pension = 0.00
		tipo_alojamiento = Tipo_alojamiento.objects.get(habitacion_tipo_alojamiento=habitacion_detail)
		if tipo_alojamiento.descripcion == 'doble':
			precio = precio_pension + 200
		elif tipo_alojamiento.descripcion == 'individual':
			precio = precio_pension + 100
		precio_total = precio

		dia1 = timedelta(days=5)
		dia2 = timedelta(days=1)
		dias = dia1 - dia2
		identificador = random.randrange(100000)
	
		user = request.user
		if fecha_entrada > fecha_salida:
			context = {
				'habitacion_detail': habitacion_detail, 
				'reservas_habitacion': reservas_habitacion,
				'reserva': reserva,
			}
		else:
			context = {
				'habitacion_detail': habitacion_detail, 
				'reservas_habitacion': reservas_habitacion,
			}
			reserva_reserva = Reserva(reserva=user, fecha_reserva=reserva)
			#Guardamos la reserva en la base de datos
			reserva_reserva.save()
			reserva_reserva = Reserva.objects.latest('fecha_reserva')
			reserva_habitacion = Reservas_habitacion(
				fecha_entrada=fecha_entrada, 
				fecha_salida=fecha_salida, 
				ocupantes=ocupantes,
				reserva_habitacion=habitacion,
				reserva_reserva=reserva_reserva,
				precio_total=(int(precio)*int(ocupantes)),
				identificador = identificador)
			# smtp_server = 'smtp.gmail.com'
			# port = 465

			# sender = 'daniferpro3@gmail.com'
			# password = 'daniferpro2016'

			# reciever = user.email
			# message = """\
			# 	Enhorabuena """ + user.username + """ por su reserva.

			# 	""" + """
			# 	Detalles de la reserva:
			# 	Fecha de entrada: """ + str(fecha_entrada) + """
			# 	Fecha de salida: """ + str(fecha_salida) + """
			# 	Ocupantes: """ + str(ocupantes) + """
			# 	Descripcion de la habitacion: """ + str(habitacion) + """
			# 	Fecha de la reserva: """ + str(reserva_reserva) + """
			# 	Precio: """ + str(precio) + """

			# 	Encantados de poder contar contigo.
			# 	"""

			# context = ssl.create_default_context()

			# with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
			# 	server.login(sender, password)
			# 	server.sendmail(sender, reciever, message)
			#Guardamos la reserva de habitación en la base de datos
			reserva_habitacion.save()

			# pasamos info al otro taplate para procesar el pago
			reserva_usuario = Reservas_habitacion.objects.all()
			reserva_usuario = reserva_usuario.filter(identificador=identificador)
			dias_reserva = fecha_salida - fecha_entrada


			template= 'pago.html'




			context = {

				'id':identificador,
				'reserva' : reserva_usuario,
				'dias' : dias_reserva

			}
			
			return render(request, template, context)

	else:
		context = {
			'habitacion_detail': habitacion_detail, 
			'reservas_habitacion': reservas_habitacion,
		}

	return render(request, template, context)




def confirmar_pago(request):

    
    reserva = Reservas_habitacion.objects.all()
    
   


    context = {

        'reserva' : reserva,
        
        

    }
    return render(request,'pago.html', context)

def mercado_pago(request):

    return render(request, 'mercado_pago.html', {})

def pago_efectivo(request):

    return render(request, 'pago_efectivo.html', {})
