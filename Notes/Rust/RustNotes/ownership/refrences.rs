fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1);    
    print!("we still do have access to s1: {}",s1);
    // now we dont.
    let mut b = String::from("haha");
    change(&mut b);
    print!("{}",b);
}
fn calculate_length(s: &String) -> usize { // s is a reference to a String
    s.len()
} // Here, s goes out of scope. But because it does not have ownership of what

  // it refers to, nothing happens.
fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
fn hello(){
    println!("ga")
}
