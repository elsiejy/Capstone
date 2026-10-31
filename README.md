# Hotel Booking Cancellation Analysis
The following uses historical reservation data to find which bookings are most likely to cancel and builds a model that predicts cancellation risk at the time of booking

👉 Interact with the model via Streamlit:[Click here](https://capstone-bq9blrvs95rrzfvxetb2jk.streamlit.app)

#### Table of content <a name="tc"></a>
- [Problem statement](#problem)
- [Research objective](#research)
- [Dataset](#dataset)
- [Repository structure](#repo)
- [Data cleansing](#clean)
- [Exploratory Data Analysis](#eda)
- [Dashboard](#dashboard)
- [Predictive analysis](#ml)
- [Insights & recommendation](#insights)

---
## Hotel Booking Dataset 📊 ####

The dataset comprises 119,390 hotel reservations across two hotel types: City Hotel (79,330 bookings) and Resort Hotel (40,060 bookings). The check-in dates span from July 2015 to August 2017. Of the total reservations, 44,224 were not fulfilled including 43,017 cancellations and 1,207 no-shows resulting in an overall cancellation rate of 37.04%. This provides a baseline for further analysis to determine whether cancellation rates vary by hotel type, market segment, distribution channel and booking characteristics.

<sub>[back to top](#tc)</sub>
## 🤔 Problem statement <a name="problem"></a>

Nearly 37% of hotel bookings are cancelled or result in no-shows** putting approximately $16.7 million in potential room revenue at risk. How can hotels use historical booking data to identify the customer segments, booking channels, travel periods and booking characteristics associated with higher cancellation rates and develop a predictive model to identify bookings likely to be cancelled before guests arrive?

The findings will help hotels make better decisions on booking management, deposit policies, and room availability to reduce potential revenue losses.

<sub>[back to top](#tc)</sub>
## 🎯 Research objective - Description analysis <a name="research"></a>

1.  Analyse reservation volumes and cancellation rates by hotel type, arrival period, market segment and distribution channel.
2.  Identify booking characteristics associated with cancellation such as lead time, deposit type, customer type, length of stay, party composition, booking changes and special requests - and rank their strength of association.
3.  Examine the association between waiting-list days and cancellation, before and after adjusting for other booking characteristics.
4.  Compare repeat-guest share and previous booking history across market segments, and test whether repeat guests cancel less within each segment.
5.  Identify booking profiles with a high cancellation rate (≥ 50%) and substantial volume (≥ 1,000 bookings), and recommend targeted cancellation-risk strategies.


> [!NOTE]
> Target definition: is_canceled = True covers both Canceled (43,017) and No-Show (1,207) reservations which account for 44,224 bookings or 37.04% (36.03% is the rate for the Canceled status alone)

<sub>[back to top](#tc)</sub>
## 📔 Dataset <a name="dataset"></a>

- File name: bookings_final.csv
- Time Horizon: July 2015 - August 2017
- Target Category: Bookings
- Key Entities: Customer, Booking, Market Segment, Booking Channel

Link to Jupyter Notebook in Google Colab:
https://colab.research.google.com/drive/1VG-cGkziLcWcOZKMRUB-KtkdLOVLJ2tT?usp=sharing

### Data dictionary

1. **Bookings.csv** (119,390 rows, one per reservation)  
   The main fact table and the source of the target variable `is_canceled` (1 = cancelled or no-show). It holds the booking characteristics such as lead time, arrival date, length of stay, party composition, repeat-guest history, booking changes, special requests, waiting-list days and average daily rate. It links to the four reference tables through `Hotel_ID`, `Market_Segment_ID`, `Customer_Type_ID` and `Reservation_ID`.

3. **Hotels.csv** (2 rows)  
   Identifies each booking's hotel type (City Hotel or Resort Hotel) so cancellation rates and risk profiles can be compared between the two properties.

5. **Market_Segments.csv** (26 rows)  
   Records how each booking was acquired: the market segment e.g. Online TA, Groups, Direct, Corporate and the distribution channel it came through e.g. TA/TO, Direct, GDS. This is used to identify which acquisition sources carry the highest cancellation risk.

7. **Customer_Types.csv** (36 rows)  
   Combines the customer type (Transient, Transient-Party, Group, Contract), the deposit policy (No Deposit, Non Refund, Refundable) and the meal plan.

9. **Reservation_Status.csv** (3 rows)  
    The final outcome of each booking: Check-Out, Canceled or No-Show.

   

#### Definitions
##### Market segment (`market_segment`): who the booking came from

| Term              | Meaning                                                                                                                                                               |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Online TA**     | Online travel agent, a booking website such as Booking.com, Expedia or Agoda.                                                                                         |
| **Offline TA/TO** | Traditional travel agents (TA) and tour operators (TO) working by phone, email or in a shop. A tour operator packages hotel, transport and activities into a holiday. |
| **Groups**        | A block of rooms booked together for one event or party e.g., a tour group, wedding or conference.                                                                    |
| **Direct**        | The guest booked with the hotel itself (hotel website, phone, email, walk-in) with no middleman.                                                                      |
| **Corporate**     | Bookings made by or for companies - often at negotiated business rates.                                                                                               |
| **Complementary** | Free stays given by the hotel (e.g. to VIPs or partners, or as compensation). Often spelled “complimentary” outside this dataset.                                     |
| **Aviation**      | Bookings linked to airlines, e.g. crew layovers or stranded passengers.                                                                                               |
##### Distribution channel (`distribution_channel`): the route the booking came through

| Term          | Meaning                                                                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **TA/TO**     | Through travel agents or tour operators, online or offline.                                                                   |
| **Direct**    | Straight to the hotel.                                                                                                        |
| **Corporate** | Through a company’s own travel booking arrangement.                                                                           |
| **GDS**       | Large booking networks e.g., Amadeus, Sabre, Travelport that travel agents and airlines use to book hotels, flights and cars. |
##### Customer type (`customer_type`)

| Term                | Meaning                                                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Transient**       | An individual booking that isn’t part of a group or contract. Typically a short-stay leisure or business traveller.            |
| **Transient-Party** | A transient booking linked to at least one other transient booking, e.g. two couples travelling together on separate bookings. |
| **Group**           | Part of a group booking.                                                                                                       |
| **Contract**        | Covered by an allotment or other contract between the hotel and a company or agent                                             |
#### Meal plan (`meal`)

| Term   | Meaning                                                    |
| ------ | ---------------------------------------------------------- |
| **BB** | Bed & Breakfast: room plus breakfast.                      |
| **HB** | Half Board: breakfast plus one other meal, usually dinner. |
| **FB** | Full Board: breakfast, lunch and dinner.                   |
| **SC** | Self Catering: room only, no meals.                        |

<sub>[back to top](#tc)</sub>

## 🗃️ Repository structure <a name="repo"></a>

├── README.md
├── Bookings.csv, Hotels.csv, Market_Segments.csv,
│   Customer_Types.csv, Reservation_Status.csv   # source data
├── bookings_final.csv             # Cleanse data for dashboard
├── Capstone.ipynb                 # Part 1: descriptive analysis (RO1–RO5)
│                                  # Part 2: predictive analysis
├── Capstone Hotel Booking.pbix    # Power BI dashboard
├── cancellation_model.pkl         # Trained model (Random Forest)
├── app.py                         # For Streamlit
└── requirements.txt               # For Streamlit

<sub>[back to top](#tc)</sub>

## 🧼 Data cleansing <a name="clean"></a>
1. Observation from bookings dataset
     - There are a total of 119,390 booking records
     - Hotel_ID, Market_Segment_ID, Customer_Type_ID, Reservation_ID are foreign keys
     - NULL values exist in children, country, agent, company
     - reservation_status_date data type should be date time
     - children, agent, and company should be int
     - is_repeated_guest and is_canceled should be boolean
2. Observation from other dataset: No empty values as they are mainly reference tables
3. Data cleansing performed on bookings dataset to:
     - Derive check-in date (arrival_date_year + arrival_date_month + arrival_date_day_of_month)
     - Update data type for reservation_status_date to date time
     - Update data type for is_repeated_guest and is_canceled to boolean
     - Update data type for children, agent and company to int
     - Handle NULL values for children, country, agent, company


<sub>[back to top](#tc)</sub>
## Exploratory Data Analysis (EDA) <a name="eda"></a>
## 📈 Power BI Dashboard <a name="dashboard"></a>

<img width="1156" height="651" alt="image" src="https://github.com/user-attachments/assets/c8b79046-00fd-4d3c-be4a-fff56635a3d8" />


<sub>[back to top](#tc)</sub>
## 🔮 Predictive analysis <a name="ml"></a>

**Objective:** To develop a model that can predict whether a hotel booking is likely to be cancelled before the guest arrives.

The model uses historical booking data to predict two possible outcomes:
- **1 = Cancelled:** The guest cancels the booking
- **0 = Not Cancelled:** The booking is not cancelled
##### Factors Used for Prediction

Based on the earlier descriptive analysis, five factors were selected because they may help predict whether a booking will be cancelled and this information is available when the booking is made.

| Factor                | Why it was selected                                                                          |
| --------------------- | -------------------------------------------------------------------------------------------- |
| **Deposit Type**      | Group with Non-Refunded deposit type is more likely to cancel                                |
| **Booking Lead Time** | Customers who book further in advance are more likely to cancel                              |
| **Market Segment**    | Group bookings and bookings made through online travel agents have higher cancellation rates |
| **Special Requests**  | Customers who make special requests are less likely to cancel their bookings                 |
| **Hotel Type**        | City Hotels have higher cancellation rates than Resort Hotels                                |
### Information Excluded from the Model

Certain booking characteristic such as the final booking status, the date the status was recorded and the number of booking changes are excluded.

This information may only become available after the booking is made or its outcome is known. Including it could give the model information that would not be available when making an actual prediction resulting in misleadingly high accuracy.

### Steps Taken

1. **Define target:** Used the five booking factors as inputs and the cancellation status (`is_canceled`) as the prediction target.
2. **Split the data:** Divided the data into 70% for training and 30% for testing.
3. **Train and evaluate the 3 models:** Tested Logistic Regression, Decision Tree and Random Forest to determine which could better predict cancellations.
4. **Compare model performance:** Measured how accurately each model predicted cancellations including how many cancellations it correctly identified and how many predictions were incorrect.
5. **Compared different feature:** Tested four combinations of booking factors using the same model and data split to see which combination produced the best results.
6. **Deployed the final model:** Saved the Random Forest model and made it available through a Streamlit web application, allowing users to enter booking details and obtain a cancellation-risk prediction.
    

### Expected Outcome

The predictive model can help hotels identify bookings with a higher risk of cancellation before guests arrive. This allows hotels to make more informed decisions about room availability, booking management and deposit policies to potentially reducing revenue losses from cancellations.


<sub>[back to top](#tc)</sub>

## 📈 Findings, insights & recommendation <a name="insights"></a>

Findings from RO
R01:City Hotel received about two-thirds of all bookings and has a higher cancellation rate than Resort Hotel throughout the year. Bookings made via Travel agents and tour operators (TA/TO) handle close to 82% of bookings and have a cancellation rate of 41.0%. While online TA accounts for the largest market segment, group bookings have the highest cancellation rate  
R02: Deposit type is the strongest single signal (Non Refund 99%) followed by lead time (City: 12% at 0–7 days → 71% at 366+ days), 
previous cancellations, market segment and special requests (no requests 48% vs ≤22% with one or more)  
R03: Waiting-list days are not an independent risk driver  
R04: Corporate, Complementary and Aviation have 27–31% repeat guests while Online TA only account for 1.1%. Repeat guests cancel less in every segment except Groups.
R05: 	After profiling all the bookings, 2 profiles have the highest risk of cancellation
- City Hotel + Non-refundable + Group booking
- City Hotel + Online TA + booked 31–365 days ahead.

<sub>[back to top](#tc)</sub>
