fn main() {
    another_function(5, 6);
    let mut b = five();
    println!("B is :{}\n",b);
    b = plus_one(b);
    println!("B plus one :{}",b);
    let mut number = 3;
    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }
    number = 25;
    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else if number % 5 == 0 {
        println!("number is divisible by 5");
    }  else {
        println!("number is not divisible by 5,4, 3, or 2");
    }
    let condition = true;
    let new_number = if condition { 5 } else { 6 };
    println!("new number is {}",new_number);
}

fn another_function(x: i32, y: i32) {
    println!("The value of x is: {}", x);
    println!("The value of y is: {}", y);
}
fn five() -> i32 {
    5
}
fn plus_one(x: i32) -> i32 {
    x + 1
}

