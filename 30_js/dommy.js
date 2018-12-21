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

var titlelist = () => {
  var newli = document.createElement('li');
  something2 += 1

  newli.innerHTML = "item " + something2;
  thelist.appendChild(newli);
  addlistener(newli)
}

var the_button = document.getElementById("b");

the_button.addEventListener("click",titlelist);



var titlechange = (newt) => {
  title.innerHTML = newt;
}

var addlistener = (itname) => {
  var newtitle = itname.innerHTML;
  itname.addEventListener("mouseover",function(){titlechange(newtitle)});
  itname.addEventListener("click",function(){itname.remove()});
  console.log(itname.innerHTML);
}

var itemsinlist = thelist.querySelectorAll("li");
console.log(itemsinlist);

for (var i = 0; i < itemsinlist.length; i++) {
  addlistener(itemsinlist[i]);
}

var og = title.innerHTML

title.addEventListener("mouseover",function(){titlechange(og)});
