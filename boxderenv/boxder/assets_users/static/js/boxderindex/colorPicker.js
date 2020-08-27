let colorPicker = document.getElementById('colorpicker');
let letterName = document.getElementById('letterName');

window.addEventListener('load', () => {
    letterName.style.backgroundColor = localStorage.getItem('color')
});

colorPicker.addEventListener('change', () => {
    window.localStorage.setItem('color', colorPicker.value);
    letterName.style.backgroundColor = localStorage.getItem('color');
});