#python

weight = [64,49,58]
total_weight = 0
for i in range(3):
    print("第{}位同學的體重為{}".format(i+1, weight[i]))
    total_weight += weight[i]
print("-----------------")
print("三位同學的體重總合為 {} 公斤".format(total_weight))
