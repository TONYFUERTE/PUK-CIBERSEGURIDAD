$("button#enviarRadiobutton").click(function(){
			
    var seleccionados = [];
    $.each($("input[type='radio']:checked"), function(){            
        seleccionados.push($(this).val());
    });
                
    $("#resultado").text(seleccionados.join(","));
});
