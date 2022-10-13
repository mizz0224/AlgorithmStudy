func solution(_ s:String) -> String {
    var str = s
    var answer = ""
    var isChangeToUppercase = true
    for char in str{
        if isChangeToUppercase {
            answer += String(char).uppercased()
        } else {
            answer += String(char).lowercased()
        }
        isChangeToUppercase = false
        if char == " " {
            isChangeToUppercase = true
        }
    }
    return answer
}