var something = -1;
var something2 = 7;


var fiblist = document.getElementById("fiblist");

var fibonaccir = () => {
    var fibitemsinlist = fiblist.querySelectorAll("li");
    console.log(fibitemsinlist);

    if (fibitemsinlist.length < 2) {
	return fibitemsinlist.length;
    }
    else {
	console.log(fibitemsinlist[fibitemsinlist.length - 1]);
	console.log(fibitemsinlist[fibitemsinlist.length - 2]);

	var newnum = parseInt(fibitemsinlist[fibitemsinlist.length - 1].innerHTML) + parseInt(fibitemsinlist[fibitemsinlist.length - 2].innerHTML);
	return newnum;
    }
}

var fibonacci = () => {
    var fib_output = document.getElementById("fiblist");
    var newli = document.createElement('li');

    newli.innerHTML = fibonaccir();
    fib_output.appendChild(newli);

    console.log(newli.innerHTML);
}

var fib_button = document.getElementById("fb");

fib_button.addEventListener("click",fibonacci);







var title = document.getElementById("h");
var thelist = document.getElementById("thelist");

var titlelist = () => {
  var newli = document.createElement('li');
  something2 += 1;

  newli.innerHTML = "item " + something2;
  thelist.appendChild(newli);
  addlistener(newli);
}

var the_button = document.getElementById("b");

the_button.addEventListener("click",titlelist);





var og = title.innerHTML;

var titlechange = (newt) => {
  title.innerHTML = newt;
}

var addlistener = (itname) => {
  var newtitle = itname.innerHTML;
  itname.addEventListener("mouseout",
                          function(){
                            titlechange(og);
                            itname.classList.remove("red");
                            itname.removeAttribute("style");
                          });
  itname.addEventListener("mouseover",
                          function(){
                            titlechange(newtitle);
                            itname.classList.add("red");
                            itname.setAttribute("style","font-size: 100px; margin-left: 100px;");
                          });
  itname.addEventListener("click",
                          function(){
                            itname.remove();
                          });
  // console.log(itname.innerHTML);
}

var itemsinlist = thelist.querySelectorAll("li");
// console.log(itemsinlist);

for (var i = 0; i < itemsinlist.length; i++) {
  addlistener(itemsinlist[i]);
}
