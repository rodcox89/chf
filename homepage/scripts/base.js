$(function() {


    $('#show_login_dialog').on('click', function(){
        event.preventDefault();


        $.loadmodal('/shop/index.loginform/')



    });

    $('#loginform').ajaxForm(function(data){

        $('#jquery-loadmodal-js-body').html(data);

    });





});
