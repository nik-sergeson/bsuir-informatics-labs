
$(document).ready(function () {
    function disableSubmitButton() {
        $(this).find(":submit").prop('disabled', true);
    }

    $('.proposal-form').submit(disableSubmitButton);
    $('.request-form').submit(disableSubmitButton);
})