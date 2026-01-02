const btn = document.getElementById("btn");
    const list = document.getElementById("listitem");
        
    btn.addEventListener("click",function () {
            const items=list.children.length+1;
            const li=document.createElement("li");
            li.textContent="Item" + items;
            list.appendChild(li);
    });