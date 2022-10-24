import Foundation
func solution(_ s:String) -> [Int] {
    var dict = [Int:Int]()
    var answer = [Int]()
    var st = ""
    for ch in s {
        if ch.isNumber {
            st += String(ch)
        } else {
            if st !=  "" {
                if dict.keys.contains(Int(st)!) {
                    dict[Int(st)!]! += 1
                } else {
                    dict[Int(st)!] = 0
                }
            }
            st = ""
        }
    }
    let sortedDitionary = dict.sorted { $0.1 > $1.1 }
    for i in 0..<sortedDitionary.count {
        answer.append(sortedDitionary[i].key)
    }
    return answer
}