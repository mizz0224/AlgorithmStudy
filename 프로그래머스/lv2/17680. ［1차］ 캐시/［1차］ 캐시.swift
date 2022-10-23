func solution(_ cacheSize:Int, _ cities:[String]) -> Int {
    var cache = [String]()
    var runningTime = 0
    var city = ""
    for citi in cities {
        city = citi.lowercased()
        if cache.contains(city) {
            runningTime += 1
            cache.remove(at: cache.firstIndex(of: city)!)
        } else {
            runningTime += 5
        }
        if cache.count >= cacheSize && cacheSize>0 {
            cache.remove(at: 0)
        }
        if cache.count < cacheSize {
            cache.append(city)
        }
    }
    return runningTime
}