$(document).ready( function() {
    $('#increment').click(function (e) {
        $('#input-number').val( parseInt($('#input-number').val()) + 1 );
    })

    $('#decrement').click(function (e) {
        $('#input-number').val( parseInt($('#input-number').val()) - 1 );
    })
     $('#increment1').click(function (e) {
        $('#input-number1').val( parseInt($('#input-number1').val()) + 1 );
    })

    $('#decrement1').click(function (e) {
        $('#input-number1').val( parseInt($('#input-number1').val()) - 1 );
    })
     $('#increment2').click(function (e) {
        $('#input-number2').val( parseInt($('#input-number2').val()) + 1 );
    })

    $('#decrement2').click(function (e) {
        $('#input-number2').val( parseInt($('#input-number2').val()) - 1 );
    })

});

// js code for increment decrement button

