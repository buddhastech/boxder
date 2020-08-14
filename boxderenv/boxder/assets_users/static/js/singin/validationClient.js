
function verificationClass(inputId, inputCollection){
    
    if (inputCollection[inputId].classList.contains('good')){
        inputCollection[inputId].classList.remove('good');
    }

};

function errorInput(inputId, inputCollection, errorCollection, errorId, msj){
    
    inputCollection[inputId].classList.add('warning');
    errorCollection[errorId].classList.add('warning');
    errorCollection[errorId].value = msj;

};

function validationForm(e){
    let flag = true;

    let dataForm = {
        'id': document.getElementById('identification_card'),
        'name': document.getElementById('name'),
        'surnames': document.getElementById('surnames'),
        'phone': document.getElementById('phone'),
        'department': document.getElementById('department'),
        'age': document.getElementById('age'),
        'email': document.getElementById('email'),
        'password': document.getElementById('pass')
    };

    let inputsError = {
        'error-text1': document.getElementById('error-text1'),
        'error-text2': document.getElementById('error-text2'),
        'error-text3': document.getElementById('error-text3'),
        'error-text4': document.getElementById('error-text4'),
        'error-text5': document.getElementById('error-text5'),
        'error-text6': document.getElementById('error-text6'),
        'error-text7': document.getElementById('error-text7'),
        'error-text8': document.getElementById('error-text8')
    };
    
    if (!parseInt(dataForm['id'].value) || dataForm['id'].value.length != 9 
        && dataForm['id'].value != ""){
        
        flag = false;        
        verificationClass('id', dataForm);
        errorInput('id', dataForm, inputsError, 'error-text1', 'Cédula inválida');

    }else{

        dataForm['id'].classList.add('good');
        inputsError['error-text1'].value = "";

    }

    if (parseInt(dataForm['name'].value) || dataForm['name'].value.length > 15 
        || dataForm['name'].value == ""){
        
        flag = false;
        
        verificationClass('name', dataForm);
        errorInput('name', dataForm, inputsError, 'error-text2', 'Nombre inválido');
    
    }else{
        
        inputsError['error-text2'].value = "";
        dataForm['name'].classList.add('good');
        
    }

    if (parseInt(dataForm['surnames'].value) || dataForm['surnames'].value.length > 50
        || dataForm['surnames'].value == ""){

        flag = false;

        verificationClass('surnames', dataForm);
        errorInput('surnames', dataForm, inputsError, 'error-text3', 'Apellidos inválidos');

    }else{
        
        inputsError['error-text3'].value = "";
        dataForm['surnames'].classList.add('good');

    }

    if (!parseInt(dataForm['phone'].value) || dataForm['phone'].value.length != 8
        || dataForm['phone'].value == ""){
        
        flag = false;
        
        verificationClass('phone', dataForm);
        errorInput('phone', dataForm, inputsError, 'error-text4', 'Número de teléfono inválido');

    }else{
        
        inputsError['error-text4'].value = "";
        dataForm['phone'].classList.add('good');

    }

    if (parseInt(dataForm['department'].value) || dataForm['department'].value.length > 25
        || dataForm['department'].value == ""){
        
        flag = false;

        verificationClass('department', dataForm);
        errorInput('department', dataForm, inputsError, 'error-text5', 'Departamento inválido')

    }else{
        
        inputsError['error-text5'].value = "";
        dataForm['department'].classList.add('good');

    }

    if (!parseInt(dataForm['age'].value) || dataForm['age'].value.length > 2 
        || dataForm['age'].value == ""){
        
        flag = false;

        verificationClass('age', dataForm);
        errorInput('age', dataForm, inputsError, 'error-text6', 'Edad inválida');

    }else{
        
        inputsError['error-text6'].value = "";
        dataForm['age'].classList.add('good');
    }

    if (parseInt(dataForm['email'].value) || dataForm['email'].value == ""){
        
        flag = false;

        verificationClass('email', dataForm);
        errorInput('email', dataForm, inputsError, 'error-text7', 'Correo inválido');

    }else{
        
        inputsError['error-text7'].value = "";
        dataForm['email'].classList.add('good');

    }

    if (dataForm['password'].value.length > 12 || dataForm['password'].value.length < 8
        || dataForm['password'].value == ""){
        
        flag = false;
        
        verificationClass('password', dataForm);
        errorInput('password', dataForm, inputsError, 'error-text8', 'Contraseña inválida');

    }else{
        
        inputsError['error-text8'].value = "";
        dataForm['password'].classList.add('good');
    }

    if (flag === false){
        
        e.preventDefault();
    }

};

window.addEventListener('submit', validationForm);
