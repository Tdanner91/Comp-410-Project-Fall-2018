$(document).ready(function() {

    $('form').on('submit', function(event) {

        $.ajax({
                data: {
                    test_code_js: $('#test-code').val()
                },
                type: 'POST',
                url: '/process'
            })
            .done(function(data) {

                if (data.test_code_returned == 'TestFail' || data.test_code_returned == 'TestAborted') {
                    $('#errorAlert').text(data.test_code_returned).show();
                    $('#successAlert').hide();
                } else {
                    $('#successAlert').text(data.test_code_returned).show();
                    $('#errorAlert').hide();
                }

            });

        event.preventDefault();

    });

});