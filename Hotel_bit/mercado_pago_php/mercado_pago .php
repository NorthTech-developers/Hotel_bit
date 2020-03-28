<?php

if(isset($_GET['payment_status'])){

    $estado=$_GET['payment_status'];
    $ref = $_GET['external_reference'];


    if($estado == 'success' | $estado == 'aprovado' | $estado == 'approved'){

        header ("Location: http://127.0.0.1:8000/contacto?aprovado&identificador=$ref");

    }elseif( $estado == 'failure' | $estado == 'fallo'){

        header ("Location: http://127.0.0.1:8000/contacto?fallo&identificador=$ref");
    }elseif( $estado == 'pending' | $estado == 'pendiente' ){

        header ("Location: http://127.0.0.1:8000/contacto?pendiente&identificador=$ref");
    };


};

require __DIR__  . '/vendor/autoload.php';

$reserva = $_GET['nombre'];
$precio = $_GET['precio'];
$usuario = $_GET['usuario'];
$idd = $_GET['id'];



// MercadoPago\SDK::setClientId("6168214163550142");
// MercadoPago\SDK::setClientSecret("q23K4fKeC7wE8poxp1B05aUuiqTsbhJJ");
MercadoPago\SDK::setAccessToken("TEST-8644071912236672-031616-391142162dc436bd4c89c86168b245ef-190894637");
MercadoPago\SDK::setPublicKey("TEST-36988e1f-7bf4-4443-b2e1-ccf88e24783d");

$preference = new MercadoPago\Preference();

  $produto = [$reserva, 1, $precio, $idd];

  $item2 = new MercadoPago\Item();
  $item2->currency_id = "UYU";
  $item2->id = $produto[3];
  $item2->collection_id = $produto[3];
  $item2->title = $produto[0]; 
  $item2->quantity = $produto[1];
  $item2->unit_price = str_replace(',', '.', $produto[2]);
  $item2->collection_id = $id;
  $item2->picture_url = "http://bit.cuti.org.uy/img/logo-bit.png";
  $item2->description =$reserva;
  

  
  $payer = new MercadoPago\Payer();
  $payer->name = $usuario;
  

  # url de retorno segun resultado de la compra al servidor local donde se ejecuta django
  $preference->back_urls = array(
    "success" => "http://hotelbit.byethost31.com/hotel/mercado_pago.php?estado=aprovado&usuario=$usuario&identificador=$idd",
    "failure" => "http://hotelbit.byethost31.com/hotel/mercado_pago.php?estado=fallo&usuario=$usuario&identificador=$idd",
    "pending" => "http://hotelbit.byethost31.com/hotel/mercado_pago.php?estado=pendiente&usuario=$usuario&identificador=$idd"
);


  $preference->external_reference = $idd;
  $preference->items = array($item2);
  $preference->payer = $payer;
  $preference->save(); # Save the preference and send the HTTP Request to create
  

  
  
 ?>


<div class="container-login100-form-btn p-t-10">
   
</div>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="description" content="">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Title -->
    <title>Hotel_BIT&amp; Mercado Pago</title>

    <!-- Favicon -->
    <link rel="icon" href="./hotel_bit/hotel/img/core-img/favicon.png">

    <!-- Stylesheet -->
    <link rel="stylesheet" href="./hotel_bit/hotel/style.css">

</head>

