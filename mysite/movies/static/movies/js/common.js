$(document).ready(function(){
  	 $('.nav-area .ic-menu').click(function(){
        $('.nav-area .ic-menu').toggleClass('active');
        $('.nav-area .menu-area').toggleClass('active');
     });

     $('.main-slider').lightSlider({
        gallery:true,
        item:1,
        thumbItem:5,
        slideMargin: 0,
        speed:500,
        auto:true,
        loop:true
    });
    $('.metiz-films').lightSlider({
        item:8,
        rtl:true
  });
    if (Modernizr.touch) {
      // handle the adding of hover class when clicked
      $(".lslide").click(function(e){
          if (!$(this).hasClass("hover")) {
            $(this).addClass("hover");
          }
      });
  } else {
      // handle the mouseenter functionality
      $(".lslide").mouseenter(function(){
          $(this).addClass("hover");
      })
      // handle the mouseleave functionality
      .mouseleave(function(){
          $(this).removeClass("hover");
      });
  }
  
    $('#datetimepicker').datetimepicker({
      format: 'yyyy-mm-dd',
      pickTime: false,
  });
});
