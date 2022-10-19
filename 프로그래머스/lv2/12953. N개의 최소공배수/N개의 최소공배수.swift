func solution(_ arr:[Int]) -> Int {
    if arr.count == 1 {
        return arr[0]
    }
    var lcm = getLCM(a: arr[0], b: arr[1])
    if arr.count == 2 {
        return lcm
    } else {
        for i in 2..<arr.count {
            lcm = getLCM(a: arr[i], b: lcm)
        }
    }
    return lcm
    
}
func getLCM(a:Int, b:Int) -> Int {
    var vA = a
    var vB = b
    while vB != 0 {
        let r = vA % vB
        vA = vB
        vB = r
    }
    return a*b/vA
}