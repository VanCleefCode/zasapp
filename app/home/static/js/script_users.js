/**** SETTINGS AJAX ****/
    var cprimary = '#ffa800';

    $(document).ajaxStart(function() {
        $('#loading').fadeIn();
    });
    $(document).ajaxStop(function() {
        $('#loading').fadeOut();
    });


    var cprimary = '#DEA846';


/**** ENVIAR AJAX DE LOGIN ****/
$( "#LoginForm" ).submit(function( event ) {

	if($('#usuario').val()==''){
		error_message('Debe Ingresar el Usuario');
    $('#usuario').css('border','1px solid red');
		return false;
	}else if($('#clave').val()==''){
		error_message('Debe Ingresar la clave');
    $('#usuario').css('border','none');
    $('#clave').css('border','1px solid red');

		return false;
	}


   $.ajax({
           type: "POST",
           url: '/usuario/login/',
           data: $("#LoginForm").serialize(), // serializes the form's elements.
           success: function(data)
           {
               if(data=='ok'){
               	window.location = '/app/';
               }else{
               	error_message(data);
                $('#username').css('border','1px solid red');
                $('#password').css('border','1px solid red');
               }
           }
         });
  event.preventDefault();
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

/**** VALIDAR EMAIL ****/
 function validateEmail($email) {
  var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
  return emailReg.test( $email );
}

/**** CHEQUIAR USER ****/
function checkuser(username){
    if($('#Rusername').val()==''){
    $('#uncheckusername').hide();
    $('#checkusername').hide();
    $('#Rusername').css('border','none');
    return false;
  }

   $.ajax({
           type: "GET",
           url: '/user_profile/checkuser/' + $('#Rusername').val() + '/',
           success: function(data)
           {
              if(data=='ok'){

                $('#checkusername').fadeIn();
                $('#uncheckusername').hide();
                $('#Rusername').css('border','none');

              }else if(data=='existeUser'){

                $('#uncheckusername').fadeIn();
                $('#checkusername').hide();
                error_message('Usuario no disponible');
                $('#Rusername').css('border','1px solid red');

              }
           }
         });
  
  event.preventDefault();

}

/**** CHEQUIAR EMAIL ****/
function checkemail(email){

    if($('#Remail').val()==''){
    $('#uncheckemail').hide();
    $('#checkemail').hide();
    $('#Remail').css('border','none');
    return false;
  }

 if( !validateEmail($('#Remail').val())) { 

        $('#Remail').css('border','1px solid red');
        error_message('Debe ingresar un email valido');
        $('#uncheckemail').fadeIn();
        $('#checkemail').hide();
        return false;
  
   }

   $.ajax({
           type: "GET",
           url: '/user_profile/checkemail/' + $('#Remail').val() + '/',
           success: function(data)
           {
              if(data=='ok'){

                $('#checkemail').fadeIn();
                $('#uncheckemail').hide();
                $('#Remail').css('border','none');

              }else if(data=='existeEmail'){

                $('#uncheckemail').fadeIn();
                $('#checkemail').hide();
                error_message('Email no disponible');
                $('#Remail').css('border','1px solid red');

              }
           }
         });
  
  event.preventDefault();

}

// PASSWORD FUERTE //

function validatePwd(fieldname) {
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//Copyright April 2004 Sani, A. I. (MCSE, MCSA, CCNA)
//sanijean@yahoo.co.uk
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 
 
//Initialise variables
var errorMsg = "";
var space  = " ";
fieldname   = document.RegistroForm.Rpassword; 
fieldvalue  = fieldname.value; 
fieldlength = fieldvalue.length; 
 
if(fieldvalue==''){
  return false;
}

//It must not contain a space
if (fieldvalue.indexOf(space) > -1) {
     errorMsg += " - No espacios";
   
}     
 
//It must contain at least one number character
if (!(fieldvalue.match(/\d/))) {
     errorMsg += " - Un numero";
}
//It must start with at least one letter     
if (!(fieldvalue.match(/^[a-zA-Z]+/))) {
     errorMsg += " - Una letra al inicio";
}
//It must contain at least one upper case character     
if (!(fieldvalue.match(/[A-Z]/))) {
     errorMsg += " - Una mayuscula";
}
//It must contain at least one lower case character
if (!(fieldvalue.match(/[a-z]/))) {
     errorMsg += " - Una minuscula";
}
//It must contain at least one special character
if (!(fieldvalue.match(/\W+/))) {
     errorMsg += " - Un carecter especial #,@,%,!";
}
//It must be at least 7 characters long.
if (!(fieldlength > 8)) {
     errorMsg += " - Minimo 8 caracteres";
}
//If there is aproblem with the form then display an error
     if (errorMsg != ""){
          errorMsg = "La clave fuerte debe tener:<br>" + errorMsg;
          $('#passwordfuerte').html(errorMsg).fadeIn();
          $('#Rpassword').css('border','1px solid red');
          fieldname.focus();
          fieldname.value='';
          return false;
     }else{
      $('#passwordfuerte').fadeOut();
      $('#Rpassword').css('border','none');
     }
     
     return true;
}