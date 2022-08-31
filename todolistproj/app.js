const todoList = []
let userInput = '0'
let deleteInput = '0'

while (userInput !== 'quit') {
    userInput = prompt('Enter your command. Valid commands are "new", "list", "delete" and "quit".').toLowerCase()
    if (userInput === 'new') {
        todoList.push(prompt('Enter your new list item'))
        console.log('Item added')
    }
    else if (userInput === 'list') {
        if (todoList.length !== 0) {
            console.log('**************')
            for (i = 0; i < todoList.length; i++) {
                console.log(`${i} ${todoList[i]}`)}
            console.log('**************')
        } else {
            console.log('Your list is empty. Use "new" command to add item')
        }

    }
    else if (userInput === 'delete') {
        if (todoList.length <= 0) {console.log('nothing to delete!')
        } else {
            console.log('**************')
            for (i = 0; i < todoList.length; i++) {
                console.log(`${i} ${todoList[i]}`)}
            console.log('**************')
            deleteInput = prompt('enter indice of item to delete from list. Please only enter 1.')
                if (isNaN(deleteInput = true)){
                    console.log('Please enter a valid Number!')
                } else {
                    todoList.splice(deleteInput,1)
                }
        }
    } else {
        console.log('try again. press refresh.')
    }
}
console.log('You are a quitter!!')




// const todoList = []
// let userInput = ''
// let addMore2List = ''
// let deleteFromList = ''

// userInput = prompt('Enter your command. Valid commands are "new", "list", "delete" and "quit".').toLowerCase()

// while (userInput !== 'quit') {
//     userInput = prompt('Enter your command. Valid commands are "new", "list", "delete" and "quit".').toLowerCase()
//     while (userInput == 'new') {
//         todoList.push(prompt('Enter your new list item'))
//         console.log('Item added')
//         addMore2List = prompt('Would you like to continue? enter "yes" or "no"').toLowerCase()
//         while (addMore2List === 'yes') {
//             todoList.push(prompt('Enter your new list item'))
//             console.log('Item added')
//         }

//     }





// }
// console.log('You are a quitter!!')
    // setTimeout(document.location.reload(), 5000);




// let userInput = prompt('Enter your command. Valid commands are "new", "list", "delete" and "quit".').toLowerCase()
// while (userInput == 'delete') {

// }
// while (userInput == 'list') {
//     if (todoList.length !== 0) {
//         console.log('**************')
//         for (i = 0; i <= todoList.length; i++) {
//             console.log(`${i} ${todoList[i]}`)
//         }
//         console.log('**************')
//     } else {
//         console.log('Your list is empty. Use "new" command to add item')
//         userInput = 'emptylist'
//     }
// }



//         else if (userInput === 'list') {
//     if (todoList.length !== 0) {
//         console.log('**************')
//         for (i = 0; i <= todoList.length; i++) {
//             console.log(`${i} ${todoList[i]}`)
//         }
//         console.log('**************')
//     } else {
//         console.log('Your list is empty. Use "new" command to add item')
//         userInput = 'emptylist'
//     }
//     // for (let listItems of todoList)
//     //     console.log('***************')
//     // console.log(``)
//     // console.log('***************')

// }
// else if (userInput === 'delete') {
//     console.log('still working on this 2')
// }
// else if (userInput === 'emptylist') {
//     console.log('your list is empty')
// }
// else {
//     console.log('try again. press refresh.')
// }
    // setTimeout(document.location.reload(), 5000);

