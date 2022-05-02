
const login = $("#login")
login.on("click", () => {
    let email = $("#email").val()
    let pwd = $("#pwd").val()
    let pwd2 = $("#pwd2").val()

    fetch("http://127.0.0.1:5000/registration" , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, password: pwd, password2:pwd2})
    })
    .then(resp => resp.json())
    .then(data => {
        if (data == 0){
            $("#error-msg").text("hiba")
        }else{
            $("#error-msg").text("siker")
        }
    })
})


