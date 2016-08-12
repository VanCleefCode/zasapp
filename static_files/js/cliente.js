
/**** ENVIAR AJAX DE CREAR CLIENTE ****/
$( "#addCliente" ).submit(function( event ) {

  if($('#id_nombre').val()==''){
    error_message('Debe ingresar el Nombre');
    $('#id_nombre').css('border','2px solid red');
    return false;
  }else{
       $('#id_nombre').css('border','1px solid #ccc');
  }

  if($('#id_apellido').val()==''){
    error_message('Debe ingresar el Apellido');
    $('#id_apellido').css('border','2px solid red');
    return false;
  }else{
       $('#id_apellido').css('border','1px solid #ccc');
  }

  if($('#id_dni').val()==''){
    error_message('Debe ingresar el DNI');
    $('#id_dni').css('border','2px solid red');
    return false;
  }else{
       $('#id_dni').css('border','1px solid #ccc');
  }

  if($('#id_telefono').val()==''){
    error_message('Debe ingresar el Teléfono');
    $('#id_telefono').css('border','2px solid red');
    return false;
  }else{
       $('#id_telefono').css('border','1px solid #ccc');
  }


  if($('#id_empresa').val()==''){
    error_message('Debe ingresar la Razon Social');
    $('#id_empresa').css('border','2px solid red');
    return false;
  }else{
       $('#id_empresa').css('border','1px solid #ccc');
  }

  if($('#id_cif').val()==''){
    error_message('Debe ingresar el CIF');
    $('#id_cif').css('border','2px solid red');
    return false;
  }else{
       $('#id_cif').css('border','1px solid #ccc');
  }

  if($('#id_email').val()==''){
    error_message('Debe ingresar el Email');
    $('#id_email').css('border','2px solid red');
    return false;
  }else{
       $('#id_email').css('border','1px solid #ccc');
  }

  if($('#id_telefono1').val()==''){
    error_message('Debe ingresar el Teléfono');
    $('#id_telefono1').css('border','2px solid red');
    return false;
  }else{
       $('#id_telefono1').css('border','1px solid #ccc');
  }

  if($('#id_ciudad').val()==''){
    error_message('Debe ingresar la Ciudad');
    $('#id_ciudad').css('border','2px solid red');
    return false;
  }else{
       $('#id_ciudad').css('border','1px solid #ccc');
  }

  if($('#id_provincia').val()==''){
    error_message('Debe ingresar la Provincia');
    $('#id_provincia').css('border','2px solid red');
    return false;
  }else{
       $('#id_provincia').css('border','1px solid #ccc');
  }

  if($('#id_codpostal').val()==''){
    error_message('Debe ingresar el Codigo Postal');
    $('#id_codpostal').css('border','2px solid red');
    return false;
  }else{
       $('#id_codpostal').css('border','1px solid #ccc');
  }

  if($('#id_direccion').val()==''){
    error_message('Debe ingresar la Dirección');
    $('#id_direccion').css('border','2px solid red');
    return false;
  }else{
       $('#id_direccion').css('border','1px solid #ccc');
  }

  
  var formData = new FormData();
  formData.append('nombre',$('#id_nombre').val());
  formData.append('apellido',$('#id_apellido').val());
  formData.append('dni',$('#id_dni').val());
  formData.append('telefono',$('#id_telefono').val());
  formData.append('empresa',$('#id_empresa').val());
  formData.append('cif',$('#id_cif').val());
  formData.append('email',$('#id_email').val());
  formData.append('telefono1',$('#id_telefono1').val());
  formData.append('ciudad',$('#id_ciudad').val());
  formData.append('direccion',$('#id_direccion').val());
  formData.append('provincia',$('#id_provincia').val());
  formData.append('codpostal',$('#id_codpostal').val());
  formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
  if($('#id_thumbnail').val()!=""){
    formData.append('file', $('#id_thumbnail')[0].files[0]);
  }

   $.ajax({
           type: "POST",
           url: '/clientes/crear-cliente/',
           enctype: 'multipart/form-data',         
           data: formData, // serializes the form's elements.
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType           
           success: function(data)
           {              
                 success_message('Se creo el CLIENTE Satisfactoriamente');
                 $("html, body").animate({scrollTop: 0}, 600);
                 setTimeout("location.href='/clientes/'", 1000);
           }      
         });
  event.preventDefault();
});


