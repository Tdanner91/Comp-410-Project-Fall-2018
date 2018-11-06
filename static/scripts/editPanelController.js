$(document).ready(function () {

    $('.editPanelOptionButton').on('click', function (event) {

        switch ($(this).text().trim()) {
            case 'Print':
                // window.alert('test');
                break;
            case 'Load':
                $('.advanced-edit-panel-options').empty();
                break;
            case 'Add':
                $('.advanced-edit-panel-options').empty();
                $('.advanced-edit-panel-options').append('<div class="form-group"><label for="scriptName"></label><input type="text" class="form-control add-input" id="scriptName" placeholder="Script Name"></div>');
                $('.advanced-edit-panel-options').append('<form><div class="form-group add-file"><label for="scriptSelection"></label><input type="file" class="form-control-file" id="scriptSelection"></div></form>');
                $('.advanced-edit-panel-options').append('<input class="btn btn-dark add-submit" type="submit" value="Submit">');
                loadAddButtonControllers();
                break;
            case 'Delete':
                $('.advanced-edit-panel-options').empty();
                break;
            case 'Edit':
                $('.advanced-edit-panel-options').empty();
                break;
            case 'Save':
                $('.advanced-edit-panel-options').empty();
                break;
            case 'Run':
                $('.advanced-edit-panel-options').empty();
                break;
        }

    });

});

function loadAddButtonControllers() {
    // This function attaches a click event after the button has been added to the DOM
    function loadSubmitController (script, scriptname){

        $('.add-submit').on('click', function (event) {
            let scriptName = $('#scriptName').val().trim();
            let scriptLocation = $('#scriptSelection').val().trim();

            $.ajax({
                data: {
                    _script: script,
                    _scriptName: scriptName
                },
                type: 'POST',
                url: '/userGeneratedScriptUploading'
            })
                .done(function (data) {
                    $('.right-panel-list').append(' <a href="#" class="list-group-item list-group-item-action">' + data.name + '</a>');

                });
        });
    }

    $('#scriptSelection').on('change', function (event) {
        let file = event.target.files;
        let reader = new FileReader();

        reader.onload = function (event) {
            let script = event.target.result;
            let scriptName = $('#scriptSelection').val().trim();
            
            loadSubmitController(script, scriptName);

        }
        reader.readAsText(file[0]);
        
    });
}

