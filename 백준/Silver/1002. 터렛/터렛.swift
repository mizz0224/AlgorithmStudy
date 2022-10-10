import Foundation

for _ in 0..<Int(readLine()!)! {
	let point = readLine()!.split(separator: " ").map{Int(String($0))!}
	let (x1,y1,r1,x2,y2,r2) = (point[0],point[1],point[2],point[3],point[4],point[5])
  let distance = sqrt(pow(Double(x1-x2),2) + pow(Double(y1-y2),2))
	if x1 == x2 && y1 == y2 && r1 == r2 { // 두원이 일치할때
    print(-1)
  } else {
    if Double(abs(r1 + r2)) == distance || Double(abs(r1 - r2)) == distance {   //두원 사이의 거리가 반지름의 합과 일치할때(한점에서 만날때) 
      print(1)
    } else if Double(r1 + r2) > distance &&  Double(abs(r1-r2)) < distance{
      print(2)
    } else {
      print(0)
    }
  }
  
}
