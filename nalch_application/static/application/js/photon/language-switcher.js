window.addEventListener('load', function (){
    var form = $('#language-switcher');
    $('#language-switcher .language-link a').each(function (index, item) {
        item.addEventListener("click", function () {
            var input = $('#language')[0];
            input.value = item.getAttribute('value');
            form.submit();
        });
    });
});