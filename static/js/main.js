$(function () {
   'use strict';

   $('.carousel').carousel();
   $('.carousel_bottom').carousel();
   
   $(".header__search-icon").on("click", function(e){
      e.preventDefault();
      $(".search").toggleClass("hide");
   });

   $(".footer__arrow").on("click", function(e){
      e.preventDefault();
      $(this).next(".footer__block").toggleClass("show");
      $(this).toggleClass("footer__arrow_up");
   });

   $(".header-mobile__icon-toggle").on("click", function(e){
      e.preventDefault();
      $(this).toggleClass("menu-open");
      $(".header").toggleClass("header_active")
   });

   $(".comments__btn").on("click", function(e){
      e.preventDefault();
      $(".comments-bottom").toggleClass("show");
      $(this).toggleClass("comments__btn_active");
      $(".comments__item_last").toggleClass("hide")
   });
   

   $(".mobile__icon.navbar-toggle").on("click", function(e){
      e.preventDefault();
      $(this).toggleClass("icon-active");
   });

   $(".gifts__type-name").on("click", function(e){
      e.preventDefault();
      $(".gifts__type-name").removeClass("gifts__type-name_active");
      $(this).addClass("gifts__type-name_active");
   });

   $(".product-detail__link").on("click", function(e){
      e.preventDefault();

      if(!$(this).parent().hasClass("product-detail__more_active")){
          $(".product-detail__table").removeClass("show");
          $(".product-detail__more").removeClass("product-detail__more_active");

         $(this).parent().addClass("product-detail__more_active");
          if($(this).hasClass("show_tissu")){
             $(".tissu").addClass("show");
          } else if($(this).hasClass("show_options")){
             $(".options").addClass("show");
          } else if($(this).hasClass("show_les")){
             $(".les").addClass("show");
          } 
      } else if($(this).parent().hasClass("product-detail__more_active")){
         $(".tissu").removeClass("show");
         $(".options").removeClass("show");
         $(".les").removeClass("show");
         $(this).parent().removeClass("product-detail__more_active")
      } 
      
   });

$(".compare-item__link").on("click", function(e) {
    e.preventDefault();

    if (!$(this).parent().hasClass("product-detail__more_active")) {

        $(this).parent().addClass("product-detail__more_active");
        if ($(this).hasClass("show_compare-description")) {
            $(this).parent().next(".compare-description").addClass("show");
        } else if($(this).hasClass("show_tissu")){
          $(this).parent().next(".tissu").addClass("show");
        }
    } else if ($(this).parent().hasClass("product-detail__more_active")) {
        $(this).parent().next(".tissu").removeClass("show");
        $(this).parent().next(".compare-description").removeClass("show");
        $(this).parent().removeClass("product-detail__more_active");
    }

});

   $(window).scroll(function() {
      $(".dropdown").removeClass('open');
       var nav = $('.header');
       var top = 200;
       if ($(window).scrollTop() >= top) {

           nav.addClass('header_onscroll');

       } else {
           nav.removeClass('header_onscroll');
       }
   });

  $(".submenu__title").on("click", function(e){
    if ($( window ).width() < 992){
      e.preventDefault();
      $(this).toggleClass("submenu__title_active").next(".menu__list").toggleClass("show");

      $(".top-line").toggleClass("hide");
      $(".menu__item-top").toggleClass("hide");
      $(".header__mobile-link").toggleClass("hide");
      $(".submenu__title").not(this).toggleClass("hide");
      if(!$(".search").hasClass("hide")){
        $(".search").addClass("hide");
      }
    }
  });

  $( window ).resize(function() {
    if ($( window ).width() > 992){
      $(".menu__list").removeClass("show");
      $(".submenu__title").removeClass("submenu__title_active");
      $(".top-line").removeClass("hide");
      $(".menu__item-top").removeClass("hide");
      $(".header__mobile-link").removeClass("hide");
      $(".submenu__title").removeClass("hide");
    }
  });

  $(".gallery-panel__bottom-arrow").on("click", function(e){
      e.preventDefault();
      $(".gallery-panel__body").toggleClass("show");
      $(".gallery-panel__bottom-actions").toggleClass("show");
      $(".gallery-panel__bottom-arrow").toggleClass("gallery-panel__bottom-arrow_open");

  });

  $(".gallery-panel__close").on("click", function(e){
      e.preventDefault();
      $(".gallery-panel__body").toggleClass("show");
      $(".gallery-panel__bottom-actions").toggleClass("show");
      
  });

  $(".gallery__block-head").on("click", function(e){
      e.preventDefault();
      $(this).next().toggleClass("hide");
      $(this).toggleClass("gallery__block-head_active");
  });

  $(".mesures__block-head").on("click", function(e){
      e.preventDefault();
      $(this).next().toggleClass("hide");
      $(this).toggleClass("gallery__block-head_active");
  });

  $(".mesures-method__block-head").on("click", function(e){
      e.preventDefault();
      $(this).next().toggleClass("hide");
      $(this).toggleClass("gallery__block-head_active");
  });

  $(".orders__more-text").on("click", function(e){
      e.preventDefault();
      $(this).next().toggleClass("show");
      $(this).closest(".orders__item").toggleClass("orders__item_active");
  });
  
  $(".account-menu-mobile").on("click", function(e){
      e.preventDefault();
      $(this).next().toggleClass("show");
  });
  
   $(".order-actions__link").on("click", function(e){
      console.log("fsdf");
      e.preventDefault();
      $(this).next().toggleClass("show");
      $(this).closest(".cart-big").toggleClass("orders__item_active");
  });

  // gallery__fancywork.html - select points of the shirt

  $( ".shirt-select__item" )
    .mouseover(function() {
      $(this).addClass("fancywork-selected");
    })
    .mouseout(function() {
      if (!$(this).hasClass( "shirt-select__item_active" )){
        $(this).removeClass("fancywork-selected");
      }
    });

  $(".shirt-select__item").on("click", function(e){

    $(".shirt-select .shirt-select__item").removeClass("shirt-select__item_active fancywork-selected");
    $(this).find("input").prop('checked', true);
    $(this).addClass("fancywork-selected");
    $(this).toggleClass("shirt-select__item_active");
  });

  // cart__step-3.html - toggle .cart-summary block

  $(".cart-toggle").on("click", function(e){
      e.preventDefault();
      $(this).toggleClass("cart-toggle_close");
      $(this).next(".cart-toggle__area").toggleClass("cart-toggle_show");
  });

 // cart__step-3.html - display hint

 // $(".card__cvc-icon").on("mouseenter mouseleave", function(e){
 //      e.preventDefault();
 //      $(this).next(".card__cvc-hint").toggleClass("show");
 //  });

// help__item.html - toggle .help-article__toggle-block

  $(".help-article-toggle").on("click", function(e){
      e.preventDefault();
      $(this).toggleClass("help-article-toggle_close");
      $(this).next(".help-article__inner-block").toggleClass("help-article-toggle_show");
  });

  $(".sartor__label").on("click", function(e){
      // e.preventDefault();
      $(this).parent().parent().next(".sartor__price").toggleClass("show");
  });
  

});