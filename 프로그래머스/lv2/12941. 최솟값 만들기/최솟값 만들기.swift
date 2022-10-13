import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int
{
    var ans = 0
    var A2 : [Int] = quicksort(A)
    var B2 : [Int] = quicksort(B)
    B2 = B2.reversed()
    for n in 0..<A2.count {
        ans += A2[n]*B2[n]
    }
    

    return ans
}
func quicksort<T: Comparable>(_ a: [T]) -> [T] {
  guard a.count > 1 else { return a }

  let pivot = a[a.count/2]
  let less = a.filter { $0 < pivot }
  let equal = a.filter { $0 == pivot }
  let greater = a.filter { $0 > pivot }

  return quicksort(less) + equal + quicksort(greater)
}