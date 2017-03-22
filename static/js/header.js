SM.didClickSearch = function() {
    var hidden = $('.search-box').attr('data-hidden') == 'true';
    $('.search-box').attr('data-hidden', hidden ? 'false' : 'true');
    $('.search-box').animate({ marginRight: hidden ? 0 : -180 }, function() {
        if (hidden) {
            $('.search-box').focus();
        } else {
            $('.search-box').blur();
        }
    });

    $('.search-box').on('keypress', function(e) {
        if (e.which == 13) {
            var search = $('.search-box').val();
            window.location.href = '/search/?q=' + encodeURIComponent(search);
        }
    });
}
