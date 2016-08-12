
/**** ENVIAR AJAX DE CREAR CONTACTO ****/

    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!

    var yyyy = today.getFullYear();
    if(dd<10){
        dd='0'+dd
    } 
    if(mm<10){
        mm='0'+mm
    } 
    var today = yyyy+'-'+mm+'-'+dd;

$( "#addCita" ).submit(function( event ) {

  if($('#id_dia').val()==''){

    error_message('Debe ingresar una fecha valida');
    $('#id_dia').css('border','2px solid red');
    return false;
  }else{
      if($('#id_dia').val() <= today){
          error_message('Debe ingresar una fecha mayor');
          $('#id_dia').css('border','2px solid red');
          return false;
      }
      $('#id_dia').css('border','1px solid #ccc');
  }
   $.ajax({
           type: "POST",
           url: '/cita/crear-cita/',
           data: $("#addCita").serialize(), // serializes the form's elements.
           success: function(data)
           {

              if(data=='existeCita'){
                error_message('Este dia ya tiene creada ciata a las ' + $('#id_hora').val());
                $('#id_hora').css('border','2px solid red');
              }else{
                  success_message('Se creo la cita Satisfactoriamente');
                  $('#NoHayTR').hide();
                  $('#cuerpotabla tr:last').after('<tr><td>' + $('#id_dia').val() + '</td><td><strong>' + $('#id_hora').val() + '</strong> </td><td align="center">--</td>');
                  $('#id_dia').css('border','1px solid #ccc');
                  $('#id_hora').css('border','1px solid #ccc');

              }
           }
         });
  event.preventDefault();
});


// CLICK CANLENDARIO TRAE LOS CREADOS DE LAS CITAS AL DIA

function traerCitas(dia){
    $.get( "/cita/lista-cita/" + dia + "/", function( data ) {
      $( "#cuerpotabla" ).html( data );
    });
}

//BORRAR CITA


function BorrarCita(id,csrf_token){

 $( "#dialog-confirm" ).dialog({
      resizable: false,
      height:160,
      modal: true,
      buttons: {
        "Si": function() {

           $.ajax({
                   type: "POST",
                   url: '/cita/eliminar-cita/' + id + '/',
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