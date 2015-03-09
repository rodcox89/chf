$(function() {

    $('.edit_user').on('click', function(){
        event.preventDefault();
        $.loadmodal({
            url: "/shop/account.edit/",

        });

    });



    $('#edit_user_form').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);

    });

    $('.change_password').on('click', function(){
        event.preventDefault();
        $.loadmodal({
            url: "/shop/account.changepassword/",

        });

    });

    $('#change_password_form').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);

    });








});
