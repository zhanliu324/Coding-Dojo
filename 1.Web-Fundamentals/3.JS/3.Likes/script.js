var likes = [0,0,0]
var neilLikes = document.querySelector("#neil-m")
var nicholeLikes = document.querySelector("#nichole-k")
var jimLikes = document.querySelector("#jim-r")

function likeNeil() {
    likes[0] += 1;
    neilLikes.innerText = likes[0] + " likes(s)"
}

function likeNichole() {
    likes[1] += 1;
    nicholeLikes.innerText = likes[1] + " likes(s)"
}

function likeJim() {
    likes[2] += 1;
    jimLikes.innerText = likes[2] + " likes(s)"
}