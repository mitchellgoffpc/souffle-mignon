$(document).ready(function() {
    // Header/Login
    $('.search-btn').click(SM.didClickSearch);
    $('.button.tw').click(SM.twitterLogin);
    $('.button.fb').click(SM.facebookLogin);

    // Detail
    if (SM.page == 'detail') {
        SM.checkLinkPosition();
        $(window).scroll(SM.checkLinkPosition);
        $('#article .links .share-fb').click(SM.shareFacebook);
        $('#article .links .like').click(SM.showLoginModal);
        $('#overlay').click(SM.hideLoginModal);
    }
});
