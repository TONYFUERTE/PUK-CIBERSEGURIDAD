document.addEventListener("DOMContentLoaded", function(event) { 
    
    
    $("button#iframebutton").click(function(){       
        var texto = $("#iframebutton").text()
        $("#iframetext").text("HAS PULSADO EL BOTON: "+texto);
    });
  });