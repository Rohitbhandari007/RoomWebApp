const emailField = document.querySelector("#email");
const passwordField = document.querySelector("#pass");
const loginButton = document.querySelector("#loginbtn");
const usernameField = document.querySelector("#username");


loginButton.addEventListener("click", (e)=>{
    e.preventDefault();
    let email = emailField.value;
    let password = passwordField.value;
    let username = usernameField.value;
    let data = {email, username, password};
    let contstraints = {
        method: "POST",
        headers: {"content-type": "application/json"},
        body: JSON.stringify(data)
    };
    fetch("http://127.0.0.1:8000/api/register/", contstraints);

})
