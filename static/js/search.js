SM.didUpdateSearch = function() {
    var query = $('#search .search-box').val();

    SM.Articles.search(query, function(err, data) {
        if (err) {
            console.error(err);
        } else {
            var html = SM.template(data);
            $('#search .content').html(html);
        }
    });
}
