const emailField = document.querySelector("#email");
const passwordField = document.querySelector("#pass");
const loginButton = document.querySelector("#loginbtn");

loginButton.addEventListener("click", (e)=>{
    e.preventDefault();
    let email = emailField.value;
    let password = passwordField.value;
    let data = {email, password};
    let contstraints = {
        method: "POST",
        headers:{
            "Content-Type": "application/json" 
        },
        body: JSON.stringify(data)
    }
    fetch("/api", contstraints);
    console.log(data);
})
