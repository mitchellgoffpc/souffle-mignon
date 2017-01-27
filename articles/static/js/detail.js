// Initialization
SM.state.linkPosition = 'TOP';
SM.state.showCommentTextbox = false;

// Sharing
SM.shareFacebook = function() {
    FB.ui({
        method: 'share',
        href: window.location.href });
}

// Link positions
SM.checkLinkPosition = function() {
    var scrollPos = $(window).scrollTop();
    var entryPos = $('#article .entry').offset().top;
    var entryHeight = $('#article .entry').height();
    var linkHeight = $('#article .links').height();

    if (scrollPos < entryPos - 100)
        SM.updateLinkPosition('TOP');
    else if (scrollPos > entryPos + entryHeight - linkHeight - 220)
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



// Like event handler
SM.didClickLikeArticle = function() {
    if ($('#article .link.like').attr('data-action') == 'show-login') {
        SM.showLoginModal();
    } else if ($('#article .link.like').attr('data-action') == 'like') {
        $('#article .link.like').addClass('selected').attr('data-action', 'unlike');
        $('#article .link.like span').addClass('fa-heart').removeClass('fa-heart-o');
        SM.like({ type: 'article', action: 'create', id: SM.article });
    } else if ($('#article .link.like').attr('data-action') == 'unlike') {
        $('#article .link.like').removeClass('selected').attr('data-action', 'like');
        $('#article .link.like span').addClass('fa-heart-o').removeClass('fa-heart');
        SM.like({ type: 'article', action: 'delete', id: SM.article });
    }
}

SM.didClickLikeComment = function(e) {
    var counter = $(e.target).closest('.response').find('.like-count');

    if ($(e.target).attr('data-action') == 'show-login') {
        SM.showLoginModal();
    } else if ($(e.target).attr('data-action') == 'like') {
        counter.html(parseInt(counter.text()) + 1);
        $(e.target).addClass('selected').attr('data-action', 'unlike');
        $(e.target).addClass('fa-heart').removeClass('fa-heart-o');
        SM.like({ type: 'comment', action: 'create', id: $(e.target).attr('data-id') });
    } else if ($(e.target).attr('data-action') == 'unlike') {
        counter.html(parseInt(counter.text()) - 1);
        $(e.target).removeClass('selected').attr('data-action', 'like');
        $(e.target).addClass('fa-heart-o').removeClass('fa-heart');
        SM.like({ type: 'comment', action: 'delete', id: $(e.target).attr('data-id') });
    }
}



// Comment event handlers
SM.didClickComment = function() {
    var write = $('#article .responses .write');

    if (write.attr('data-action') == 'show-login') {
        SM.showLoginModal();
    } else if (write.attr('data-action') == 'comment' && !SM.state.showCommentTextbox) {
        SM.state.showCommentTextbox = true;
        SM.showCommentTextbox();
    }
}
SM.didClickOutsideComment = function() {
    var write = $('#article .responses .write');

    if (SM.state.showCommentTextbox && write.find('.textbox').html().length == 0) {
        SM.state.showCommentTextbox = false;
        SM.hideCommentTextbox();
    }
}

SM.showCommentTextbox = function() {
    var write = $('#article .responses .write');
    write.find('.name-wrapper .lbl').velocity({ marginTop: -18 }, 100);
    write.velocity({ height: write.get(0).scrollHeight }, 200, function() {
        write.height('auto');
        write.find('.textbox').focus();
    });
}
SM.hideCommentTextbox = function() {
    var write = $('#article .responses .write');
    write.find('.name-wrapper .lbl').velocity({ marginTop: 0 }, 100);
    write.css({ height: write.height() });
    write.velocity({ height: 80 }, 200);
}



SM.didClickPublishComment = function() {
    var write = $('#article .responses .write');
    var entry = htmlToText(write.find('.textbox').html());
    var data = { action: 'create', article: SM.article, entry: entry };
    write.find('.spinner').show();

    SM.post('/articles/comment/', data, function(result) {
        SM.state.showCommentTextbox = false;
        SM.hideCommentTextbox();
        write.find('.textbox').html('');
        write.find('.spinner').hide();
        write.after(result);
    }, function() {
        write.find('.spinner').hide();
    });
}



// Ajax functions
SM.like = function(data) { SM.post('/articles/like/', data); }
SM.comment = function(data) { SM.post('/articles/comment/', data); }

SM.post = function(url, data, success, error) {
    $.post({
        url: url,
        data: data,
        headers: { 'X-CSRFToken': Cookies.get('csrftoken') },
        success: success,
        error: error });
}
