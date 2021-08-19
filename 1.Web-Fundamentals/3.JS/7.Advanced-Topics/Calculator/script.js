var num1 = "";
var num2 = "";
var operator = null;
var displayDiv = document.querySelector("#display");

function clr() {
    num1 = "";
    num2 = "";
    operator = null;
    displayDiv.innerText = 0;
}

function press(digit) {
    if (operator == null) {
        num1 = num1 + digit;
        displayDiv.innerText = num1;
    } else {
        num2 = num2 + digit;
        displayDiv.innerText = num2;
    }
}

function setOP(op) {
    operator = op;
}

function calculate() {
    if (operator == "+") {
        result = num1 + num2;
    } else if (operator == "-") {
        result = num1 - num2;
    } else if (operator == "*") {
        result = num1 * num2;
    } else if (operator == "/") {
        result = num1 / num2;
    } else {
        result = 0;
    }
    displayDiv.innerText = result;
    num1 = "";
    num2 = "";
    operator = null;
}