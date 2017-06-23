SM.didClickSearch = function() {
    var search = $('.header .search-box');
    var hidden = search.attr('data-hidden') == 'true';
    search.attr('data-hidden', hidden ? 'false' : 'true');
    search.animate({ marginRight: hidden ? 0 : -180 }, function() {
        if (hidden) {
            search.focus();
        } else {
            search.blur();
        }
    });
}

SM.didTypeSearch = function(e) {
    if (e.which == 13) {
        var query = $('.header .search-box').val();
        window.location.href = '/search/?q=' + encodeURIComponent(query);
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
