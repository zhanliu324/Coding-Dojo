var requestLines = [
    document.querySelector(".user-line#todd"),
    document.querySelector(".user-line#phil")
]

var requestNum = document.querySelector("#request-num")
var connectNum = document.querySelector("#connect-num")
var requests = 2
var connections = 418

function changeName() {
    document.querySelector("#user-name").innerText = "Name Changed"
}

function accept(idx) {
    requestLines[idx].remove(),
    requests -= 1,
    requestNum.innerText = requests,
    connections += 1,
    connectNum.innerText = connections
}

function decline(idx) {
    requestLines[idx].remove(),
    requests -= 1,
    requestNum.innerText = requests
}