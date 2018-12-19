Jiayang Chen, Rachel Ng
SoftDev1 pd7
K28 -- Sequential Progression
2018-12-18

var fibonacci = (n) => {
    var first = 0;
    var second = 1;
    for (i = 0; i < n; i++) {
	var temp = second;
	second += first;
	first = temp;
    }
    return first;
}

var gcd = (a,b) => {
    var max = 1;
    for (i = 1; i <= Math.min(a,b); i++) {
	if (a % i == 0 && b % i == 0) {
	    max = i;
	}
    }
    return max;
}


var randomStudent = () => {
    var names = ["Marcene Bradly", "Harold Bivens", "Jamel Degregorio", "Eunice Lastinger", "Loura Nickelson", "Ruthanne Oxford","Bret Goodpaster",  "Terri Fray",  "Sanford Feenstra",  "Stella Taber",  "Benito Hocutt",  "Katerine Bolenbaugh",  "Darrell Thorpe",  "Helga Wrona",  "Denny Bonet",  "Sumiko Hennessy",  "Lavada Sottile",  "Karina Woodall",  "Karyn Gutierres","Quiana Kottwitz"];
    var i = Math.floor(Math.random() * names.length);
    return names[i];
}
