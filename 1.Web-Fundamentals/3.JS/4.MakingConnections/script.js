var requestLines = [
    document.querySelector(".user-line#todd"),
    document.querySelector(".user-line#phil")
]

var requestNum = document.querySelector("#request-num")
var connectNum = document.querySelector("#connect-num")

function changeName() {
    document.querySelector("#user-name").innerText = "Name Changed"
}

function accept(idx) {
    requestLines[idx].remove(),
    requestNum.innerText--,
    connectNum.innerText++
}

function decline(idx) {
    requestLines[idx].remove(),
    requestNum.innerText--
}