$(function() {


    $('#show_login_dialog').on('click', function(){
        $.loadmodal({

            url: '/shop/index.loginform/',
            title: 'Login Please:',
            width: '600px',
            });

    });//click
/* -------------------------- video 2 -------------------------- */
    // console.log($("A:this one is working"))
    // // bind 'myForm' and provide a simple callback function
    // ---('#loginform').ajaxForm(function(data) {
    //     console.log(data);
    //     $('#loginform_container').html(data);
    // })




/* -------------------------- video 1 -------------------------- */
    // ('#id_username').on('change' , function () {
    // console.log('change');
    //
    // var username = $('#id_username').val();
    //
    // console.log(username);
    //
    // .ajax({
    //     url: '/shop/index.check_username/',
    //     data:{
    //         'username': username,
    //     },
    //     success: function(resp){
    //     if (resp == 'good' ){
    //         $('#username_message').text('Check mark');
    //     }
    //     else{
    //         $('#username_message').text('Try another username');
    //     }
    //     },//success
    // });
    //
    // });



});
