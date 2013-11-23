$(function () {

    var time = 5000;

    function rotate() {

        var slide = $('.slider__i'),
            slideAct = $('.slider__i.active');
        if (slideAct.next().length) {
            slideAct.next().css('left', 1000).animate({left: 0}).end().animate({left: -1000}, function () {
                $('.slider__i.active').next().addClass("active").end().removeClass("active")
            });
        }
        else {
            slide.eq(0).css('left', 1000).animate({left: 0});
            slideAct.animate({left: -1000}, function () {
                slideAct.removeClass("active");
                slide.eq(0).addClass("active");

            });
        }

    }

    play = setInterval(rotate, time);


    $(".slider__next").click(function () {
        var slide = $('.slider__i'),
            slideAct = $('.slider__i.active');
        if (!slide.is(':animated')) {
            clearInterval(play);
            rotate();
            play = setInterval(rotate, time);

        }
    });
    $(".slider__prev").click(function () {
        var slide = $('.slider__i'),
            slideAct = $('.slider__i.active'),
            index = slideAct.index();
        if (!slide.is(':animated')) {
            clearInterval(play);
            if (slideAct.prev().length) {
                slideAct.prev().animate({left: 0}).end().animate({left: 1000}, function () {
                    $('.slider__i.active').prev().addClass("active").end().css('left', -1000).removeClass("active")
                });
            }
            else {
                slide.eq(-1).animate({left: 0});
                slideAct.animate({left: 1000}, function () {
                    slideAct.css('left', -1000).removeClass("active");
                    slide.eq(-1).addClass("active");

                });
            }
            play = setInterval(rotate, time);
        }

    });
    $(".footer__slider__next").click(function () {
        var slider = $(".footer__slider__container"),
            slide = $('.footer__slider__i'),
            slideWidth = slide.width();
        if (!slider.is(":animated")) {

            slider.animate({
                left: '-=115'
            }, function () {
                $(".footer__slider__i").eq(0).clone(true).appendTo(slider);
                $(".footer__slider__i").eq(0).remove();
                slider.css('left', '+=115')
            })
        }

    });
    $(".footer__slider__prev").click(function () {
        var slider = $(".footer__slider__container"),
            slide = $('.footer__slider__i'),
            slideWidth = slide.width();
        if (!slider.is(":animated")) {
            slider.animate({
                left: '+=115'
            }, function () {
                $(".footer__slider__i").eq(-1).clone(true).prependTo(slider);
                $(".footer__slider__i").eq(-1).remove();
                slider.css('left', '-=115')
            })

        }
    });
    $(".popup__layout, .popup___close").click(function () {
        $('.popup__layout').fadeOut();
        $(".popup").fadeOut(500);
    });
    $("#sign").click(function () {
        $('.popup__layout').fadeIn();
        $(".popup-sign").fadeIn(500);
    });
    $("#get").click(function () {
        $('.popup__layout').fadeIn();
        $(".popup-get").fadeIn(500);
    });
    $(document).ready(function () {
        $(".gallery").each(function (index, v) {
            $(this).find('.gallery__item').colorbox({rel: 'gallery' + index });
        });
        
        $(".footer__slider__container").each(function (index, v) {
            $(this).find('.slider_item').colorbox();
        });
        
        $(".slider_video").colorbox({html: '<iframe width="560" height="315" src="//www.youtube.com/embed/lTPN-3YPx-w?rel=0" frameborder="0" allowfullscreen></iframe>', width: '630px', height: '400px'});

    });
    $(".sidebar__nav").find("li a").click(function(){
        $(".sidebar__nav").find("li a").removeClass("active");
         $(this).addClass("active");
    });
    $(".g-nav").find("li a").click(function(){
       var index =  $(this).parent().index();
        $(".g-nav").find("li a").removeClass("active");
        $(".g-nav").find("li").removeClass("active");
        $(this).addClass("active");
        $(this).parent().addClass("active");
        $(".sidebar__nav").find("li a").removeClass("active");
        $(".sidebar__nav").find("li").eq(index).find("a").addClass("active");
    });
});
