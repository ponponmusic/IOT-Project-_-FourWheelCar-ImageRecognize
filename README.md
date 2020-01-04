# IOT-Project-_-零食防偷車

## 1. 關於專案
將零食放置在四驅車上，透過鏡頭拍攝回傳的照片，去偵測是否本人接近，若是非本人接近，四驅車直接往其他方向逃離。

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
* 四個直流減速電機
* 一套雙層四驅自走車底盤(包含四顆輪胎)
* 捆線帶 (目的:捆住單芯線與杜邦線)
* 魔鬼氈 (目的:固定住車上裝載的裝置)
* 筆電

## 5. 材料細節
* L298N馬達驅動模組
<img src="https://github.com/ponponmusic/IOT-Project-_-FourWheelCar-ImageRecognize/blob/master/L298N.png" width = "50%" height = "50%"/>
![image](https://github.com/ponponmusic/IOT-Project-_-FourWheelCar-ImageRecognize/blob/master/L298N.png 80%)


