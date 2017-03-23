$(document).ready(function() {
    // Header/Login
    $('.header .search-box').keypress(SM.didTypeSearch);
    $('.header .search-btn').click(SM.didClickSearch);
    $('.button.tw').click(SM.twitterLogin);
    $('.button.fb').click(SM.facebookLogin);

    $(document).on('click', function(e) {
        if ($(e.target).closest('.header .menu-icon').length) {
            SM.didClickMenu();
        } else if ($(e.target).closest('.header .menu').length == 0) {
            SM.didClickOutsideMenu();
        }
    })

    // Detail
    if (SM.page == 'detail') {
        SM.checkLinkPosition();
        $(window).scroll(SM.checkLinkPosition);

        $('#overlay').on('click', SM.hideLoginModal);
        $('#article .links .share-fb').on('click', SM.shareFacebook);
        $('#article .links .like').on('click', SM.didClickLikeArticle);
        $('#article .responses .write .publish').on('click', SM.didClickPublishComment);

        $(document).on('click', '#article .responses .like', SM.didClickLikeComment);
        $(document).on('click', function(e) {
            if ($(e.target).closest('#article .responses .write').length) {
                SM.didClickComment();
            } else {
                SM.didClickOutsideComment();
            }
        })
    }
});
