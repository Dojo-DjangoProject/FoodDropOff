
$(".rightpane").height($(".container").height()-$(".header").height());

$(window).on('resize',function(){
    $(".rightpane").height($(".container").height()-$(".header").height());
});

$(".main").on('click', '.ajax-message', function() {
    $(".leftpane").animate({
        width: '73%'
    }, 0);
    $(".rightpane").animate({
        width: '25%'
    }, 0);
    $(".message-header").html("Message John<span><a href='#' class='close-message'>Close</a></span>");
    $(".message-content").html("Message Content Here");
    $(".message-footer").html("<textarea name='message' id='message' rows='2'></textarea>")
});
$(".main").on('click', '.close-message', function() {
    $(".message-header").html("");
    $(".message-content").html("");
    $(".message-footer").html("")    
    $(".leftpane").animate({
        width: '100%'
    }, 0);
    $(".rightpane").animate({
        width: '0%'
    }, 0);
    
});