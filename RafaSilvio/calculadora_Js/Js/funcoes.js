function somar (){

    var valor1 = parseInt(document.getElementById("valor1").value);
    var valor2 = parseInt(document.getElementById("valor2").value);

    /* na linha 7 a variavel resultOP1 é responsavel por dar um print na tela do resultado*/

    var resultOP1 = document.getElementById("resutadoOp1");

    var soma = valor1 + valor2;

    resultOP1.value = soma;
}

function subtrair (){
    var subtrair1 = parseInt(document.getElementById("subtrair1").value);
    var subtrair2 = parseInt(document.getElementById("subtrair2").value);

    var resultOP2 = document.getElementById("resutadoOp1");

    var subtrair = subtrair1 - subtrair2;

    resultOP2.value = subtrair
}

function multiplicar (){
    var multiplicar1 = parseInt(document.getElementById("multiplicar1").value);
    var multiplicar2 = parseInt(document.getElementById("multiplicar2").value);

    var resultOP3 = document.getElementById("resutadoOp1");

    var multiplicar = multiplicar1 * multiplicar2;

    resultOP3.value = multiplicar
}

function dividir (){
    var dividir1 = parseInt(document.getElementById("dividir1").value);
    var dividir2 = parseInt(document.getElementById("dividir2").value);

    var resultOP4 = document.getElementById("resutadoOp1");

    var dividir = dividir1 / dividir2;

    resultOP4.value = dividir
}