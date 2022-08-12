num = document.getElementById('cashpot');
num.innerText = "00";
let finishDate = 0;
let startDate = new Date().getMinutes();
let x = document.getElementById("myAudio"); 
let cash = document.getElementById('bal');
let val = document.getElementById('val');
let guess = document.getElementById('guess');

function randomNum(){
    if (finishDate >= 30000){
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


function submitVal(){
    let guessnum = guess.value;
    console.log(guessnum);
}