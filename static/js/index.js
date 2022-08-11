num = document.getElementById('guess');
num.innerText = 13;

function randomNum(){
    num.innerText = Math.floor(Math.random() * 33);
    setTimeout(randomNum, 300);
    
}
