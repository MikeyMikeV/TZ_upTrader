function isEmpty( el ){
    return !$.trim(el.html())
}

$.fn.extend({
    treed: function (o) {

        var openedClass = 'opened';
        var closedClass = 'closed';

        var tree = $(this);
        tree.addClass("tree");
        tree.find('li').has("ul").each(function () {
            var branch = $(this); //li with children ul
            branch.addClass('branch closed');
            branch.on('click', function (e) {
                if (this == e.target) {
                    $(this).toggleClass(openedClass+' '+closedClass)
                    $(this).children().children().toggle();
                }
            })
            branch.children().children().toggle();
            if (isEmpty($(this).find('ul'))) {
                $(this).addClass('branch empty')
            }
        });
    }
});

$('.tree1').treed();

var selected_id = $(".menu").attr("id")
if (selected_id) {
    var selected = $('li[id="'+selected_id+'"]')
    $(selected).parents('li').children().children().toggle()
}