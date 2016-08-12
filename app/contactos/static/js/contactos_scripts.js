
/**** ENVIAR AJAX DE CREAR CONTACTO ****/
$( "#addContacto" ).submit(function( event ) {

  if($('#id_nombre').val()==''){
    error_message('Debe ingresar el nombre');
    $('#id_nombre').css('border','2px solid red');
    return false;
  }else{
       $('#id_nombre').css('border','1px solid #ccc');
  }

  if($('#id_apellido').val()==''){
    error_message('Debe ingresar el apellido');
    $('#id_apellido').css('border','2px solid red');
    return false;
  }else{
       $('#id_apellido').css('border','1px solid #ccc');
  }

  if($('#id_email').val()==''){
    error_message('Debe ingresar el email');
    $('#id_email').css('border','2px solid red');
    return false;
  }else{
       $('#id_email').css('border','1px solid #ccc');
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
           url: '/contacto/crear/',
           data: $("#addContacto").serialize(), // serializes the form's elements.
           success: function(data)
           {

              if(data=='existeEmail'){
                error_message('El email esta registrado');
                $('#id_email').css('border','2px solid red');
              }else if(data=='ok'){
                  success_message('Creado exitosamente');
                  setTimeout("location.href='/contacto/'", 2000);
              }
           }
         });
  event.preventDefault();
});


/**** ENVIAR AJAX DE EDITAR CONTACTO ****/
$( "#updateContacto" ).submit(function( event ) {

  if($('#id_nombre').val()==''){
    error_message('Debe ingresar el nombre');
    $('#id_nombre').css('border','2px solid red');
    return false;
  }else{
       $('#id_nombre').css('border','1px solid #ccc');
  }

  if($('#id_apellido').val()==''){
    error_message('Debe ingresar el apellido');
    $('#id_apellido').css('border','2px solid red');
    return false;
  }else{
       $('#id_apellido').css('border','1px solid #ccc');
  }

  if($('#id_email').val()==''){
    error_message('Debe ingresar el email');
    $('#id_email').css('border','2px solid red');
    return false;
  }else{
       $('#id_email').css('border','1px solid #ccc');
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
           url: '/contacto/editar-contacto/' + $('#id_id').val() + '/',
           data: $("#updateContacto").serialize(), // serializes the form's elements.
           success: function(data)
           {

              if(data=='existeEmail'){
                error_message('El email esta registrado');
                $('#id_email').css('border','2px solid red');
              }else if(data=='ok'){
                  success_message('Editado exitosamente');
                  setTimeout("location.href='/contacto/'", 2000);
              }
           }
         });
  event.preventDefault();
});



function BorrarContacto(id,csrf_token){

 $( "#dialog-confirm" ).dialog({
      resizable: false,
      height:160,
      modal: true,
      buttons: {
        "Si": function() {

           $.ajax({
                   type: "POST",
                   url: '/contacto/eliminar-contacto/' + id + '/',
                   data: { 'pk' : id,'csrfmiddlewaretoken': csrf_token },

                   success: function(data)
                   {

                      if(data=='ok'){
                          success_message('Eliminado exitosamente');
                          $("#" + id + "_fila").fadeOut("slow");
                      }
                   }
                 });
             $( this ).dialog( "close" );

          },
        Cancel: function() {
          $( this ).dialog( "close" );
        }
      }
    });

    event.preventDefault();

}