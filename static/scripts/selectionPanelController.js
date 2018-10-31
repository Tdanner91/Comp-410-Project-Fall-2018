$(document).ready(function() {

    $('.selectionPanelButton').on('click', function(event) {
        db = "";
        switch ($(this).text().trim()) {
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

        // console.log('FROM JS CONTROLLER: db = ' + db);

        $.ajax({
                data: {
                    database: db
                },
                type: 'POST',
                url: '/databaseFunctions'
            })
            .done(function(data) {
                $('.right-panel-list').empty();
                for (let i = 0; i < data.length; i++) {
                    $(".right-panel-list").append(' <a href="#" class="list-group-item list-group-item-action">' + data[i] + '</a>');
                }

            })

        event.preventDefault();

    });

});