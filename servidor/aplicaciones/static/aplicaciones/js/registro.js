
document.addEventListener("DOMContentLoaded", function() {
    /* nombre */
    var firstNameInput = document.getElementById("id_first_name");
    var nombreInput = document.getElementById("id_nombre");
    /* apellido */
    var lastNameInput = document.getElementById("id_last_name");
    var apellidoInput = document.getElementById("id_apellido");
    /* rut */
    var usernameInput =document.getElementById("id_username");
    /* correo */
    var correoInput = document.getElementById("id_correo");
    /* contraseña 1 */
    var password1Input = document.getElementById("id_password1");
    var contraInput = document.getElementById("id_contra");



    // Asignar el valor del campo 'first_name' al campo 'nombre' al cambiar su valor
    firstNameInput.addEventListener("input", function() {
        nombreInput.value = firstNameInput.value;
    });
    nombreInput.addEventListener("input", function() {
        firstNameInput.value = nombreInput.value;
    });

    lastNameInput.addEventListener("input", function(){
        apellidoInput.value = lastNameInput.value;
    });
    apellidoInput.addEventListener("input", function(){
        lastNameInput.value = apellidoInput.value;
    })

    usernameInput.addEventListener("input", function(){
        correoInput.value = usernameInput.value;
    });
    correoInput.addEventListener("input", function(){
        usernameInput.value= correoInput.value;
    });

    password1Input.addEventListener("input", function() {
        contraInput.type = "text";  // Cambiar temporalmente a campo de texto
        contraInput.value = password1Input.value;
        contraInput.type = "password";  // Cambiar nuevamente a campo de contraseña
    });
    
    contraInput.addEventListener("input", function() {
        password1Input.type = "text";
        password1Input.value = contraInput.value;
        password1Input.type = "password";
    });

});

/* cliente  ["correo","contra","direccion","region","comuna","telefono"] */

/* user     ["email","password1",'password2'] */