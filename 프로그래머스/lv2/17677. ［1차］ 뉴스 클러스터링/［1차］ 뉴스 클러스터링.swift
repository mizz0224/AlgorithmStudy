import Foundation

func solution(_ str1:String, _ str2:String) -> Int {
    if str1.lowercased() == str2.lowercased() {
        //print("same")
        return 65536
        
    }
    var arr1 = makeStrArr(s: str1.lowercased())
    var arr2 = makeStrArr(s: str2.lowercased())
    
    var unionLen = arr1.count + arr2.count
    var intersectionLen = 0
    for i in 0..<arr1.count {
        for j in 0..<arr2.count {
            if arr1[i] == arr2[j] {
                intersectionLen += 1
                arr2.remove(at: j)
                break
            }
        }
    }
    unionLen -= intersectionLen
    if intersectionLen == 0 && unionLen > 0 { return 0 }
    unionLen = unionLen == 0 ? 1 : unionLen
    intersectionLen = intersectionLen == 0 ? 1: intersectionLen
    return Int(Double(intersectionLen)/Double(unionLen) * Double(65536))
}
func makeStrArr(s : String) -> [String] {
    var arr = [String]()
    var st = ""
    for i in 0..<s.count {
        if i > s.count-2 { break }
        let ch1 = s[s.index(s.startIndex, offsetBy: i)]
        let ch2 = s[s.index(s.startIndex, offsetBy: i+1)]
        if ch1.isLetter && ch2.isLetter {
            st = String(ch1) + String(ch2)
            arr.append(st)
        }
        
    }
    return arr
}