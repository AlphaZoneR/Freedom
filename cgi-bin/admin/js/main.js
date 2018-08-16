(function($) {
    if (window.location.hash == '#board') {
        setTimeout(() => {fetch_board()}, 0);
    } else if (window.location.hash == '#contacts') {
        setTimeout(() => {fetch_contacts()}, 0);
    } else if (window.location.hash == "#posts") {
        setTimeout(() => {fetch_posts()}, 0);
    } else if (window.location.hash == "#overall") {
        setTimeout(() => {fetch_overall()}, 0);
    } else if (window.location.hash == "#edit") {
        setTimeout(() => (fetch_account_edit(), 0));
    }

    $('#contact-button').click(function() {
        window.location.hash = '#contacts';
        fetch_contacts();        
    })

    $('#board-button').click(function() {
        window.location.hash = '#board';
        fetch_board();
    })

    $("#posts-button").click(function () {
        window.location.hash = '#posts';
        fetch_posts();
    })

    $("#overall-button").click(function () {
        window.location.hash = '#overall';
        fetch_overall();
    })

    window.sr = ScrollReveal();

    $("#logout-button").click(function () {
        window.location.replace('/logout')
    });

    $('#edit-button').click(function () {
        fetch_account_edit();
    });

    $('#register').click(function() {
        alert('register');
    })

    let i = 0;
   
})(jQuery);

function fetch_contacts() {
    $.ajax({
        url: 'contacts',
        type: 'POST',
        success: function (response) {
            $('.right').html(response);
        },
        error: function (response) {console.log(response)},
    })
}

function fetch_board() {
    $.ajax({
        url: 'board',
        type: 'POST',
        success: function (response) {
            $('.right').html(response);
        },
        error: function (response) {console.log(response)},
    })
}

function fetch_posts() {
    $.ajax({
        url: 'posts/',
        type: 'POST',
        success: function (response) {
            $('.right').html(response);
        },
        error: function (response) {console.log(response)},
    })
}

function fetch_overall() {
    $.ajax({
        url: 'overall',
        type: 'POST',
        success: function (response) {
            $('.right').html(response);
        },
        error: function (response) {console.log(response)},
    })
}

function fetch_account_edit() {
    $.ajax({
        url: 'edit',
        type: 'POST',
        success: function (response) {
            $('.right').html(response);
        },
        error: function (error) {
            console.log(error);
        }
    })
}