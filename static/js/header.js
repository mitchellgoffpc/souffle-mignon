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
}

SM.didTypeSearch = function(e) {
    if (e.which == 13) {
        var search = $('.search-box').val();
        window.location.href = '/search/?q=' + encodeURIComponent(search);
    }
}

SM.didClickMenu = function() {
    var hidden = $('.header .menu').attr('data-hidden') == 'true';
    $('.header .menu').attr('data-hidden', hidden ? 'false' : 'true');
    $('.header .menu').css('display', hidden ? 'block' : 'none');
}

SM.didClickOutsideMenu = function() {
    if ($('.header .menu').attr('data-hidden') == 'false') {
        $('.header .menu').attr('data-hidden', 'true');
        $('.header .menu').css('display', 'none');
    }
}
