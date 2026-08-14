# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Paul Jacob 
**Section:** Platinum
**Last Name:** Biñas
**Date:** Date Completed
---

## Step 1: Identify the Big Problem
### Main Problem
The main problem of the school canteen’s queue is its Efficiency, the system cannot calculate the change of students and track the inventory of the canteen and students don’t have a systematic way to choose what to buy so it creates a slow line
---
## Step 2: Identify the Sub-Problems
1. No clear area where students can choose what to buy rather than simply going to the line and create a delay when choosing
2. No automatically way to calculate the change of students
3. No tracking system where it can check the inventory of the canteen
4. Canteen's accomodation system is not effiecent 
---
## Step 3: Apply Computational Thinking Skills

| Sub-problem 1 | Breaking down complexity | By making a sytem where students can choose what to buy, the queue time to get their purchases will lessen |
| Sub-problem 2 |Efficiency | By making a efficient way to calculate the change of students the effiency of the the queue |
| Sub-problem 3 | Breaking down complexity | By breaking each part of the canteens stock or inventory we can track how much is left in the canteens storage |
| Sub-problem 4 | Clarity and focus | By focusing the accomodation system to make the queue time quicker |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Sub-Problem 1
### Pseudocode
START
DISPLAY available products
INPUT "Enter the product you want to buy"

IF product is available THEN
    ADD product to order
    DISPLAY "Product added to order"
ELSE
    DISPLAY "Product is unavailable"
END IF

DISPLAY "Proceed to payment"
INPUT amount paid
CALCULATE change = amount paid - total price
DISPLAY change

UPDATE inventory
DISPLAY "Order complete"

END
---