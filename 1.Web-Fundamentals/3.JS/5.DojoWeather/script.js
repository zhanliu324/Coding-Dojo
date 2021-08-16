function removeAlert() {
    document.querySelector(".bottom").remove()
}

var celsius = [24, 18, 27, 19, 21, 16, 26, 21]
var fahrenheit = [75, 65, 80, 66, 69, 61, 78, 70]
var temperatures = [
    document.querySelector("#today .high"),
    document.querySelector("#today .low"),
    document.querySelector("#tomorrow .high"),
    document.querySelector("#tomorrow .low"),
    document.querySelector("#friday .high"),
    document.querySelector("#friday .low"),
    document.querySelector("#saturday .high"),
    document.querySelector("#saturday .low")
]

function changeTempUnit(element) {
    console.log(element.value);
    if (element.value == "celsius") {
        for (var index = 0; index < 8; index++) {
            temperatures[index].innerText = celsius[index] + "°";
        }
    } else {
        for (var index = 0; index < 8; index++) {
            temperatures[index].innerText = fahrenheit[index] + "°";
        }
    }
}