fn main() {

    let x = 5;

    let x = x + 1;

    let x = x * 2;
    // much like using a mut, shadowing replaces the valuable, but while shadowing you can change
    // the data type
    // also, check this for more info https://stackoverflow.com/questions/53235334/in-rust-whats-the-difference-between-shadowing-and-mutability
    println!("The value of x is: {}", x);


}
