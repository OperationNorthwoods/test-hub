const form = document.querySelector('#firstForm');
const form2 = document.querySelector('#secondForm');
const data = document.querySelector('#info');
const data2 = document.querySelector('#howMany');
const list = document.querySelector('#list');
const para = document.querySelector('#live');
const button = document.querySelector('#delete');

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
    const entries = document.querySelectorAll('li');

});


form2.addEventListener("input", function (e) {
    e.preventDefault();
    console.log("======");
    console.log(`${data2.value}`);
    const input = data2.value;
    const buttonChange = button
    buttonChange.innerText = `Delete all but ${input} lines`;
    console.log("======");
    console.log("Button Changed");
    // form.reset();
});

form2.addEventListener("submit", function (e) {
    e.preventDefault();
    // needs iteration through created lis
    // operate on ul first to address all created lis
});

// Future feature idea:
// iterate over all 'LI's and delete the oldest ones,
// once the amount of 'LI's stored under the 'UL' 
// reaches a certain number of entries.