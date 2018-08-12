$(function() {
    $('.table-data').click(function() {
        $('.modal-title').html('Vizualizare mesaj ' + $(this).data('name'))
        $('#modal-name').val($(this).data('name'));
        $('#modal-email').val($(this).data('email'));
        $('#modal-title').val($(this).data('subject'));
        $('#modal-timestamp').val($(this).data('timestamp'));
        $('#modal-body').val($(this).data('body'));
        $("#myModal").modal('show');
    })

    sr.reveal($('.contact-holder'));
})