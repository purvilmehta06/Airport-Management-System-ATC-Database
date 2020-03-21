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
