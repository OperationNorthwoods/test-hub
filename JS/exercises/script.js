// https://www.w3resource.com/javascript-exercises/javascript-functions-exercises.php
//exercise 1: complete

function bob(input) {
    const letters = []
    for (x of input) {
        letters.push(x)
    }
    return letters.reverse().join('')
}

//exercise 2

function isPalindrome(input) {
    if (input === input.split('').reverse().join('')) {
        return console.log('true')
    } else {
        return console.log('false')
    }
}

function organize(input) {
    input.split('')
}