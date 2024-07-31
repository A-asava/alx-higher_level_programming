$('document').ready(function(){
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data){
        console.log(data)
        $("DIV#hello").text(data.hello);
    });
})
