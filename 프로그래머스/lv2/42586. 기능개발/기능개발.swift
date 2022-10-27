import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var answer = [Int]()
    var nowProgresses = progresses
    var index = 0
    var oldIndex = index
    while index < nowProgresses.count {
        oldIndex = index
        while oldIndex == index {
            nowProgresses = add(progresses: nowProgresses, speeds: speeds, index: index,day: 1 )
            index = counting(progresses: nowProgresses, index: index)
            //print(nowProgresses, index)
        }
        
        answer.append(index-oldIndex)
    }
    return answer
}
func add(progresses:[Int],speeds:[Int],index:Int,day:Int) -> [Int] {
    var vProgress = progresses
    for i in index..<progresses.count {
        vProgress[i] = progresses[i]+(speeds[i]*day)
    }
    return vProgress
}
func counting(progresses:[Int],index:Int) -> Int {
    for i in index..<progresses.count {
        if progresses[i] < 100 {
            return i
        }
    }
    return progresses.count
    //return progresses.count-1
}