// submit language form on language change
window.addEventListener('load', function(){
    $('#language-switcher').change(function(element) {
        console.log(element.currentTarget);
        element.currentTarget.submit();
    });
});