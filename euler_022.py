###############################################################################
# 022 Names scores
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
 begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
 multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN,
 which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
 So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
'''

entire_alphabet='abcdefghijklmnopqrstuvwxyz'
alpha_num = { entire_alphabet[i] : i+1 for i in range(len(entire_alphabet))}

with open('d:/euler/p022_names.txt') as file:
    name_list = file.readline().split(',')
name_list = [i.replace('"','').lower() for i in name_list]
name_list.sort()

# 이름별 점수(순서 적용 안 함) 모으기
sub_score_list = []
for name in name_list:
    sub_score = 0
    for x in name:
        sub_score += alpha_num[x]
    sub_score_list.append(sub_score)
# 합산하기 (앗차! 순서는 1부터 시작이지)
total_sum = 0
for i in range(len(name_list)):
    total_sum += (i+1) * sub_score_list[i]
print(total_sum) # 871198282