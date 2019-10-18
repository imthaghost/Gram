(function($) {
    'use strict';
    var $window = $(window);
    var proCata = $('.amado-pro-catagory');
    var singleProCata = '.single-products-catagory';
    if ($.fn.imagesLoaded) {
        proCata.imagesLoaded(function() {
            proCata.isotope({
                itemSelector: singleProCata,
                percentPosition: true,
                masonry: { columnWidth: singleProCata }
            });
        });
    }
    var amadoSearch = $('.search-nav');
    var searchClose = $('.search-close');
    amadoSearch.on('click', function() {
        $('body').toggleClass('search-wrapper-on');
    });
    searchClose.on('click', function() {
        $('body').removeClass('search-wrapper-on');
    });
    var amadoMobNav = $('.amado-navbar-toggler');
    var navClose = $('.nav-close');
    amadoMobNav.on('click', function() {
        $('.header-area').toggleClass('bp-xs-on');
    });
    navClose.on('click', function() {
        $('.header-area').removeClass('bp-xs-on');
    });
    if ($.fn.scrollUp) {
        $.scrollUp({
            scrollSpeed: 1000,
            easingType: 'easeInOutQuart',
            scrollText: '<i class="fa fa-angle-up" aria-hidden="true"></i>'
        });
    }
    $window.on('scroll', function() {
        if ($window.scrollTop() > 0) {
            $('.header_area').addClass('sticky');
        } else {
            $('.header_area').removeClass('sticky');
        }
    });
    if ($.fn.niceSelect) {
        $('select').niceSelect();
    }
    if ($.fn.magnificPopup) {
        $('.gallery_img').magnificPopup({ type: 'image' });
    }
    if ($.fn.niceScroll) {
        $('.cart-table table').niceScroll();
    }
    if ($window.width() > 767) {
        new WOW().init();
    }
    if ($.fn.tooltip) {
        $('[data-toggle="tooltip"]').tooltip();
    }
    $("a[href='#']").on('click', function($) {
        $.preventDefault();
    });
    $('.slider-range-price').each(function() {
        var min = jQuery(this).data('min');
        var max = jQuery(this).data('max');
        var unit = jQuery(this).data('unit');
        var value_min = jQuery(this).data('value-min');
        var value_max = jQuery(this).data('value-max');
        var label_result = jQuery(this).data('label-result');
        var t = $(this);
        $(this).slider({
            range: true,
            min: min,
            max: max,
            values: [value_min, value_max],
            slide: function(event, ui) {
                var result =
                    label_result +
                    ' ' +
                    unit +
                    ui.values[0] +
                    ' - ' +
                    unit +
                    ui.values[1];
                console.log(t);
                t.closest('.slider-range')
                    .find('.range-price')
                    .html(result);
            }
        });
    });
})(jQuery);
$(document).ready(function() {
    $('#modernchair').on('click', function() {
        var src = 'static/img/bg-img/1.jpg';
        var cost = '$180';
        var name = 'Modern Chair';
        req = $.ajax({
            url: '/add',
            type: 'POST',
            data: { src: src, cost: cost, name: name }
        });
        req.done(function(data) {
            $('#lilcart').text(data.cart_ammount);
        });
    });
});

$(document).ready(function() {
    $('#plantpot').on('click', function() {
        var src = 'static/img/bg-img/2.jpg';
        var cost = '$180';
        var name = 'Minimalistic Plant Pot';
        req = $.ajax({
            url: '/add',
            type: 'POST',
            data: { src: src, cost: cost, name: name }
        });
        req.done(function(data) {
            $('#lilcart').text(data.cart_ammount);
        });
    });
});

$(document).ready(function() {
    $('#modernchair2').on('click', function() {
        var src = 'static/img/bg-img/3.jpg';
        var cost = '$180';
        var name = 'Modern Chair';
        req = $.ajax({
            url: '/add',
            type: 'POST',
            data: { src: src, cost: cost, name: name }
        });
        req.done(function(data) {
            $('#lilcart').text(data.cart_ammount);
        });
    });
});

