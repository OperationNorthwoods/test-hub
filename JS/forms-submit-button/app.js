const form = document.querySelector('#firstForm');
const data = document.querySelector('#info');
const list = document.querySelector('#list')

form.addEventListener("submit", function (e) {
    e.preventDefault();
    console.log("======");
    console.log(`${data.value}`);
    const input = data.value;
    const newLI = document.createElement('LI');
    newLI.innerText = input;
    console.log("======");
    list.append(newLI);
    form.reset();
});
