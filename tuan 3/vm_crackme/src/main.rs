
fn main() {
    let p1: i32 = 0x13371337 - (0x2648ED87 ^ 0x13371337);
    let p1 = p1.rotate_right(6);
    
    let p2: i64 = 0xDEADBEEF - 0x94C3E659;
    
    let p3: u32 = 0x5469A57F;
    let p3 = !((!p3 - 0x89ABCDEF) ^ 0xABBAABBA);
    let p3 = p3.rotate_left(4);

    println!("{:X}", p3);
}
