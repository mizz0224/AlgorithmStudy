import Foundation

func solution(_ n:Int, _ a:Int, _ b:Int) -> Int
{
    var answer = 0
    var a = a
    var b = b
    var count = 0
    while true {
        count += 1
        if a%2 == 0 {
            a = a/2
        } else {
            a = (a+1)/2
        }
        if b%2 == 0 {
            b = b/2
        } else {
            b = (b+1)/2
        }
        if a == b {
            return count
        }
    }
    
    return answer
}
