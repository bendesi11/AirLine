
const login = $("#login")
login.on("click", () => {
    let email = $("#email").val()
    let pwd = $("#pwd").val()

    fetch("http://127.0.0.1:5000/login" , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, password: pwd })
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


