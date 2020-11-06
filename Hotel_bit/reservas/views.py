from django.shortcuts import redirect, render
import random
from django.contrib.auth.models import User
from .forms import ReservasHabitacionForm, HabitacionForm
from .models import Habitacion, Reserva_habitacion, Habitaciones, Reserva, CantidadReservas
from datetime import date, datetime, timedelta
from _datetime import timedelta
from .models import Reserva, Reservas_habitacion, Tipo_alojamiento
from asyncio.sslproto import ssl
import smtplib
from django.http import request
from django.db.models import Q

###########################################################################################################################################################

	# Las Habitaciones tienen una cantidad establecida en 10. se muestra si la hab tiene menos de su limite (10) en las fechas indicadas
	# Para restablecer la habitacion se debe de modificar el atributo cantidad de la misma en la bd,
	# o esperar hasta la fecha de hoy que corra la funcion actualizar habitaciones, 
	# la cual toma las fecha finales de las reservas y si son menores que hoy suma 1 a la cantidad disponible de esa habitacion.

############################################################################################################################################################


def filtrar(request): # FILTRAR & ACTUALIZAR ESTADO DE RESERVAS Y HABITACIONES

###########################################
#         ACTUALIZAR HABITACIONES         #
###########################################	

#SUMAMOS 1 A LA HABITACION SI LLEGA LA FECHA DE SALIDA DE LA RESERVA.

	hoy = date.today()

	reservas_vencidas = Reservas_habitacion.objects.all()
	reservas_vencidas = reservas_vencidas.filter(fecha_salida__lte=hoy).exclude(status_payment='Finalizada')

	habitaciones_ = [] #lista de ahbitaciones total
	for i in Habitaciones.objects.all():
		habitaciones_.append(i)
	
	for hab in reservas_vencidas:
		reservas_vencidas_list=[]
		for i in reservas_vencidas:
			reservas_vencidas_list.append(i)
		for i in reservas_vencidas_list:
			i.status_payment='Finalizada'
			i.save()
			hab_ = i.reserva_habitacion
			a3 = hab_.cantidad
			hab_.cantidad = a3 +1
			hab_.save()
			

# DESCONTAMOS UNA HABITACION SI LLEGA LA FECHA DE ENTRADA DE LA RESERVA Y LA COLOCAMOS COMO ACTIVA

	reservas_del_dia = Reservas_habitacion.objects.filter(Q(fecha_entrada__lte=hoy) &Q(status_payment='Aprovado') |Q(status_payment='Pendiente'))

	habitaciones_ = [] #lista de habitaciones 
	for i in Habitaciones.objects.all():
		habitaciones_.append(i)
	
	
	for hab in reservas_del_dia:
		reservas_=[]
		for i in reservas_del_dia:
			reservas_.append(i)
		for i in reservas_:
			i.status_payment='Activa'
			i.save()
			habitacion = i.reserva_habitacion
			cantidad = habitacion.cantidad
			habitacion.cantidad = cantidad -1
			habitacion.save()
			

