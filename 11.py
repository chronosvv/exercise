def packbag(weight, value, totalValue):
    weight_value = [[0 for i in range(totalValue+1)] for j in range(len(weight)+ 1)]
    weight = [0] + weight
    value = [0] + value
    for item in range(1, 5+1):
        for total_weight in range(1, 10+1):
            weight_value[item][total_weight] = weight_value[item-1][total_weight]
            if total_weight - weight[item] < 0:
                this_value = weight_value[item-1][total_weight]
            else:
                this_value = weight_value[item-1][total_weight-weight[item]] + value[item]

            if this_value > weight_value[item][total_weight]:
                weight_value[item][total_weight] = this_value

    choose = []
    for item_num in range(len(weight)-1, 0, -1):
        if weight_value[item_num][totalValue] > weight_value[item_num-1][totalValue]:
            choose.append(item_num)
            totalValue = totalValue - weight[item_num]
    total = 0
    for i in choose:
        total += value[i]

    return total, choose

if __name__ == "__main__":
    weight = [2, 2, 6, 5, 4]
    value = [6, 3, 5, 4, 6]
    totalValue = 10
    rtn, choose = packbag(weight, value, totalValue)
    print("total value:%d, choose:%s" %(rtn, str(choose)))

def packbag2(weight, value, totalValue):
    weight_value = [[0 for i in range(totalValue+1)] for j in range(len(weight)+1)]
    weight = [0] + weight
    value = [0] + value
    for item in range(1, 5+1):
        for total_weight in range(1, 10+1):
            weight_value[item][total_weight] = weight_value[item-1][total_weight]
            if total_weight - weight[item] < 0:
                this_value = weight_value[item-1][total_weight]
            else:
                this_value = weight_value[item-1][total_weight-weight[item]] + value[item]

            if this_value > weight_value[item][total_weight]:
                weight_value[item][total_weight] = this_value
    choose = []
    for item_num in range(len(weight)-1, 0, -1):
        if weight_value[item_num][totalValue] > weight_value[item_num-1][totalValue]:
            choose.append(item_num)
            totalValue = totalValue - weight[item_num]
    total = 0
    for i in choose:
        total += value[i]

    return total, choose

if __name__ == "__main__":
    weight = [2, 2, 6, 5, 4]
    value = [6, 3, 5, 4, 6]
    totalValue = 10
    rtn, choose = packbag2(weight, value, totalValue)
    print("total value:%d, choose:%s"%(rtn, str(choose)))