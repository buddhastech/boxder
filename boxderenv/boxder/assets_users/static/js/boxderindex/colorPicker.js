let colorButtonOne = document.getElementById('color1');
let colorButtonTwo = document.getElementById('color2');
let colorButtonTree = document.getElementById('color3');
let colorButtonFour = document.getElementById('color4');
let colorButtonFive = document.getElementById('color5');
let colorButtonSix = document.getElementById('color6');

let letterName = document.getElementById('button-letter');
let letterAside = document.getElementById('letterName');


function changeColor(backColor, letterColor, objectColor){
    objectColor.style.backgroundColor = backColor;
    objectColor.style.color = letterColor;
}

window.addEventListener('load', function() {
    letterName.style.backgroundColor = localStorage.getItem('color'); // local storage
    letterAside.style.backgroundColor = localStorage.getItem('color'); 

    if (localStorage.getItem('color') != "#FFEC4F"){
        letterName.style.color = "white";
        letterAside.style.color = "white";
    }else{
        letterName.style.color = "#333";
        letterAside.style.color = "#333";
    }

});

colorButtonOne.addEventListener('click', function() {
    window.localStorage.setItem('color', "#C73B2F");
    letterAside.style.backgroundColor = localStorage.getItem('color'); 
    letterAside.style.color = "white";
    changeColor(localStorage.getItem('color'), "white", letterName);

});

colorButtonTwo.addEventListener('click', function() {
    window.localStorage.setItem('color', "#3EA71C");
    letterAside.style.backgroundColor = localStorage.getItem('color'); 
    letterAside.style.color = "white";
    changeColor(localStorage.getItem('color'), "white", letterName);
});

colorButtonTree.addEventListener('click', function() {
    window.localStorage.setItem('color', "#1E79BD");
    letterAside.style.backgroundColor = localStorage.getItem('color'); 
    letterAside.style.color = "#white";
    changeColor(localStorage.getItem('color'), "white", letterName);
});

colorButtonFour.addEventListener('click', function() {
    window.localStorage.setItem('color', "#FFEC4F");
    letterAside.style.backgroundColor = localStorage.getItem('color'); 
    letterAside.style.color = "#333";
    changeColor(localStorage.getItem('color'), "#333", letterName);
});


colorButtonFive.addEventListener('click', function() {
    window.localStorage.setItem('color', "#E718F1");
    letterAside.style.backgroundColor = localStorage.getItem('color'); 
    letterAside.style.color = "white";
    changeColor(localStorage.getItem('color'), "white", letterName);
});


colorButtonSix.addEventListener('click', function() {
    window.localStorage.setItem('color', "#7B41FF");
    letterAside.style.backgroundColor = localStorage.getItem('color'); 
    letterAside.style.color = "white";
    changeColor(localStorage.getItem('color'), "white", letterName);
});



