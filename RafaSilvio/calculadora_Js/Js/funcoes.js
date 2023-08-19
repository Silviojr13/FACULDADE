function somar (){
    var valor1 = parseInt(document.getElementById("valor1").value);
    var valor2 = parseInt(document.getElementById("valor2").value);
    var resultOP1 = document.getElementById("resutadoOp1");

    var soma = valor1 + valor2;

    resultOP1.value = soma;
}

function subtrair (){
    var subtrair1 = parseInt(document.getElementById("subtrair1").value);
    var subtrair2 = parseInt(document.getElementById("subtrair2").value);

    var subtrair = subtrair1 - subtrair2;

    alert(subtrair);
}

function multiplicar (){
    var multiplicar1 = parseInt(document.getElementById("multiplicar1").value);
    var multiplicar2 = parseInt(document.getElementById("multiplicar2").value);

    var multiplicar = multiplicar1 * multiplicar2;

    alert(multiplicar);
}

function dividir (){
    var dividir1 = parseInt(document.getElementById("dividir1").value);
    var dividir2 = parseInt(document.getElementById("dividir2").value);

    var dividir = dividir1 / dividir2;

    alert(dividir);
}