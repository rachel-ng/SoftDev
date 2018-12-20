// team Cygnus... Vismund Cygnus
// SoftDev pd7
// K29 -- sequential progression progression
// 2018-12-20

var fib_output = document.getElementById("fib_output");
var gcd_output = document.getElementById("gcd_output");
var rand_output = document.getElementById("rand_output");

var fib_input = document.getElementById("fib_input");
var gcd_input1 = document.getElementById("gcd_input1");
var gcd_input2 = document.getElementById("gcd_input2");


var fibonaccir = (n) => {
    return n < 2 ? n : fibonaccir(n-1) + fibonaccir(n-2);
}

var fibonacci = () => {
    fib_output.innerHTML = fibonaccir(fib_input.value);
}

var gcd = () => {
    a = gcd_input1.value;
    b = gcd_input2.value;
	console.log(a + ", " + b);
    var max = 1;
    for(var i = 1; i <= a && i <= b; i += max)
	if(a % i === 0 && b % i === 0)
	    max = i;
    gcd_output.innerHTML = max;
}

KREWES = [
    ['William Lu', 'Qian', 'Peter', 'Ahnaf', 'Kenny', 'Sophia', 'Sajed', 'Emily', 'Hasif', 'Brian ', 'Dennis', 'Jiayang', 'Shafali ', 'Isaac ', 'Tania', 'Derek', 'Shin', 'Vincent', 'Ricky', 'Puneet', 'Wei Wen', 'Tim', 'Jeffrey', 'Joyce ', 'Mohtasim', 'Simon', 'Thomas', 'Ray', 'Jack', 'Karen', 'Robin', 'Jabir', 'Johnny ', 'Matthew', 'Johnson Li', 'Angela', 'Crystal', 'Jiajie', 'Theodore (Dont really care)', 'Anton', 'Max', 'Bo', 'Andrew', 'Kendrick', 'Kevin', 'Kyle', 'Jamil', 'Mohammed', 'Ryan', 'Jason'],
    ['Daniel', 'Aleksandra', 'Addison', 'Hui Min', 'Aaron', 'Rubin', 'Raunak', 'Stefan', 'Cheryl', 'Cathy', 'Mai', 'Claire ', 'Alex', 'Bill', 'Daniel', 'Jason'],
    ['Derek', 'Britni', 'Joan', 'Vincent', 'Jared', 'Ivan', 'Thomas', 'Maggie', 'Damian', 'Tina', 'Fabiha', 'John', 'Susan ', 'Kaitlin', 'Michelle', 'Clara', 'Rachel', 'Amit', 'Jerry', 'Raymond', 'Zane', 'Soojin', 'Maryann', 'Adil', 'Josh', 'Imad']
]


var randomStudent = () => {
    // come to the computer interaction club
    students = KREWES[Math.floor(Math.random()*KREWES.length)];
    rand_output.innerHTML = students[Math.floor(Math.random()*students.length)];
}


var fib_button = document.getElementById("fib_button");
var gcd_button = document.getElementById("gcd_button");
var rand_button = document.getElementById("rand_button");

fib_button.addEventListener("click", fibonacci);
gcd_button.addEventListener("click", gcd);
rand_button.addEventListener("click", randomStudent);
