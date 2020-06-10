
/*hide show
html:
<button id="hide">Hide</button>
<button id="show">Show</button>


       $(document).ready(function(){
  $("#hide").click(function(){
    $(".menu").hide();
  });
  $("#show").click(function(){
    $(".menu").show();
  });
});
*/

/*toggle v2
$(document).ready(function(){
    $(".menu").hide();
    });
*/

$(document).ready(function(){

/*hides toggle menu when resized */
var resizeTimer;
$(window).on('resize', function (e) {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
        if ($(window).width() > 860) {
            $('.menu').show();
        } else {
            $('.menu').hide();
        }
    }, 250);
});

  $(".toggle-nav").click(function(){
      $(".menu").toggle();

  });
});