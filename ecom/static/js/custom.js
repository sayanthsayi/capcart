$(document).ready(function () {
    $('.increment').click(function (e) { 
        e.preventDefault();

        let value = $('.prod_qty').val()
        
        if (value<10){
            value++
            $('.prod_qty').val(value)
        }
        console.log(value)
        
    });

    $('.decrement').click(function (e) { 
        e.preventDefault();

        let value =$('.prod_qty').val()

        if(value>1){
            value--

            $('.prod_qty').val(value)

            console.log(value)
        }
    });

    $('.cart_btn').click(function (e) { 
        e.preventDefault();

        let id =$('.prod_id').val()

        let qty = $('.prod_qty').val()
        let token = $('input[name=csrfmiddlewaretoken]').val()

        $.ajax({
            type: "POST",
            url: "/cart/AddToCart/",
            data: {
                'id':id,
                'qty':qty,
                csrfmiddlewaretoken :token

            },
            dataType: "json",
            success: function (response) {
                alert(response.status)
            }
        }); 
    });
    $('.wishlist_btn').click(function (e) { 
        e.preventDefault();

        let id =$('.prod_id').val()
        let token = $('input[name=csrfmiddlewaretoken]').val()

        $.ajax({
            type: "POST",
            url: "/cart/AddToishlist/",
            data: {
                'id':id,
                csrfmiddlewaretoken :token
            },
            dataType: "json",
            success: function (response) {
                alert(response.status)
            }
        }); 
    });

});

