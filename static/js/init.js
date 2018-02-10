var Algolia = {
    APP_ID: "FDH6H58XJI",
    API_KEY: "d3f8417e2ebfb6f7c807b9b52f908a65" }


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

    // Image preloading
    $('.preloader').one('load', function(e) {
        var $landing = $(e.target).closest('.landing')
        var $background = $landing.find('.background')

        $landing.addClass('loaded');
        $background.css('background-image', 'url(' + $(e.target).attr('src') + ')')
    }).each(function() {
        if (this.complete) $(this).trigger('load');
    })

    $('.landing .overlay').hover(function(e) {
        $(e.target).closest('.landing').addClass('hovered')
    }, function(e) {
        $(e.target).closest('.landing').removeClass('hovered')
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

    if (SM.page == 'search') {
        SM.Algolia = algoliasearch(Algolia.APP_ID, Algolia.API_KEY);
        SM.Articles = SM.Algolia.initIndex('Article');

        var source = $("#search-template").html();
        SM.template = Handlebars.compile(source);
        Handlebars.registerHelper('formatDate', formatDate);

        SM.didUpdateSearch();
        $('#search .search-box').focus();
        $('#search .search-box').on('input', SM.didUpdateSearch);
    }
});



// Helper functions
function formatDate(dt, format) {
    return moment.unix(dt).format(format);
}
