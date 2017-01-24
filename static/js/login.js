// Functions
SM.twitterLogin = function() {
    window.location.href = '/auth/twitter/?' +
        'callback=' + encodeURIComponent(window.location.href);
}

SM.facebookLogin = function() {
    FB.getLoginStatus(function(response) { callback(response, true) });
}

function callback(response, retry) {
    if (response.status === 'connected') {
        window.location.href = '/auth/facebook/?' +
            'callback=' + encodeURIComponent(window.location.href) +
            '&access_token=' + encodeURIComponent(response.authResponse.accessToken);
    } else if (retry) {
        FB.login(function(response) { callback(response, false) });
    }
}


// Animations
SM.showLoginModal = function() {
    $('#login').addClass('visible');
    $('#overlay').addClass('visible');
}

SM.hideLoginModal = function() {
    $('#login').removeClass('visible');
    $('#overlay').removeClass('visible');
}
