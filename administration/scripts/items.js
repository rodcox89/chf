$(function() {
    $('.return').on('click', function() {
        event.preventDefault();
        console.log('items.js');
        var rid = $(this).attr('data-rid');
        $.loadmodal({
            url: "/administration/items.return_rental/" + rid,
            title: "Rental Return",
            width: "50%",
            onShow: function() {
                // $('.was_returned').bootstrapSwitch({
                //     // 'size':'small',
                //     // 'onColor': 'success',
                //     // 'onText': 'Returned',
                //     // 'offText': 'Out',
                // });
                // $('.fee').parent().addClass('col-md-2');
            },

        });
    });
    $('#return-form').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);
    });

    $('.btn-email').on('click', function() {
        var email = $(this).attr('data-batch');
        $.ajax({
            url: '/administration/items.sendmail/' + email,
            success: function(data) {
                console.log("Email Sent");
            },

        });
    });
});
