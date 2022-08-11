num = document.getElementById('guess');
num.innerText = 13;
let finishDate;
let startDate = new Date().getMinutes();

function randomNum(){
    num.innerText = Math.floor(Math.random() * 33);
    setTimeout(randomNum, 300);
    console.log(startDate);
}

function initiallizeCount(){
    finishDate = startDate+1;
}