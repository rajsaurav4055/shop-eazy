$(document).ready(function(){
    // Add to cart
    $(document).on('click',".add-to-cart",function(){
        var _vm=$(this);
        var _index=_vm.attr('data-index');
        var _qty=$(".product-qty-"+_index).val();
        var _productId=$(".product-id-"+_index).val();
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
            success:function(data){
                // $(".cart-list").text(res.totalitems);
                _vm.attr('disabled',false);
                console.log(data);
                
            }
        });
        // End
    });
    // End

    $('select[name="discount"]').change(function(){

        if ($(this).val() == "10"){
            var totalAmount= $('.total-amount').text();
            console.log(totalAmount);
            totalAmount.replace('$','');
            console.log("after replace"+ totalAmount);
            totalAmount = parseInt(totalAmount);
            console.log("after parseInt"+ totalAmount);
            var discountedPrice= 0.9*totalAmount;
            console.log(discountedPrice);
            $('.total_price').text("$ "+discountedPrice);
        }
            

        else if($(this).val() == "20"){
            var totalAmount= $('.total-amount').text();
            console.log(totalAmount);
            totalAmount.replace('$','');
            console.log("after replace"+ totalAmount);
            totalAmount = parseInt(totalAmount);
            console.log("after parseInt"+ totalAmount);
            var discountedPrice= 0.8*totalAmount;
            console.log(discountedPrice);
            $('.total_price').text("$ "+discountedPrice);
        }
            
        else{
            var totalAmount= $('.total-amount').text();
            console.log(totalAmount);
            totalAmount.replace('$','');
            console.log("after replace"+ totalAmount);
            totalAmount = parseInt(totalAmount);
            console.log("after parseInt"+ totalAmount);
            var discountedPrice= 0.7*totalAmount;
            console.log(discountedPrice);
            $('.total_price').text("$ "+discountedPrice);
        }
        
    });

});

