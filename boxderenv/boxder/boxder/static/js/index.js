let formLogin = document.getElementById('form-login'); 
let inputOne = document.getElementById('identification_card');
let inputTwo = document.getElementById('password');
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

