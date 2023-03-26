<h1>weather_data_analysis</h1>
<h2>Climate data for historic stations</h2>
Monthly data are available for a selection of long-running historic stations. The series typically range from 50 to more than 100 years in length.

<h2>Our historic station data consists of:</h2>

Mean daily maximum temperature (tmax)
Mean daily minimum temperature (tmin)
Days of air frost (af)
Total rainfall (rain)
Total sunshine duration (sun)
Monthly mean temperature
The monthly mean temperature is calculated from the average of the mean daily maximum and mean daily minimum temperature i.e. (tmax+tmin)/2.

<h2>How do run the script?</h2>
<u><li>Download the code as zip file.</li>
<li>Extract the zip file and navigate to weatherReport.py file location</li>
<li>To open the command prompt in file location</li>
<li>Install required modules by entering below command</li>
&nbsp;&nbsp;&nbsp;&nbsp;pip install -r requirements.txt 
<li>Run the program by entering below command.</li>
&nbsp;&nbsp;&nbsp;&nbsp;python weatherReport.py
<li>Enter the number respective station</li>
<li>Select number for data analysis</li>
<li>You have to close the chart for next one</li>
<li>You have to end the program for next station by run again</li></ul>
<h2>Process</h2>
&nbsp;&nbsp;&nbsp;&nbsp;0 ,  Aberporth</br>
&nbsp;&nbsp;&nbsp;&nbsp;1 ,  Armagh</br>
&nbsp;&nbsp;&nbsp;&nbsp;2 ,  Ballypatrick</br>
&nbsp;&nbsp;&nbsp;&nbsp;3 ,  Bradford</br>
&nbsp;&nbsp;&nbsp;&nbsp;4 ,  Camborne</br>
&nbsp;&nbsp;&nbsp;&nbsp;5 ,  Cambridge NIAB</br>
&nbsp;&nbsp;&nbsp;&nbsp;6 ,  Cardiff Bute Park</br>
&nbsp;&nbsp;&nbsp;&nbsp;7 ,  Chivenor</br>
&nbsp;&nbsp;&nbsp;&nbsp;8 ,  Dunstaffnage</br>
&nbsp;&nbsp;&nbsp;&nbsp;9 ,  Durham</br>
<p>After enter the station number, it will download the data as txt file and that data file convert into valid csv file. Then, it will read the csv file to DataFrame and filter to get the last 20 years data.</p>
&nbsp;&nbsp;&nbsp;&nbsp;0 ,  Monthly Averages for minimum and maximum temperature</br>
&nbsp;&nbsp;&nbsp;&nbsp;1 ,  Monthly Averages for precipitation</br>
&nbsp;&nbsp;&nbsp;&nbsp;2 ,  Monthly Averages for Hours of Sunlight</br>
&nbsp;&nbsp;&nbsp;&nbsp;3 ,  All Data</br>
&nbsp;&nbsp;&nbsp;&nbsp;4 ,  End</br>
<p>Enter the number to call the particular data and data visualization. You can end the program by enter 4.</p>
