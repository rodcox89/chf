$(function() {

    $('#change_password_form').ajaxForm(function(data) {
        console.log('account.changepassword.js ran');
        $('#jquery-loadmodal-js-body').html(data);

    });


});
