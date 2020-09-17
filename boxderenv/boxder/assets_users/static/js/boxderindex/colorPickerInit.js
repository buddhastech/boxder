
let letterName = document.getElementById('letterName');

window.addEventListener('load', function() {
    letterName.style.backgroundColor = localStorage.getItem('color') // local storage
    
    if (localStorage.getItem('color') != "#FFEC4F"){
        letterName.style.color = "white";
    }else{
        letterName.style.color = "#333";
    }

});