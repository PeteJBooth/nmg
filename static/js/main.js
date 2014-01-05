$(document).ready(function() {
 
  $("#home-carousel").owlCarousel({
  	singleItem:true,
  });

  flashy_panels = $('.color-flash');

  function do_flashy_panels(){
  	//get new col width
		new_width = $(flashy_panels[0]).next().width();
		var new_styles = {
	      borderTopWidth : new_width,
	      borderRightWidth: new_width
	    };

		flashy_panels.css(new_styles);

		flashy_panels.each(function(){
			$(this).parent().height(new_width);
		});
  }

  $( window ).resize(function() {
  	do_flashy_panels();
  });
  do_flashy_panels();
 
});