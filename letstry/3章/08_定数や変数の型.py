MY_HEIGHT = 1.7 #身長[m]
my_weight = 70 #体重[kg]
message = 'あなたのBMIは、'

#BMI=体重[kg]÷(身長[m]×身長[m])
my_bmi = my_weight / (MY_HEIGHT * MY_HEIGHT)
print(message)
print(my_bmi)
print(my_bmi > 25)
