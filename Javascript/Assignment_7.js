const form = document.getElementById("form");
form.addEventListener("submit", function(event) {
    event.preventDefault();

        const name =document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const age = document.getElementById("age").value.trim();
        

        let isValid = true;
        if(name=="") {
            alert("Please enter valid name!");
            isValid = false;
        }
        const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if(email=="" || (!pattern.test(email))) {
            alert("Please enter valid email!");
            isValid = false;
        }
        if(age !=="" && Number(age)<=18){
            alert("Please entr valid age");
            isValid=false;
        }

        if (isValid) {
            alert("Submitted Successfully!")
        }

    });

