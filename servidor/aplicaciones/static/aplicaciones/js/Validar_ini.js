function b() {
    swal("Ingresa tu correo para poder cambiar la contraseña", {
        content: "input",
    })
        .then((value) => {
            swal(`Se a enviado un correo para cambio de contraseña.`);
        });
}


function login(){
    var user,contra
    user=document.getElementById("username").value;
    contra=document.getElementById("password").value;

    if(user=="gaby" && contra=="gaby"){
        location.href ="http://127.0.0.1:8000/iniciocliente";
    }else{
        swal("Usuario o contraseña incorrectos","","warning");
    }
    
    if(user=="nico" && contra=="nico"){
        location.href ="http://127.0.0.1:8000/";
    }else{
        swal("Usuario o contraseña incorrectos","","warning");
    }

}