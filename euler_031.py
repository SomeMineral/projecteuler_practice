###############################################################################
# 031 Coin sums
'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''
# 근성의 코딩... 이걸 어떻게 줄일 수 있을까...
value = 200
cur = [200,100,50,20,10,5,2,1]
max_coins = [int(value/i) for i in cur]
coin_count = 0
case_list = []

temp = value
for a0 in range(max_coins[0] + 1):
    temp0 = temp - a0 * cur[0]
    if temp0 >= 0:
        for a1 in range(max_coins[1] + 1):
            temp1 = temp0 - a1 * cur[1]
            if temp1 >= 0:
                for a2 in range(max_coins[2] + 1):
                    temp2 = temp1 - a2 * cur[2]
                    if temp2 >= 0:
                        for a3 in range(max_coins[3] + 1):
                            temp3 = temp2 - a3 * cur[3]
                            if temp3 >= 0:
                                for a4 in range(max_coins[4] + 1):
                                    temp4 = temp3 - a4 * cur[4]
                                    if temp4 >= 0:
                                        for a5 in range(max_coins[5] + 1):
                                            temp5 = temp4 - a5 * cur[5]
                                            if temp5 >= 0:
                                                for a6 in range(max_coins[6] + 1):
                                                    temp6 = temp5 - a6 * cur[6]
                                                    if temp6 >= 0:
                                                        for a7 in range(max_coins[7] + 1):
                                                            temp7 = temp6 - a7 * cur[7]
                                                            if temp7 == 0:
                                                                coin_count += 1
                                                                case_list.append((a0,a1,a2,a3,a4,a5,a6,a7))
                                                                break
                                                    else:
                                                        break
                                            else:
                                                break
                                    else:
                                        break
                            else:
                                break
                    else:
                        break
            else:
                break
    else:
        break

print(coin_count) #73682 