num = document.getElementById('cashpot');
num.innerText = "00";
let finishDate = 0;
let randNum = 0 ;
let x = document.getElementById("myAudio"); 

let y = document.getElementById("myAudio1"); 

let z = document.getElementById("myAudio2"); 

let cash = document.getElementById('bal');
let val = document.getElementById('val');
let guess = document.getElementById('guess');

function add(sum){
    fetch("/api/add/"+sum, {
        method:"POST"
    }).then(data =>data.json()).then(json =>{
        cash.innerText = json.newscore;
    }).catch(

    );
}

function sub(sum){
    fetch("/api/sub/"+sum, {
        "method":"POST"
    }).then(data => data.json()).then(json =>{
        cash.innerText = json.newscore;
    }).catch(

    );
}



val.addEventListener('mouseover', () =>{
    document.getElementById('Profit').innerText = 0+val.value*2;
});
val.addEventListener('mouseout', () =>{
    document.getElementById('Profit').innerText = 0+val.value*2;
});
function randomNum(){
    let guessnum = guess.value;
    if (finishDate >= 7000){
        finishDate = 0;
        randNum = num.innerText;
        console.log(randNum);
        checknumber(randNum, guessnum);
    }
    else{
        
    num.innerText = Math.floor(Math.random() * 33);
    setTimeout(randomNum, 100);
    x.play();
    finishDate += 100;
    }
}


function checknumber(num, guessnum){
    if (num == guessnum){
        alert("You won");
        add(val.value * 2);
        z.play();
    }
    else if (num-guessnum>-4 && num-guessnum<4){
        alert("Close enough");
        add(val.value * 1.5);
        z.play();
    }
    else{
        sub(val.value);
        y.play();

    }
}


function generateCash(){
    add(1000);
    setTimeout(generateCash, 100000);
    }

generateCash();

