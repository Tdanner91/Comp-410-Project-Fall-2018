$(document).ready(function () {

    $('form').on('submit', function (event) {

        $.ajax({
            data: {
                num1: $('#num1').val(),
                num2: $('#num2').val(),
            },
            type: 'POST',
            url: '/process'
        })
            .done(function (data) {

                if (data.error) {
                    $('#errorAlert').text(data.error).show();
                    $('#successAlert').hide();
                }
                else {
                    $('#successAlert').text(data.sum).show();
                    $('#errorAlert').hide();
                }

            });

        event.preventDefault();

    });

});