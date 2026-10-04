const bname = document.getElementById("bname")
const password = document.getElementById("password")
const login = document.getElementById("login")


login.addEventListener("click", function(){
    if(bname.value === "Malte Lehmann" && password.value === "1109")
        alert("Willkommen" + bname.value)
})