import cv2 as cv
import numpy as np
import mediapipe as mp
import tqdm
import time
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=100):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "static/font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv.cvtColor(np.asarray(img), cv.COLOR_RGB2BGR)


def hand_predict(image_path):
    mp_hand = mp.solutions.hands
    print(image_path)

    # 导入模型
    hands = mp_hand.Hands(static_image_mode=False,
                          max_num_hands=1,
                          min_detection_confidence=0.3,
                          min_tracking_confidence=0.3
                          )

    # 导入绘图函数
    mpDraw = mp.solutions.drawing_utils
    img = cv.imread('./static/' + image_path + '.jpg')  # 需要标记的手掌图片的位置
    # look_img(img)
    img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(img_RGB)
    lmList = []
    result_path = './static/' + image_path + '_r.jpg'
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

    if lmList[12][2] < lmList[0][2]:
        if lmList[4][1] < lmList[20][1]:
            print('手心')
            textSize = 80
            cx0, cy0 = lmList[0][1], lmList[0][2]
            cx1, cy1 = lmList[1][1], lmList[1][2]
            img = cv2ImgAddText(img, "鱼际穴", cx1, cy1, (0, 0, 0), textSize)
            cv.circle(img, (cx1, cy1), 10, (255, 0, 255), cv.FILLED)
            cx4, cy4 = lmList[4][1], lmList[4][2]
            img = cv2ImgAddText(img, "十宣穴1", cx4, cy4, (0, 0, 0), textSize)
            cv.circle(img, (cx4, cy4), 10, (255, 0, 255), cv.FILLED)
            cx6, cy6 = lmList[6][1], lmList[6][2]
            img = cv2ImgAddText(img, "四缝穴1", cx6, cy6, (0, 0, 0), textSize)
            cv.circle(img, (cx6, cy6), 10, (255, 0, 255), cv.FILLED)
            cx8, cy8 = lmList[8][1], lmList[8][2]
            img = cv2ImgAddText(img, "十宣穴2", cx8, cy8, (0, 0, 0), textSize)
            cv.circle(img, (cx8, cy8), 10, (255, 0, 255), cv.FILLED)
            cx9, cy9 = lmList[9][1], lmList[9][2]
            cv.circle(img, ((3 * cx9 + cx0) // 4, (3 * cy9 + cy0) // 4), 10, (255, 0, 255), cv.FILLED)
            img = cv2ImgAddText(img, "劳宫穴", (3 * cx9 + cx0) // 4, (3 * cy9 + cy0) // 4, (0, 0, 0), textSize)
            x_center, y_center = (cx9 + cx0) // 2, (cy9 + cy0) // 2
            cx10, cy10 = lmList[10][1], lmList[10][2]
            img = cv2ImgAddText(img, "四缝穴2", cx10, cy10, (0, 0, 0), textSize)
            cv.circle(img, (cx10, cy10), 10, (255, 0, 255), cv.FILLED)
            cx11, cy11 = lmList[11][1], lmList[11][2]
            cx12, cy12 = lmList[12][1], lmList[12][2]
            img = cv2ImgAddText(img, "十宣穴3", cx12, cy12, (0, 0, 0), textSize)
            cv.circle(img, (cx12, cy12), 10, (255, 0, 255), cv.FILLED)
            img = cv2ImgAddText(img, "中冲穴", (2 * cx12 + cx11) // 3, (2 * cy12 + cy11) // 3, (0, 0, 0), textSize)
            cv.circle(img, ((2 * cx12 + cx11) // 3, (2 * cy12 + cy11) // 3), 10, (255, 0, 255), cv.FILLED)
            cx14, cy14 = lmList[14][1], lmList[14][2]
            img = cv2ImgAddText(img, "四缝穴3", cx14, cy14, (0, 0, 0), textSize)
            cv.circle(img, (cx14, cy14), 10, (255, 0, 255), cv.FILLED)
            cx16, cy16 = lmList[16][1], lmList[16][2]
            img = cv2ImgAddText(img, "十宣穴4", cx16, cy16, (0, 0, 0), textSize)
            cv.circle(img, (cx16, cy16), 10, (255, 0, 255), cv.FILLED)
            cx17, cy17 = lmList[17][1], lmList[17][2]
            img = cv2ImgAddText(img, "少府穴", (3 * cx17 + cx0) // 4, (3 * cy17 + cy0) // 4, (0, 0, 0), textSize)
            cv.circle(img, ((3 * cx17 + cx0) // 4, (3 * cy17 + cy0) // 4), 10, (255, 0, 255), cv.FILLED)
            cx18, cy18 = lmList[18][1], lmList[18][2]
            img = cv2ImgAddText(img, "四缝穴4", cx18, cy18, (0, 0, 0), textSize)
            cv.circle(img, (cx18, cy18), 10, (255, 0, 255), cv.FILLED)
            cx20, cy20 = lmList[20][1], lmList[20][2]
            img = cv2ImgAddText(img, "十宣穴5", cx20, cy20, (0, 0, 0), textSize)
            cv.circle(img, (cx20, cy20), 10, (255, 0, 255), cv.FILLED)
            cv.imwrite(result_path, img)  # 标记后的图片存储位置
        else:
            print('手背')
            textSize = 70
            cx0, cy0 = lmList[0][1], lmList[0][2]
            cx1, cy1 = lmList[1][1], lmList[1][2]
            x_zhongquan, y_zhongquan = (3 * cx0 + cx1) // 4, (3 * cy0 + cy1) // 4
            img = cv2ImgAddText(img, "中泉穴", x_zhongquan, y_zhongquan, (0, 0, 0), textSize)
            cv.circle(img, (x_zhongquan, y_zhongquan), 10, (255, 0, 255), cv.FILLED)
            cx2, cy2 = lmList[2][1], lmList[2][2]
            cx3, cy3 = lmList[3][1], lmList[3][2]
            img = cv2ImgAddText(img, "大骨空穴", cx3, cy3, (0, 0, 0), textSize)
            cv.circle(img, (cx3, cy3), 10, (255, 0, 255), cv.FILLED)
            cx4, cy4 = lmList[4][1], lmList[4][2]
            x_shaoshang, y_shaoshang = (cx3 + cx4) // 2, (cy3 + cy4) // 2
            img = cv2ImgAddText(img, "少商穴", x_shaoshang, y_shaoshang, (0, 0, 0), textSize)
            cv.circle(img, (x_shaoshang, y_shaoshang), 10, (255, 0, 255), cv.FILLED)
            img = cv2ImgAddText(img, "十宣穴1", cx4, cy4, (0, 0, 0), textSize)
            cv.circle(img, (cx4, cy4), 10, (255, 0, 255), cv.FILLED)
            cx5, cy5 = lmList[5][1], lmList[5][2]
            x_053, y_053 = (3 * cx5 + cx0) // 4, (3 * cy5 + cy0) // 4
            x_05, y_05 = (cx5 + cx0) // 2, (cy5 + cy0) // 2
            x_sanjian, y_sanjian = (x_053 + cx2) // 2, (y_053 + cy2) // 2
            x_hegu, y_hegu = (x_05 + cx2) // 2, (y_05 + cy2) // 2
            img = cv2ImgAddText(img, "三间穴", x_sanjian, y_sanjian, (0, 0, 0), textSize)
            cv.circle(img, (x_sanjian, y_sanjian), 10, (255, 0, 255), cv.FILLED)
            img = cv2ImgAddText(img, "合谷穴", x_hegu, y_hegu, (0, 0, 0), textSize)
            cv.circle(img, (x_hegu, y_hegu), 10, (255, 0, 255), cv.FILLED)
            x_baxie1, y_baxie1 = (cx2 + cx5) // 2, (cy2 + cy5) // 2
            img = cv2ImgAddText(img, "八邪穴1", x_baxie1, y_baxie1, (0, 0, 0), textSize)
            cv.circle(img, (x_baxie1, y_baxie1), 10, (255, 0, 255), cv.FILLED)
            x_yaotong1, y_yaotong1 = (cx5 + cx0) // 2, (cy5 + cy0) // 2
            img = cv2ImgAddText(img, "腰痛点1", x_yaotong1, y_yaotong1, (0, 0, 0), textSize)
            cv.circle(img, (x_yaotong1, y_yaotong1), 10, (255, 0, 255), cv.FILLED)
            cx8, cy8 = lmList[8][1], lmList[8][2]
            img = cv2ImgAddText(img, "十宣穴2", cx8, cy8, (0, 0, 0), textSize)
            cv.circle(img, (cx8, cy8), 10, (255, 0, 255), cv.FILLED)
            cx9, cy9 = lmList[9][1], lmList[9][2]
            x_baxie2, y_baxie2 = (cx9 + cx5) // 2, (cy9 + cy5) // 2
            img = cv2ImgAddText(img, "八邪穴2", x_baxie2, y_baxie2, (0, 0, 0), textSize)
            cv.circle(img, (x_baxie2, y_baxie2), 10, (255, 0, 255), cv.FILLED)
            cx10, cy10 = lmList[10][1], lmList[10][2]
            img = cv2ImgAddText(img, "中魁穴", cx10, cy10, (0, 0, 0), textSize)
            cv.circle(img, (cx10, cy10), 10, (255, 0, 255), cv.FILLED)
            cx12, cy12 = lmList[12][1], lmList[12][2]
            img = cv2ImgAddText(img, "十宣穴3", cx12, cy12, (0, 0, 0), textSize)
            cv.circle(img, (cx12, cy12), 10, (255, 0, 255), cv.FILLED)
            cx13, cy13 = lmList[13][1], lmList[13][2]
            x_baxie3, y_baxie3 = (cx9 + cx13) // 2, (cy9 + cy13) // 2
            img = cv2ImgAddText(img, "八邪穴3", x_baxie3, y_baxie3, (0, 0, 0), textSize)
            cv.circle(img, (x_baxie3, y_baxie3), 10, (255, 0, 255), cv.FILLED)
            x_yaotong2, y_yaotong2 = (cx0 + cx13) // 2, (cy0 + cy13) // 2
            img = cv2ImgAddText(img, "腰痛点2", x_yaotong2, y_yaotong2, (0, 0, 0), textSize)
            cv.circle(img, (x_yaotong2, y_yaotong2), 10, (255, 0, 255), cv.FILLED)
            cx16, cy16 = lmList[16][1], lmList[16][2]
            img = cv2ImgAddText(img, "十宣穴4", cx16, cy16, (0, 0, 0), textSize)
            cv.circle(img, (cx16, cy16), 10, (255, 0, 255), cv.FILLED)
            cx17, cy17 = lmList[17][1], lmList[17][2]
            img = cv2ImgAddText(img, "后溪穴", cx17, cy17, (0, 0, 0), textSize)
            cv.circle(img, (cx17, cy17), 10, (255, 0, 255), cv.FILLED)
            x_baxie4, y_baxie4 = (cx13 + cx17) // 2, (cy13 + cy17) // 2
            img = cv2ImgAddText(img, "八邪穴4", x_baxie4, y_baxie4, (0, 0, 0), textSize)
            cv.circle(img, (x_baxie4, y_baxie4), 10, (255, 0, 255), cv.FILLED)
            cx18, cy18 = lmList[18][1], lmList[18][2]
            img = cv2ImgAddText(img, "小骨空穴", cx18, cy18, (0, 0, 0), textSize)
            cv.circle(img, (cx18, cy18), 10, (255, 0, 255), cv.FILLED)
            cx20, cy20 = lmList[20][1], lmList[20][2]
            img = cv2ImgAddText(img, "十宣穴5", cx20, cy20, (0, 0, 0), textSize)
            cv.circle(img, (cx20, cy20), 10, (255, 0, 255), cv.FILLED)
            cv.imwrite(result_path, img)  # 标记后的图片存储位置
    else:
        if lmList[4][1] > lmList[20][1]:
            print('手心')
            textSize = 80
            cx0, cy0 = lmList[0][1], lmList[0][2]
            cx1, cy1 = lmList[1][1], lmList[1][2]
            img = cv2ImgAddText(img, "鱼际穴", cx1, cy1, (0, 0, 0), textSize)
            cv.circle(img, (cx1, cy1), 10, (255, 0, 255), cv.FILLED)
            cx4, cy4 = lmList[4][1], lmList[4][2]
            img = cv2ImgAddText(img, "十宣穴1", cx4, cy4, (0, 0, 0), textSize)
            cv.circle(img, (cx4, cy4), 10, (255, 0, 255), cv.FILLED)
            cx6, cy6 = lmList[6][1], lmList[6][2]
            img = cv2ImgAddText(img, "四缝穴1", cx6, cy6, (0, 0, 0), textSize)
            cv.circle(img, (cx6, cy6), 10, (255, 0, 255), cv.FILLED)
            cx8, cy8 = lmList[8][1], lmList[8][2]
            img = cv2ImgAddText(img, "十宣穴2", cx8, cy8, (0, 0, 0), textSize)
            cv.circle(img, (cx8, cy8), 10, (255, 0, 255), cv.FILLED)
            cx9, cy9 = lmList[9][1], lmList[9][2]
            cv.circle(img, ((3 * cx9 + cx0) // 4, (3 * cy9 + cy0) // 4), 10, (255, 0, 255), cv.FILLED)
            img = cv2ImgAddText(img, "劳宫穴", (3 * cx9 + cx0) // 4, (3 * cy9 + cy0) // 4, (0, 0, 0), textSize)
            x_center, y_center = (cx9 + cx0) // 2, (cy9 + cy0) // 2
            cx10, cy10 = lmList[10][1], lmList[10][2]
            img = cv2ImgAddText(img, "四缝穴2", cx10, cy10, (0, 0, 0), textSize)
            cv.circle(img, (cx10, cy10), 10, (255, 0, 255), cv.FILLED)
            cx11, cy11 = lmList[11][1], lmList[11][2]
            cx12, cy12 = lmList[12][1], lmList[12][2]
            img = cv2ImgAddText(img, "十宣穴3", cx12, cy12, (0, 0, 0), textSize)
            cv.circle(img, (cx12, cy12), 10, (255, 0, 255), cv.FILLED)
            img = cv2ImgAddText(img, "中冲穴", (2 * cx12 + cx11) // 3, (2 * cy12 + cy11) // 3, (0, 0, 0), textSize)
            cv.circle(img, ((2 * cx12 + cx11) // 3, (2 * cy12 + cy11) // 3), 10, (255, 0, 255), cv.FILLED)
            cx14, cy14 = lmList[14][1], lmList[14][2]
            img = cv2ImgAddText(img, "四缝穴3", cx14, cy14, (0, 0, 0), textSize)
            cv.circle(img, (cx14, cy14), 10, (255, 0, 255), cv.FILLED)
            cx16, cy16 = lmList[16][1], lmList[16][2]
            img = cv2ImgAddText(img, "十宣穴4", cx16, cy16, (0, 0, 0), textSize)
            cv.circle(img, (cx16, cy16), 10, (255, 0, 255), cv.FILLED)
            cx17, cy17 = lmList[17][1], lmList[17][2]
            img = cv2ImgAddText(img, "少府穴", (3 * cx17 + cx0) // 4, (3 * cy17 + cy0) // 4, (0, 0, 0), textSize)
            cv.circle(img, ((3 * cx17 + cx0) // 4, (3 * cy17 + cy0) // 4), 10, (255, 0, 255), cv.FILLED)
            cx18, cy18 = lmList[18][1], lmList[18][2]
            img = cv2ImgAddText(img, "四缝穴4", cx18, cy18, (0, 0, 0), textSize)
            cv.circle(img, (cx18, cy18), 10, (255, 0, 255), cv.FILLED)
            cx20, cy20 = lmList[20][1], lmList[20][2]
            img = cv2ImgAddText(img, "十宣穴5", cx20, cy20, (0, 0, 0), textSize)
            cv.circle(img, (cx20, cy20), 10, (255, 0, 255), cv.FILLED)
            cv.imwrite(result_path, img)  # 标记后的图片存储位置
        else:
            print('手背')
            textSize = 70
            cx0, cy0 = lmList[0][1], lmList[0][2]
            cx1, cy1 = lmList[1][1], lmList[1][2]
            x_zhongquan, y_zhongquan = (3 * cx0 + cx1) // 4, (3 * cy0 + cy1) // 4
            img = cv2ImgAddText(img, "中泉穴", x_zhongquan, y_zhongquan, (0, 0, 0), textSize)
            cv.circle(img, (x_zhongquan, y_zhongquan), 10, (255, 0, 255), cv.FILLED)
            cx2, cy2 = lmList[2][1], lmList[2][2]
            cx3, cy3 = lmList[3][1], lmList[3][2]
            img = cv2ImgAddText(img, "大骨空穴", cx3, cy3, (0, 0, 0), textSize)
            cv.circle(img, (cx3, cy3), 10, (255, 0, 255), cv.FILLED)
            cx4, cy4 = lmList[4][1], lmList[4][2]
            x_shaoshang, y_shaoshang = (cx3 + cx4) // 2, (cy3 + cy4) // 2
            img = cv2ImgAddText(img, "少商穴", x_shaoshang, y_shaoshang, (0, 0, 0), textSize)
            cv.circle(img, (x_shaoshang, y_shaoshang), 10, (255, 0, 255), cv.FILLED)
            img = cv2ImgAddText(img, "十宣穴1", cx4, cy4, (0, 0, 0), textSize)
            cv.circle(img, (cx4, cy4), 10, (255, 0, 255), cv.FILLED)
            cx5, cy5 = lmList[5][1], lmList[5][2]
            x_053, y_053 = (3 * cx5 + cx0) // 4, (3 * cy5 + cy0) // 4
            x_05, y_05 = (cx5 + cx0) // 2, (cy5 + cy0) // 2
            x_sanjian, y_sanjian = (x_053 + cx2) // 2, (y_053 + cy2) // 2
            x_hegu, y_hegu = (x_05 + cx2) // 2, (y_05 + cy2) // 2
            img = cv2ImgAddText(img, "三间穴", x_sanjian, y_sanjian, (0, 0, 0), textSize)
            cv.circle(img, (x_sanjian, y_sanjian), 10, (255, 0, 255), cv.FILLED)
            img = cv2ImgAddText(img, "合谷穴", x_hegu, y_hegu, (0, 0, 0), textSize)
            cv.circle(img, (x_hegu, y_hegu), 10, (255, 0, 255), cv.FILLED)
            x_baxie1, y_baxie1 = (cx2 + cx5) // 2, (cy2 + cy5) // 2
            img = cv2ImgAddText(img, "八邪穴1", x_baxie1, y_baxie1, (0, 0, 0), textSize)
            cv.circle(img, (x_baxie1, y_baxie1), 10, (255, 0, 255), cv.FILLED)
            x_yaotong1, y_yaotong1 = (cx5 + cx0) // 2, (cy5 + cy0) // 2
            img = cv2ImgAddText(img, "腰痛点1", x_yaotong1, y_yaotong1, (0, 0, 0), textSize)
            cv.circle(img, (x_yaotong1, y_yaotong1), 10, (255, 0, 255), cv.FILLED)
            cx8, cy8 = lmList[8][1], lmList[8][2]
            img = cv2ImgAddText(img, "十宣穴2", cx8, cy8, (0, 0, 0), textSize)
            cv.circle(img, (cx8, cy8), 10, (255, 0, 255), cv.FILLED)
            cx9, cy9 = lmList[9][1], lmList[9][2]
            x_baxie2, y_baxie2 = (cx9 + cx5) // 2, (cy9 + cy5) // 2
            img = cv2ImgAddText(img, "八邪穴2", x_baxie2, y_baxie2, (0, 0, 0), textSize)
            cv.circle(img, (x_baxie2, y_baxie2), 10, (255, 0, 255), cv.FILLED)
            cx10, cy10 = lmList[10][1], lmList[10][2]
            img = cv2ImgAddText(img, "中魁穴", cx10, cy10, (0, 0, 0), textSize)
            cv.circle(img, (cx10, cy10), 10, (255, 0, 255), cv.FILLED)
            cx12, cy12 = lmList[12][1], lmList[12][2]
            img = cv2ImgAddText(img, "十宣穴3", cx12, cy12, (0, 0, 0), textSize)
            cv.circle(img, (cx12, cy12), 10, (255, 0, 255), cv.FILLED)
            cx13, cy13 = lmList[13][1], lmList[13][2]
            x_baxie3, y_baxie3 = (cx9 + cx13) // 2, (cy9 + cy13) // 2
            img = cv2ImgAddText(img, "八邪穴3", x_baxie3, y_baxie3, (0, 0, 0), textSize)
            cv.circle(img, (x_baxie3, y_baxie3), 10, (255, 0, 255), cv.FILLED)
            x_yaotong2, y_yaotong2 = (cx0 + cx13) // 2, (cy0 + cy13) // 2
            img = cv2ImgAddText(img, "腰痛点2", x_yaotong2, y_yaotong2, (0, 0, 0), textSize)
            cv.circle(img, (x_yaotong2, y_yaotong2), 10, (255, 0, 255), cv.FILLED)
            cx16, cy16 = lmList[16][1], lmList[16][2]
            img = cv2ImgAddText(img, "十宣穴4", cx16, cy16, (0, 0, 0), textSize)
            cv.circle(img, (cx16, cy16), 10, (255, 0, 255), cv.FILLED)
            cx17, cy17 = lmList[17][1], lmList[17][2]
            img = cv2ImgAddText(img, "后溪穴", cx17, cy17, (0, 0, 0), textSize)
            cv.circle(img, (cx17, cy17), 10, (255, 0, 255), cv.FILLED)
            x_baxie4, y_baxie4 = (cx13 + cx17) // 2, (cy13 + cy17) // 2
            img = cv2ImgAddText(img, "八邪穴4", x_baxie4, y_baxie4, (0, 0, 0), textSize)
            cv.circle(img, (x_baxie4, y_baxie4), 10, (255, 0, 255), cv.FILLED)
            cx18, cy18 = lmList[18][1], lmList[18][2]
            img = cv2ImgAddText(img, "小骨空穴", cx18, cy18, (0, 0, 0), textSize)
            cv.circle(img, (cx18, cy18), 10, (255, 0, 255), cv.FILLED)
            cx20, cy20 = lmList[20][1], lmList[20][2]
            img = cv2ImgAddText(img, "十宣穴5", cx20, cy20, (0, 0, 0), textSize)
            cv.circle(img, (cx20, cy20), 10, (255, 0, 255), cv.FILLED)
            cv.imwrite(result_path, img)  # 标记后的图片存储位置

    print(lmList)
    return image_path + '_r.jpg'
