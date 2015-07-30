loadMessages()

function loadMessages() {
    $.ajax({
        url: '/all-messages/',
        success: function(result) {
            $('#all-messages').append(result);
        }
    })
}

$('#all-messages').on('click', '.delete-message-link', function(e){
    e.preventDefault();
    var id = $(this).parents('.message').attr('data-message-id');
    var trash = $(this).children('.glyphicon')

    if (trash.hasClass('glyphicon')){
        if (confirm('Are you sure you want to delete this post?')) {
            $.ajax({
                url: '/message/' + id + '/',
                method: 'DELETE',
                beforeSend: function(xhr){
                    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
                },
                success: function() {
                    $('[data-message-id="' + id + '"]').remove();
                    // var current_id = $('#post_form input[name="id"').val();
                }
            })
        }
    }
})


function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}


/***** FAVORITE TOGGLE *****/
$('#all-messages').on('click', '.favorite-message-link', function(e){
    e.preventDefault();
    var id = $(this).parents('.message').attr('data-message-id');
    var star = $(this).children('.glyphicon')
    
    if (star.hasClass('glyphicon-star-empty')){
        star.addClass('glyphicon-star').removeClass('glyphicon-star-empty')
    }else if (star.hasClass('glyphicon-star')){
        star.addClass('glyphicon-star-empty').removeClass('glyphicon-star')
    }
})


/***** ANIMATION FOR LOGIN PAGE *****/
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


/***** ANIMATION FOR NEW POST ON FRONT PAGE *****/
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


/***** ANIMATION FOR GROWING THE TEXTBOX *****/
$(function() {
    $('#content-box1').css('overflow', 'hidden').autogrow();
});
