function makeid(length, patron) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < 3; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    result += patron;
    for ( var i = 3; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
     }
    return result;
 }


//LÓGICA PARA XPath
$("button").each(function(){
    $(this).click(function(){
        alert("Has pulsado el botón: "+$(this).val()+" con atributo "+$(this).attr("randomattribute")+" y " + $(this).parent().attr("value") + " de XPATH");
    });
});

 
$('button').each(function(){
    $(this).attr("randomattribute",makeid(5,"KK"));
});

 //$('#buttonAlertSimple').attr("id",makeid(4));