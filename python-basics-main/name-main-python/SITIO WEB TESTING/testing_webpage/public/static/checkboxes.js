$("button#enviarCheckboxbutton").click(function(){
			
    var seleccionados = [];
    $.each($("input[type='checkbox']:checked"), function(){            
        seleccionados.push($(this).val());
    });
                
    $("#resultado").text(seleccionados.join(","));
});