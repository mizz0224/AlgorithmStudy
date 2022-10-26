import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var dict = [String:[String]]()
    for cloth in clothes {
        let type = cloth[1]
        let name = cloth[0]
        print(type,name)
        if !dict.keys.contains(type) {
            dict[type] = [name]
        } else {
            dict[type]!.append(name)
        }
    }
    var count = 1
    for type in dict.keys{
        count *= dict[type]!.count + 1
    }
    return count - 1
}