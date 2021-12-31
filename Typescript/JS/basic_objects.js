// https://javascript.info/object
let user = {     // an object
    name: "John",  // by key "name" store value "John"
    age: 30        // by key "age" store value 30
};
alert( user.name ); // John
alert( user.age ); // 30


let user1 = { name: "John", age: 30 };

alert( "age" in user1 ); // true, user.age exists
alert( "blabla" in user1 ); // false, user.blabla doesn't exist