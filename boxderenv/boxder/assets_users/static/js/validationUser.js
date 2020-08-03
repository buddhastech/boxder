
window.addEventListener('submit', (e) => {
    let data = {
        'id': document.getElementById('identification_card'),
        'name': document.getElementById('name'),
        'surnames': document.getElementById('surnames'),
        'phone': document.getElementById('phone'),
        'department': document.getElementById('department'),
        'email': document.getElementById('email'),
        'password': document.getElementById('password')
    }
    
    if (data.id.value == "" || data.name.value == "" || 
        data.surnames.value == "" || data.phone.value == "" || 
        data.department.value == "" || data.email.value == "" || 
        data.password.value == ""){

        e.preventDefault();

        Swal.fire({
            title: 'Error',
            text: 'Verifica que la información sea válida',
            icon: 'error',
            confirmButtonText: 'Ok'
          });
    }

});
