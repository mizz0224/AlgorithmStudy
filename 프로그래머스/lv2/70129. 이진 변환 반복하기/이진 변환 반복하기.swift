import Foundation

func solution(_ s:String) -> [Int] {
    var count = 0
    var zeroCount = 0
    var totalZeroCount = 0
    var str = s
    //return [Int(String(repeating:"1", count:str.count-zeroCounter(getStr:str)))!,str.count-zeroCounter(getStr:str)]
    while true {
        zeroCount = zeroCounter(getStr:str)
        if str == "1" {
            break
        }
        str = String(str.count-zeroCount,radix:2)
        totalZeroCount += zeroCount
        count += 1
    }
    return [count,totalZeroCount]
}

func zeroCounter(getStr:String) -> Int {
    var zeroCount = 0
    for ch in getStr {
        if ch == "0" {
            zeroCount += 1
        }
    }
    return zeroCount
}