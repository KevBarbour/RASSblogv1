$(document).ready(function() {
jQuery(document).ready(function() {
    jQuery('.toggle-nav').click(function(e) {
        jQuery(this).toggleClass('active1');
        jQuery('.menu ul').toggleClass('active1');

        e.preventDefault();
    });
});
        // JQuery code to be added in here.
});



/*

try when fix the button it dissapears the list


jQuery('.toggle-nav, .menu a').click(function(e) {
    jQuery('.toggle-nav').toggleClass('active');
    jQuery('.menu ul').toggleClass('active');
e.preventDefault(); });*/
