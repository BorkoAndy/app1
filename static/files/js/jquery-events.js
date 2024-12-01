// Html ready
$(document).ready(function () {
    // Getting django-message by id
    var notification = $('#notification');
    // Closing in 5 sec
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 3000);
    }

    // Clicking on cart icon calling modal window
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Clicking on close button closes cart window
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Event with radio button for delivery
    $("input[name='requires_delivery']").change(function() {
        var selectedValue = $(this).val();
        // Show/hide delivery adress
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

});