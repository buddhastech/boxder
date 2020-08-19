let regex = {
    'especialCharacters': /\*|\@|\#|\$|\%|\&|\?|\(|\)|\+|\-|\/|\\|\||\=|\¡|\¿|\'|\<|\>|\[|\]/,
    'numbers': /[0-9]/,
    'letters': /[a-zA-Z]/,
    'emailDomains': /.com|.es|.org|.net|.yahoo|.outlook|.pro|.edu|.gov|.tv|.info|.cc/,
}
let errorInputs = {
    "error-text1": document.getElementById('error-text1'),
    "error-text2": document.getElementById('error-text2')
}

function errorInput(input){

    input.classList.remove('active')
    input.classList.add('warning');

};

function errorText(input, msj){

    input.classList.add('warning');
    input.value = msj;

};

function validateData(e){

    let identification_card = document.getElementById('identification_card');
    let password = document.getElementById('password');
    let flag = true;

    if (!parseInt(identification_card.value) || identification_card.value == "" 
        || identification_card.value.length > 9 || identification_card.value.match(regex['especialCharacters'])
        || identification_card.value.match(regex['letters'])){

        flag = false;
        errorInput(identification_card);
        errorText(errorInputs['error-text1'], "Cedula inválida");
        
    }
    if (password.value.length < 8 || 
        password.value == ""){
        flag = false;
        errorInput(password);
        errorText(errorInputs['error-text2'], "Contraseña inválida");
        
    }
    
    if (flag === false){
        e.preventDefault();
    }
};

window.addEventListener('submit',validateData);