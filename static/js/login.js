// Global object
window.SM = window.SM || { state: {} };

// Functions
SM.checkLoginStatus = function() {
    FB.getLoginStatus(function(response) {
        if (response.status == "connected") {
            // Update the state
            console.log(response.authResponse.userID);
        }
    });
}

SM.login = function() {
    FB.login(function(response) {
        console.log(response.authResponse.userID);
    });
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
