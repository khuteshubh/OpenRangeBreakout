import pandas as pd
df = pd.read_csv("C:\\Users\\shubh\\Downloads\\BANKNIFTY.csv",header=None,names=["Nanes","Date","Time","Open","High","Low","Close","EMAQ","SMA26"])
List_Of_Date = df["Date"];
List_Of_Time = df["Time"];
BUY = False
SELL = False
buyorder = 0
exit_time = "15:15"
no_trade_time = "15:16"
stoplossbuy = 0
stoplosssell = 0
entry_time = "09:16"
entry_time1 = "09:17"
entry_time2 = "09:18"
entry_time3 = "09:19"
entry_time4 = "09:20"
entry_time5 = "09:21"
entry_time6 = "09:22"
entry_time7 = "09:23"
entry_time8 = "09:24"
entry_time9 = "09:25"
entry_time10 = "09:26"
entry_time11 = "09:27"
entry_time12 = "09:28"
entry_time13 = "09:29"
entry_time14 = "09:30"
stoplosshit = 0
cumprofit = 0
cumloss = 0
count = 0
for i in range(len(df["Time"])):
    if (entry_time in df["Time"][i]):
        print("Date {} {}".format(df["Date"][i],df["Time"][i]));
        lowtemp = []
        lowtemp.append(df["Low"][i]);
        lowtemp.append(df["Low"][i + 1]);
        lowtemp.append(df["Low"][i + 2]);
        lowtemp.append(df["Low"][i + 3]);
        lowtemp.append(df["Low"][i + 4]);
        lowtemp.append(df["Low"][i + 5]);
        lowtemp.append(df["Low"][i + 6]);
        lowtemp.append(df["Low"][i + 7]);
        lowtemp.append(df["Low"][i + 8]);
        lowtemp.append(df["Low"][i + 9]);
        lowtemp.append(df["Low"][i + 10]);
        lowtemp.append(df["Low"][i + 11]);
        lowtemp.append(df["Low"][i + 12]);
        lowtemp.append(df["Low"][i + 13]);
        lowtemp.append(df["Low"][i + 14]);
        stoplossbuy = min(lowtemp);
        hightemp = []
        hightemp.append(df["High"][i]);
        hightemp.append(df["High"][i + 1]);
        hightemp.append(df["High"][i + 2]);
        hightemp.append(df["High"][i + 3]);
        hightemp.append(df["High"][i + 4]);
        hightemp.append(df["High"][i + 5]);
        hightemp.append(df["High"][i + 6]);
        hightemp.append(df["High"][i + 7]);
        hightemp.append(df["High"][i + 8]);
        hightemp.append(df["High"][i + 9]);
        hightemp.append(df["High"][i + 10]);
        hightemp.append(df["High"][i + 11]);
        hightemp.append(df["High"][i + 12]);
        hightemp.append(df["High"][i + 13]);
        hightemp.append(df["High"][i + 14]);
        stoplosssell = max(hightemp);
        print("{}.........{}".format(stoplossbuy,stoplosssell));

    if(df["High"].values [i] > stoplosssell and BUY == False and buyorder == 0 and  entry_time1 not in df["Time"][i] and entry_time2 not in df["Time"][i]  and entry_time3 not in df["Time"][i]  and entry_time4 not in df["Time"][i]  and entry_time5 not in df["Time"][i]  and entry_time6 not in df["Time"][i]  and entry_time7 not in df["Time"][i]  and entry_time8 not in df["Time"][i]  and entry_time9 not in df["Time"][i]  and entry_time10 not in df["Time"][i]  and entry_time11 not in df["Time"][i]  and entry_time12 not in df["Time"][i]  and entry_time13 not in df["Time"][i]  and entry_time14 not in df["Time"][i]   and df["Time"] [i] < no_trade_time ):
        print("order for buy is placed  at = {} {}".format(df["Date"][i],df["Time"][i]));
        BUY = True
        buyorder = 1;
        count += 1;
    if(df["Low"].values[i] < stoplossbuy and SELL == False and buyorder == 0 and  entry_time1 not in df["Time"][i] and entry_time2 not in df["Time"][i] and entry_time3 not in df["Time"][i] and entry_time4 not in df["Time"][i] and entry_time5 not in df["Time"][i] and entry_time6 not in df["Time"][i] and entry_time7 not in df["Time"][i] and entry_time8 not in df["Time"][i] and entry_time9 not in df["Time"][i] and entry_time10 not in df["Time"][i] and entry_time11 not in df["Time"][i] and entry_time12 not in df["Time"][i] and entry_time13 not in df["Time"][i] and entry_time14 not in df["Time"][i]  and df["Time"] [i] < no_trade_time):
        print("order for sell is placed  at = {} {}".format(df["Date"][i], df["Time"][i]));
        SELL = True
        buyorder = 1;
        count += 1;
    if (exit_time in df["Time"][i]):
        if (BUY == True and stoplosshit == 0):
            print("sell of exit time = {} {} ".format(df["Date"][i],df["Time"][i]));
            BUY = False
            buyorder = 0
            cumprofit = cumprofit + df["Close"][i] - stoplosssell
            cumloss = cumprofit - (stoplosssell - stoplossbuy)
            print("cumprofit is {} ".format(cumprofit));
            print("cumloss is {} ".format(cumloss));
            stoplosshit = 0
        if (SELL == True and stoplosshit == 0):
            print("sell of exit time = {} {} ".format(df["Date"][i], df["Time"][i]));
            SELL = False
            buyorder = 0
            cumprofit = cumprofit + stoplossbuy - df["Close"][i]
            cumloss = cumprofit - (stoplosssell - stoplossbuy)
            print("cumprofit is {} ".format(cumprofit));
            print("cumloss is {} ".format(cumloss));
            stoplosshit = 0
    if (SELL ==True and df["High"][i] > stoplosssell and stoplosshit == 0):
        print("stoploss hit at = {} {}".format(df["Date"][i],df["Time"][i]));
        stoplosshit = 1;
    if (BUY ==True and df["Low"][i] < stoplossbuy and stoplosshit == 0):
        print("stoploss hit at = {} {}".format(df["Date"][i],df["Time"][i]));
        stoplosshit = 1;
    if (stoplosshit == 1 and BUY == True):
        BUY = False
        buyorder = 0
        stoplosshit = 0
        cumprofit = cumprofit - (stoplosssell - stoplossbuy)
        cumloss = cumprofit - (stoplosssell - stoplossbuy)
        print("cumprofit is {} {} {}".format(cumprofit,df["Date"][i],df["Time"][i]));
        print("cumloss is {} {} {} ".format(cumloss, df["Date"][i], df["Time"][i]));
    if (stoplosshit == 1 and SELL == True):
        SELL = False
        buyorder = 0
        stoplosshit = 0
        cumprofit = cumprofit - (stoplosssell - stoplossbuy)
        cumloss = cumprofit - (stoplosssell - stoplossbuy)
        print("cumprofit is {} {} {}".format(cumprofit, df["Date"][i], df["Time"][i]));
        print("cumloss is {} {} {} ".format(cumloss,df["Date"][i],df["Time"][i]));
print("cum profit in the end "+ str(round(cumprofit,2)));
print("cum loss in the end = {} ".format(round(cumloss,2)));
print("Number of trade taken in the period {}".format(count));










