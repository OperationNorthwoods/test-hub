// window.onclick = myFunction;

// function myFunction() {
//     for (let i = 0; i < 10; i++) {
//         document.getElementsByid(`a${i}`)[0].classList.add(`itty${i}`);
//         document.getElementsByid(`a${i}`)[0].style.backgroundColor = "yellow";
//     }
// }

// myFunction1(){
//     getElementById('demo').innerHTML = " Lorem ipsum dolor sit amet consectetur adipisicing elit.At illum nulla dolor eaque molestias, ut accusantium nihil repellat, tempore odio quia adipisci commodi nobisvelit voluptates cupiditate labore minima ? Nulla."
// }

const c1 = document.querySelector('#click1')
const c2 = document.querySelector('#click2')
const c3 = document.querySelector('#click3')
const c4 = document.querySelector('#click4')
const c5 = document.querySelector('#click5')
const c6 = document.querySelector('#click6')

c1.onclick = function () {
    for (let i = 1; i < 11; i++) {
        alert(`I am cool! This is alert number ${i}`)
    }
}

c2.onclick = function () {
    for (let i = 1; i < 110; i++) {
        alert(`You're unlucky! This is alert number ${i}`)
    }
}

c3.onclick = function () {
    for (let i = 1; i > 0; i++) {
        alert(`Whoops... Infinite Loop! This is alert number ${i}`)
    }
}

c4.addEventListener('click', alert('Woah, that worked! (button 4)'))
// ^^^ this contains "alert" which is automatically called as soon as the script it run.
// it doesn't wait for the click event. Everytime refresh is hit this alert triggers

c5.addEventListener('click', function () {
    alert('Woah, that worked! (buton 5)')
})
// ^^^ this contains "alert", but placed inside of an anonymous function.
// this means the function is called by the script but not executed until a 
// click event on button 5 happens