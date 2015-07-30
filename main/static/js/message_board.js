loadMessages()

function loadMessages() {
    $.ajax({
        url: '/all-messages/',
        success: function(result) {
            $('#all-messages').append(result);
        }
    })
}

$('#switch-to-create').click(function(e){
    e.preventDefault();

    $('#user-login-form').fadeOut(function(){
        $('#user-create-form').fadeIn()
    });
    
})

$('#switch-to-login').click(function(e){
    e.preventDefault();

    $('#user-create-form').fadeOut(function(){
        $('#user-login-form').fadeIn()
    });
    
})

$('#show-create-message').click(function(e){
    e.preventDefault();

    $('#new-message-form').fadeOut(function(){
        $('#create-message').fadeIn()
    });
    
})

$('#cancel-create-message').click(function(e){
    e.preventDefault();

    $('#create-message').fadeOut(function(){
        $('#new-message-form').fadeIn()
    });

    $('#message-form input[name="title"').val('')
    $('#message-form textarea[name="text"').val('')
    
})

$(function() {
    $('#content-box1').css('overflow', 'hidden').autogrow();
});
