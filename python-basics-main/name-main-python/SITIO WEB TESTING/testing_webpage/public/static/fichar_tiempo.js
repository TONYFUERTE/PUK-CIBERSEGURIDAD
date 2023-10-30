$("button#entrada").click(function(){			
    var tiempo = new Date();
    var minutos = String(tiempo.getMinutes()).padStart(2,"0");
    $("#resultado").text("Se ha tomado tu hora de ENTRADA a las: "+tiempo.getHours()+":"+minutos);
});

$("button#salida").click(function(){			
    var tiempo = new Date();
    var minutos = String(tiempo.getMinutes()).padStart(2,"0");
    $("#resultado").text("Se ha tomado tu hora de SALIDA a las: "+tiempo.getHours()+":"+minutos);
});
