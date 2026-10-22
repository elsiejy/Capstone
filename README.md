**Prepared by: Elsie**  
**Dataset used: Hotel Bookings**

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


