# Hotel_bit

Hotel Bit es un sistema de gestion de reservas creado en Python haciendo uso de su FrameWork Django
Está dividido en varias aplicaciones como:

#### Reservas
Cuenta con un filtro que toma en cuenta las fechas de entrada y salida mas la cantidad de personas que harán uso del establecimiento, como primera instancia se filtra por capacidad, luego las fechas que el usuario a seleccionado para luego devolver una lista de habitaciones disponible las cuales se pueden reservar,Las habitaciones cuentan con un tope máximo preestablecido de 10 disponibles por habitacion, aunque es totalmente modificable desde el admin, teniendo en cuenta esto, se ha establecido un segundo filtro que se encarga de buscar cuantas reservas existen para cada habitacion en un periodo de tiempo, si la cantidad de reservas en ese período es igual al capacidad máxima de la habitación, la misma será excluida de la lista final que será mostrada al usuario.
Tambien cuenta como metodo de pago dos opciones 

  ##### Mercado Pago
El sistema de MP esta realizado en php, el cual se encuentra en la carpeta MercadoPago, esta alojada en un hosting para poder hacer uso de la misma más facilmente sin tener que correr 2 servidores simultaneamente como el server de python y un server apache para php.

  ##### Pago en Efectivo
Actualiza el estado de pago de la reserva como pendiente puesto que el usuario abonará en el Hotel.
  #### Cancelar la reserva
  Cancela la reserva actualizando su estado en la bd sin eliminarla
  
### Users

Aquí podemos hacer uso de un Regsiter & Login para dar de alta usuarios en el sistema, los agrega a la bd, pudiendo asi ingresar en un futuro a la aplicacion para hacer uso de la misma

### Comentarios
Aquí contamos con un formulario que aparecerá en la descripcion de cada habitacion o en forma general del establecimiento, dejando una lista de comentarios y puntuaciones que se verán plasmadas como experiencias de usuario, esto llevará a que los usuarios tomen en cuenta las experiencias de otros para elejir su habitacion.

### Newsletter
  Se encuentra en el footer de la plataforma, al ingresar un email, quedará registrado en la bd para que la gerencia o administracion del establecimiento envie boletines de noticias o cupones de descuentos aumentando asi la probabildiad de que potenciales clientes reserven una habitacion.
  
  

