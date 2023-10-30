
if(intervalo){
    clearInterval(intervalo);
}    
var current = 0;
var intervalo = setInterval(function(){        
    current = current +1;        
    $("div#contador").text("Han transcurrido..."+current+" segundos.");    

},1000);


//LÓGICA PARA IMPLICIT WAIT
setTimeout(function(){
    var botonImplicitWait =  $("<button/>", {
        text: "No aparezco hasta pasados 3 segundos después de cargar la web!",
        id: "implicitWaitButton",
        click: function(){
            $("#resultado").text("Has pulsado el botón IMPLICIT WAIT con éxito!");
        }
    });
    
    $("div#implicitWaitDiv").append(botonImplicitWait);
},3000);

//LÓGICA PARA IMPLICIT WAIT
setTimeout(function(){
    var botonExplicitWait =  $("<button/>", {
        text: "No aparezco hasta pasados 3 segundos después de cargar la web...y no me habilito hasta pasados 6!",
        id: "explicitWaitButton",
        click: function(){
            $("#resultado").text("Has pulsado el botón EXPLICIT WAIT con éxito!");
        }
    });
    
    botonExplicitWait.attr("disabled",true);
    
    $("div#explicitWaitDiv").append(botonExplicitWait);
},3000);

setTimeout(function(){
    $("#explicitWaitButton").attr("disabled",false);
},6000)
