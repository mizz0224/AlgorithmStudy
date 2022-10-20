import Foundation

func solution(_ n:Int) -> Int 
{
    
    //return String(n, radix:2).filter{$0 == "1"}.count
    var N:Int = n
    var count = 0
    while (N != 0) {
        if N%2 == 1 {
            count += 1
        }
        N /= 2
    }
    return count
}
/*
    1 1 
    2 1 점 
    3 1 점 1 
    4 1 점 점 
    5 1 점 점 1 
    */
