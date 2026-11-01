# Hotel Booking Cancellation Analysis
The following uses historical reservation data to find which bookings are most likely to cancel and builds a model that predicts cancellation risk at the time of booking

👉 Interact with the model via Streamlit: [Click here](https://capstone-tqruvmtq4hdj2dyydrqggv.streamlit.app)

#### Table of content <a name="tc"></a>
- [Problem statement](#problem)
- [Research objective](#research)
- [Dataset](#dataset)
- [Exploratory Data Analysis](#eda)
- [Dashboard](#dashboard)
- [Predictive analysis](#ml)
- [Insights & recommendation](#insights)

---
## Hotel Booking Dataset 📊 ####

The dataset comprises 119,390 hotel reservations across two hotel types: City Hotel (79,330 bookings) and Resort Hotel (40,060 bookings). The check-in dates span from July 2015 to August 2017. Of the total reservations, 44,224 were not fulfilled including 43,017 cancellations and 1,207 no-shows resulting in an overall cancellation rate of 37.04%. This provides a baseline for further analysis to determine whether cancellation rates vary by hotel type, market segment, distribution channel and booking characteristics.

<sub>[back to top](#tc)</sub>
## 🤔 Problem statement <a name="problem"></a>

Nearly 37% of bookings at a city hotel and a resort hotel were cancelled or ended in no-shows between July 2015 and August 2017, putting approximately $16.7 million of booked room revenue at risk, a third of it cancelled within 30 days of arrival. How can hotels use historical booking data to identify the customer segments, booking channels, travel periods and booking characteristics associated with higher cancellation risk and lost revenue and develop a predictive model to identify bookings likely to be cancelled before guests arrive?

The findings will help hotels make better decisions on booking management, deposit and cancellation policies, channel strategy and room availability (including overbooking) to reduce revenue losses.

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

### Repository structure

- README.md
- Source dataset: Bookings.csv, Hotels.csv, Market_Segments.csv, Customer_Types.csv, Reservation_Status.csv
- Python notebook (Google Colab): Capstone_final.ipynb
- Cleaned dataset for Power BI dashboard: Capstone Hotel Booking.pbix
- Interactive Power BI dashboard: Capstone Hotel Booking.pbix
- Trained model: cancellation_model.pkl
- Files for streamlit: cancellation_model.pkl, app.py, requirements.txt

### Data dictionary

The dataset consists of one booking-level fact table and four reference tables. Together, they describe hotel reservations, how they were made, the type of customer, and their final outcome.

| File | Rows | Grain / purpose |
| --- | ---: | --- |
| **Bookings.csv** | 119,390 | One row per reservation. This is the main fact table and contains the target variable, `is_canceled` (`1` = cancelled or no-show). It includes booking characteristics such as lead time, arrival date, length of stay, party composition, repeat-guest history, booking changes, special requests, waiting-list days, and average daily rate. It links to the reference tables through `Hotel_ID`, `Market_Segment_ID`, `Customer_Type_ID`, and `Reservation_ID`. |
| **Hotels.csv** | 2 | Identifies the hotel for each booking: **City Hotel** or **Resort Hotel**. This enables comparisons of cancellation rates and risk profiles between the two properties. |
| **Market_Segments.csv** | 26 | Describes how a booking was acquired, including its market segment (for example, Online TA, Groups, Direct, or Corporate) and distribution channel (for example, TA/TO, Direct, or GDS). Use it to assess cancellation risk by acquisition source. |
| **Customer_Types.csv** | 36 | Combines the customer type (Transient, Transient-Party, Group, or Contract), deposit policy (No Deposit, Non Refund, or Refundable), and meal plan. |
| **Reservation_Status.csv** | 3 | Records the final booking outcome: Check-Out, Canceled, or No-Show. |

#### Definitions

##### Market segment (`market_segment`): who the booking came from

| Term | Meaning |
| --- | --- |
| **Online TA** | An online travel agent: a booking website such as Booking.com, Expedia, or Agoda. |
| **Offline TA/TO** | Traditional travel agents (TA) and tour operators (TO) working by phone, email, or in person. A tour operator typically bundles accommodation, transport, and activities into a holiday package. |
| **Groups** | A block of rooms booked together for an event or party, such as a tour group, wedding, or conference. |
| **Direct** | The guest booked directly with the hotel—through the hotel website, by phone or email, or as a walk-in—with no intermediary. |
| **Corporate** | A booking made by or for a company, often at a negotiated business rate. |
| **Complementary** | A complimentary stay provided by the hotel, for example to a VIP or partner, or as compensation. The term is commonly spelled *complimentary* outside this dataset. |
| **Aviation** | A booking associated with an airline, such as a crew layover or accommodation for disrupted passengers. |

##### Distribution channel (`distribution_channel`): the route the booking came through

| Term | Meaning |
| --- | --- |
| **TA/TO** | A booking made through a travel agent or tour operator, online or offline. |
| **Direct** | A booking made straight with the hotel. |
| **Corporate** | A booking made through a company's travel-booking arrangement. |
| **GDS** | A global distribution system—such as Amadeus, Sabre, or Travelport—used by travel agents and airlines to book hotels, flights, and cars. |

##### Customer type (`customer_type`)

| Term | Meaning |
| --- | --- |
| **Transient** | An individual booking that is not part of a group or contract, typically for a short-stay leisure or business traveller. |
| **Transient-Party** | A transient booking connected to one or more other transient bookings, such as two couples travelling together on separate reservations. |
| **Group** | A booking that forms part of a group reservation. |
| **Contract** | A booking covered by an allotment or another contract between the hotel and a company or agent. |

#### Meal plan (`meal`)

| Term | Meaning |
| --- | --- |
| **BB** | Bed & Breakfast: room plus breakfast. |
| **HB** | Half Board: breakfast plus one other meal, usually dinner. |
| **FB** | Full Board: breakfast, lunch, and dinner. |
| **SC** | Self Catering: room only, with no meals included. |

<sub>[back to top](#tc)</sub>

## Exploratory Data Analysis (EDA) <a name="eda"></a>
### Data cleansing
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

## 📈 Power BI Dashboard <a name="dashboard"></a>

<img width="1156" height="651" alt="image" src="https://github.com/user-attachments/assets/c8b79046-00fd-4d3c-be4a-fff56635a3d8" />


<sub>[back to top](#tc)</sub>
## 🔮 Predictive analysis <a name="ml"></a>

**Objective:** To develop a model that can predict whether a hotel booking is likely to be cancelled before the guest arrives.

The model uses historical booking data to predict two possible outcomes:
- **1 = Cancelled:** The guest cancels the booking
- **0 = Not Cancelled:** The booking is not cancelled


### Factors Used for Prediction

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
