window.addEventListener('load', function(){
    
    let form = document.getElementById('form-regist');
    let infoForm = document.getElementById('info-form');
    let button = document.getElementById('back-button');

    form.classList.add('active');
    infoForm.classList.add('active');
    button.classList.add('active');

    // al pasar 3 segundos y medios elimina la clase active para que vuelva al estado original
    setTimeout(function(){
        infoForm.classList.remove('active');
        button.classList.remove('active');
    }, 3500);
    
});