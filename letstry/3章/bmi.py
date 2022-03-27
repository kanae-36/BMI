def calc(weight, height) :
    #BMI=体重[kg]÷(身長[m]×身長[m])
    bmi = weight / (height * height)
    return bmi

def message(bmi) :
    #タプル
    bmi_checks = (
        (0, 18.5, '栄養不足に注意しましょう'),
        (18.5, 25, '今の状態を維持しましょう'),
        (25, 99, '食事改善や運動を検討しましょう')
    )

    #BMI値によって肥満度を分類する
    if bmi < bmi_checks[0][1] :
        bmi_msg = bmi_checks[0][2]
    elif bmi >= bmi_checks[1][0] and bmi < bmi_checks[1][1] :
        bmi_msg = bmi_checks[1][2]
    else:
        bmi_msg = bmi_checks[2][2]
    
    return bmi_msg
