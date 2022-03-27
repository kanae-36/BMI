import sys
import kitchen

if len(sys.argv)<2:
    print('表示したい名前を指定してください。')
    sys.exit()

my_name = sys.argv[1]

#身長と今のキッチンの高さ情報をひとまとめにする
kitchen_elements = [0.0, 0.0]
kitchen_messages = ['身長(cm)', '今のキッチンの高さ(cm)']

#2つの項目を入力
num = 0
for entry in kitchen_messages :
    kitchen_elements[num] = input(entry + 'を入力してください：')
    num = num + 1

print('-----')

try:
    #それぞれの高さ情報を文字から浮動小数点に変換
    human_height = float(kitchen_elements[0])
    kitchen_height = float(kitchen_elements[1])

    print(f'あなたの身長は{human_height}cmです。')
    print('-----')

    #計算結果の表示メッセージ
    kitchen_message = my_name + 'さんの最適なキッチンの高さ(そのn)は'

    #キッチンの高さの目安計算（その1）
    kitchen1 = kitchen.calc1(height=human_height)
    message = kitchen_message.replace('そのn', 'その1')
    print(f'{message}{kitchen1}cmです。')

    kitchen.resultmessage(calc_kitchen=kitchen1, now_kitchen=kitchen_height)

    print('-----')

    #キッチンの高さの目安計算（その2）
    kitchen2 = kitchen.calc2(height=human_height)
    message = kitchen_message.replace('そのn', 'その2')
    print(f'{message}{kitchen2}cmです。')

    kitchen.resultmessage(calc_kitchen=kitchen2, now_kitchen=kitchen_height)

    print('-----')

except ValueError as e:
    print('身長または今のキッチンの高さを見直してください。')
    print(e)
except:
    import traceback
    traceback.print_exc()

