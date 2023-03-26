import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import duckdb
import csv

class weatherReport:
    def __init__(self, url):
        self.url=url
    def covertTodataFrame(self):
        raw_data=requests.get(self.url)
        open('data.txt', 'wb').write(raw_data.content)
        txt_data = open('data.txt', 'r')
        month=['January','February','March','April','May','June','July','Agust','September','October','November','December']
        header=['year','month','tmax','tmin', 'af', 'rain', 'sunlight']
        with open('csvData.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for i,data in enumerate(txt_data):
                if i >6:
                    new_row=[]
                    row=data.split()
                    for j,it in enumerate(row):
                        value=it.replace("---","")
                        value=value.replace("#","")
                        value=value.replace("*","")
                        new_row.append(value)
                        if(j==len(header)-1):
                            break
                    
                    new_row[1]=month[int(new_row[1])-1]
                    writer.writerow(new_row)

        weather_data=pd.read_csv("csvData.csv",header=[0])
        print("\nConverted file Data to Dataframe")
        print("*******************************\n")
        print(weather_data)
        return weather_data
    def last_20years_data(self,df):

        today = datetime.date.today()
        year = today.year
        print("\nGetting last 20 years data")
        print("*******************************\n")
        last_20years = df[df['year'].between(year-20, year)]
        print(last_20years)
        return last_20years
        
    def tmin_tmax_average(self,df):
        print("\nMonthly Averages for minimum and maximum temperature")
        print("******************************************************\n")


        query="select month, AVG((IFNULL(tmax,0)+IFNULL(tmin,0))/2) as tmin_tmax_average from df group by month"
        average=duckdb.query(query).df()
        print(average)


        sns.barplot( x='month',y='tmin_tmax_average', data = average).set_title('Monthly Averages for minimum and maximum temperature - Barplot')
        plt.show()


        sns.pointplot( x='month',y='tmin_tmax_average', data = average).set_title('Monthly Averages for minimum and maximum temperature - Pointplot')

        plt.show()

        sns.swarmplot(x='month',y='tmin_tmax_average', data = average).set_title('Monthly Averages for minimum and maximum temperature - Swarmplot')
        plt.show()
    def precipitation(self,df):
        print("\nMonthly Averages for precipitation")
        print("******************************************************\n")


        query="select month, AVG(IFNULL(rain,0)) as rain from df group by month"
        average=duckdb.query(query).df()
        
        print(average)
        sns.barplot( x='month',y='rain', data = average).set_title('Monthly Averages for precipitation - Barplot')
        plt.show()


        sns.pointplot( x='month',y='rain', data = average).set_title('Monthly Averages for precipitation - Pointplot')

        plt.show()

        sns.swarmplot(x='month',y='rain', data = average).set_title('Monthly Averages for precipitation - Swarmplot')
        plt.show()
        
    def hours_sunlight(self,df):
        print("\nMonthly Averages for Hours of Sunlight")
        print("******************************************************\n")


        query="select month, AVG(IFNULL(sunlight,0)) as sunlight from df group by month"
        average=duckdb.query(query).df()
        
        print(average)
        sns.barplot( x='month',y='sunlight', data = average).set_title('Monthly Averages for Hours of Sunlight - Barplot')
        plt.show()


        sns.pointplot( x='month',y='sunlight', data = average).set_title('Monthly Averages for Hours of Sunlight - Pointplot')

        plt.show()

        sns.swarmplot(x='month',y='sunlight', data = average).set_title('Monthly Averages for Hours of Sunlight - Swarmplot')
        plt.show()
    def overall(self,df):
        query ="select month, AVG(IFNULL(sunlight,0)) as sunlight, AVG(IFNULL(rain,0)) as rain, AVG((IFNULL(tmax,0)+IFNULL(tmin,0))/2) as temperature from df group by month"
        average =average=duckdb.query(query).df()
        print(average)
        
        average.plot( x='month',y=['sunlight','rain','temperature'], kind='bar')
        plt.show()
if __name__=="__main__":
    stations=['Aberporth','Armagh','Ballypatrick','Bradford','Camborne','Cambridge NIAB','Cardiff Bute Park','Chivenor','Dunstaffnage','Durham']
    for i,station in enumerate(stations):
        print(i,", ",station)
    selected_station =int(input("Enter your station number: "))
    while selected_station not in range(0,len(stations)):
        if selected_station > len(stations):
            for i,station in enumerate(stations):
                print(i,", ",station)
            selected_station =int(input("Enter valid number: "))
        else:
            break
    split_key= stations[selected_station].lower().split()       
    url ="https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/"+split_key[0]+"data.txt"
    weatherObj =weatherReport(url)
    df=weatherObj.covertTodataFrame()
    df=weatherObj.last_20years_data(df)
    
    weathers=['Monthly Averages for minimum and maximum temperature','Monthly Averages for precipitation','Monthly Averages for Hours of Sunlight','All Data','End']
    for j,weather in enumerate(weathers):
        print(j,", ",weather)
    selected_weather =int(input("Enter weather number: "))
    while selected_weather in range(0, len(weathers)):
        if selected_weather > len(weathers):
            print("\nSelect weather")
            print("****************\n")
            for j,weather in enumerate(weathers):
                print(j,", ",weather)
            selected_weather=int(input("Enter valid number: "))
        elif selected_weather ==0:
            weatherObj.tmin_tmax_average(df)
            print("\nSelect weather")
            print("****************\n")
            for j,weather in enumerate(weathers):
                print(j,", ",weather)
            selected_weather=int(input("Enter weather number: "))
        elif selected_weather ==1:
            weatherObj.precipitation(df)
            print("\nSelect weather")
            print("****************\n")
            for j,weather in enumerate(weathers):
                print(j,", ",weather)
            selected_weather=int(input("Enter weather number: "))
        elif selected_weather ==2:
            weatherObj.hours_sunlight(df)
            print("\nSelect weather")
            print("****************\n")
            for j,weather in enumerate(weathers):
                print(j,", ",weather)
            selected_weather=int(input("Enter weather number: "))
        elif selected_weather ==3:
            weatherObj.overall(df)
            print("\nSelect weather")
            print("****************\n")
            for j,weather in enumerate(weathers):
                print(j,", ",weather)
            selected_weather=int(input("Enter weather number: "))
        else:
            break
