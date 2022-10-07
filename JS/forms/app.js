const form = document.querySelector('#firstForm');
const data = document.querySelector('#info');

form.addEventListener("submit", function (e) {
    e.preventDefault();
    console.log("SUBMITTED!!")
    console.log(info.value)
});
