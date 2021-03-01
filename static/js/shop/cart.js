$(document).ready(function(){
  $(".offer").click(function(event){
    $.ajax({
	url: '/api/cart',
	method: 'put',
	dataType: 'json',
	success: function(data){
		alert('Заказ успешно оформлен!');
	}});
  });
});