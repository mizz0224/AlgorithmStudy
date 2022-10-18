import Foundation

func solution(_ n:Int, _ words:[String]) -> [Int] {
    var oldWord = words[0]
    var newWord = ""
    var oldWords = [String]()
    oldWords.append(oldWord)
    for wordIndex in 1..<words.count {
        newWord = words[wordIndex]
        if oldWord[oldWord.index(oldWord.endIndex,offsetBy:-1)] != newWord[newWord.startIndex] || oldWords.contains(newWord){
            var who = (wordIndex + 1) % n
            who = who == 0 ? n : who
            var turn = Int(ceil(Double(wordIndex + 1) / Double(n)))
            return [who,turn]
        }
        
        oldWord = newWord
        oldWords.append(oldWord)
        
    }
    print(oldWords)
    return [0,0]
}
