num = document.getElementById('guess');
num.innerText = 13;
let finishDate;
let startDate = new Date().getMinutes();
let x = document.getElementById("myAudio"); 

function randomNum(){
    num.innerText = Math.floor(Math.random() * 33);
    setTimeout(randomNum, 100);
    console.log(startDate);
    x.play();
}

function initiallizeCount(){
    finishDate = startDate+1;
}