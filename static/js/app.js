$(document).ready(function(){

    if ($(".overlay").length >0) {
        $('body,html').addClass("hidden-overflow")
    }
    $(".overlay-close").on("click", function(){
        $(".overlay").addClass("closed")
        $('body,html').removeClass("hidden-overflow")
    })


})