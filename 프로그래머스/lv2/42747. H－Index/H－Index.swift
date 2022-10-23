func solution(_ citations:[Int]) -> Int {
    let sorted = quicksort(citations)
    for index in 0..<sorted.count{
        if index >= sorted[index]{
            return index
        }
        
    }
    return sorted.count
}

func quicksort<T: Comparable>(_ a: [T]) -> [T] {
  guard a.count > 1 else { return a }

  let pivot = a[a.count/2]
  let less = a.filter { $0 > pivot }
  let equal = a.filter { $0 == pivot }
  let greater = a.filter { $0 < pivot }

  return quicksort(less) + equal + quicksort(greater)
}