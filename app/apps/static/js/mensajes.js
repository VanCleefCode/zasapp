	
    $(document).ajaxStart(function() {
        $('#loading').fadeIn();
    });
    $(document).ajaxStop(function() {
        $('#loading').fadeOut();
    });

/**** MENSAJE DE ERROR ****/

function error_message(msj){

  $('#error').html(msj);
  $('.error').fadeIn('slow', function () {
    $(this).delay(3000).fadeOut('slow');
  });
}

function success_message(msj){
  console.log('esta entrando');

  $('#success').html(msj);
  $('.success').fadeIn('slow', function () {
    $(this).delay(3000).fadeOut('slow');
  });
}
