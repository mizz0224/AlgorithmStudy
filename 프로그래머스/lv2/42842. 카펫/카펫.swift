import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    let area = brown + yellow
    let sqrtNum = Int(sqrt(Double(area)))
    var height = sqrtNum
    var width = area / sqrtNum
    while height > 1 {
        if height * width == area && (height-2) * (width-2) == yellow {
            return [width , height]
        }
        height = height - 1
        width = area / height
    }
    
    return [area,1]
}