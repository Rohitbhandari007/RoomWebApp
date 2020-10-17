const emailField = document.querySelector("#email");
const passwordField = document.querySelector("#pass");
const registerButton = document.querySelector("#registerbtn");
const usernameField = document.querySelector("#username");

registerButton.addEventListener("click", (e) => {
    e.preventDefault();
    let email = emailField.value;
    let password = passwordField.value;
    let username = usernameField.value;
    let data = { email, username, password }
    let contstraints = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }

    fetch("http://127.0.0.1:8000/api/register/", contstraints)
        .then((res) => {
            console.log(res.body)
            return res.text();
        })
        .then((source) => {
            console.log( typeof source)
            console.log("Data from Server = " + JSON.parse(source));
        })
        .catch((error) => {
            console.log("An error occured" + error);
        });
    
})
    
    
