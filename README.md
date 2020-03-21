# Airport-Management-System-ATC-Database
The aim of database to record various details of entities like airport, airlines, aircraft, flight and its scheduling and passengers and the relationships among these entities like arrival and departure airport of a flight, the airlines to which a flight belongs to, flight booked by a passenger etc. This database also includes the baggage history of individual passenger. Not only these, it also includes the pilot detail and their relationship to particular flight.

# Assumption
1) A particular (unique) flight code can be associated with either domestic or international flight, and not both (hence removes type from being the key).
2) Actual and scheduled gates and runway will be the same.
3) Flight_Type consists of four parameters (International ,Domestic, Cargo International, Cargo Domestic).
4) Aircraft Codes are unique under an aircraft model/type i.e.weak entity
5) Same department with same position can have multiple salaries
6) Passport numbers are globally unique. We record that detail for every passenger, irrespective of whether they book domestic or international flight.
7) Domestic airport locality- state. International airport locality- country

# Console Application Procedure
There are 5 files required for the console.

1) The (*_doc.txt) files contain the description of the in built queries and updates/inserts.

2) The console.py file is the main file which contains the logic for connecting to and updating the database on the server.

3) The my_queries.py file is the file containing the function definitions for the in-built queries. We can add more functions to this file to support many more types of queries.

4) The console has 4 options.
	a) Write your own query: We can write SQL statements here to execute the queries on the server and we will be shown the results and errors (if any). This is as per the annexure-A of the project guideline pdf.
	b) Queries: The user can input query parameter to some queries we have designed.
	c) Updates: The user can input update parameter to some update scenarios we have designed.
	d) Insert: To insert data to some table
	
	Note: Options b, c, and d can also be done through option a if the user knows SQL.
	
# Some Example Queries
1)  Total number of passengers who are flying from/to north east India on dd/mm/yyyy.
```sql
select * 
from
	(
	select * 
	from booking natural join flight_time_table 
	where exp_dep_date = '2019-10-17'
	) as r join airport 
on r.des_airport_code = airport.airport_code 
where states_country = 'Manipur' or states_country = 'Meghalaya' or states_country = 'Mizoram' or states_country = 'Arunachal Pradesh' 
```
2)  Total expected immigrants and their details in INDIA- mumbai airport on dd/mm/yyyy date.
```sql
Select * 
from
	(
	select * 
	from booking 
	where visatype = 'Immigrant' and exp_arr_date = '2019-10-13'
	) as r natural join flight_time_table 
where des_airport_code = 'BOM'  natural join passenger 
```
3)  All flights arriving in Delhi between 3pm to 4pm on terminal B on ddmmyy. 
```sql
select * 
from flight_time_table 
where des_airport_code='DEL' and sch_arr_terminal = '2' and (sch_dep_time::time+(duration_in_hours||' hours')::interval) < '16:00:00' and (sch_dep_time::time+(duration_in_hours||' hours')::interval) > '15:00:00' 
```
4)  Average delay time for all flights.
```sql
select flight_code, avg((dep_timestamp::timestamp::time+(duration_in_hours||' hours')::interval) - (arr_timestamp::timestamp::time) )
from flight_time_table natural join actual_arr_dep 
group by flight_code;
```
5)  Total AirIndia aircraft which are more than 5 years old.
```sql
select * 
from physical_instance_of_aircraft 
where  airline_code = 'AI' and DATE_PART('year',now()::date)- DATE_PART('year',manufacturing_date::date)>5;
```
6)  Passport no of all the passengers who travelled from x to y on mmddyy.
```sql
select passportno 
from
	(
	booking natural join flight_time_table 
	where exp_dep_date = '2019-12-01' and src_airport_code = 'PNQ' and des_airport_code ='BOM'
	) as r natural join passenger
```
7)  All available flights from mumbai to hyderabad on wednesday.
```sql
select flight_time_table.* 
from flight_time_table natural join availability_code 
where wednesday=true and src_airport_code = 'BOM' and des_airport_code = 'HYD' 
```
8)  Display all pilots who have operated at least one flight from delhi-chennai
```sql
select count(pilot_id) as cnt,pilot_id,pilot_name 
from  pilots natural join flight_time_table 
where src_airport_code = 'DEL' and des_airport_code = 'MAA'
group by pilot_id
having count(pilot_id)>=2
```
9)  All shop owners who have shops at the different airports.
```sql
select owner_name,count(airport_code) 
from commercial_shop
group by owner_name
having count(airport_code) >= 2
```
10) Display cost of each class and each flight from Kolkata to Hyderabad.
```sql
select flight_code,class,cost 
from prices natural join flight_time_table 
where src_airport_code = 'CCU' and des_airport_code = 'DEL' 
group by (class,flight_code)
```
11) All airports with at least one runway that was checked 6 months ago or before from now.
```sql
select distinct (airport_code),airport_name 
from runway_maintenance natural join airport 
where  DATE_PART('year',now()::date)- DATE_PART('year',check_date::date)>1.5;
```
12) List the airlines with the aircrafts who have less than one year left in their service.
```sql
select airline_code,count(airline_code) 
from physical_instance_of_aircraft natural join aircraft 
where  lifetime-(DATE_PART('year',now()::date)- DATE_PART('year',manufacturing_date::date))>1
group by airline_code;
```
13) Sort the airport based on the latest date on which their runways were checked.
```sql
select airport_code,airport_name,mx 
from 
	(
	select airport_code,max(check_date) as mx 
	from runway_maintenance 
	group by airport_code
	) as r natural join airport
order by mx desc
```
14) Sort the pilots based on their frequency of flights between 2 given dates.
```sql
select pilot_id, pilot_name, cnt 
from 
	(
	select pilot_id,count(pilot_id) as cnt 
	from flight_flew 
	where dep_timestamp::date>'2019-10-5' and dep_timestamp::date<'2019-10-15'
	group by pilot_id
	) as r natural join pilots;
```
15) List flights and its empty seats it has on avg weekends/weekdays.
```sql
select flight_code,sum(capacity-cnt)*100/sum(capacity) as Empty_Seats 
from
	(
		(
			select flight_code,cnt,da,aircraft_type 
			from 
				(
				select booking.flight_code,count(passenger_id)as cnt ,date(actual_arr_dep.dep_timestamp)as da 
				from booking join actual_arr_dep 
				on booking.exp_dep_date = (DATE(actual_arr_dep.dep_timestamp)) and booking.exp_arr_date = (DATE(actual_arr_dep.arr_timestamp)) 
				group by booking.flight_code,date(actual_arr_dep.dep_timestamp)
				) as r natural join flight_time_table
		)
	) as t 
natural join aircraft
group by flight_code
```
16) No of avg international/domestic passengers on delhi airport over some time span
```sql
select count(pnr) 
from 
	(
	select * 
	from flight_time_table natural join actual_arr_dep 
	where src_airport_code = 'DEL' or des_airport_code = 'DEL'
	) as r natural join booking 
where date(dep_timestamp) >= '2019-10-13' and date(dep_timestamp) <= '2019-10-16' and date(arr_timestamp) >= '2019-10-13' and date(arr_timestamp) >= '2019-10-13' 
```
17) Passengers who flew more than 5 times with the same airlines
```sql
select airlines.airline_name,passenger_name,count(pnr) 
from booking natural join flight_time_table natural join airlines natural join passenger
group by passenger.passenger_id,airlines.airline_code 
having count(pnr)>5
```
