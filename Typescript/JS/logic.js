// as if it fucking has any.

alert( true || true );   // true
alert( false || true );  // true
alert( true || false );  // true
alert( false || false ); // false

alert( !true ); // false
alert( !0 ); // true

alert( true && true );   // true
alert( false && true );  // false
alert( true && false );  // false
alert( false && false ); // false


// ?? checks if the value exists.
let user;

alert(user ?? "Anonymous"); // Anonymous (user not defined)

let user2 = "John";

alert(user2 ?? "Anonymous"); // John (user defined)


let firstName = null;
let lastName = null;
let nickName = "Supercoder";

// shows the first defined value:
alert(firstName ?? lastName ?? nickName ?? "Anonymous"); // Supercoder