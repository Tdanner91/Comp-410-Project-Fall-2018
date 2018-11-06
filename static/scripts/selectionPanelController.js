$(document).ready(function () {

    $('.selectionPanelButton').on('click', function (event) {

        switch ($(this).text().trim()) {
            case 'Devices':
                $.ajax({
                    data: {
                        repository: 'device_repository'
                    },
                    type: 'POST',
                    url: '/selectionPanelResponse'
                })
                    .done(function (data) {
                        $('.right-panel-list').empty();

                        for (var i = 0; i < data.length; i++) {
                            $('.right-panel-list').append(' <a href="#" class="list-group-item list-group-item-action">' + data[i] + '</a>');
                        }
                    });

                event.preventDefault();
                break;
            case 'Test Cases':
                $.ajax({
                    data: {
                        repository: 'test_case_repository'
                    },
                    type: 'POST',
                    url: '/selectionPanelResponse'
                })
                    .done(function (data) {
                        $('.right-panel-list').empty();

                        for (var i = 0; i < data.length; i++) {
                            $('.right-panel-list').append(' <a href="#" class="list-group-item list-group-item-action">' + data[i] + '</a>');
                        }
                    });

                event.preventDefault();
                break;
            case 'Saved Results':
                $('.right-panel-list').empty();
                window.alert('Not Implemented')
        }
    });
});