$(document).ready(function() {

    $('.selectionPanelButton').on('click', function(event) {
        repoName = ''
        switch ($(this).text().trim()) {
            case 'Devices':
                db = 'device_repository';
                break;
            case 'Test Cases':
                db = 'test_case_repository';
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
                for (let i = 0; i < data.length; i++) {
                    $('.right-panel-list').append(' <a href="#" class="list-group-item list-group-item-action">' + data[i] + '</a>');
                }

            })

        event.preventDefault();

    });

});