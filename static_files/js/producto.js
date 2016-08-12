
/**** ENVIAR AJAX DE LOGIN ****/
$( "#crearProducto" ).submit(function( event ) {

    if($('#id_nombre').val()==''){
        error_message('Debe ingresar el nombre del producto');
        $('#id_nombre').css('border','2px solid red');
        return false;
      }else{
          $('#id_nombre').css('border','none');
    }

    if($('#id_descripcion').val()==''){
        error_message('Debe ingresar la descripción del producto');
        $('#id_descripcion').css('border','2px solid red');
        return false;
      }else{
          $('#id_descripcion').css('border','none');
    }

    if($('#id_precio').val()==''){
        error_message('Debe ingresar el precio del producto');
        $('#id_precio').css('border','2px solid red');
        return false;
      }else{
          $('#id_precio').css('border','none');
    }
    
   
  var formData = new FormData();
  formData.append('nombre',$('#id_nombre').val());
  formData.append('descripcion',$('#id_descripcion').val());
  formData.append('precio',$('#id_precio').val());
  formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
  if($('#id_thumbnail').val()!=""){
    formData.append('file', $('#id_thumbnail')[0].files[0]);
  }

   $.ajax({
           type: "POST",
           url: '/producto/crear-producto/',
           enctype: 'multipart/form-data',         
           data: formData, // serializes the form's elements.
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType           
           success: function(data)
           {              
                 success_message('Se creo el PRODUCTO Satisfactoriamente');
                 $('#id_nombre').val('');
                 $('#id_descripcion').val('');
                 $('#id_precio').val('');
                 $('#id_thumbnail').val('');
                 $("html, body").animate({scrollTop: 0}, 600);
                 $("#blah").attr("src","/media/pic_folder_productos/None/no-image.png");
                 setTimeout("location.href='/producto/'", 2000);
           }      
         });
  event.preventDefault();
});

/**** ENVIAR AJAX DE LOGIN ****/
$( "#EditarProducto" ).submit(function( event ) {

    if($('#id_nombre').val()==''){
        error_message('Debe ingresar el nombre del producto');
        $('#id_nombre').css('border','2px solid red');
        return false;
      }else{
          $('#id_nombre').css('border','none');
    }

    if($('#id_descripcion').val()==''){
        error_message('Debe ingresar la descripción del producto');
        $('#id_descripcion').css('border','2px solid red');
        return false;
      }else{
          $('#id_descripcion').css('border','none');
    }

    if($('#id_precio').val()==''){
        error_message('Debe ingresar el precio del producto');
        $('#id_precio').css('border','2px solid red');
        return false;
      }else{
          $('#id_precio').css('border','none');
    }
    
   
  var formData = new FormData();
  formData.append('nombre',$('#id_nombre').val());
  formData.append('descripcion',$('#id_descripcion').val());
  formData.append('precio',$('#id_precio').val());
  formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
  if($('#id_thumbnail').val()!=""){
    formData.append('file', $('#id_thumbnail')[0].files[0]);
  }

   $.ajax({
           type: "POST",
           url: '/producto/editar-producto/' + $('#id_id').val() +'/',
           enctype: 'multipart/form-data',         
           data: formData, // serializes the form's elements.
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType           
           success: function(data)
           {              
                 success_message('Se creo el PRODUCTO Satisfactoriamente');
                 $('#id_nombre').val('');
                 $('#id_descripcion').val('');
                 $('#id_precio').val('');
                 $('#id_thumbnail').val('');
                 $("html, body").animate({scrollTop: 0}, 600);
                 $("#blah").attr("src","/media/pic_folder_productos/None/no-image.png");
                 setTimeout("location.href='/producto/'", 2000);
           }      
         });
  event.preventDefault();
});

/**** ENVIAR AJAX DE LOGIN ****/
$( "#AddTemplate" ).submit(function( event ) {

    if($('#nombreP').val()==''){
        error_message('Debe ingresar el nombre del template');
        $('#nombreP').css('border','2px solid red');
        return false;
      }else{
          $('#nombreP').css('border','none');
    }

    if($('#urlP').val()==''){
        error_message('Debe ingresar la descripción del producto');
        $('#urlP').css('border','2px solid red');
        return false;
      }else{
          $('#urlP').css('border','none');
    }

   
  var formData = new FormData();
  formData.append('idP',$('#id_id').val());
  formData.append('nombreP',$('#nombreP').val());
  formData.append('urlP',$('#urlP').val());
  formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());

   $.ajax({
           type: "POST",
           url: '/producto/crear-template/',
           enctype: 'multipart/form-data',         
           data: formData, // serializes the form's elements.
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType           
           success: function(data)
           {              
                 success_message('Se creo el Template Satisfactoriamente');
                 $('#NoFila').hide();
                 $('#cuerpotabla tr:last').after('<tr><td>' + $('#nombreP').val() + '</td><td>' + $('#urlP').val() + '</td><td align="center"><i class="fa fa-edit"></i></td></tr>');
                 $('#nombreP').val('');
                 $('#urlP').val('');
                 
           }      
         });
  event.preventDefault();
});
