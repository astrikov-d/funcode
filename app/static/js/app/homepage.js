$(function () {
    var form = $('#id_form');
    form.ajaxForm({
        dataType: 'json',
        beforeSubmit: function () {
            $('.errors, .error-container', form).remove();
        },
        success: function (response) {
            if (response.result == 'success') {

            } else {
                for (var index in response.errors) {
                    if (response.errors.hasOwnProperty(index)) {
                        var error_list = '<div class="errors">';
                        for (var err in response.errors[index]) {
                            error_list += '<p class="text-danger">' + response.errors[index][err] + '</p>';
                        }
                        error_list += '</div>';

                        if (index == '__all__') {
                            form.prepend('<div class="alert alert-danger error-container">' + error_list + '</div>');
                        } else {
                            $('#id_' + index).after(error_list);
                        }
                    }
                }
            }
        }
    })
});