###########################################
#      FIN ACTUALIZAR HABITACIONES        #
###########################################

	ocupantes = request.POST['Numero_Personas']

	fecha_entrada_str =  str(request.POST['Fecha_ingreso'])
	fecha_entrada = datetime.strptime(fecha_entrada_str, '%Y-%m-%d')

	fecha_salida_str =  str(request.POST['Fecha_egreso'])
	fecha_salida = datetime.strptime(fecha_salida_str, '%Y-%m-%d')

	#########################################################################################################################################

	# Se han establecido 4 tipos posibles de cruces de fechas las cuales se resumen a continacion tomando en cuenta las siguientes variables:
	# fecha_entrada = fecha que es introducida en el form por el usuario
	# fecha_salida =  fecha que es introducida en el form por el usuario
	# fecha_entrada_r = fecha de la reserva en la base de datos
	# fecha_salida_r =  fecha de la reserva en la base de datos

	#caso 1 = fecha_entrada_r >= fecha_entrada & fecha_salida_r <= fecha_salida
	#caso 2 = fecha_entrada_r <= fecha_entrada & fecha_salida_r <= fecha_salida & fecha_entrada_r <= fecha_salida
	#caso 3 = fecha_entrada_r >= fecha_entrada & fecha_salida_r >= fecha_salida & fecha_entrada_r <= fecha_salida
	#caso 4 = fecha_entrada_r <= fecha_entrada & fecha_salida_r >= fecha_salida

	##########################################################################################################################################
	 
	reservas_para_filtrar = Reservas_habitacion.objects.all().exclude(Q(status_payment='Cancelado') &Q (status_payment='Fallo') &Q (status_payment='Finalizada'))
	
	reservas = reservas_para_filtrar.filter(
	 Q(fecha_entrada__gte=fecha_entrada) 
	&Q(fecha_salida__lte=fecha_salida)#caso1 

	|Q(fecha_entrada__lte=fecha_entrada)
	&Q(fecha_salida__lte=fecha_salida)
	&Q(fecha_salida__gte=fecha_entrada)#caso2
	
	|Q(fecha_entrada__gte=fecha_entrada)
	&Q(fecha_salida__gte=fecha_salida)
	&Q(fecha_entrada__lte=fecha_salida)#caso3

	|Q(fecha_entrada__lte=fecha_entrada)
	&Q(fecha_salida__gte=fecha_salida))#caso4	

	################################################################################
					# CREANDO LISTAS PARA MOSTRAR AL USUARIO #
	################################################################################
	
	lista = [] # contiene las reservas que coniciden con las fechas del usuario
	for descripcion in reservas :

		habitacion_lista = descripcion.reserva_habitacion # obtenemos la Habitación Reservada en esa fecha
		lista.append(habitacion_lista) # agregamos a lista las habitaciones que estan reservadas en la fecha que el user ingreso

	################################################################################
	# Filtro las reservas en fechas para obtener el numero de reservas para cada hab
	# si la hab está en su limite para esa fecha será agregada a la lista
	# para no ser mostrada
	################################################################################

	hab_quitar = [] # contine las habitaciones que se deben de quitar para no ser mostradas al usuario final
	
	for i in lista:
		max_r_hab = CantidadReservas.objects.get(reserva_habitacion=i) # int() máximo posible de reservas por habitacion
		variable_1 = lista.count(i)	# contamos cuantas reservas hay por habitacion
		if variable_1 == max_r_hab.limite: # si la cantidad de reservas para esa hab. es igual a su limite se agrega a la lista hab_quitar.
			hab_quitar.append(i) 

		
	
	lista2 = [] # lista final a mostrar al usuario
	for i in Habitaciones.objects.filter(capacidad__gte=ocupantes):
		# Creamos una lista con las habitaciones que coinciden los ocupantes y hay por lo menos 1 habitacion disponible
		lista2.append(i)
		
		
	for i in hab_quitar:
		if i in lista2:
			lista2.remove(i) # removemos los elemtos de la lista  en lista 2 (eliminamos las habitaciones reservadas de la lista2)
	
	
	if lista:
	 	lista	# si hay elementos en la lista[reservas hechas en esas fechas] continua, sino lista2 tendra todas las habitacionos solo x filtro de ocupantes y dicponibilidad
	else:
	 	lista2 = Habitaciones.objects.filter(capacidad__gte=ocupantes, cantidad__gte=1)

	


	template='editar_reserva.html'
	context={
		'habitacion' : lista2,
		'fecha_ingreso' : fecha_entrada,
		'fecha_egreso' : fecha_salida,
		'cantidad_personas' : ocupantes,
		'fecha_entrada' : fecha_entrada_str,
		'fecha_salida' : fecha_salida_str
				 	
		
	}

	return render(request, template, context)


