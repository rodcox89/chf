
$('.delete_button').on('click', function(){

    var pid = $(this).attr('data-pid');
    var product_boolean = $(this).attr('data-productbool')
    event.preventDefault();

    $.loadmodal({
        url: "/shop/shopping_cart.delete/" + pid + "/"+ product_boolean + "/",
        title: 'Your Cart',
        width: '800px',
        closeButton: false,

    });

});



$('.show_login_dialog').on('click', function(){
    event.preventDefault();
    console.log('load modal worked  ');

    $.loadmodal('/shop/index.loginform/')



});
