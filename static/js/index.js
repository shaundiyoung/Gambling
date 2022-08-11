num = document.getElementById('guess');
num.innerText = "00";
let finishDate = 0;
let startDate = new Date().getMinutes();
let x = document.getElementById("myAudio"); 
let cash = document.getElementById('bal');

function randomNum(){
    if (finishDate >= 10000){
        finishDate = 0;
    }
    else{
        
    num.innerText = Math.floor(Math.random() * 33);
    setTimeout(randomNum, 100);
    console.log(startDate);
    x.play();
    finishDate += 100;
    }
}

function initiallizeCount(){
    finishDate = startDate+1;
}