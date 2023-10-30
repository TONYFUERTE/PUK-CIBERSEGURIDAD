$("#buttonAlertSimple").click(function(){
    alert("Esto es un Alert SIMPLE");
});
$("#buttonAlertConfirm").click(function(){
    var respuesta = confirm("Esto es un Alert CONFIRM");
    if(respuesta == true){
        $("#resultado").text("Has pulsado ACEPTAR en el alert");
    } else{
        $("#resultado").text("Has pulsado CANCELAR en el alert");
    }
});
$("#buttonAlertPrompt").click(function(){
    var texto = prompt("Esto es un Alert PROMPT");
    
    if(texto != null){
        $("#resultado").text("Tu texto es: "+texto);
    } 
});