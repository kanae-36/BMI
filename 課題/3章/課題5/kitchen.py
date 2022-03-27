def calc1(height) :
    #キッチンの高さの目安計算（その1）
    #キッチンの高さ＝身長[cm]÷2＋5cm
    kitchen = height / 2 + 5
    return kitchen

def calc2(height) :
    #キッチンの高さの目安計算（その2）
    #キッチンの高さ＝肘高cm－10cm
    #肘高はおおよそ「身長[cm]－60cm」と言われています
    kitchen = height - 60 - 10
    return kitchen

def resultmessage(calc_kitchen, now_kitchen) :
    #タプル
    k_messages = (
        ('最適な高さです', 'スリッパの厚みを変えて微調整してみましょう'),
        ('目安より低いようです', '腰痛に注意しましょう'),
        ('目安より高いようです', '肩こりに注意しましょう')
    )

    #今のキッチンの高さと比較し目安と同じなら適合
    #それ以外なら高い・低いと表示する
    if calc_kitchen == now_kitchen :
        print(k_messages[0][0])
        print(k_messages[0][1])
    elif calc_kitchen > now_kitchen :
        print(k_messages[1][0])
        print(k_messages[1][1])
    else:
        print(k_messages[2][0])
        print(k_messages[2][1])
