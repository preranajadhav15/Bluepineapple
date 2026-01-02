const textDiv = document.getElementById("text");
    const btn = document.getElementById("button");
    btn.addEventListener("click",function () {
        textDiv.textContent = "You clicked the button!"
    });