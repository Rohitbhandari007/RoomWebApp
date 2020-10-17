const emailField = document.querySelector("#email");
const passwordField = document.querySelector("#pass");
const registerButton = document.querySelector("#registerbtn");
const usernameField = document.querySelector("#username");

registerButton.addEventListener("click", async (e) => {
    e.preventDefault();
    let email = emailField.value;
    let password = passwordField.value;
    let username = usernameField.value;
    let data = { email, username, password }
    let contstraints = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify(data)
    }  

    try {
        let response = await fetch("http://localhost:8000/api/register/", contstraints);
        response = await response.json();
        console.log(response)
        window.location.href = "D:/programming%20stuff/ROOM%20WEB%20APP/RoomWebApp/public/login.html";
    } catch(err) {
        console.error(err)
    }
    
})
    
    
