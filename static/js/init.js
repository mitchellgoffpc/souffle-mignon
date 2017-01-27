$(document).ready(function() {
    // Header/Login
    $('.search-btn').click(SM.didClickSearch);
    $('.button.tw').click(SM.twitterLogin);
    $('.button.fb').click(SM.facebookLogin);

    // Detail
    if (SM.page == 'detail') {
        SM.checkLinkPosition();
        $(window).scroll(SM.checkLinkPosition);

        $('#overlay').click(SM.hideLoginModal);
        $('#article .links .share-fb').click(SM.shareFacebook);
        $('#article .links .like').click(SM.didClickLikeArticle);
        $('#article .responses .like').click(SM.didClickLikeComment);
        $('#article .responses .write .publish').click(SM.didClickPublishComment);

        $(document).click(function(e) {
            if ($(e.target).closest('#article .responses .write').length) {
                SM.didClickComment();
            } else {
                SM.didClickOutsideComment();
            }
        })
    }
});
