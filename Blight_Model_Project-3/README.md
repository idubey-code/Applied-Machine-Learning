<h1>Understanding and Predicting Property Maintenance Fines</h1>

This assignment is based on a data challenge from the Michigan Data Science Team (MDST).

The Michigan Data Science Team (MDST) and the Michigan Student Symposium for Interdisciplinary Statistical Sciences (MSSISS) have partnered with the City of Detroit 
to help solve one of the most pressing problems facing Detroit - blight. 
Blight violations are issued by the city to individuals who allow their properties to remain in a deteriorated condition. 
Every year, the city of Detroit issues millions of dollars in fines to residents and every year, many of these fines remain unpaid. 
Enforcing unpaid blight fines is a costly and tedious process, so the city wants to know: how can we increase blight ticket compliance?

The first step in answering this question is understanding when and why a resident might fail to comply with a blight ticket. 
This is where predictive modeling comes in. For this assignment, your task is to predict whether a given blight ticket will be paid on time.

All data for this assignment has been provided to us through the Detroit Open Data Portal.

We provide you with two data files for use in training and validating your models: train.csv and test.csv. 
Each row in these two files corresponds to a single blight ticket, and includes information about when, why, and to whom each ticket was issued. 
The target variable is compliance, which is True if the ticket was paid early, on time, or within one month of the hearing data, 
False if the ticket was paid after the hearing date or not at all, and Null if the violator was found not responsible. 
Compliance, as well as a handful of other variables that will not be available at test-time, are only included in train.csv.

<strong>Note</strong>: All tickets where the violators were found not responsible are not considered during evaluation. 
They are included in the training set as an additional source of data for visualization, and to enable unsupervised and semi-supervised approaches. 
However, they are not included in the test set.

<h2>Data fields</h2>

<h3>train.csv & test.csv</h3>

<ul>
<li>ticket_id - unique identifier for tickets</li>
<li>agency_name - Agency that issued the ticket</li>
<li>inspector_name - Name of inspector that issued the ticket</li>
<li>violator_name - Name of the person/organization that the ticket was issued to</li>
<li>violation_street_number, violation_street_name, violation_zip_code - Address where the violation occurred</li>
<li>mailing_address_str_number, mailing_address_str_name, city, state, zip_code, non_us_str_code, country - Mailing address of the violator</li>
<li>ticket_issued_date - Date and time the ticket was issued</li>
<li>hearing_date - Date and time the violator's hearing was scheduled</li>
<li>violation_code, violation_description - Type of violation</li>
<li>disposition - Judgment and judgement type</li>
<li>fine_amount - Violation fine amount, excluding fees</li>
<li>admin_fee - $20 fee assigned to responsible judgments</li>
<li>state_fee - $10 fee assigned to responsible judgments</li>
<li>late_fee - 10% fee assigned to responsible judgments</li>
<li>discount_amount - discount applied, if any</li>
<li>clean_up_cost - DPW clean-up or graffiti removal cost</li>
<li>judgment_amount - Sum of all fines and fees</li>
<li>grafitti_status - Flag for graffiti violations</li>
</ul>

<h3>train.csv only</h3>

<ul>
<li>payment_amount - Amount paid, if any</li>
<li>payment_date - Date payment was made, if it was received</li>
<li>payment_status - Current payment status as of Feb 1 2017</li>
<li>balance_due - Fines and fees still owed</li>
<li>collection_status - Flag for payments in collections</li>
<li>compliance [target variable for prediction]
<ul>
 <li>Null = Not responsible
 <li>0 = Responsible, non-compliant
 <li>1 = Responsible, compliant
</ul>
</li>
<li>compliance_detail - More information on why each ticket was marked compliant or non-compliant</li>
</ul>

<h2>Evaluation</h2>

<ul>
<li>Your predictions will be given as the probability that the corresponding blight ticket will be paid on time.</li>

<li>The evaluation metric for this assignment is the Area Under the ROC Curve (AUC).</li>

<li>Your grade will be based on the AUC score computed for your classifier. A model which with an AUROC of 0.7 passes this assignment, over 0.75 will recieve full points.</li>

<li>For this assignment, create a function that trains a model to predict blight ticket compliance in Detroit using train.csv. 
Using this model, return a series of length 61001 with the data being the probability that each corresponding ticket from test.csv will be paid, 
and the index being the ticket_id.</li>
</ul>

<h3>Example:</h3>

ticket_id

   <p>284932  &nbsp&nbsp  0.531842</p>
   
   <p>285362  &nbsp&nbsp  0.401958</p>
   
   <p>285361  &nbsp&nbsp  0.105928</p>
   
   <p>285338  &nbsp&nbsp  0.018572</p>
   
   <p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  ...   &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</p>
             
   <p>376499  &nbsp&nbsp  0.208567</p>
   
   <p>376500  &nbsp&nbsp  0.818759</p>
   
   <p>369851  &nbsp&nbsp  0.018528</p>
   
   Name: compliance, dtype: float32
   
<h2>Hints</h2>

<li>Make sure your code is working before submitting it to the autograder.</li>

<li>Print out your result to see whether there is anything weird (e.g., all probabilities are the same).</li>

<li>Generally the total runtime should be less than 10 mins. You should NOT use Neural Network related classifiers (e.g., MLPClassifier) in this question.</li>

<li>Try to avoid global variables. If you have other functions besides blight_model, you should move those functions inside the scope of blight_model.</li>