def habitacion_detail(request): 
	#Función para ver en datalle la habitación seleccionada
	#Creamos las variables que recogen todas las habitaciones en base de datos, reservas,
	# y reservas de habitaciones
	habitacion_detail = Habitaciones.objects.get(descripcion=request.POST['nombre_habitacion'])
	reserva = Reserva.objects.all()
	reservas_habitacion = Reservas_habitacion.objects.all()
	template = 'pago.html'


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
			precio_pension = 500.00
		elif tipo_pension == 'media':
			precio_pension = 250.00
		elif tipo_pension == 'desayuno':
			precio_pension = 200.00
		elif tipo_pension == 'nada':
			precio_pension = 0.00
		tipo_alojamiento = Tipo_alojamiento.objects.get(habitacion_tipo_alojamiento=habitacion_detail)
		if tipo_alojamiento.descripcion == 'doble':
			precio = precio_pension + precio_pension
		elif tipo_alojamiento.descripcion == 'individual':
			precio = precio_pension + 100
		precio_total = precio

		

		dia1 = timedelta(days=5)
		dia2 = timedelta(days=1)
		dias = dia1 - dia2

		identificador = random.randrange(100000)
	
		user1 = request.user
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
			reserva_reserva = Reserva(reserva=user1, fecha_reserva=reserva)
			#Guardamos la reserva en la base de datos
			reserva_reserva.save()
			# cramos la reserva Habitacion con los datos correspondientes y la guardamos en la bd
			reserva_habitacion = Reservas_habitacion(
				usuario = user1,
				fecha_entrada=fecha_entrada, 
				fecha_salida=fecha_salida, 
				ocupantes=ocupantes,
				reserva_habitacion=habitacion,
				reserva_reserva=reserva_reserva,
				precio_total=(int(precio_total)*int(ocupantes)),
				identificador = identificador)
			# actualizar = habitacion_detail.cantidad -1
			# habitacion_detail.cantidad = actualizar
			# habitacion_detail.save() 
			# configuracion de servicio smtp para emails


			###############################################################
			#                  ENVIO DE EMAIL AL USUARIO                  #
			###############################################################

			smtp_server = 'smtp.gmail.com'
			port = 465

			sender = 'daniferpro3@gmail.com'
			password = 'Daniferpro2021'

			reciever = user1.email

			message = """\
				
				Muchas Gracias """ + user1.username + """ por su reserva.

				""" + """
				Detalles de la reserva:
				Fecha de entrada: """ + str(fecha_entrada) + """
				Fecha de salida: """ + str(fecha_salida) + """
				Ocupantes: """ + str(ocupantes) + """
				Descripcion de la habitacion: """ + str(habitacion) + """
				Fecha de la reserva: """ + str(reserva_reserva) + """
				Precio: """ + str(precio_total) + """
				Puede ver su reserva aqui-> http://127.0.0.1:8000/reservar/mis_reservas

				Encantados de poder contar contigo. Hotel BIT 2020
				"""

			context = ssl.create_default_context()

			with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
				server.login(sender, password)
				server.sendmail(sender, reciever, message, )

			###############################################################
			#                 FIN ENVIO DE EMAIL AL USUARIO               #
			###############################################################
			
			#Guardamos la reserva de habitación en la base de datos

			reserva_habitacion.save()

			# pasamos info al template para procesar el pago

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
			###############################################################
			#                   OPCIONES DE PAGO Y ESTADO                 #
			###############################################################



def cancel_res(request):# cancelar la reserva

	if request.method == 'POST':

		id_reserva = request.POST['id_reserva']

		reserva_a_cancelar = Reservas_habitacion.objects.get(identificador=id_reserva)
		actualizarForm = ReservasHabitacionForm(request.POST, instance=reserva_a_cancelar)

		reserva_a_cancelar.status_payment = 'Cancelado'
		reserva_a_cancelar.save()

	template = 'pago.html'
	context = {

		'reserva_cancelada' : reserva_a_cancelar
	}

	return render(request, template, context)


	#	aquí modificamos los atributos de la reserva para establecer si se cancelará
	#	si sera pago en efectivo o por Mercado Pago

def mercado_pago(request):

	if request.method == 'GET':

		id1 = request.GET['identificador']
		metodo = 'Mercado Pago'
		statusPayment = request.GET['estado']

		reserva_actual = Reservas_habitacion.objects.get(identificador=id1)
		# reserva_actual = reserva_actual1.get(identificador=id1)
		actualizarForm = ReservasHabitacionForm(request.GET, instance=reserva_actual)


		reserva_actual.metodo_de_pago = metodo
		reserva_actual.status_payment = statusPayment


		reserva_actual.save()
		

	template = 'pago.html'
	context = {

		'metodo' : metodo,
		'id' : id1,
		'estado' : statusPayment
		
	}

	return render(request, template, context)


def actualizacion(request):
	
	if request.method == 'POST':

		id1 = request.POST['id1']
		metodo = request.POST['metodo']
		statusPayment = request.POST['StatusPayment']

		reserva_actual = Reservas_habitacion.objects.get(identificador=id1)
		# reserva_actual = reserva_actual1.get(identificador=id1)
		actualizarForm = ReservasHabitacionForm(request.POST, instance=reserva_actual)
		

		reserva_actual.metodo_de_pago = request.POST['metodo']
		reserva_actual.status_payment = request.POST['StatusPayment']

		reserva_actual.save()
		

	template = 'pago.html'
	context = {

		'metodo' : metodo,
		'id' : id1,
		'estado' : statusPayment
		
	}

	return render(request, template, context)

			###############################################################
			#                 FIN  OPCIONES DE PAGO Y ESTADO              #
			###############################################################

def listar_reservas(request):
	
	usuario1 = request.user
	reservas1 = Reservas_habitacion.objects.all()
	reservas = (reservas1.filter(usuario=usuario1))


	template = 'listar_reservas.html'
	context = {

		'usuario' : usuario1,
		'reservas' : reservas
	}

	return render(request, template, context)

def eliminar_reserva(request):

	if request.method == 'POST':

		identificador = request.POST['identificador']
		reserva_to_delete = Reservas_habitacion.objects.filter(identificador=identificador)

		reserva_to_delete.delete()

		return redirect('mis_reservas')

