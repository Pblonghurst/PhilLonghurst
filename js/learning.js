var please = Math.random();
    console.log(please);

const user = {
    name: "Phil",
    age: 20,
    height: 6,
    greet: function() {
        console.log("hello there")
    }
};

console.log(user.name);
user.greet();


var day;
switch (new Date().getDay()) {
case 0:
day = "Sunday!";
break;
case 1:
day = "Monday";
break;
case 2:
day = "Tuesday";
break;
case 3:
day = "Wednesday";
break;
case 4:
day = "Thursday";
break;
case 5:
day = "Friday!";
break;
case 6:
day = "Saturday!";
}

document.getElementById("futureAge").innerHTML = "today is " + day;

var i = 5;
while (i < 10) {
    function change () {
        document.getElementById("futureAge").textContent += i;      
    }
    i++;    
}
