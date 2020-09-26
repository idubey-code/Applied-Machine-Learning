<h2>Hypothesis Testing</h2>

<strong>Hypothesis</strong>: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (price_ratio=quarter_before_recession/recession_bottom)

<h4>The following data files are available for this project:</h4>
<ul>
<li>From the Zillow research data site there is housing data for the United States. In particular the datafile for all homes at a city level,
City_Zhvi_AllHomes.csv, has median home sale prices at a fine grained level.</li>

<li>From the Wikipedia page on college towns is a list of university towns in the United States which has been copy and pasted into the file university_towns.txt.</li>

<li>From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars (use the chained value in 2009 dollars), 
in quarterly intervals, in the file gdplev.xls. For this project, only look at GDP data from the first quarter of 2000 onward.</li>
</ul>

<h4>Definitions:</h4>
<ul>
<li>A <strong>quarter</strong> is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.</li>
<li>A <strong>recession</strong> is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.</li>
<li>A <strong>recession bottom</strong> is the quarter within a recession which had the lowest GDP.</li>
<li>A <strong>university town</strong> is a city which has a high percentage of university students compared to the total population of the city.</li>
</ul>
