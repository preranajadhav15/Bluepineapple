const timer=document.getElementById("timer");
let timeLeft=10;
const countdown=setInterval(function() {
    if (timeLeft>0) {
        timer.textContent=`Time Remaining: ${timeLeft} seconds`;
        timeLeft--;
    } else {
        timer.textContent="Time's up!";
        clearInterval(countdown);
    }
},1000);

    