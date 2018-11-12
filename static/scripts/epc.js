$(document).ready(function () {

   

});


function AddEditPanelOptions() {
    $('.editPanelView').append('<div class="form-group"><label for="scriptName"></label><input type="text" class="form-control add-input" id="scriptName" placeholder="Script Name"></div>');
    $('.editPanelView').append('<form><div class="form-group add-file"><label for="scriptSelection"></label><input type="file" class="form-control-file" id="scriptSelection"></div></form>');
    $('.editPanelView').append('<input class="btn btn-dark add-submit" type="submit" value="Submit">');
}


///////////////////////////////////////////////////////////////////////////////////////
//Add Panel Button Handlers
///////////////////////////////////////////////////////////////////////////////////////
function AddScriptToRepo() {

    function loadSubmitController(script, scriptname) {

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

