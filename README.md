**Prepared by: Elsie**  
**Dataset used: Hotel Bookings**

**Table of content**
- Problem Statement
- Research Objective
- Dataset & definitions
- Exploratory Data Analysis (EDA)
- Data Visualization
- Predictive analysis
- Insights and recommendation

---
## Hotel Booking Dataset 📊 ####

The dataset contains 119,390 hotel reservations of which 43,017 were cancelled representing an overall cancellation rate of 36.03%. This establishes the baseline for investigating whether cancellation risk varies across hotel types, market segments, distribution channels and booking characteristics.

## 🤔 Problem statement

How can the hotel use historical reservation data to identify market, channel, arrival-period and booking profiles associated with a high risk of cancellation and develop a pre-arrival cancellation-risk model to support targeted booking, deposit-policy and inventory-management decisions?

## 🎯 Research objective - Description analysis

1.  Analyse reservation volumes and cancellation rates by hotel type, arrival period, market segment and distribution channel.
2.  Identify booking characteristics associated with cancellation such as lead time, deposit type, customer type, length of stay, party composition, booking changes and special requests - and rank their strength of association.
3.  Examine the association between waiting-list days and cancellation, before and after adjusting for other booking characteristics.
4.  Compare repeat-guest share and previous booking history across market segments, and test whether repeat guests cancel less within each segment.
5.  Identify booking profiles with a high cancellation rate (≥ 50%) and substantial volume (≥ 1,000 bookings), and recommend targeted cancellation-risk strategies.

Target definition: is_canceled = True covers both Canceled (43,017) and No-Show (1,207) reservations which account for 44,224 bookings or 37.04% (36.03% is the rate for the Canceled status alone)

## 🔮 Predictive analysis

Build and evaluate a time-based cancellation-risk model using only information available before the outcome and translate scores into action tiers

## ℹ️ Dataset overview

- File name: bookings_clean
- Time Horizon: July 2015 - August 2017
- Target Category: Bookings
- Key Entities: Customer, Booking, Market Segment, Booking Channel

Link to Jupyter Notebook in Google Colab:
https://colab.research.google.com/drive/168JyWdrVqyX05fLt2Pwlso-BhbiR0CPI?usp=sharing

## 📔 Data Dictionary



### Definitions

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

| Term          | Meaning                                                              |
| ------------- | -------------------------------------------------------------------- |
| **BB**        | Bed & Breakfast: room plus breakfast.                                |
| **HB**        | Half Board: breakfast plus one other meal, usually dinner.           |
| **FB**        | Full Board: breakfast, lunch and dinner.                             |
| **SC**        | Self Catering: room only, no meals.                                  |



