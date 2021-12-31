fn main() {
    
    let guess: u32 = "42".parse().expect("Not a number!");
    
    // floats
    
    let x = 2.0; // f64

    let y: f32 = 3.0; // f32
    
    // addition
    let sum = 5 + 10;

    // subtraction
    let difference = 95.5 - 4.3;

    // multiplication
    let product = 4 * 30;

    // division
    let quotient = 56.7 / 32.2;

    // remainder
    let remainder = 43 % 5;
    
    let t = true;

    let f: bool = false; // with explicit type annotation
    
    // chars
    let c = 'z';
    let z = 'ℤ';
    let heart_eyed_cat = '😻';

    /*
     *8-bit	i8	u8
     *16-bit	i16	u16
     *32-bit	i32	u32
     *64-bit	i64	u64
     *128-bit	i128	u128
     *arch	isize	usize
     */
    ////////////////////////////////
    
    /*
    *Decimal	98_222
    *Hex	0xff
    *Octal	0o77
    *Binary	0b1111_0000
    *Byte (u8 only)	b'A'
     */
}
