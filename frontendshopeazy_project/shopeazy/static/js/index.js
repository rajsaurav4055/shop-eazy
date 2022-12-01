$(document).ready(function(){
    // Add to cart
	$(document).on('click',".add-to-cart",function(){
		var _vm=$(this);
		var _index=_vm.attr('data-index');
		var _qty=$(".product-qty-"+_index).val();
		var _productId=$(".product-productid-"+_index).val();
		var _productImage=$(".product-image-"+_index).val();
		var _productName=$(".product-pname-"+_index).val();
		var _productPrice=$(".product-price-"+_index).val();
		// Ajax
		$.ajax({
			url:'/add-to-cart',
			data:{
				'productid':_productId,
				'image':_productImage,
				'qty':_qty,
				'pname':_productName,
				'price':_productPrice
			},
			dataType:'json',
			beforeSend:function(){
				_vm.attr('disabled',true);
			},
			success:function(res){
				// $(".cart-list").text(res.totalitems);
				_vm.attr('disabled',false);
			}
		});
		// End
	});
	// End

});