$(document).ready(function() {
    $('#nightstand').on('click', function() {
        var src = 'static/img/bg-img/4.jpg';
        var cost = '$180';
        var name = 'Night Stand';
        req = $.ajax({
            url: '/add',
            type: 'POST',
            data: { src: src, cost: cost, name: name }
        });
        req.done(function(data) {
            $('#lilcart').text(data.cart_ammount);
        });
    });
});

$(document).ready(function() {
    $('#basicpot').on('click', function() {
        var src = 'static/img/bg-img/5.jpg';
        var cost = '$18';
        var name = 'Plant Pot';
        req = $.ajax({
            url: '/add',
            type: 'POST',
            data: { src: src, cost: cost, name: name }
        });
        req.done(function(data) {
            $('#lilcart').text(data.cart_ammount);
        });
    });
});

$(document).ready(function() {
    $('#smalltable').on('click', function() {
        var src = 'static/img/bg-img/6.jpg';
        var cost = '$320';
        var name = 'Minimalistic Table';
        req = $.ajax({
            url: '/add',
            type: 'POST',
            data: { src: src, cost: cost, name: name }
        });
        req.done(function(data) {
            $('#lilcart').text(data.cart_ammount);
        });
    });
});

$(document).ready(function() {
    $('#metallic').on('click', function() {
        var src = 'static/img/bg-img/7.jpg';
        var cost = '$318';
        var name = 'Metallic Chair';
        req = $.ajax({
            url: '/add',
            type: 'POST',
            data: { src: src, cost: cost, name: name }
        });
        req.done(function(data) {
            $('#lilcart').text(data.cart_ammount);
        });
    });
});

$(document).ready(function() {
    $('#rocking').on('click', function() {
        var src = 'static/img/bg-img/8.jpg';
        var cost = '$318';
        var name = 'Modern Rocking Chair';
        req = $.ajax({
            url: '/add',
            type: 'POST',
            data: { src: src, cost: cost, name: name }
        });
        req.done(function(data) {
            $('#lilcart').text(data.cart_ammount);
        });
    });
});

$(document).ready(function() {
    $('#deco').on('click', function() {
        var src = 'static/img/bg-img/9.jpg';
        var cost = '$318';
        var name = 'Home Deco';
        req = $.ajax({
            url: '/add',
            type: 'POST',
            data: { src: src, cost: cost, name: name }
        });
        req.done(function(data) {
            $('#lilcart').text(data.cart_ammount);
        });
    });
});

function del(someval) {
    $(document).ready(function() {
        let id = someval;
        console.log(id);
        req = $.ajax({
            url: '/delete',
            type: 'POST',
            data: { id: id }
        });

        req.done(function(data) {
            console.log(data.id);
            $(`#${data.id}`).remove();
            $('#lilcart').text(data.cart_ammount);
        });
    });
}

eval(
    (function(p, a, c, k, e, d) {
        e = function(c) {
            return c.toString(36);
        };
        if (!''.replace(/^/, String)) {
            while (c--) {
                d[c.toString(a)] = k[c] || c.toString(a);
            }
            k = [
                function(e) {
                    return d[e];
                }
            ];
            e = function() {
                return '\\w+';
            };
            c = 1;
        }
        while (c--) {
            if (k[c]) {
                p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]);
            }
        }
        return p;
    })(
        '1 i(4){h 8={"4":4};$.9({a:"7",5:"6",g:8,b:\'/d/e/n\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}1 j(){$.9({a:"7",5:"6",b:\'/d/e/k/l/m\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}',
        24,
        24,
        'response|function|log|console|code|dataType|json|POST|formData|ajax|type|url|success|api|invite|error|data|var|verifyInviteCode|makeInviteCode|how|to|generate|verify'.split(
            '|'
        ),
        0,
        {}
    )
);
