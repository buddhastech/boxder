
window.addEventListener('submit', (e) => {
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

        dataForm['id'].style.borderColor = "#D34638";
        inputsError['error-text1'].value = "Cedula inválida";
        inputsError['error-text1'].style.color = "#D34638";
        dataForm['id'].onmouseout = () => {dataForm['id'].style.borderColor = "#D34638"};
        dataForm['id'].onmouseenter = () => {dataForm['id'].style.borderColor = "#D34638"};

    }else{

        inputsError['error-text1'].value = "";
        dataForm['id'].style.borderColor = "lightgray";
        dataForm['id'].onmouseout = () => {dataForm['id'].style.borderColor = "lightgray"};
        dataForm['id'].onmouseenter = () => {dataForm['id'].style.borderColor = "#168AF7"};
    }
    if (parseInt(dataForm['name'].value) || dataForm['name'].value.length > 15 
        || dataForm['name'].value == ""){
        
        flag = false;
        
        dataForm['name'].style.borderColor = "#D34638";
        inputsError['error-text2'].value = "Nombre inválido";
        inputsError['error-text2'].style.color = "#D34638";
        dataForm['name'].onmouseout = () => {dataForm['name'].style.borderColor = "#D34638"};
        dataForm['name'].onmouseenter = () => {dataForm['name'].style.borderColor = "#D34638"};
    
    }else{
        
        inputsError['error-text2'].value = "";
        dataForm['name'].style.borderColor = "lightgray";
        dataForm['name'].onmouseout = () => {dataForm['name'].style.borderColor = "lightgray"};
        dataForm['name'].onmouseenter = () => {dataForm['name'].style.borderColor = "#168AF7"};
        
    }
    if (parseInt(dataForm['surnames'].value) || dataForm['surnames'].value.length > 50
        || dataForm['surnames'].value == ""){

        flag = false;
        dataForm['surnames'].style.borderColor = "#D34638";
        inputsError['error-text3'].value = "Apellidos inválidos";
        inputsError['error-text3'].style.color = "#D34638";
        dataForm['surnames'].onmouseout = () => {dataForm['surnames'].style.borderColor = "#D34638"};
        dataForm['surnames'].onmouseenter = () => {dataForm['surnames'].style.borderColor = "#D34638"};

    }else{
        
        inputsError['error-text3'].value = "";
        dataForm['surnames'].style.borderColor = "lightgray";
        dataForm['surnames'].onmouseout = () => {dataForm['surnames'].style.borderColor = "lightgray"};
        dataForm['surnames'].onmouseenter = () => {dataForm['surnames'].style.borderColor = "#168AF7"};
        
    }

    if (!parseInt(dataForm['phone'].value) || dataForm['phone'].value.length != 8
        || dataForm['phone'].value == ""){
        
        flag = false;
        dataForm['phone'].style.borderColor = "#D34638";
        inputsError['error-text4'].value = "Número de teléfono inválido";
        inputsError['error-text4'].style.color = "#D34638";
        dataForm['phone'].onmouseout = () => {dataForm['phone'].style.borderColor = "#D34638"};
        dataForm['phone'].onmouseenter = () => {dataForm['phone'].style.borderColor = "#D34638"};
          
    }else{
        
        inputsError['error-text4'].value = "";
        dataForm['phone'].style.borderColor = "lightgray";
        dataForm['phone'].onmouseout = () => {dataForm['phone'].style.borderColor = "lightgray"};
        dataForm['phone'].onmouseenter = () => {dataForm['phone'].style.borderColor = "#168AF7"};
    
    }
    if (parseInt(dataForm['department'].value) || dataForm['department'].value.length > 25
        || dataForm['department'].value == ""){
        
        flag = false;
        dataForm['department'].style.borderColor = "#D34638";
        inputsError['error-text5'].value = "Departamento inválido";
        inputsError['error-text5'].style.color = "#D34638";
        dataForm['department'].onmouseout = () => {dataForm['department'].style.borderColor = "#D34638"};
        dataForm['department'].onmouseenter = () => {dataForm['department'].style.borderColor = "#D34638"};

    }else{
        
        inputsError['error-text5'].value = "";
        dataForm['department'].style.borderColor = "lightgray";
        dataForm['department'].onmouseout = () => {dataForm['department'].style.borderColor = "lightgray"};
        dataForm['department'].onmouseenter = () => {dataForm['department'].style.borderColor = "#168AF7"};
    
    }
    if (!parseInt(dataForm['age'].value) || dataForm['age'].value.length > 2 
        || dataForm['age'].value == ""){
        
        flag = false;
        dataForm['age'].style.borderColor = "#D34638";
        inputsError['error-text6'].value = "Edad inválida";
        inputsError['error-text6'].style.color = "#D34638";
        dataForm['age'].onmouseout = () => {dataForm['age'].style.borderColor = "#D34638"};
        dataForm['age'].onmouseenter = () => {dataForm['age'].style.borderColor = "#D34638"};

    }else{
        
        inputsError['error-text6'].value = "";
        dataForm['age'].style.borderColor = "lightgray";
        dataForm['age'].onmouseout = () => {dataForm['age'].style.borderColor = "lightgray"};
        dataForm['age'].onmouseenter = () => {dataForm['age'].style.borderColor = "#168AF7"};
    
    }
    if (parseInt(dataForm['email'].value) || dataForm['email'].value == ""){
        
        flag = false;
        dataForm['email'].style.borderColor = "#D34638";
        inputsError['error-text7'].value = "Correo inválido";
        inputsError['error-text7'].style.color = "#D34638";
        dataForm['email'].onmouseout = () => {dataForm['email'].style.borderColor = "#D34638"};
        dataForm['email'].onmouseenter = () => {dataForm['email'].style.borderColor = "#D34638"};

    }else{
        
        inputsError['error-text7'].value = "";
        dataForm['email'].style.borderColor = "lightgray";
        dataForm['email'].onmouseout = () => {dataForm['email'].style.borderColor = "lightgray"};
        dataForm['email'].onmouseenter = () => {dataForm['email'].style.borderColor = "#168AF7"};
    
    }
    if (dataForm['password'].value.length > 12 || dataForm['password'].value.length < 8
        || dataForm['password'].value == ""){
        
        flag = false;
        dataForm['password'].style.borderColor = "#D34638";
        inputsError['error-text8'].value = "Contraseña inválida";
        inputsError['error-text8'].style.color = "#D34638";
        dataForm['password'].onmouseout = () => {dataForm['password'].style.borderColor = "#D34638"};
        dataForm['password'].onmouseenter = () => {dataForm['password'].style.borderColor = "#D34638"};

        }else{
        
            inputsError['error-text8'].value = "";
            dataForm['password'].style.borderColor = "lightgray";
            dataForm['password'].onmouseout = () => {dataForm['password'].style.borderColor = "lightgray"};
            dataForm['password'].onmouseenter = () => {dataForm['password'].style.borderColor = "#168AF7"};
        
        }

    if (flag === false){
        
        e.preventDefault();
    }

});
