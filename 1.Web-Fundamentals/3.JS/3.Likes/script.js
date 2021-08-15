var likes = [9,12,9]
var spans = [
    document.querySelector("#neil-m"),
    document.querySelector("#nichole-k"),
    document.querySelector("#jim-r"),
]
function like(idx) {
    likes[idx] += 1;
    spans[idx].innerText = likes[idx] + " likes(s)"
}
