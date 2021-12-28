use std::io;

fn solve() {
    io::stdin().read_line(&mut String::new()).unwrap();
    let mut energy_consumption = String::new();
    io::stdin()
        .read_line(&mut energy_consumption).unwrap();
    let energy_consumption: f32 = energy_consumption.trim().parse().unwrap();
    
    let mut baubles_without_power = String::new();
    io::stdin()
        .read_line(&mut baubles_without_power).unwrap();
    let baubles_without_power: u32 = baubles_without_power.trim().split(" ")
        .filter_map(|s| s.parse::<u32>().ok())
        .sum();

    let req: f32 = energy_consumption * baubles_without_power as f32 - 0.0001;
    let result: u32 = req as u32 / 5 * 5;
    println!("{}", if (result as f32) < req { result + 5 } else { result });
}

fn main() {
    let mut testcases = String::new();
    io::stdin()
        .read_line(&mut testcases).unwrap();
    let testcases: u16 = testcases.trim().parse().unwrap();
    for _t in 0..testcases {
        solve();
    }
}