<body>
    <!-- Preloader -->
    <div id="preloader">
        <div class="loader"></div>
    </div>
    <!-- /Preloader -->

    <!-- Header Area Start -->
    <header class="header-area">
        <!-- Search Form -->
        <div class="search-form d-flex align-items-center">
            <div class="container">
                <form action="index.html" method="get">
                    <input type="search" name="search-form-input" id="searchFormInput" placeholder="Type your keyword ...">
                    <button type="submit"><i class="icon_search"></i></button>
                </form>
            </div>
        </div>

        <!-- Top Header Area Start -->
        <div class="top-header-area">
            <div class="container">
                <div class="row">

                    <div class="col-8">
                        <div class="top-header-content">
                            <a href="#"><i class="icon_phone"></i> <span>(+598) 099 999 999</span></a>
                            <a href="mailto:contacto@hotelbit.com.uy"><i class="icon_mail"></i> <span>contacto@hotelbit.com.uy</span></a>
                            <a href="#"><i class="fa fa-user-circle" aria-hidden="true"></i> 

                               
                                    <span><?php echo $usuario;?></span>

            
                              
                               
                          
                            
                            </a>

                        </div>
                    </div>

                    <div class="col-4">
                        <div class="top-header-content">
                            <!-- Top Social Area -->
                            <div class="top-social-area ml-auto">
                                <a href="#"><i class="fa fa-facebook" aria-hidden="true"></i></a>
                                <a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a>
                                <a href="#"><i class="fa fa-tripadvisor" aria-hidden="true"></i></a>
                                <a href="#"><i class="fa fa-instagram" aria-hidden="true"></i></a>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
        <!-- Top Header Area End -->

        <!-- Main Header Start -->
        <div class="main-header-area">
            <div class="classy-nav-container breakpoint-off">
                <div class="container">
                    <!-- Classy Menu -->
                    <nav class="classy-navbar justify-content-between" id="robertoNav">

                        <!-- Logo -->
                        <a class="nav-brand" href="../home"><img src="./hotel_bit/hotel/img/core-img/logo_header.png" alt="Logo"></a>

                        <!-- Navbar Toggler -->
                        <div class="classy-navbar-toggler">
                            <span class="navbarToggler"><span></span><span></span><span></span></span>
                        </div>

                        <!-- Menu -->
                        <div class="classy-menu">
                            <!-- Menu Close Button -->
                            <div class="classycloseIcon">
                                <div class="cross-wrap"><span class="top"></span><span class="bottom"></span></div>
                            </div>
                            <!-- Nav Start -->
                            <div class="classynav">
                                <ul id="nav">
                                    <li class="active"><a href="../home">Inicio</a></li>
                                    <li><a href="../habitaciones">Habitaciones</a>
                                        <ul class="dropdown">
                                            <li><a href="../habitacion_vip">Habitacion Pequeña</a></li>
                                            <li><a href="../habitacion_vip">Habitacón Común</a></li>
                                            <li><a href="../habitacion_vip">Habitación Premium</a></li>
                                            <li><a href="../habitacion_vip">Habitación Vip</a></li>
                                            <li><a href="../habitacion_vip">Habitación Real</a></li>
                                        </ul>
                                    </li>

                                    <li><a href="../galeria">Galeria</a></li>
                                    <li><a href="../sobre_nosotros">Sobre nosotros</a></li>
                                    <li><a href="../contacto">Contacto</a></li>
                                </ul>

                                <!-- Search -->
                                <div class="search-btn ml-4">
                                    <i class="fa fa-search" aria-hidden="true"></i>
                                </div>

                                <!-- Book Now -->
                                <div class="book-now-btn ml-3 ml-lg-5">
                                    
                                    
                                    <a href="">Cerrar Sesion <i class="fa fa-long-arrow-right" aria-hidden="true"></i></a>
                                </div>
                            </div>
                            <!-- Nav End -->
                        </div>
                    </nav>
                </div>
            </div>
        </div>
    </header>
    <!-- Header Area End -->

    <!-- Breadcrumb Area Start -->
    <div class="breadcrumb-area bg-img bg-overlay jarallax" style="background-image: url(./hotel_bit/hotel/img/bg-img/17.jpg);">
        <div class="container h-100">
            <div class="row h-100 align-items-center">
                <div class="col-12">
                    <div class="breadcrumb-content text-center">
                        <div class="breadcrumb-post-content">
                            <h2 class="post-title">Continua con el pago de $<?php echo $precio?></h2>
                            <div class="post-meta">
                                                               
 <form>                       
  <script
   src="https://www.mercadopago.com.uy/integrations/v1/web-payment-checkout.js"
   data-preference-id="<?php echo $preference->id; ?>">
  </script>
