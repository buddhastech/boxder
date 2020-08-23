let colorPicker = document.getElementById('colorpicker');
let letterName = document.getElementById('letterName');

colorPicker.addEventListener('change', (e) => {
    letterName.style.backgroundColor = colorPicker.value;
});