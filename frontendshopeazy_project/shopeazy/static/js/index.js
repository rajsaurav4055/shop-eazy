$(document).ready(function(){
    var price_after_discount;
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
                $(".cart-list").text(data.totalitems);
                _vm.attr('disabled',false);
                console.log(data);
                
            }
        });
        // End
    });
    // End

    $('.coupon').on('click',function(){
        if ($('.coupon1').val() == "XMAS10"){
            if($('.invalid').text()== "Invalid Coupon" || $('.invalid').text("Please enter the coupon code!")){
                var totalAmount= $('.total-amount').text();
                console.log(totalAmount);
                totalAmount.replace('$','');
                console.log("after replace"+ totalAmount);
                totalAmount = parseInt(totalAmount);
                console.log("after parseInt"+ totalAmount);
                var discountedPrice= parseInt(0.9*totalAmount);
                price_after_discount=discountedPrice;
                console.log(discountedPrice);
                $('.invalid').text("Coupon Applied Successfully!!!");
                document.getElementById("coupon-result").style.color = "green";
                // myAjax();
                $('.total_price').text("$ "+discountedPrice);

                return false;
            }
            else{
            var totalAmount= $('.total-amount').text();
            console.log(totalAmount);
            totalAmount.replace('$','');
            console.log("after replace"+ totalAmount);
            totalAmount = parseInt(totalAmount);
            console.log("after parseInt"+ totalAmount);
            var discountedPrice= parseInt(0.9*totalAmount);
            price_after_discount=discountedPrice;
            console.log(discountedPrice);
            $('.invalid').text("Coupon Applied Successfully!!!");
            document.getElementById("coupon-result").style.color = "green";
            // myAjax();
            $('.total_price').text("$ "+discountedPrice);
            return false;
            }   
        }
            

        else if($('.coupon1').val() == "FIFA20"){
            if($('.invalid').text()== "Invalid Coupon" || $('.invalid').text("Please enter the coupon code!")){
                var totalAmount= $('.total-amount').text();
                console.log(totalAmount);
                totalAmount.replace('$','');
                console.log("after replace"+ totalAmount);
                totalAmount = parseInt(totalAmount);
                console.log("after parseInt"+ totalAmount);
                var discountedPrice= parseInt(0.8*totalAmount);
                price_after_discount=discountedPrice;
                console.log(discountedPrice);
                $('.invalid').text("Coupon Applied Successfully!!!");
                document.getElementById("coupon-result").style.color = "green";
                // myAjax();
                $('.total_price').text("$ "+discountedPrice);
                return false;
            }
            else{
                var totalAmount= $('.total-amount').text();
                console.log(totalAmount);
                totalAmount.replace('$','');
                console.log("after replace"+ totalAmount);
                totalAmount = parseInt(totalAmount);
                console.log("after parseInt"+ totalAmount);
                var discountedPrice= parseInt(0.8*totalAmount);
                price_after_discount=discountedPrice;
                console.log(discountedPrice);
                $('.total_price').text("$ "+discountedPrice);
                $('.invalid').text("Coupon Applied Successfully!!!");
                document.getElementById("coupon-result").style.color = "green";
                // myAjax();
                return false;
            }
        }
            
        else if($('.coupon1').val() == "BOX30"){
            if($('.invalid').text()== "Invalid Coupon" || $('.invalid').text("Please enter the coupon code!")){
                var totalAmount= $('.total-amount').text();
                console.log(totalAmount);
                totalAmount.replace('$','');
                console.log("after replace"+ totalAmount);
                totalAmount = parseInt(totalAmount);
                console.log("after parseInt"+ totalAmount);
                var discountedPrice= parseInt(0.7*totalAmount);
                price_after_discount=discountedPrice;
                console.log(discountedPrice);
                $('.total_price').text("$ "+discountedPrice);
                $('.invalid').text("Coupon Applied Successfully!!!");
                document.getElementById("coupon-result").style.color = "green";
                // myAjax();
                return false;
            }
            else{
                var totalAmount= $('.total-amount').text();
                console.log(totalAmount);
                totalAmount.replace('$','');
                console.log("after replace"+ totalAmount);
                totalAmount = parseInt(totalAmount);
                console.log("after parseInt"+ totalAmount);
                var discountedPrice= parseInt(0.7*totalAmount);
                price_after_discount=discountedPrice;
                console.log(discountedPrice);
                $('.total_price').text("$ "+discountedPrice);
                $('.invalid').text("Coupon Applied Successfully!!!");
                document.getElementById("coupon-result").style.color = "green";
                // myAjax();
                return false;
            }
        }
        else if($('.coupon1').val() == ""){
            $('.invalid').text("Please enter the coupon code!");
            document.getElementById("coupon-result").style.color = "yellow";
            var totalAmount= $('.total-amount').text();
            $('.total_price').text("$ "+totalAmount);
            return false;
        }
        else{
            $('.invalid').text("Invalid Coupon!");
            document.getElementById("coupon-result").style.color = "red";
            var totalAmount= $('.total-amount').text();
            $('.total_price').text("$ "+totalAmount);
            return false;
        }
        
    });

    //Delete item from cart
    // $('.delete-item').on('click', function(){
    //         console.log("inside delete item logic")
    //         var _pId = $(this).attr('data-item');
    //         console.log(_pId);
    // });

    $(document).on('click','.delete-item', function(){
        console.log("inside delete item logic")
        var _pId = $(this).attr('data-item');
        console.log(_pId);
        var _vm=$(this);

         // Ajax
         $.ajax({
            url:'/delete-from-cart',
            data:{
                'id':_pId,
            },
            dataType:'json',
            beforeSend:function(){
                _vm.attr('disabled',true);
            },
            success:function(res){
                $(".cart-list").text(res.totalitems);
                _vm.attr('disabled',false);
                console.log(res);
                $("#cartList").html(res.data);
                
            }
        });
    });

    $(document).on('click','.checkout-button', function(){
        console.log("inside checkout button logic")
        if($('.invalid').text()!="Coupon Applied Successfully!!!"){
            var temp_pad=$('.total-amount').text();
            console.log("temp_pad "+temp_pad)
            temp_pad.replace('$','');
            console.log("after replace"+ temp_pad);
            temp_pad = parseInt(temp_pad);
            console.log("after parseInt"+ temp_pad);
            price_after_discount= temp_pad;
            console.log("price after discount when no coupons applied"+ price_after_discount);
        }
        console.log("Ajax k andr price after discount "+ price_after_discount)
        $('.checkout-price').text(price_after_discount);
        console.log("Price after discount: "+ price_after_discount);

         // Ajax
         $.ajax({
            url:'/get_discounted_price',
            data:{
                'price_after_discount':price_after_discount,
            },
            dataType:'json',
            success:function(res){
                // $(".cart-list").text(res.totalitems);
                // _vm.attr('disabled',false);
                console.log("Ajax call successful"+res.data);
                // $("#cartList").html(res.data);
                
            }
        });
    });


});