</form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Breadcrumb Area End -->

    <!-- Blog Area Start -->
    
    <!-- Footer Area Start -->
     <!-- Footer Area Start -->
     <footer class="footer-area section-padding-80-0">
        <!-- Main Footer Area -->
        <div class="main-footer-area">
            <div class="container">
                <div class="row align-items-baseline justify-content-between">
                    <!-- Single Footer Widget Area -->
                    <div class="col-12 col-sm-6 col-lg-3">
                        <div class="single-footer-widget mb-80">
                            <!-- Footer Logo -->
                            <a href="../home" class="footer-logo"><img src="./hotel_bit/hotel/img/core-img/logo_footer.png" alt=""></a>

                            <h4>(+598) 099 999 999</h4>
                            <span><a href="mailto:contacto@hotelbit.com.uy"><span>contacto@hotelbit.com.uy</a></span>
                            <span>Edificio Central, Av Italia 6201, 11500 Montevideo, Departamento de Montevideo</span>
                        </div>
                    </div>

                    <!-- Single Footer Widget Area -->
                    <div class="col-12 col-sm-6 col-lg-3">
                        <div class="single-footer-widget mb-80">
                            <!-- Widget Title -->
                            <h5 class="widget-title">Nuestro Blog</h5>

                            <!-- Single Blog Area -->
                            <div class="latest-blog-area">
                                <a href="#" class="post-title">Trucos de diseño independiente</a>
                                <span class="post-date"><i class="fa fa-clock-o" aria-hidden="true"></i> Jun 02, 2019</span>
                            </div>

                            <!-- Single Blog Area -->
                            <div class="latest-blog-area">
                                <a href="#" class="post-title">Publicidad gratuita en línea</a>
                                <span class="post-date"><i class="fa fa-clock-o" aria-hidden="true"></i> Jun 02, 2019</span>
                            </div>
                        </div>
                    </div>

                    <!-- Single Footer Widget Area -->
                    <div class="col-12 col-sm-4 col-lg-2">
                        <div class="single-footer-widget mb-80">
                            <!-- Widget Title -->
                            <h5 class="widget-title">Enlaces</h5>

                            <!-- Footer Nav -->
                            <ul class="footer-nav">
                                <li><a href="../home"><i class="fa fa-caret-right" aria-hidden="true"></i> Inicio</a></li>
                                <li><a href="../habitaciones"><i class="fa fa-caret-right" aria-hidden="true"></i> Habitaciones</a></li>
                                <li><a href="../galeria"><i class="fa fa-caret-right" aria-hidden="true"></i> Galeria</a></li>
                                <li><a href="../sobre_nosotros"><i class="fa fa-caret-right" aria-hidden="true"></i> Sobre nosotros</a></li>
                                <li><a href="../contacto"><i class="fa fa-caret-right" aria-hidden="true"></i> Contacto</a></li>
                            </ul>
                        </div>
                    </div>

                    <!-- Single Footer Widget Area -->
                    <div class="col-12 col-sm-8 col-lg-4">
                        <div class="single-footer-widget mb-80">
                            <!-- Widget Title -->
                            <h5 class="widget-title">
                                Suscribirse a Newsletter</h5>
                            <span>Suscríbase a nuestro boletín de noticias para recibir notificaciones sobre nuevas actualizaciones.</span>

                            <!-- Newsletter Form -->
                            <form action="#" method="post" class="nl-form">
                                <input type="email" name="email_newsletter" required class="form-control" placeholder="Ingrese su E-mail...">
                                <button type="submit"><i class="fa fa-paper-plane" aria-hidden="true"></i></button> {% csrf_token %}
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Copywrite Area -->
        <div class="container">
            <div class="copywrite-content">
                <div class="row align-items-center">
                    <div class="col-12 col-md-8">
                        <!-- Copywrite Text -->
                        <div class="copywrite-text">
                            <p>
                                <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                                Copyright &copy;
                                <script>
                                    document.write(new Date().getFullYear());
                                </script> Todos los derechos reservados | Creado con <i class="fa fa-heart-o" aria-hidden="true"></i> por <a href="#" target="_blank">NorthTech Developers</a>
                                <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                            </p>
                        </div>
                    </div>
                    <div class="col-12 col-md-4">
                        <!-- Social Info -->
                        <div class="social-info">
                            <a href="#"><i class="fa fa-facebook" aria-hidden="true"></i></a>
                            <a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a>
                            <a href="#"><i class="fa fa-instagram" aria-hidden="true"></i></a>
                            <a href="#"><i class="fa fa-linkedin" aria-hidden="true"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    <!-- Footer Area End -->

    <!-- **** All JS Files ***** -->
    <!-- jQuery 2.2.4 -->
    <script src="./hotel_bit/hotel/js/jquery.min.js"></script>
    <!-- Popper -->
    <script src="./hotel_bit/hotel/js/popper.min.js"></script>
    <!-- Bootstrap -->
    <script src="./hotel_bit/hotel/js/bootstrap.min.js"></script>
    <!-- All Plugins -->
    <script src="./hotel_bit/hotel/js/roberto.bundle.js"></script>
    <!-- Active -->
    <script src="./hotel_bit/hotel/js/default-assets/active.js"></script>

</body>

</html>