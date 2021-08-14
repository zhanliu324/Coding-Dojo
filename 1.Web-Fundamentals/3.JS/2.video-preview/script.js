console.log("page loaded...");

var my_video = document.querySelector("video") 

function playVid() {
    my_video.muted = true;
    my_video.play()
}

function pauseVid() {
    my_video.pause()
}