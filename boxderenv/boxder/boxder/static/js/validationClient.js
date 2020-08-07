
function errorInput(input){
    input.style.borderColor = "#D34638";
};

function validateData(e){

    let identification_card = document.getElementById('identification_card');
    let password = document.getElementById('password');
    let flag = true;

    if (!parseInt(identification_card.value) || identification_card.value == "" || 
        identification_card.value.length > 9){
        flag = false;
        errorInput(identification_card);
    }
    if (password.value.lengt > 12 || password.value.length < 8 || 
        password.value == ""){
        flag = false;
        errorInput(password);
    }
    if (flag === false){
        e.preventDefault();
    }
};

window.addEventListener('submit',validateData);