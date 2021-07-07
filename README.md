# Love Sandwiches
## By Anna Greaves, CI  

A follow along Code Institute project, Love Sandwiches, by Anna Greaves.  
The program is run in the command line, and is fully back end operational.   
It is deployed on Heroku to allow users to access the application.

It is a market stall which sells sandwiches. They make some beforehand each day (stock), 
keep track of how many are sold (sales), make extra for customers if they run out (negative surplus values) and 
throw away leftovers (positive surplus values).

## What app should do
- Collect sales data from user
- Add sales data into sales worksheet
- Calculate surplus numbers
- Add surplus data to worksheet
- Calculate the average sales for the last 5 markets, to decide how many to make for the next one
- Print stock recommendations to terminal
- Check that the sales data input from the user is valid

## Key features:
- Link google sheet and google drive APIs to allow Python to access and edit the data