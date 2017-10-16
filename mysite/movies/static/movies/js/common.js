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
  //Login and register
  $('.metiz-form').find('input').on('keyup blur focus', function(e) {
      label = $(this).prev('label');
      if (e.type === 'keyup') {
        if ($(this).val() === '' ) {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
      } else if (e.type === 'blur') {
        if ($(this).val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
      } else if (e.type === 'focus') {
        if ($(this).val() === '') {
          label.removeClass('highlight');
        } else if ($(this).val() !== '') {
          label.addClass('highlight');
        }
      }
  });
    $('#datetimepicker').datetimepicker({
      format: 'yyyy-mm-dd',
      pickTime: false,
  });
});
