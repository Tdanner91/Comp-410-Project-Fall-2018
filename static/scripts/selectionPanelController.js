$(document).ready(function () {

    $('.selectionPanelButton').on('click', function (event) {

        db = "";
        switch ($(this).val()) {
            case "Devices":
                db = "DUTdummybase";
                break;
            case "Test Cases":
                db = "Testdummybase";
                break;
            case "Saved Results":
                db = "Resultsdummybase";
                break;
        }

        $.ajax({
            data: {
                database: db
            },
            type: 'POST',
            url: '/databaseFunctions'
        })
            .done(function (data) {
                $(".right-panel-list").append(' <a href="#" class="list-group-item list-group-item-action">' + data.value + '</a>');
            })

        event.preventDefault();

    });

});