import Foundation

func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    let m = arr1.count
    let n = arr2.count
    let p = arr2[0].count
    var answer = Array(repeating: [Int](), count: m)
    var result = 0
    for i in 0..<m {
        for j in 0..<p {
            result = 0
            for k in 0..<n {
                result += arr1[i][k] * arr2[k][j]
            }
            answer[i].append(result)
        }
    }
    return answer
}