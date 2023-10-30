$("button#loginButton").click(function(){
    
    var valores = [];

    valores.push("USERNAME: "+$("#username").val());
    valores.push("PASSWORD: "+$("#password").val());
                
    $("#resultado").text(valores.join(","));  
    
    window.location.href = "/elements/fichar_tiempo";
});
