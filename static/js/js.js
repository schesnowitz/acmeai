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


function showDiv() {
    document.getElementById('Login').style.display = "none";
    document.getElementById('loadingGif').style.display = "block";
    setTimeout(function() {
      document.getElementById('loadingGif').style.display = "none";
      document.getElementById('showme').style.display = "block";
    },2000);
     
  }