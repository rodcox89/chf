$(function() {

    $('#show_login_dialog').on('click', function(){
        event.preventDefault();
        console.log('load modal worked  ');

        $.loadmodal('/shop/index.loginform/')



    });

    $('#loginform').ajaxForm(function(data){
        event.preventDefault();

        console.log('jquery-loadmodal-js-body worked');
        $('#jquery-loadmodal-js-body').html(data);

    });

    $('.add_button').on('click', function(){

        var iid = $(this).attr('data-iid');
        var qty = $('#quantity').val();

        if(! qty){
            qty = 1;
        }

        $.loadmodal({
            url: "/shop/shopping_cart.add/"+ iid + "/" + qty,

        });

    });


    $('#search_button').click(function(){

        var input = $("#search_input").val()


        var options = {

            data:{
                'input': input,
            },

            success: function(data) {
                console.log('it was a success');
                $('#item-loop').html(data);

            }

        }

        $('#search_go').ajaxForm(options);

    });


    $('#cart').click(function(){
        event.preventDefault();
        $.loadmodal({
                url: "/shop/shopping_cart",
        });
    })
});
