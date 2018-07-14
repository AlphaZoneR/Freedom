(function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 48)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  var last_scroll = 0;

  $(window).scroll(function(event) {
    var st = $(this).scrollTop();

    if (st > last_scroll) {
      $('#mainNav').css('opacity', '0.0');
      $('#mainNav').css('height', '0px');
    } else {
      $('#mainNav').css('opacity', '1.0');
      $('#mainNav').css('height', '100px');
    }

    last_scroll = st;
  })
  

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 54
  });

  // Collapse Navbar
  var navbarCollapse = function() {
    if ($("#mainNav").offset().top > 100) {
      $("#mainNav").addClass("navbar-shrink");
    } else {
      $("#mainNav").removeClass("navbar-shrink");
    }
  };
  // Collapse now if page is not at top
  navbarCollapse();
  // Collapse the navbar when page is scrolled
  $(window).scroll(navbarCollapse);

})(jQuery); // End of use strict


(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));

// Google Maps Scripts
var map = null;
// When the window has finished loading create our google map below
google.maps.event.addDomListener(window, 'load', init);
google.maps.event.addDomListener(window, 'resize', function() {
  map.setCenter(new google.maps.LatLng(46.779904, 23.605433));
});

function init() {
  // Basic options for a simple Google Map
  // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
  var mapOptions = {
    // How zoomed in you want the map to start at (always required)
    zoom: 15,

    // The latitude and longitude to center the map (always required)
    center: new google.maps.LatLng(46.779904, 23.605433), // New York

    // Disables the default Google Maps UI components
    disableDefaultUI: true,
    scrollwheel: false,
    draggable: false,

    // How you would like to style the map.
    // This is where you would paste any style found on Snazzy Maps.
    styles: [{
      "featureType": "water",
      "elementType": "geometry",
      "stylers": [{
        "color": "#000000"
      }, {
        "lightness": 17
      }]
    }, {
      "featureType": "landscape",
      "elementType": "geometry",
      "stylers": [{
        "color": "#000000"
      }, {
        "lightness": 20
      }]
    }, {
      "featureType": "road.highway",
      "elementType": "geometry.fill",
      "stylers": [{
        "color": "#000000"
      }, {
        "lightness": 17
      }]
    }, {
      "featureType": "road.highway",
      "elementType": "geometry.stroke",
      "stylers": [{
        "color": "#000000"
      }, {
        "lightness": 29
      }, {
        "weight": 0.2
      }]
    }, {
      "featureType": "road.arterial",
      "elementType": "geometry",
      "stylers": [{
        "color": "#000000"
      }, {
        "lightness": 18
      }]
    }, {
      "featureType": "road.local",
      "elementType": "geometry",
      "stylers": [{
        "color": "#000000"
      }, {
        "lightness": 16
      }]
    }, {
      "featureType": "poi",
      "elementType": "geometry",
      "stylers": [{
        "color": "#000000"
      }, {
        "lightness": 21
      }]
    }, {
      "elementType": "labels.text.stroke",
      "stylers": [{
        "visibility": "on"
      }, {
        "color": "#000000"
      }, {
        "lightness": 16
      }]
    }, {
      "elementType": "labels.text.fill",
      "stylers": [{
        "saturation": 36
      }, {
        "color": "#000000"
      }, {
        "lightness": 40
      }]
    }, {
      "elementType": "labels.icon",
      "stylers": [{
        "visibility": "off"
      }]
    }, {
      "featureType": "transit",
      "elementType": "geometry",
      "stylers": [{
        "color": "#000000"
      }, {
        "lightness": 19
      }]
    }, {
      "featureType": "administrative",
      "elementType": "geometry.fill",
      "stylers": [{
        "color": "#000000"
      }, {
        "lightness": 20
      }]
    }, {
      "featureType": "administrative",
      "elementType": "geometry.stroke",
      "stylers": [{
        "color": "#000000"
      }, {
        "lightness": 17
      }, {
        "weight": 1.2
      }]
    }]
  };

  $('#fb-share').click(function() {
    FB.ui({
      method: 'feed',
      link: document.URL,
      caption: 'An example caption',
    }, function (response) {
      console.log(response)
    })
  })

  $('.intro-body').mousemove(function(event) {
    var text = 'translate(' + String( - event.clientX / 75) + 'px, ' + String(-event.clientY / 75) + 'px)';
    $('.intro-text').css('transform', text);
    $('.brand-heading').css('transform', text);
  })

  window.sr = ScrollReveal();

  sr.reveal('.container', {
    delay: 200
  })

  var i = 0;
  $('.specialization').each(function() {
    ++i;
    sr.reveal($(this), {
      delay: i * 500
     
    })
  })

  i = 0;
  $('.item').each(function() {
    ++i;
    sr.reveal($(this), {
      useDelay: 'once',
      delay: i * 100,
      reset: false
    })
  })


  sr.reveal('#contact')

  $("#mainNav").find(".container").css('opacity', '1')
  
  // new nicEditor({
  //   fullPanel : true
  // })
  
  // bkLib.onDomLoaded(function() { 
  //   nicEditors.allTextAreas()
  // });
  
  $("#mainNav").addClass('float_in');
  $('#mainNav').find('.container').addClass('float_in')
  $("#info").addClass('float_in');
  

  $('.item').mouseenter(function (event) {
    $('.item').addClass('faded');
    $(this).removeClass('faded')
  })

  $('.item').mouseleave(function (event) {
    $('.item').removeClass('faded');
  })

  $($('.name-area').children()[0]).focus(check_contact_data);
  $($('.name-area').children()[1]).focus(check_contact_data);
  $($('.email-area').children()[0]).focus(check_contact_data);
  $($('.subject-area').children()[0]).focus(check_contact_data);
  $($('.text-area').children()[0]).focus(check_contact_data);
  $($('.text-area').children()[0]).focusout(check_contact_data)

  $('#submit-contact').click(function() {
    var ok = check_contact_data()
    if (ok) {
      $.post({
        url: '/freedom/api/contact/add',
        type: 'POST',
        data: {
          'fname':  $($('.name-area').children()[0]).val(),
          'lname':  $($('.name-area').children()[1]).val(),
          'email': $($('.email-area').children()[0]).val(),
          'subject': $($('.subject-area').children()[0]).val(),
          'body': $($('.text-area').children()[0]).val()
        },
        success: function(response) {
          response = JSON.parse(response);
          if (response['status'] == 'OK') {
            $('.success-div').addClass('visible');
          }
        },
        error: function(error){
          $('.error-div').children[0].html('În acest moment nu se poate trimite formularul!<br>Vâ rugâm încercaţi mai tărziu!')
          $('.error-div').addClass('visible')
        }
      })
    }
  })

  // Get the HTML DOM element that will contain your map
  // We are using a div with id="map" seen below in the <body>
  var mapElement = document.getElementById('map');

  // Create the Google Map using out element and options defined above
  map = new google.maps.Map(mapElement, mapOptions);

  // Custom Map Marker Icon - Customize the map-marker.png file to customize your icon
  var image = 'img/map-marker.svg';
  var myLatLng = new google.maps.LatLng(46.779904, 23.605433);
  var beachMarker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    icon: image
  });

  var EMAIL_REG = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

  function check_contact_data() {
    var error = false;
    $($('.name-area').children()[0]).removeClass('input-error');
    $($('.name-area').children()[1]).removeClass('input-error');
    $($('.email-area').children()[0]).removeClass('input-error');
    $($('.subject-area').children()[0]).removeClass('input-error');
    $($('.text-area').children()[0]).removeClass('input-error');
    $('.error-div').removeClass('visible');
    
    if ($($('.name-area').children()[0]).val().length == 0) {
      $($('.name-area').children()[0]).addClass('input-error');
      $($('.name-area').children()[0]).removeClass('input-okay');
      error = true;
    } else {
      $($('.name-area').children()[0]).addClass('input-okay');
    }

    if ($($('.name-area').children()[1]).val().length == 0) {
      $($('.name-area').children()[1]).addClass('input-error');
      $($('.name-area').children()[1]).removeClass('input-okay');
      error = true;
    } else {
      $($('.name-area').children()[1]).addClass('input-okay');
    }

    if (!EMAIL_REG.exec($($('.email-area').children()[0]).val())) {
      $($('.email-area').children()[0]).addClass('input-error');
      $($('.email-area').children()[0]).removeClass('input-okay');
      error = true;
    } else {
      $($('.email-area').children()[0]).addClass('input-okay');
    }


    if ($($('.subject-area').children()[0]).val().length == 0){
      
      $($('.subject-area').children()[0]).addClass('input-error');
      $($('.subject-area').children()[0]).removeClass('input-okay');
      error = true;
    } else {
      $($('.subject-area').children()[0]).addClass('input-okay');
    }
    
    if ($($('.text-area').children()[0]).val().length == 0){
      $($('.text-area').children()[0]).addClass('input-error');
      $($('.text-area').children()[0]).removeClass('input-okay');
      error = true;
    } else {
      $($('.text-area').children()[0]).addClass('input-okay');
    }

    if (error) {
      $('.error-div').addClass('visible');
    }

    return !error
  }
}

