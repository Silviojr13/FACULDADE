function somar (){

    var valor1 = parseInt(document.getElementById("valor1").value);
    var valor2 = parseInt(document.getElementById("valor2").value);

    /* na linha 7 a variavel resultOP1 é responsavel por dar um print na tela do resultado*/

    var resultOP1 = document.getElementById("resutadoOp1");

    var soma = valor1 + valor2;


    resultOP1.value = soma;
}

function limpar1 (){
    
    var resultado = document.getElementById("resutadoOp1");
    var inputValor1 = document.getElementById("valor1");
    var inputValor2 = document.getElementById("valor2");

    resultado.value = "";
    inputValor1.value = "";
    inputValor2.value = "";
}

function subtrair (){
    var subtrair1 = parseInt(document.getElementById("subtrair1").value);
    var subtrair2 = parseInt(document.getElementById("subtrair2").value);

    var resultOP2 = document.getElementById("resutadoOp2");

    var subtrair = subtrair1 - subtrair2;

    resultOP2.value = subtrair
}

function limpar2 (){
    
    var resultado = document.getElementById("resutadoOp2");
    var inputValor1 = document.getElementById("subtrair1");
    var inputValor2 = document.getElementById("subtrair2");

    resultado.value = "";
    inputValor1.value = "";
    inputValor2.value = "";
}

function multiplicar (){
    var multiplicar1 = parseInt(document.getElementById("multiplicar1").value);
    var multiplicar2 = parseInt(document.getElementById("multiplicar2").value);

    var resultOP3 = document.getElementById("resutadoOp3");

    var multiplicar = multiplicar1 * multiplicar2;

    resultOP3.value = multiplicar
}

function limpar3 (){
    
    var resultado = document.getElementById("resutadoOp3");
    var inputValor1 = document.getElementById("multiplicar1");
    var inputValor2 = document.getElementById("multiplicar2");

    resultado.value = "";
    inputValor1.value = "";
    inputValor2.value = "";
}

function dividir (){
    var dividir1 = parseInt(document.getElementById("dividir1").value);
    var dividir2 = parseInt(document.getElementById("dividir2").value);

    var resultOP4 = document.getElementById("resutadoOp4");

    var dividir = dividir1 / dividir2;

    resultOP4.value = dividir
}

function limpar4 (){
    
    var resultado = document.getElementById("resutadoOp4");
    var inputValor1 = document.getElementById("dividir1");
    var inputValor2 = document.getElementById("dividir2");

    resultado.value = "";
    inputValor1.value = "";
    inputValor2.value = "";
}

function cor() {
    
    var corr = document.getElementById("color");
    corr.style.backgroundColor = "#EE5000";  
}