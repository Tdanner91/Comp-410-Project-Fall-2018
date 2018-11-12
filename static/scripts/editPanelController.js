$(document).ready(function () {
    
        $('.editPanelOptionButton').on('click', function (event) {
            buttonText = $(this).text().trim();
            window.alert(buttonText);
            switch (buttonText) {
                case 'Print':
                    // window.alert('test');
                    break;
                case 'Load':
                    $('.advanced-edit-panel-options').empty();
                    break;
                case 'Add Script to Repo':
                    $('.editPanelView').empty();
                    $('.editPanelView').append('<div class="form-group"><label for="scriptName"></label><input type="text" class="form-control add-input" id="scriptName" placeholder="Script Name"></div>');
                    $('.editPanelView').append('<form><div class="form-group add-file"><label for="scriptSelection"></label><input type="file" class="form-control-file" id="scriptSelection"></div></form>');
                    $('.editPanelView').append('<input class="btn btn-dark add-submit" type="submit" value="Submit">');
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

