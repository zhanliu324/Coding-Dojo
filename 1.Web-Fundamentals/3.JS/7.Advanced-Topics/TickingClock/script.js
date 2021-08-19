function getSecondsSinceStartOfDay() {
    return new Date().getSeconds() + 
      new Date().getMinutes() * 60 + 
      new Date().getHours() * 3600;
}

setInterval( function() {
    var time = getSecondsSinceStartOfDay();
    console.log(time);
    // your code here
    var hour = time / 3600;
    if (hour > 12) {
        hour = hour - 12;
    };
    document.getElementById("hour").style.setProperty("--hourDeg", "rotate("+(hour/12*360+180)+"deg)");
    document.getElementById("minutes").style.setProperty("--minDeg", "rotate("+(time%3600/60/60*360+180)+"deg)");
    document.getElementById("seconds").style.setProperty("--secDeg", "rotate("+(time%60/60*360+180)+"deg)");
}, 1000);
