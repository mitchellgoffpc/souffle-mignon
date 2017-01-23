// Global object
window.SM = window.SM || { state: {} };
SM.state.linkPosition = 'TOP';

// Functions
SM.shareFacebook = function() {
    FB.ui({
        method: 'share',
        href: window.location.href });
}

SM.checkLinkPosition = function() {
    var scrollPos = $(window).scrollTop();
    var entryPos = $('#article .entry').offset().top;
    var entryHeight = $('#article .entry').height();
    var linkHeight = $('#article .links').height();

    if (scrollPos < entryPos - 100)
        SM.updateLinkPosition('TOP');
    else if (scrollPos > entryPos + entryHeight - linkHeight - 100)
        SM.updateLinkPosition('BOTTOM');
    else
        SM.updateLinkPosition('FIXED');
}

SM.updateLinkPosition = function(pos) {
    if (pos != SM.state.linkPosition) {
        SM.state.linkPosition = pos;
        var entryPos = $('#article .entry').offset().left;
        var entryHeight = $('#article .entry').height();
        var linkHeight = $('#article .links').height();

        if (pos == 'TOP')
            $('#article .links').css({ 'position': 'absolute', 'top': 20, 'left': -100 });
        else if (pos == 'BOTTOM')
            $('#article .links').css({ 'position': 'absolute', 'top': entryHeight - linkHeight - 100, 'left': -100 });
        else if (pos == 'FIXED')
            $('#article .links').css({ 'position': 'fixed', 'top': 120, 'left': entryPos - 100 });
    }
}


// Event handlers
$(document).ready(function() {
    SM.checkLinkPosition();
    $(window).scroll(SM.checkLinkPosition);
    $('#article .links .share-fb').click(SM.shareFacebook);
    $('#article .links .like').click(SM.showLoginModal);
    $('#overlay').click(SM.hideLoginModal);
});
