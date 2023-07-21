$(function(){
    if ($('#ms-menu-trigger')[0]) {
         $('body').on('click', '#ms-menu-trigger', function() {
             $('.ms-menu').toggleClass('toggled'); 
         });
     }
 });


 $(document).ready(function () {
    // Handler for .ready() called.
    $('html, body').animate({
        scrollTop: $('#what').offset().top
    }, 'slow');
});