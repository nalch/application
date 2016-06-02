// submit language form on language change
window.addEventListener('load', function(){
    $('#language-switcher').change(function(element) {
        element.currentTarget.submit();
    });
});