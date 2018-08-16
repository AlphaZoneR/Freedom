$(document).ajaxStop(function () {
    $('#loading').fadeOut();
    $('#mainNav').addClass('float_in');
});

$(document).ajaxStart(function () {
    $('#loading').show();
});

$(function () {

    window.sr = ScrollReveal();

    var last_scroll = 0;

    $(window).scroll(function (event) {
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

    $('.js-scroll-trigger').click(function () {
        $('.navbar-collapse').collapse('hide');
    });
    $('body').scrollspy({
        target: '#mainNav',
        offset: 54
    });
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-shrink");
        } else {
            $("#mainNav").removeClass("navbar-shrink");
        }
    };
    navbarCollapse();

    $(window).scroll(navbarCollapse);
})

$.ajax({
    type: 'GET',
    url: '/static/footer.html',
    success: (response) => {
        $('#fill-footer').html(response)
    },
    error: (error) => {
        console.log('error')
        console.log(error);
    }
})

$.ajax({
    url: '/api/post/get',
    type: 'GET',
    success: function (response) {
      $('#news-holder').html(response);
    },
    error: function (response) {
      console.log(response)
    }
})
