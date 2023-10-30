$("button#enviaComboboxes").click(function(){
    var seleccionados = [];
    $.each($("#combobox1 option:selected"), function(){            
        seleccionados.push($(this).val());
    });
    
    $.each($("#combobox2 option:selected"), function(){            
        seleccionados.push($(this).val());
    });
    
    $("#resultado").text(seleccionados.join(","));
});