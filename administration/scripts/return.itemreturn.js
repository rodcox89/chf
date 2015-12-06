$(function() {
    $('.return').on('click', function() {
        console.log('clicked')
        event.preventDefault();
        var rid = $(this).attr('data-rid');
        $.loadmodal({
            url: "/administration/items.rental/" + rid,
            title: "Rental Return",
            width: "50%",
            onShow: function() {
                $('.was_returned').bootstrapSwitch({
                    'size':'small',
                    'onColor': 'success',
                    'onText': 'Returned',
                    'offText': 'Out',
                });
                $('.fee').parent().addClass('col-md-2');
            },

        });
    });
    $('#return-form').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);
    });

});
