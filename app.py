from flask import Flask, jsonify, render_template, request
from datetime import datetime, timedelta
import torchvision.transforms as transforms
import torch.utils.data.dataloader as Data
from PIL import Image
import io
import random
import json
from uils import hand_predict

app = Flask(__name__)

# 自动重载模板文件
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
# 设置静态文件缓存过期时间
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


@app.route("/", methods=["GET", "POST"])
def root():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    info = {}
    try:
        image = request.files["file"]
        img_bytes = image.read()
        image = Image.open(io.BytesIO(img_bytes))
        nowTime = datetime.now().strftime("%Y%m%d%H%M%S")
        randomNum = random.randint(0, 99)
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        image_path = 'data/' + uniqueNum
        image.save('./static/' + image_path + '.jpg')
        result_path = hand_predict(image_path)
        info['result'] = result_path
        print(result_path)
    except Exception as e:
        info['err'] = str(e)
    return info  # json格式传至前端


@app.route("/fore1", methods=["GET", "POST"])
def fore1():
    return render_template("fore1.html")


@app.route("/fore2", methods=["GET", "POST"])
def fore2():
    return render_template("fore2.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2222)
