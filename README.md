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

