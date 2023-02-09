$(document).ready(function () {
    $("a.toggled").click(function (e) {
        e.preventDefault();
        var target = $(this).data('id');
        $('div#'+target).toggle(300);
    });
});