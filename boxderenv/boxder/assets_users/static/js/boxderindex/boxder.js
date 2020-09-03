let closeSesionButton = document.getElementById('close-sesion');
let newAssets = document.getElementById('new-asset');
let overlay = document.getElementById('overlay');
let popup = document.getElementById('popup');
let close = document.getElementById('close-popup');

newAssets.addEventListener('click', () => {
  overlay.classList.add('active');
  popup.classList.add('active');
});

close.addEventListener('click', () => {
  popup.classList.remove('active');
  overlay.classList.remove('active');
});

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