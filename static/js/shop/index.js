$(document).ready(function(){
  $(".add-to-cart").click(function(event){
    product = $(event.target).attr('data');
    $.ajax({
	url: '/api/cart',
	method: 'post',
	dataType: 'json',
	data: {add_to_cart: product},
	success: function(data){
		alert('Товар добавлен в корзину!');
	}});
  });
});