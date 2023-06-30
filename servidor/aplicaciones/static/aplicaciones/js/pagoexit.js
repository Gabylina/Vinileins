//redirigir despues 2
setTimeout(function(){
    var urlRedireccion = document.getElementById('redireccion').getAttribute('href');
    // Redirigir automáticamente a la URL obtenida
    window.location.href = urlRedireccion;
}, 100);
