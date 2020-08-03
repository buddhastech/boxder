let formLogin = document.getElementById('form-login');  // Elemento h2 del main
let inputOne = document.getElementById('cedula');
let inputTwo = document.getElementById('contra');
let identificationIcon = document.getElementById('card');
let passwordIcon = document.getElementById('pass');
let submitButton = document.getElementById('submit-button');
let registerButton = document.getElementById('register');

window.addEventListener('load', () => {
    
    identificationIcon.classList.add('active');
    passwordIcon.classList.add('active');
    formLogin.classList.add('active');
    inputOne.classList.add('active');
    inputTwo.classList.add('active');
    submitButton.classList.add('active');
    registerButton.classList.add('active');
    
});

