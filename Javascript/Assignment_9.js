const paragraph =document.getElementById("text");
const blueButton = document.getElementById("blueButton");
const redButton = document.getElementById("redButton");

blueButton.addEventListener("click",function() {
    paragraph.style.color = "blue";
});

redButton.addEventListener("click",function() {
    paragraph.style.color = "red";
});
