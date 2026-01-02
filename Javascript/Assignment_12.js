const button=document.getElementById("button");
const closeBtn=document.getElementById("closeBtn");
const modal=document.getElementById("modal");
button.addEventListener("click",function() {
    modal.classList.add("show");
});
closeBtn.addEventListener("click",function() {
    modal.classList.remove("show");
});
modal.addEventListener("click",function(e) {
    if (e.target===modal) {
        modal.classList.remove("show");
    }
});




