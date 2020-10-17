const passwordField = document.querySelector("#pass");
const loginButton = document.querySelector("#loginbtn");
const usernameField = document.querySelector("#username");

loginButton.addEventListener("click", async (e) => {
    e.preventDefault();
    let password = passwordField.value;
    let username = usernameField.value;
    let data = {username, password}
    let contstraints = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify(data)
    }  

    try {
        let response = await fetch("http://localhost:8000/api/login/", contstraints);
        response = await response.json();
        console.log(response)
        window.location.href = "D:/programming%20stuff/ROOM%20WEB%20APP/RoomWebApp/public/index.html";

    } catch(err) {
        console.error(err)
    }
    
})
    
    
