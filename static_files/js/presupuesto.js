
/** BUSCAR CLIENTE **/
$('#cliente').click(function(event){
	$.get('/clientes/buscarCliente/',{},function(data){
		$('#modalCliente').html(data).fadeIn();
	});
});

$('#id_producto').change(function(event){
	$.get('/producto/traer/?id=' + $(this).val(),{},function(data){
		$('#Ctemplates').html(data).fadeIn();
	});

});