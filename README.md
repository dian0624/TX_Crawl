# TX_Crawl
## 功能說明:
爬取台灣期貨交易所-台股期貨TX(2019/12/30)往前30天的資料，並且製作圖表且觀察圖表達中隱藏的訊息。

  ![image](https://github.com/dian0624/TX_Crawl/blob/master/TX_image/1585124181267.jpg)
---------------------------------------------------------------------------------------------

## 爬蟲

1. 利用**Selenium模塊**爬取臺股期貨(TX)，使用**chromedriver設置無頭模式**作為瀏覽器模擬器，**模擬輸入、點擊、選擇表單內容**。
2. 使用**time.sleep等待網頁完整輸出**，以整張表為基準xpath匹配個別元素，利用**split拆分和join連接切片**擷取所需元素。
3. 取得當日日期並使用**re正則表達式**取得所需格式內容，並使用**Mongodb數據庫儲存**。 

---------------------------------------------------------------------------------------------
## 資料處理與製圖

利用Jupyter Notebook使用Numpy、Pandas、Matplotlib、Seaborn等模塊，進行基礎資料處理與資料型態轉換。
1. 使用**re正則表達式**處理["漲跌%"]、["漲跌%"]的特殊符號，檢查遺漏值並填充。
2. 將交易日期轉為日datetime格式，到期月份(週別)、交易日期、契約格式不動，漲跌% 轉為float，其餘轉為int。
3. 製圖

---------------------------------------------------------------------------------------------
## 觀察:
1. 根據交易日期2019/12月 - TX-到期月份(202001) 最後成交價與成交量圖，發現成交量、交易量高低隨著價格波動。
   12/10到12/18趨勢是上升，交易量隨著價格持續上漲，直到12/19開始下降，12/20星期五交易量來到最高點，猜測周
   末不開市，預期下禮拜也會有降低的趨勢導致此狀況產生。
   
   ![image](https://github.com/dian0624/TX_Crawl/blob/master/TX_image/1585124735676.jpg)
   ![image](https://github.com/dian0624/TX_Crawl/blob/master/TX_image/1585124774402.jpg)
   
2. 根據2019/12月份 - TX-到期月份(201912 ~ 202012) 成交量，快到期的201912和日期較近的202001，在成交量上
    與其他月份有明顯差別，推估投資客心理因素，認為日期較近市場的變化幅度較可預測，日期較遠變數較大則會處於觀望狀態。
    
    ![image](https://github.com/dian0624/TX_Crawl/blob/master/TX_image/1585124766466.jpg)
    ![image](https://github.com/dian0624/TX_Crawl/blob/master/TX_image/1585205020225.jpg)







