
$( document ).ready(function() {
    

    $("#boton1").click(function(){    
        $("#resultado").text("HAS PULSADO EL BOTÓN DE ROOT DOM");    
    });
    
    var shadowHost = document.querySelector('#nodoShadowHost');
    
    var shadowRoot = shadowHost.attachShadow ({mode : 'open'});
    

    shadowRoot.innerHTML = `
    <div id="seccion1">
        <label>ESTE APARTADO ESTÁ EN EL SHADOW DOM</label>
        <div><button id="boton2">Botón en SHADOW DOM</button></div>
        <h2>Mensaje:</h2>
        <div id="resultado"></div>
    </div>
    `

    var script = document.createElement("script");
    script.textContent = `

        var shadow = document.querySelector("#nodoShadowHost").shadowRoot;
        
        shadow.getElementById("boton2").addEventListener("click", function(){
            shadow.getElementById("resultado").textContent = "HAS PULSADO EL BOTÓN DE SHADOW DOM";
        });
    `;
    shadowRoot.appendChild(script);

});

