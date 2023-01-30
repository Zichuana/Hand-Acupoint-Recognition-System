(function($) {

	"use strict";

    $('.select').niceSelect();


    document.getElementById('change-theme-btn').addEventListener('click', function () {
        let darkThemeEnabled = document.body.classList.toggle('light-theme');
        localStorage.setItem('light-theme-enabled', darkThemeEnabled);
    });

    if (JSON.parse(localStorage.getItem('light-theme-enabled'))) {
        document.body.classList.add('light-theme');
    }



    /*------------------------------------------
        = ALL ESSENTIAL FUNCTIONS
    -------------------------------------------*/

    // Toggle mobile navigation
    function toggleMobileNavigation() {
        var navbar = $(".navigation-holder");
        var openBtn = $(".navbar-header .open-btn");
        var closeBtn = $(".navigation-holder .close-navbar");
        var body = $(".page-wrapper");

        openBtn.on("click", function() {
            if (!navbar.hasClass("slideInn")) {
                navbar.addClass("slideInn");
                body.addClass("body-overlay");
            }
            return false;
        })

        closeBtn.on("click", function() {
            if (navbar.hasClass("slideInn")) {
                navbar.removeClass("slideInn");
            }
            body.removeClass("body-overlay");
            return false;
        })
    }

    toggleMobileNavigation();


    // Function for toggle class for small menu
    function toggleClassForSmallNav() {
        var windowWidth = window.innerWidth;
        var mainNav = $("#navbar > ul");

        if (windowWidth <= 991) {
            mainNav.addClass("small-nav");
        } else {
            mainNav.removeClass("small-nav");
        }
    }

    toggleClassForSmallNav();


    // Function for small menu
    function smallNavFunctionality() {
        var windowWidth = window.innerWidth;
        var mainNav = $(".navigation-holder");
        var smallNav = $(".navigation-holder > .small-nav");
        var subMenu = smallNav.find(".sub-menu");
        var megamenu = smallNav.find(".mega-menu");
        var menuItemWidthSubMenu = smallNav.find(".menu-item-has-children > a");

        if (windowWidth <= 991) {
            subMenu.hide();
            megamenu.hide();
            menuItemWidthSubMenu.on("click", function(e) {
                var $this = $(this);
                $this.siblings().slideToggle();
                 e.preventDefault();
                e.stopImmediatePropagation();
            })
        } else if (windowWidth > 991) {
            mainNav.find(".sub-menu").show();
            mainNav.find(".mega-menu").show();
        }
    }

    smallNavFunctionality();


   // Parallax background
    function bgParallax() {
        if ($(".parallax").length) {
            $(".parallax").each(function() {
                var height = $(this).position().top;
                var resize     = height - $(window).scrollTop();
                var doParallax = -(resize/5);
                var positionValue   = doParallax + "px";
                var img = $(this).data("bg-image");

                $(this).css({
                    backgroundImage: "url(" + img + ")",
                    backgroundPosition: "50%" + positionValue,
                    backgroundSize: "cover"
                });
            });
        }
    }


    // Hero slider background setting
    function sliderBgSetting() {
        if ($(".hero-slider .slide").length) {
            $(".hero-slider .slide").each(function() {
                var $this = $(this);
                var img = ($this.find(".slider-bg").attr("src")) ? $this.find(".slider-bg").attr("src") : false;

                if(img) {
                    $this.css({
                        backgroundImage: "url("+ img +")",
                        backgroundSize: "cover",
                        backgroundPosition: "center center"
                    })
                }
            });
        }
    }


    //Setting hero slider
    function heroSlider() {
        if ($(".hero-slider").length) {
            $(".hero-slider").slick({
                arrows: true,
                prevArrow: '<button type="button" class="slick-prev">Previous</button>',
                nextArrow: '<button type="button" class="slick-next">Next</button>',
                dots: true,
                fade: true,
                cssEase: 'linear',
            });
        }
    }

    

/*------------------------------------------
    TweenMax Initialize  // quick ball gsap
    -------------------------------------------*/
  function initGsapParallax() {
    const mouse = { x: 0, y: 0 };
    const pos = { x: 0, y: 0 };
    const ratio = 0.65;
    let active = false;
    const ball = document.getElementById('ball');

    gsap.set(ball, {
      xPercent: -50, yPercent: -50, scale: 0.5, borderWidth: '4px',
    });

    document.addEventListener('mousemove', mouseMove);

    function mouseMove(e) {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      mouse.x = e.pageX;
      mouse.y = e.pageY - scrollTop;
    }

    gsap.ticker.add(updatePosition);

    function updatePosition() {
      if (!active) {
        pos.x += (mouse.x - pos.x) * ratio;
        pos.y += (mouse.y - pos.y) * ratio;

        gsap.to(ball, { duration: 0.4, x: pos.x, y: pos.y });
      }
    }

    $('.theme-btn,.theme-btn-s2, #change-theme-btn, .bigCursor').mouseenter((e) => {
      gsap.to(ball, {
        duration: 0.3, scale: 3, backgroundColor: 'rgb(246 125 74 / 80%)', borderColor: 'transparent', opacity: 0.1,
      });
    });

    $('.theme-btn,.theme-btn-s2, #change-theme-btn, .bigCursor').mouseleave((e) => {
      gsap.to(ball, {
        duration: 0.3, scale: 0.5, backgroundColor: 'transparent', borderColor: '#999999', opacity: 1,
      });
    });

    $('.slick-arrow,.flaticon-play-button, .bigCursor').mouseenter((e) => {
      gsap.to(ball, {
        duration: 0.3, scale: 3, backgroundColor: 'rgb(246 125 74 / 80%)', borderColor: 'transparent', opacity: 0.1,
      });
    });

    $('.slick-arrow,.flaticon-play-button, .bigCursor').mouseleave((e) => {
      gsap.to(ball, {
        duration: 0.3, scale: 0.5, backgroundColor: 'transparent', borderColor: '#999999', opacity: 1,
      });
    });

    // product-img
    $('.product-img').mouseenter((e) => {
      gsap.to(ball, {
        duration: 0.3, scale: 0.3, backgroundColor: '#000', borderColor: 'transparent', opacity: 0.3,
      });
    });

    $('.product-img').mouseleave((e) => {
      gsap.to(ball, {
        duration: 0.3, scale: 0.5, backgroundColor: 'transparent', borderColor: '#999999', opacity: 1,
      });
    });

    // parallax wrap
    $('.parallax-wrap').mouseenter(function (e) {
      gsap.to(this, { duration: 0.3, scale: 2 });
      gsap.to(ball, {
        duration: 0.3, scale: 0.9, borderWidth: '2px', opacity: 1,
      });
      gsap.to($(this).children(), { duration: 0.3, scale: 0.5 });
      active = true;
    });

    $('.parallax-wrap').mouseleave(function (e) {
      gsap.to(this, { duration: 0.3, scale: 1 });
      gsap.to(ball, {
        duration: 0.3, scale: 0.5, borderWidth: '4px', opacity: 1, borderColor: '#999999',
      });
      gsap.to($(this).children(), {
        duration: 0.3, scale: 1, x: 0, y: 0,
      });
      active = false;
    });

    $('.parallax-wrap').mousemove(function (e) {
      parallaxCursor(e, this, 2);
      callParallax(e, this);
    });

    function callParallax(e, parent) {
      parallaxIt(e, parent, parent.querySelector('.parallax-element'), 20);
    }

    function parallaxIt(e, parent, target, movement) {
      const boundingRect = parent.getBoundingClientRect();
      const relX = e.pageX - boundingRect.left;
      const relY = e.pageY - boundingRect.top;
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

      gsap.to(target, {
        duration: 0.3,
        x: (relX - boundingRect.width / 2) / boundingRect.width * movement,
        y: (relY - boundingRect.height / 2 - scrollTop) / boundingRect.height * movement,
        ease: Power2.easeOut,
      });
    }

    function parallaxCursor(e, parent, movement) {
      const rect = parent.getBoundingClientRect();
      const relX = e.pageX - rect.left;
      const relY = e.pageY - rect.top;
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      pos.x = rect.left + rect.width / 2 + (relX - rect.width / 2) / movement;
      pos.y = rect.top + rect.height / 2 + (relY - rect.height / 2 - scrollTop) / movement;
      gsap.to(ball, { duration: 0.3, x: pos.x, y: pos.y });
    }
  }



    //Active heor slider
    heroSlider();


    $('.tp-payment-select .addToggle').on('click', function(){
    $('.payment-name').addClass('active')
    $('.tp-payment-option').removeClass('active')
    })


    $('.tp-payment-select .removeToggle').on('click', function(){
        $('.tp-payment-option').addClass('active')
        $('.payment-name').removeClass('active')
    });


    /*------------------------------------------
    = HIDE PRELOADER
    -------------------------------------------*/
    function preloader() {
        if($('.preloader').length) {
            $('.preloader').delay(100).fadeOut(500, function() {

                //active wow
                wow.init();

            });
        }
    }


    /*------------------------------------------
        = WOW ANIMATION SETTING
    -------------------------------------------*/
    var wow = new WOW({
        boxClass:     'wow',      // default
        animateClass: 'animated', // default
        offset:       0,          // default
        mobile:       true,       // default
        live:         true        // default
    });


    /*------------------------------------------
        = ACTIVE POPUP IMAGE
    -------------------------------------------*/
    if ($(".fancybox").length) {
        $(".fancybox").fancybox({
            openEffect  : "elastic",
            closeEffect : "elastic",
            wrapCSS     : "project-fancybox-title-style"
        });
    }


    /*------------------------------------------
        = POPUP VIDEO
    -------------------------------------------*/
    if ($(".video-btn").length) {
        $(".video-btn").on("click", function(){
            $.fancybox({
                href: this.href,
                type: $(this).data("type"),
                'title'         : this.title,
                helpers     : {
                    title : { type : 'inside' },
                    media : {}
                },

                beforeShow : function(){
                    $(".fancybox-wrap").addClass("gallery-fancybox");
                }
            });
            return false
        });
    }


    /*------------------------------------------
        = ACTIVE GALLERY POPUP IMAGE
    -------------------------------------------*/
    if ($(".popup-gallery").length) {
        $('.popup-gallery').magnificPopup({
            delegate: 'a',
            type: 'image',

            gallery: {
              enabled: true
            },

            zoom: {
                enabled: true,

                duration: 300,
                easing: 'ease-in-out',
                opener: function(openerElement) {
                    return openerElement.is('img') ? openerElement : openerElement.find('img');
                }
            }
        });
    }


    /*------------------------------------------
        = FUNCTION FORM SORTING GALLERY
    -------------------------------------------*/
    function sortingGallery() {
        if ($(".sortable-gallery .gallery-filters").length) {
            var $container = $('.gallery-container');
            $container.isotope({
                filter:'*',
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false,
                }
            });

            $(".gallery-filters li a").on("click", function() {
                $('.gallery-filters li .current').removeClass('current');
                $(this).addClass('current');
                var selector = $(this).attr('data-filter');
                $container.isotope({
                    filter:selector,
                    animationOptions: {
                        duration: 750,
                        easing: 'linear',
                        queue: false,
                    }
                });
                return false;
            });
        }
    }

    sortingGallery();



    /*------------------------------------------
        = MASONRY GALLERY SETTING
    -------------------------------------------*/
    function masonryGridSetting() {
        if ($('.masonry-gallery').length) {
            var $grid =  $('.masonry-gallery').masonry({
                itemSelector: '.grid-item',
                columnWidth: '.grid-item',
                percentPosition: true
            });

            $grid.imagesLoaded().progress( function() {
                $grid.masonry('layout');
            });
        }
    }

    // masonryGridSetting();


    /*------------------------------------------
        = STICKY HEADER
    -------------------------------------------*/

    // Function for clone an element for sticky menu
    function cloneNavForSticyMenu($ele, $newElmClass) {
        $ele.addClass('original').clone().insertAfter($ele).addClass($newElmClass).removeClass('original');
    }

    // clone home style 1 navigation for sticky menu
    if ($('.tp-site-header .navigation').length) {
        cloneNavForSticyMenu($('.tp-site-header .navigation'), "sticky-header");
    }

    var lastScrollTop = '';

    function stickyMenu($targetMenu, $toggleClass) {
        var st = $(window).scrollTop();
        var mainMenuTop = $('.tp-site-header .navigation');

        if ($(window).scrollTop() > 1000) {
            if (st > lastScrollTop) {
                // hide sticky menu on scroll down
                $targetMenu.removeClass($toggleClass);

            } else {
                // active sticky menu on scroll up
                $targetMenu.addClass($toggleClass);
            }

        } else {
            $targetMenu.removeClass($toggleClass);
        }

        lastScrollTop = st;
    }


    /*------------------------------------------
        = Header search toggle
    -------------------------------------------*/
    if($(".header-search-form-wrapper").length) {
        var searchToggleBtn = $(".search-toggle-btn");
        var searchContent = $(".header-search-form");
        var body = $("body");

        searchToggleBtn.on("click", function(e) {
            searchContent.toggleClass("header-search-content-toggle");
            e.stopPropagation();
        });

        body.on("click", function() {
            searchContent.removeClass("header-search-content-toggle");
        }).find(searchContent).on("click", function(e) {
            e.stopPropagation();
        });
    }


    /*------------------------------------------
        = Header shopping cart toggle
    -------------------------------------------*/
    if($(".mini-cart").length) {
        var cartToggleBtn = $(".cart-toggle-btn");
        var cartContent = $(".mini-cart-content");
        var body = $("body");

        cartToggleBtn.on("click", function(e) {
            cartContent.toggleClass("mini-cart-content-toggle");
            e.stopPropagation();
        });

        body.on("click", function() {
            cartContent.removeClass("mini-cart-content-toggle");
        }).find(cartContent).on("click", function(e) {
            e.stopPropagation();
        });
    }


    /*------------------------------------------
        = NEW PRODUCT SLIDER
    -------------------------------------------*/
    if($(".new-product-slider".length)) {
        $(".new-product-slider").owlCarousel({
            mouseDrag: false,
            smartSpeed: 500,
            margin: 30,
            loop:true,
            nav: true,
            navText: ['<i class="fi ti-angle-left"></i>','<i class="fi ti-angle-right"></i>'],
            dots: false,
            items: 1
        });
    }  


    /*------------------------------------------
        = FUNFACT
    -------------------------------------------*/
    if ($(".odometer").length) {
        $('.odometer').appear();
        $(document.body).on('appear', '.odometer', function(e) {
            var odo = $(".odometer");
            odo.each(function() {
                var countNumber = $(this).attr("data-count");
                $(this).html(countNumber);
            });
        });
    }


    /*------------------------------------------
        = TESTIMONIALS SLIDER
    -------------------------------------------*/
    if ($(".tp-testimonial-slider").length) {
        $(".tp-testimonial-slider").owlCarousel({
            center: true,
            loop:true,
            margin: 30,
            responsive:{
                0 : {
                    items: 1,
                },
                
                650 : {
                    items: 2,
                    center: false,
                    margin: 10
                },
                
                992:{
                    items:3
                }
            }
        });
    }


    /*------------------------------------------
        = TEAM SLIDER
    -------------------------------------------*/
    if ($(".tp-case-slider").length) {
        $(".tp-case-slider").owlCarousel({
            loop:true,
            margin: 20,
            nav: true,
            navText: ['<i class="fi ti-angle-left"></i>','<i class="fi ti-angle-right"></i>'],
            dots: false,
            responsive:{
                0 : {
                    items: 1,
                },
                
                550 : {
                    items: 2,
                    center: false,
                    margin: 10
                },
                
                992:{
                    items:3
                },
                
                1200:{
                    items:3
                }
            }
        });
    }


    /*------------------------------------------
        = POST SLIDER
    -------------------------------------------*/
    if($(".post-slider".length)) {
        $(".post-slider").owlCarousel({
            mouseDrag: false,
            smartSpeed: 500,
            margin: 30,
            loop:true,
            nav: true,
            navText: ['<i class="fi ti-angle-left"></i>','<i class="fi ti-angle-right"></i>'],
            dots: false,
            items: 1
        });
    }  
    
    // Single gallery slider
    function productGallary() {
        if ($('.tp-testimonial-active').length && $('.tp-testimonial-thumbnil-active').length) {

            var $sync1 = $(".tp-testimonial-active"),
                $sync2 = $(".tp-testimonial-thumbnil-active"),
                flag = false,
                duration = 500;

            $sync1
                .owlCarousel({
                    items: 1,
                    margin: 0,
                    nav: true,
                    navText: ['<i class="ti-angle-left"></i>', '<i class="ti-angle-right"></i>'],
                    dots: false
                })
                .on('changed.owl.carousel', function(e) {
                    if (!flag) {
                        flag = true;
                        $sync2.trigger('to.owl.carousel', [e.item.index, duration, true]);
                        flag = false;
                    }
                });

            $sync2
                .owlCarousel({
                    margin: 10,
                    items: 3,
                    nav: false,
                    dots: false,
                    center: false,
                    responsive: {
                        0: {
                            items: 2,
                            autoWidth: false
                        },
                        400: {
                            items: 2,
                            autoWidth: false
                        },
                        500: {
                            items: 3,
                            center: false,
                            autoWidth: false
                        },
                        600: {
                            items: 5,
                            autoWidth: false
                        },
                        1200: {
                            items: 5,
                            autoWidth: false
                        }
                    },
                })
                .on('click', '.owl-item', function() {
                    $sync1.trigger('to.owl.carousel', [$(this).index(), duration, true]);

                })
                .on('changed.owl.carousel', function(e) {
                    if (!flag) {
                        flag = true;
                        $sync1.trigger('to.owl.carousel', [e.item.index, duration, true]);
                        flag = false;
                    }
                });

        };
    }

    productGallary();

    /*------------------------------------------
        = CONTACT FORM SUBMISSION
    -------------------------------------------*/
    if ($("#contact-form").length) {
        $("#contact-form").validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },

                name2: "required",

                email: "required",

                subject: "required",

                address: "required"
            },

            messages: {
                name: "Please enter your name",
                name2: "Please enter your name",
                email: "Please enter your email address",
                subject: "Please enter your Subject",
            },

            submitHandler: function (form) {
                $.ajax({
                    type: "POST",
                    url: "mail.php",
                    data: $(form).serialize(),
                    success: function () {
                        $( "#loader").hide();
                        $( "#success").slideDown( "slow" );
                        setTimeout(function() {
                        $( "#success").slideUp( "slow" );
                        }, 3000);
                        form.reset();
                    },
                    error: function() {
                        $( "#loader").hide();
                        $( "#error").slideDown( "slow" );
                        setTimeout(function() {
                        $( "#error").slideUp( "slow" );
                        }, 3000);
                    }
                });
                return false; // required to block normal submit since you used ajax
            }

        });
    }



    /*------------------------------------------
        = BACK TO TOP BTN SETTING
    -------------------------------------------*/
    $("body").append("<a href='#' class='back-to-top'><i class='ti-arrow-up'></i></a>");

    function toggleBackToTopBtn() {
        var amountScrolled = 1000;
        if ($(window).scrollTop() > amountScrolled) {
            $("a.back-to-top").fadeIn("slow");
        } else {
            $("a.back-to-top").fadeOut("slow");
        }
    }

    $(".back-to-top").on("click", function() {
        $("html,body").animate({
            scrollTop: 0
        }, 700);
        return false;
    })  



    /*==========================================================================
        WHEN DOCUMENT LOADING
    ==========================================================================*/
        $(window).on('load', function() {

            preloader();
            
            sliderBgSetting();

            toggleMobileNavigation();

            smallNavFunctionality();

            productGallary();

            sortingGallery();

            initGsapParallax();

        });



    /*==========================================================================
        WHEN WINDOW SCROLL
    ==========================================================================*/
    $(window).on("scroll", function() {

		if ($(".tp-site-header").length) {
            stickyMenu( $('.tp-site-header .navigation'), "sticky-on" );
        }

        toggleBackToTopBtn();

    });


    /*==========================================================================
        WHEN WINDOW RESIZE
    ==========================================================================*/
    $(window).on("resize", function() {
        
        toggleClassForSmallNav();

        clearTimeout($.data(this, 'resizeTimer'));
        $.data(this, 'resizeTimer', setTimeout(function() {
            smallNavFunctionality();
        }, 200));

    });



    // login

        $(".reveal6").on('click', function() {
        var $pwd = $(".pwd6");
        if ($pwd.attr('type') === 'text') {
            $pwd.attr('type', 'password');
        } else {
            $pwd.attr('type', 'text');
        }
    });


    $(".reveal3").on('click', function() {
        var $pwd = $(".pwd2");
        if ($pwd.attr('type') === 'text') {
            $pwd.attr('type', 'password');
        } else {
            $pwd.attr('type', 'text');
        }
    });  

    $(".reveal2").on('click', function() {
        var $pwd = $(".pwd3");
        if ($pwd.attr('type') === 'text') {
            $pwd.attr('type', 'password');
        } else {
            $pwd.attr('type', 'text');
        }
    });



})(window.jQuery);
