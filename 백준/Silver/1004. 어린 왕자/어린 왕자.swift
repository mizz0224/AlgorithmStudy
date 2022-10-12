//
//  main.swift
//  algorithmStudy
//
//  Created by heojaenyeong on 2022/10/12.
//

import Foundation
var countArr:[Int] = []
for _ in 0..<Int(readLine()!)! {
    let point = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (x1,y1,x2,y2) = (point[0],point[1],point[2],point[3])
    var count:Int = 0
    for _ in 0..<Int(readLine()!)!{
        let point = readLine()!.split(separator: " ").map{Int(String($0))!}
        let (cx,cy,r) = (point[0],point[1],point[2])
        if pow(Double(r),2.0) > pow(Double(cx-x1),2.0) + pow(Double(cy-y1),2.0) ||  pow(Double(r),2.0) > pow(Double(cx-x2),2.0) + pow(Double(cy-y2),2.0){
            count = count+1
        }
        if pow(Double(r),2.0) > pow(Double(cx-x1),2.0) + pow(Double(cy-y1),2.0) &&  pow(Double(r),2.0) > pow(Double(cx-x2),2.0) + pow(Double(cy-y2),2.0){
            count = count-1
        }
    }
    countArr.append(count)
}
for count in countArr{
    print(count)
}
