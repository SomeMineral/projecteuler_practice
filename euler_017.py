###############################################################################
# 017 Number letter counts
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
 how many letters would be used?
NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

# 코딩 작업으로 구사하기 실패. 단순 계산으로 찾음.

# 'and' : 01 ~ 99 in 세자리 자연수.
# => len('and') * 99 * 9 = 2673
# 'one', ... , 'nine' 백의 자리 : 100~199, 200~299, ..., 900~999 : 각각 100개씩.
# => len('onetwothreefourfivesixseveneightnine') * 100 = 3600
# 'hundred' 100 ~ 999: 900개
# => len('hundred') * 900
# 십의자리 0(2)0~0(2)9, 0(3)0~0(3)9, ..., 0(9)0~0(9)9 // 1(2)0~1(2)9, ... , 1(9)0~1(9)9 // ... // 9(2)0~9(2)9, ... , 9(9)0~9(9)9//
# => len('twentythirtyfortyfiftysixtyseventyeightyninety') * 10 * 10 = 4600 
# 십의자리+일의자리 0(10) ~ 0(19), 1(10)~1(19), ..., 9(10)~9(19)
# => len('teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen') * 10 = 700 
# 일의자리 00(1)~00(9), 02(1)~02(9), 03(1)~03(9), ... , 09(1)~09(9) // ... // 99(1)~99(9)
# => len('onetwothreefourfivesixseveneightnine') * 9 * 10 = 3240
# => len('onethousand') = 11

2673+3600+6300+4600+700+3240+11 #21124