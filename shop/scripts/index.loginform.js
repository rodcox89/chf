$(function() {
    $('#loginform').ajaxForm(function(data){
        event.preventDefault();

        $('#jquery-loadmodal-js-body').html(data);
    });


    $('.show_login_dialog').on('click', function(){
        event.preventDefault();

        $.loadmodal('/shop/index.loginform/')



    });


    });
