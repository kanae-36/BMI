#あなたの身長は？（単位cm）
HEIGHT = 160

print(f'あなたの身長は{HEIGHT}cmです。')
print('-----')

#計算結果の表示メッセージ
kitchen_message = '最適なキッチンの高さ(そのn)は'

#キッチンの高さの目安計算（その1）
#キッチンの高さ＝身長[cm]÷2＋5cm
kitchen1 = HEIGHT / 2 + 5
message = kitchen_message.replace('そのn', 'その1')
print(f'{message}{kitchen1}cmです。')
print('-----')

#キッチンの高さの目安計算（その2）
#キッチンの高さ＝肘高cm－10cm
#肘高はおおよそ「身長[cm]－60cm」と言われています
kitchen2 = HEIGHT - 60 - 10
message = kitchen_message.replace('そのn', 'その2')
print(f'{message}{kitchen2}cmです。')
print('-----')
