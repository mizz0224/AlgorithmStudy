func solution(_ s:String) -> String {
    let sset = s.split(separator: " ").map{Int(String($0))!}
    return String(sset.min()!) + " " + String(sset.max()!)
}
