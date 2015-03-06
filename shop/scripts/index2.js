$(function() {

    $('.add_button').on('click', function(){
        console.log($('this'));

        var iid = $(this).attr('data-iid');
        var qty = 1;
        console.log(iid);

        $.loadmodal({
            url: "/shop/shopping_cart.add/"+ iid + "/" + qty,

        });

    });






});

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
