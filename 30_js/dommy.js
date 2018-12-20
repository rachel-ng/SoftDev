var something = -1
var something2 = 7

var fibonaccir = (n) => {
    return n < 2 ? n : fibonaccir(n-1) + fibonaccir(n-2);
}

var fibonacci = () => {
    var fib_output = document.getElementById("fiblist");
    var newli = document.createElement('li');

    something += 1
    
    newli.innerHTML = fibonaccir(something);
    fib_output.appendChild(newli);
}

var fib_button = document.getElementById("fb");

fib_button.addEventListener("click",fibonacci);






var title = document.getElementById("h");
var thelist = document.getElementById("thelist");
