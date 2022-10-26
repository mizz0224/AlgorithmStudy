func solution(_ n:Int, _ left:Int64, _ right:Int64) -> [Int] {
    //var arr = [[Int]]()
    var arr = [Int]()
    var isFinish = false
    let start = Int(left)/n+1
    for i in start...n {
        if i == start {
            for j in Int(left)%n+1...n {
                if j < i {
                    arr.append(i)
                } else {
                    arr.append(j)
                }
                if (i-1)*n+j > right {
                    isFinish = true
                    break
                }
            }
        } else {
            for j in 1...n {
                if j < i {
                    arr.append(i)
                } else {
                    arr.append(j)
                }
                if (i-1)*n+j > right {
                    isFinish = true
                    break
                }
            }
        }
        if isFinish {
            break
        }
    }
    return arr
    //return Array(arr[Int(left)...arr.endIndex-1])
}