(function($) {
    'use strict';
    $('#email, #confirm_password, #password').each(function() {
        $(this).on('blur', function() {
            if (validate('#email') == false) {
                showValidate('#email');
            } else if (hasWhiteSpace($('#email').val())) {
                showValidate('#email');
            } else {
                $('#email')
                    .parent()
                    .addClass('true-validate');
            }
            $('#confirm_password, #password').on(
                'change keyup paste',
                function() {
                    if (
                        // if the passwords arent equal or equal to null show error
                        $('#password').val() != $('#confirm_password').val() ||
                        $('#password').val() == undefined ||
                        hasWhiteSpace($('#password').val())
                    ) {
                        console.log('error');
                        showValidate('#confirm_password, #password');
                    } else {
                        $('#confirm_password, #password')
                            .parent()
                            .addClass('true-validate');
                    }
                    if (
                        $('#password').val() == $('#confirm_password').val() &&
                        $('#password').val() != undefined
                    ) {
                        $('#email, #confirm_password, #password').each(
                            function() {
                                $(this).focus(function() {
                                    hideValidate(this);
                                    $(this)
                                        .parent()
                                        .removeClass('true-validate');
                                });
                            }
                        );
                    }
                }
            );
        });
    });

    // var input = $('#username, #confirm_password, #password');
    // $('.validate-form').on('submit', function() {
    //     var check = true;
    //     for (var i = 0; i < input.length; i++) {
    //         if (validate(input[i]) == false) {
    //             showValidate(input[i]);
    //             check = false;
    //         }
    //     }
    //     return check;
    // });
    $('#email, #confirm_password, #password').each(function() {
        $(this).focus(function() {
            hideValidate(this);
            $(this)
                .parent()
                .removeClass('true-validate');
        });
    });
    function validate(input) {
        if (
            $(input).attr('type') == 'email' ||
            $(input).attr('name') == 'email'
        ) {
            if (
                $(input)
                    .val()
                    .trim()
                    .match(
                        /^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/
                    ) == null
            ) {
                return false;
            }
        } else {
            if (
                $(input)
                    .val()
                    .trim() == ''
            ) {
                return false;
            }
        }
    }

    function hasWhiteSpace(s) {
        return s.indexOf(' ') >= 0;
    }
    function showValidate(input) {
        var thisAlert = $(input).parent();
        //$(thisAlert).addClass('alert-validate');
        $(thisAlert).append('<span class="btn-hide-validate">&#xf135;</span>');
        $('.btn-hide-validate').each(function() {
            $(this).on('click', function() {
                hideValidate(this);
            });
        });
    }
    function hideValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).removeClass('alert-validate');
        $(thisAlert)
            .find('.btn-hide-validate')
            .remove();
    }
})(jQuery);
