<?php
require __DIR__  . '../../../../../../vendor/autoload.php';


// MercadoPago\SDK::setClientId("6168214163550142");
// MercadoPago\SDK::setClientSecret("q23K4fKeC7wE8poxp1B05aUuiqTsbhJJ");
MercadoPago\SDK::setAccessToken("APP_USR-6168214163550142-061000-8fdabbe8a7c255dcb03cd24cfabeb2b7-190894637");
MercadoPago\SDK::setPublicKey("APP_USR-812c544c-9c4d-4cd9-81e2-33d73f8d6f28");

$preference = new MercadoPago\Preference();

  $produto = [$clase, 1, $clases['precio'], $id];

  $item2 = new MercadoPago\Item();
  $item2->currency_id = "UYU";
  $item2->id = $produto[3];
  $item2->collection_id = $produto[3];
  $item2->title = $produto[0]; 
  $item2->quantity = $produto[1];
  $item2->unit_price = str_replace(',', '.', $produto[2]);
  $item2->collection_id = $id;
  $item2->picture_url = "localhost\plataforma\images\images\logo4.png";
  $item2->description = "Studere Platform Tacuarembó Uruguay";
  

  
  $payer = new MercadoPago\Payer();
  $payer->email = $hola;
  $payer->name = $a['Nombre']." ".$a['Apellido'];
  

  # url de retorno segun resultado de la compra
  $preference->back_urls = array(
    "success" => "localhost/prueba/usuarios/plataforma/clases/1bc/procesos/actualizaciondatos.php?aprovado",
    "failure" => "localhost/prueba/usuarios/plataforma/clases/1bc/procesos/actualizaciondatos.php?fallo",
    "pending" => "localhost/prueba/usuarios/plataforma/clases/1bc/procesos/actualizaciondatos.php?pendiente"
);


  $preference->external_reference = $id;
  $preference->items = array($item2);
  $preference->payer = $payer;
  $preference->save(); # Save the preference and send the HTTP Request to create
  


?>

{% extends 'base.html' %} {%load static%} {%block title%} Hotel BIT | Editar Reserva{% endblock title%} {% block nombre_usuario %} {% if user.is_autenticate %}
<span>hola username</span> {% else %}
<span>No has iniciado sesión</span> {% endif %} {% endblock nombre_usuario %} {% block content %}
<div class="breadcrumb-area bg-img bg-overlay jarallax" style="background-image: url(../static/img/bg-img/16.jpg);">
    <div class="container h-100">
        <div class="row h-100 align-items-center">
            <div class="col-12">
                <div class="breadcrumb-content text-center">
                    <h2 class="page-title">Mercado Pago</h2>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb justify-content-center">
                            <li class="breadcrumb-item"><a href="index.html">Inicio</a></li>
                            <li class="breadcrumb-item active" aria-current="page">Datos extras y pago</li>
                        </ol>
                    </nav>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock content %} {% block habitaciones %}

<h2> Habitaciones Disponibles para ti</h2>

{% endblock habitaciones %} {% block habitaciones_slide %}


               

               
                 
                <section class="roberto-blog-area section-padding-100-0">
    <div class="container">
        <div class="row">
            <!-- Section Heading -->
            <div class="col-12">
                
            </div>
        </div>
        <?php 
                       echo "<a class='btn btn-success' href='$preference->sandbox_init_point '>Comprar Clase</a>";
                        ?>
        

        </div>
    </div>
</section>

        

    {% endblock habitaciones_slide %}