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
        headers:{
            "content-type": "application/json" 
        },
        body: JSON.stringify(data)
<<<<<<< HEAD
    }
    fetch("/api", contstraints)
    .then((res)=>{
        res.json();
    }).then((data)=>{
        console.log("Data from Server = "+ data)
    }).catch((error)=>{
        console.log("An error occured" + error);
    });
=======
    };
    fetch("http://127.0.0.1:8000/api/register/", contstraints);
>>>>>>> 980c5359589b5fb3a9402a9dc5e0e827f6f8e6ad

})
