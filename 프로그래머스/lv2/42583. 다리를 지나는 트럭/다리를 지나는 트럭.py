def solution(bridge_length, weight, truck_weights):
    answer = 0
    end = []
    onBridge = []
    wait = truck_weights
    while True :
        #print(answer,"||", end, "||",onBridge,"||", wait)
        totalWieght = 0
        if len(onBridge) > 0 :
            toDelete = []
            for car in onBridge :
                car[1] += 1
                if car[1] >= bridge_length : 
                    toDelete.append(car)
                else :
                    totalWieght += car[0]
            for car in toDelete :
                end.append(onBridge.pop(onBridge.index(car)))
        if len(wait) > 0:
            if totalWieght+wait[0] <= weight :
                onBridge.append([wait.pop(0),0])

        if len(onBridge) == 0 and len(wait) == 0 :
            return answer+1
        
        answer += 1