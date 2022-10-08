const form = document.querySelector('#firstForm');
const data = document.querySelector('#info');
const list = document.querySelector('#list');
const para = document.querySelector('#live');

form.addEventListener("input", function (e) {
    e.preventDefault();
    console.log("======");
    console.log(`${data.value}`);
    const input = data.value;
    const newLI = document.createElement('LI');
    newLI.innerText = input;
    para.innerText = input;
    list.append(newLI);
    console.log("======");
    // form.reset();
    const listArr = Array.from(entries)
});
const entries = document.querySelectorAll('li');


// Future feature idea:
// iterate over all 'LI's and delete the oldest ones,
// once the amount of 'LI's stored under the 'UL' 
// reaches a certain number of entries.