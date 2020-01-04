# IOT-Project______零食防偷車______

## 1. 關於專案
將零食放置在四驅車上，透過鏡頭拍攝回傳的照片，去偵測是否本人接近，若非本人接近，四驅車直接往其他方向逃離。

## 2. 專案緣由
身為研究生總是會有許多零食擺在實驗室，防止其他人來偷零食，順便嚇偷零食的人。

## 3. 專案構想
四駒車上的鏡頭會間隔幾秒照相，並且回傳照片給Rasberry Pi 3，透過影像辨識，查看相片是否為本人，若照片並非本人，四駒車會逃跑離開。

## 4. 專案所需實體材料
* 一個Rasberry Pi 3
* 一個Raspberry Pi 樹莓派UPS 鋰電池擴充板USB 電源供應模組行動電源
* 一個L298N馬達驅動模組
* 一個四顆並聯電池盒(包含正負極單芯線)
* 四顆1.5v電池
* 一顆鏡頭
* 8條單芯線 (目的:連接直流減速電機馬達與L298N)
* 四條母對母杜邦線 (目的:連接Rasberry Pi與L298N,傳達指令)
* 一條公對母杜邦線 (目的:連接Rasberry Pi與L298N,輸入5V電壓)
* Micro USB傳輸線
* 四個直流減速電機
* 一套雙層四驅自走車底盤(包含四顆輪胎)
* 捆線帶 (目的:捆住單芯線與杜邦線)
* 魔鬼氈 (目的:固定住車上裝載的裝置)
* 筆電

## 5. 材料細節
* **L298N馬達驅動模組**
<img src="https://github.com/ponponmusic/IOT-Project-_-FourWheelCar-ImageRecognize/blob/master/Markdown%20Pictures_Videos/L298N.png" width = "45%" height = "45%"/>

* **直流減速電機**
<img src="https://github.com/ponponmusic/IOT-Project-_-FourWheelCar-ImageRecognize/blob/master/Markdown%20Pictures_Videos/DC%20geared%20motor.png" width = "45%" height = "45%"/>

## 6. 線路設計,指令表與實體照片
<img src="https://github.com/ponponmusic/IOT-Project-_-FourWheelCar-ImageRecognize/blob/master/Markdown%20Pictures_Videos/FourWheelCar.png" width = "75%" height = "75%"/>
<img src="https://github.com/ponponmusic/IOT-Project-_-FourWheelCar-ImageRecognize/blob/master/Markdown%20Pictures_Videos/Command%20Table.jpg" width = "75%" height = "75%"/>
<img src="https://github.com/ponponmusic/IOT-Project-_-FourWheelCar-ImageRecognize/blob/master/Markdown%20Pictures_Videos/FourWheelCar01.jpg" width = "75%" height = "75%"/>
<img src="https://github.com/ponponmusic/IOT-Project-_-FourWheelCar-ImageRecognize/blob/master/Markdown%20Pictures_Videos/FourWheelCar02.jpg" width = "75%" height = "75%"/>

## 7. 程式設計
`00.PerOperation`
* data___________________# DataGenerator檔生出來的照片
   * class0 (一堆皮丘照片,但只有正面照)
   * class1 (一堆小熊跟維尼照片,但只有正面照)
* 00.DataGenerator.py_____# ImageDataGenerator生成照片
* 01.GetData.py___________# cv2將照片轉numpy array,以及resize ,再吐出data與label的pickle檔(X.pickle/y.pickle)
* 02.CNN_model.py___________# 用X.pickle/y.pickle train CNN model ,再吐出json以及h5檔
* 03.ReadModel_predict.py_____# load model以及test predict

`01.FourWheelCar_ImageRecognize`
* CarClass.py_______# 執行車子指令(B,BR,R,F,BL,L,F,S)
* ImagePredict.py_____# load model&predict the image
* main.py_____# import CarClass和ImagePredict ,如果ImagePredict回傳class1, CarClass對車子進行指令
* model.h5
* model.json

## 8. 影片呈現連結
* https://youtu.be/jYPKu4qlEhM
* https://youtu.be/rr9BEdd6IZE

## 9. 可以改進或其他發想
* dataset可以使用各種不同角度的物體照片,這樣predict才能更精確
* 車子位於地板上導致鏡頭過低,可以用支架提高它的拍攝角度
* 可以加上避障模組,使之快碰壁時可以轉向之類
* 可以從拍照偵測目標物轉變為錄影方式直接偵測
