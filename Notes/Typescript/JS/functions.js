/*
function name(parameter1, parameter2, ... parameterN) {
  ...body...
}
*/
function showMessage() {
    alert( 'Hello everyone!' );
}
function showAnotherMessage(from, text) { // parameters: from, text
alert(from + ': ' + text);
}
function sum(a, b) {
    return a + b; // can also be used with no value, causes an exit.
  }
  
let result = sum(1, 2);

function sayHi() {
    alert( "Hello" );
}
let func = sayHi;    // (2) copy

func(); // Hello     // (3) run the copy (it works)!
sayHi(); // Hello    //     this still works too (why wouldn't it)

// also arrow functions:

let sum2 = (a, b) => a + b;
let double = n => n * 2;