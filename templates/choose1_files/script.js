/*! http://tinynav.viljamis.com v1.2 by @viljamis */
(function (a, k, g) {
    a.fn.tinyNav = function (l) {
        var c = a.extend({active: "selected", header: "", indent: "- ", label: ""}, l);
        return this.each(function () {
            g++;
            var h = a(this), b = "tinynav" + g, f = ".l_" + b, e = a("<select/>").attr("id", b).addClass("tinynav " + b);
            if (h.is("ul,ol")) {
                "" !== c.header && e.append(a("<option/>").text(c.header));
                var d = "";
                h.addClass("l_" + b).find("a").each(function () {
                    d += '<option value="' + a(this).attr("href") + '">';
                    var b;
                    for (b = 0; b < a(this).parents("ul, ol").length - 1; b++)d += c.indent;
                    d += a(this).text() + "</option>"
                });
                e.append(d);
                c.header || e.find(":eq(" + a(f + " li").index(a(f + " li." + c.active)) + ")").attr("selected", !0);
                e.change(function () {
                    k.location.href = a(this).val()
                });
                a(f).after(e);
                c.label && e.before(a("<label/>").attr("for", b).addClass("tinynav_label " + b + "_label").append(c.label))
            }
        })
    }
})(jQuery, this, 0);

function longnavi() {
    var counter = 0;
    if ($("section#menu").css('display') != 'none') {
        if ($('section#menu ol').outerWidth() + 40 > $('section#menu li:not(.logo)').outerWidth() && $(window).width() > 500) {
            $('section#menu ol').append('<li class="more"><a href="#" class="more_btn">Ещё &darr;</a></li>');
            while ($('section#menu ol').outerWidth() + 40 > $('section#menu li:not(.logo)').outerWidth() && counter < 150) {
                $('section#menu ol > li:not(.more):visible:last').hide();
                counter++;
            }
            $('section#menu ol > li:hidden').wrapAll('<div class="more_nav"></div>');
            $("div.more_nav").appendTo("li.more").css("top", $('section#menu ol').height() + 10);
            $('div.more_nav li:hidden').each(function () {
                $(this).show().css('display', 'block');
            });
        }
        $('section#menu ol').css('visibility', 'visible');
    }
}


$(document).ready(function () {
    longnavi();

    $("section#mobile a.block").click(function (e) {
        e.preventDefault();
        $("section#mobile ul.slideMenu").slideToggle();
    });

    $(document).on("mouseenter", "li.more", function () {
        $("div.more_nav").slideDown(100);
    });

    $(document).on("mouseleave", "section#menu", function () {
        $("div.more_nav").slideUp(100);
    });
});