(function ($) {
    $.fn.shorten = function (settings) {

        var config = {
            showChars: 100,
            ellipsesText: "...",
            moreText: "more",
            lessText: "less"
        };

        if (settings) {
            $.extend(config, settings);
        }

        $(document).off("click", '.morelink');

        $(document).on({
            click: function () {

                var $this = $(this);
                if ($this.hasClass('less')) {
                    $this.removeClass('less');
                    $this.html(config.moreText);
                } else {
                    $this.addClass('less');
                    $this.html(config.lessText);
                }
                $this.parent().prev().toggle();
                $this.prev().toggle();
                return false;
            }
        }, '.morelink');

        return this.each(function () {
            var $this = $(this);
            if ($this.hasClass("shortened")) return;

            $this.addClass("shortened");
            var content = $this.html();
            if (content.length > config.showChars) {
                var c = content.substr(0, config.showChars);
                var h = content.substr(config.showChars, content.length - config.showChars);
                var html = c + '<span class="moreellipses">' + config.ellipsesText + ' </span><span class="morecontent"><span>' + h + '</span> <a href="#" class="morelink">' + config.moreText + '</a></span>';
                $this.html(html);
                $(".morecontent span").hide();
            }
        });

    };

})(jQuery);
var makeShorten = function () {
    $("td.address>span:not(:contains('Не назначен'))").shorten({
        "showChars": 0,
        "ellipsesText": "",
        "moreText": "показать",
        "lessText": "скрыть"
    });
    //td.comment
    $("td.comment").shorten({
        "showChars": 8,
        "ellipsesText": "...",
        "moreText": "показать",
        "lessText": "скрыть"
    });
    $('.headerAddress').append(' <a href="#" class="toggle_morelink">[+]</a>');
    $('a.toggle_morelink').on('click', function () {
        var text = $(this).text();
        $(this).text(text == '[+]' ? '[-]' : '[+]');
        $("td.address a.morelink").click();
    });

};
makeShorten();