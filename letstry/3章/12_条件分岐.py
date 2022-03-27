#名前を入力
my_name = input('名前を入力してください：')
message = my_name + 'さんのBMIは、'

#BMI=体重[kg]÷(身長[m]×身長[m])
my_bmi = 70 / (1.7 * 1.7)
print(f'{message}{my_bmi}です。')

#BMI値によって肥満度を分類する
#出典：日本肥満学会（http://www.jasso.or.jp/data/magazine/pdf/chart_A.pdf）より
if my_bmi < 18.5 :
    print('低体重(Underweight)')
elif my_bmi >= 18.5 and my_bmi < 25 :
    print('標準体重(Normal range)')
elif my_bmi >= 25 and my_bmi < 30 :
    print('肥満度1(Pre-obese)')
elif my_bmi >= 30 and my_bmi < 35 :
    print('肥満度2(Obese class I)')
elif my_bmi >= 35 and my_bmi < 40 :
    print('肥満度3(Obese class II)')
else:
    print('肥満度4(Obese class III)')
