$(document).ready(function() {

    $('.selectionPanelButton').on('click', function(event) {
        repoName = '';
        switch ($(this).text().trim()) {
            case 'Devices':
                repoName = 'device_repository';
                break;
            case 'Test Cases':
                repoName = 'test_case_repository';
                break;
        }


        $.ajax({
                data: {
                    repository: repoName
                },
                type: 'POST',
                url: '/selectionPanelResponse'
            })
            .done(function(data) {
                $('.right-panel-list').empty();

                for (var i = 0; i < data.length; i++) {
                    $('.right-panel-list').append(' <a href="#" class="list-group-item list-group-item-action">' + data[i] + '</a>');
                }

            });

        event.preventDefault();

    });

});