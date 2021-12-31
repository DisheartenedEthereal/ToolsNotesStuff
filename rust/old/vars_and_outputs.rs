use std::io::stdin;
fn main() {
        // Variable values are immutable (Can't change)
    let num = 10;

    // Define a 32 bit mutable integer
    let mut age: i32 = 40;
    // There are booleans
    let is_it_true: bool = true;

    // Characters
    let let_x: char = 'x';

    // Place variable values in output
    println!("I am {} years old", age);

    // You can define multiple variables
    let (f_name, l_name) = ("Derek", "Banas");

    // ---------- OUTPUT ----------

    // You can place data multiple times
    println!("It is {0} that {1} is {0}",
    is_it_true, let_x);

    // Format output
    println!("{:.2}", 1.234);
    println!("B: {:b} H: {:x} O: {:o}", 10, 10, 10);

    // Use named arguments
    // Define whitespace before data
    println!("{ten:>ws$}", ten=10, ws=5);

    // Pad output with zeros
    println!("{ten:>0ws$}", ten=10, ws=5);

}
