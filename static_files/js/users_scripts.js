
/**** ENVIAR AJAX DE CREAR CONTACTO ****/
$( "#addUsuario" ).submit(function( event ) {

  if($('#id_username').val()==''){
    error_message('Debe ingresar el Nick');
    $('#id_username').css('border','2px solid red');
    return false;
  }else{
       $('#id_username').css('border','1px solid #ccc');
  }

  if($('#id_email').val()==''){
    error_message('Debe ingresar el email');
    $('#id_email').css('border','2px solid red');
    return false;
  }else{
       $('#id_email').css('border','1px solid #ccc');
  }


  if($('#id_first_name').val()==''){
    error_message('Debe ingresar el nombre');
    $('#id_first_name').css('border','2px solid red');
    return false;
  }else{
       $('#id_first_name').css('border','1px solid #ccc');
  }

  if($('#id_last_name').val()==''){
    error_message('Debe ingresar el apellido');
    $('#id_last_name').css('border','2px solid red');
    return false;
  }else{
       $('#id_last_name').css('border','1px solid #ccc');
  }

  if($('#id_telefono').val()==''){
    error_message('Debe ingresar el teléfono');
    $('#id_telefono').css('border','2px solid red');
    return false;
  }else{
       $('#id_telefono').css('border','1px solid #ccc');
  }



   $.ajax({
           type: "POST",
           url: '/usuario/crear-usuario/',
           data: $("#addUsuario").serialize(), // serializes the form's elements.
           success: function(data)
           {

              if(data=='existeEmail'){
                error_message('El email esta registrado');
                $('#id_email').css('border','2px solid red');
              }else if(data=='ok'){
                  success_message('Creado exitosamente');
                  setTimeout("location.href='/usuario/'", 2000);
              }
           }
         });
  event.preventDefault();
});



/**** ENVIAR AJAX DE EDITAR CONTACTO ****/
$( "#updateUsuario" ).submit(function( event ) {

 if($('#id_username').val()==''){
    error_message('Debe ingresar el Nick');
    $('#id_username').css('border','2px solid red');
    return false;
  }else{
       $('#id_username').css('border','1px solid #ccc');
  }

  if($('#id_email').val()==''){
    error_message('Debe ingresar el email');
    $('#id_email').css('border','2px solid red');
    return false;
  }else{
       $('#id_email').css('border','1px solid #ccc');
  }


  if($('#id_first_name').val()==''){
    error_message('Debe ingresar el nombre');
    $('#id_first_name').css('border','2px solid red');
    return false;
  }else{
       $('#id_first_name').css('border','1px solid #ccc');
  }

  if($('#id_last_name').val()==''){
    error_message('Debe ingresar el apellido');
    $('#id_last_name').css('border','2px solid red');
    return false;
  }else{
       $('#id_last_name').css('border','1px solid #ccc');
  }

  if($('#id_telefono').val()==''){
    error_message('Debe ingresar el teléfono');
    $('#id_telefono').css('border','2px solid red');
    return false;
  }else{
       $('#id_telefono').css('border','1px solid #ccc');
  }


   $.ajax({
           type: "POST",
           url: '/usuario/editar-usuario/' + $('#id_id').val() + '/',
           data: $("#updateUsuario").serialize(), // serializes the form's elements.
           success: function(data)
           {

              if(data=='existeEmail'){
                error_message('El email esta registrado');
                $('#id_email').css('border','2px solid red');
              }else if(data=='ok'){
                  success_message('Editado exitosamente');
                  setTimeout("location.href='/usuario/'", 2000);
              }
           }
         });
  event.preventDefault();
});


