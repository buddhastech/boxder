let closeSesionButton = document.getElementById('close-sesion');

closeSesionButton.addEventListener('click', () => {
    Swal.fire({
        title: '¿Seguro que desea salir?',
        text: "Si cierra la sesión deberá acceder de nuevo con sus datos",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, cerrar sesión'
      }).then((result) => {
        if (result.value) {
            window.location.href = "../inicio";
        }
      })
});