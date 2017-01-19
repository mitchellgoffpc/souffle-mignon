// Global object
window.SM = {}

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