/**** ENVIAR AJAX DE CREAR CLIENTE ****/
$( "#editCliente" ).submit(function( event ) {

  if($('#id_nombre').val()==''){
    error_message('Debe ingresar el Nombre');
    $('#id_nombre').css('border','2px solid red');
    return false;
  }else{
       $('#id_nombre').css('border','1px solid #ccc');
  }

  if($('#id_apellido').val()==''){
    error_message('Debe ingresar el Apellido');
    $('#id_apellido').css('border','2px solid red');
    return false;
  }else{
       $('#id_apellido').css('border','1px solid #ccc');
  }

  if($('#id_dni').val()==''){
    error_message('Debe ingresar el DNI');
    $('#id_dni').css('border','2px solid red');
    return false;
  }else{
       $('#id_dni').css('border','1px solid #ccc');
  }

  if($('#id_telefono').val()==''){
    error_message('Debe ingresar el Teléfono');
    $('#id_telefono').css('border','2px solid red');
    return false;
  }else{
       $('#id_telefono').css('border','1px solid #ccc');
  }


  if($('#id_empresa').val()==''){
    error_message('Debe ingresar la Razon Social');
    $('#id_empresa').css('border','2px solid red');
    return false;
  }else{
       $('#id_empresa').css('border','1px solid #ccc');
  }

  if($('#id_cif').val()==''){
    error_message('Debe ingresar el CIF');
    $('#id_cif').css('border','2px solid red');
    return false;
  }else{
       $('#id_cif').css('border','1px solid #ccc');
  }

  if($('#id_email').val()==''){
    error_message('Debe ingresar el Email');
    $('#id_email').css('border','2px solid red');
    return false;
  }else{
       $('#id_email').css('border','1px solid #ccc');
  }

  if($('#id_telefono1').val()==''){
    error_message('Debe ingresar el Teléfono');
    $('#id_telefono1').css('border','2px solid red');
    return false;
  }else{
       $('#id_telefono1').css('border','1px solid #ccc');
  }

  if($('#id_ciudad').val()==''){
    error_message('Debe ingresar la Ciudad');
    $('#id_ciudad').css('border','2px solid red');
    return false;
  }else{
       $('#id_ciudad').css('border','1px solid #ccc');
  }

  if($('#id_provincia').val()==''){
    error_message('Debe ingresar la Provincia');
    $('#id_provincia').css('border','2px solid red');
    return false;
  }else{
       $('#id_provincia').css('border','1px solid #ccc');
  }

  if($('#id_codpostal').val()==''){
    error_message('Debe ingresar el Codigo Postal');
    $('#id_codpostal').css('border','2px solid red');
    return false;
  }else{
       $('#id_codpostal').css('border','1px solid #ccc');
  }

  if($('#id_direccion').val()==''){
    error_message('Debe ingresar la Dirección');
    $('#id_direccion').css('border','2px solid red');
    return false;
  }else{
       $('#id_direccion').css('border','1px solid #ccc');
  }

  
  var formData = new FormData();
  formData.append('nombre',$('#id_nombre').val());
  formData.append('apellido',$('#id_apellido').val());
  formData.append('dni',$('#id_dni').val());
  formData.append('telefono',$('#id_telefono').val());
  formData.append('empresa',$('#id_empresa').val());
  formData.append('cif',$('#id_cif').val());
  formData.append('email',$('#id_email').val());
  formData.append('telefono1',$('#id_telefono1').val());
  formData.append('ciudad',$('#id_ciudad').val());
  formData.append('direccion',$('#id_direccion').val());
  formData.append('provincia',$('#id_provincia').val());
  formData.append('codpostal',$('#id_codpostal').val());
  formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
  if($('#id_thumbnail').val()!=""){
    formData.append('file', $('#id_thumbnail')[0].files[0]);
  }

   $.ajax({
           type: "POST",
           url: '/clientes/editar-cliente/' + $('#id_id').val() + '/',
           enctype: 'multipart/form-data',         
           data: formData, // serializes the form's elements.
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType           
           success: function(data)
           {              
                 success_message('Se edito el CLIENTE Satisfactoriamente');
                 $("html, body").animate({scrollTop: 0}, 600);
                 setTimeout("location.href='/clientes/'", 1000);
           }      
         });
  event.preventDefault();
});

