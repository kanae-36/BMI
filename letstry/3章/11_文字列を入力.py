#名前を入力
my_name = input('名前を入力してください：')
message = my_name + 'さんのBMIは、'

#BMI=体重[kg]÷(身長[m]×身長[m])
my_bmi = 70 / (1.7 * 1.7)
print(f'{message}{my_bmi}です。')
