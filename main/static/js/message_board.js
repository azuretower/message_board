loadMessages()

function loadMessages() {
    $.ajax({
        url: '/all-messages/',
        success: function(result) {
            $('#all-messages').append(result);
        }
    })
}