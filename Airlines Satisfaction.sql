use airlines;
# Get total number of passengers
SELECT COUNT(*) FROM airline_data;
# Count of satisfied vs. dissatisfied passengers
SELECT satisfaction, COUNT(*) FROM airline_data GROUP BY satisfaction;
# Find the average age of passengers
SELECT AVG(Age) FROM airline_data;
# List of unique travel classes available
SELECT DISTINCT Class FROM airline_data;
# Average flight distance by customer type
SELECT "Customer Type", AVG("Flight Distance") FROM airline_data GROUP BY "Customer Type";
# Top 5 most delayed flights (by arrival delay)
SELECT * FROM airline_data ORDER BY "Arrival Delay in Minutes" DESC LIMIT 5;
# Find gender-based satisfaction rates
SELECT Gender, satisfaction, COUNT(*) FROM airline_data GROUP BY Gender, satisfaction;
# Compare delays between different classes
SELECT Class, AVG("Departure Delay in Minutes") AS Avg_Departure_Delay, AVG("Arrival Delay in Minutes") AS Avg_Arrival_Delay FROM airline_data GROUP BY Class;
# Identify services that have the highest impact on satisfaction
SELECT "Seat comfort", "Inflight wifi service", "Inflight entertainment", "Online boarding", "Cleanliness", COUNT(*) AS Frequency FROM airline_data WHERE satisfaction = 'satisfied' GROUP BY "Seat comfort", "Inflight wifi service", "Inflight entertainment", "Online boarding", "Cleanliness" ORDER BY Frequency DESC;
# Find the percentage of flights delayed over 30 minutes
SELECT (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM airline_data)) AS Delay_Percentage FROM airline_data WHERE "Arrival Delay in Minutes" > 30;
# Check if higher baggage handling ratings result in better satisfaction
SELECT "Baggage handling", satisfaction, COUNT(*) FROM airline_data GROUP BY "Baggage handling", satisfaction ORDER BY "Baggage handling" DESC;
# Correlation between online booking ease and satisfaction
SELECT "Ease of Online booking", satisfaction, COUNT(*) FROM airline_data GROUP BY "Ease of Online booking", satisfaction ORDER BY "Ease of Online booking";