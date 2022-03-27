import sys
import cv2

if len(sys.argv)<2:
    print('表示したいファイル名を指定してください。')
    sys.exit()

file = sys.argv[1]

try:
    img = cv2.imread(file)

    if img is None:
        raise ValueError('ファイルが見つかりません。')

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    retValue, img_thresh = cv2.threshold(img_gray, 100, 200, cv2.THRESH_BINARY)
#   retValue, img_thresh = cv2.threshold(img_gray, 90, 200, cv2.THRESH_BINARY)
#   retValue, img_thresh = cv2.threshold(img_gray, 90, 200, cv2.THRESH_BINARY_INV)
#   retValue, img_thresh = cv2.threshold(img_gray, 90, 200, cv2.THRESH_TOZERO)
#   retValue, img_thresh = cv2.threshold(img_gray, 90, 200, cv2.THRESH_TOZERO_INV)

    cv2.imshow(file, img_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except ValueError as e:
    print(e)
except:
    import traceback
    traceback.print_exc()
