num = document.getElementById('cashpot');
num.innerText = "00";
let finishDate = 0;
let startDate = new Date().getMinutes();
let x = document.getElementById("myAudio"); 
let cash = document.getElementById('bal');
let val = document.getElementById('val');
let guess = document.getElementById('guess');



val.addEventListener('mouseover', () =>{
    document.getElementById('Profit').innerText = 0+val.value*2;
});
val.addEventListener('mouseout', () =>{
    document.getElementById('Profit').innerText = 0+val.value*2;
});
function randomNum(){
    if (finishDate >= 7000){
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