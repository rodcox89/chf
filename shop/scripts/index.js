$(function() {


    $('#show_login_dialog').on('click', function(){
        $.loadmodal({

            url: '/shop/index.loginform/',
            title: 'Login Please:',
            width: '600px',
            });

    });//click




});
