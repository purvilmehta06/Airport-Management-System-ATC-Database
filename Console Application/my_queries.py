def executeQuery(conn, cursor):
	query = input('Enter query: ')
	if query[-1] != ';':
		query += ';'
	try:
		cursor.execute(query)
		for result in cursor.fetchall():
			print(*result)
		conn.commit()
	except Exception as e:
		print(e)
	return None



def query1(cursor):
	query = "select passenger_name from (Select * from (select * from booking where visatype = 'Immigrant' and exp_arr_date = '{}') as r natural join flight_time_table where des_airport_code = '{}') as r2  natural join passenger ;"
	
	date = input('Input Query Date (yy-mm-dd): ')
	airport_code = input('Input Query Airport Code: ')
	cursor.execute(query.format(date, airport_code))
	
	try:
		results = cursor.fetchall()
		final = []
		for result in results:
			final.append(*result)
	except Exception as e:
		return [(e)]
	
	return final


def query2(cursor):
	query = "SELECT get_delay();"
	
	try:
		cursor.execute(query)
	except Exception as e:
		return [(e)]
	
	return cursor.fetchall()


def query3(cursor):
	query = "select * from physical_instance_of_aircraft where  airline_code = '{}' and DATE_PART('year',now()::date)- DATE_PART('year',manufacturing_date::date)>{};"

	try:
		airline_code = input('Input Airline: ')
		years = input('Input Minimum Years Left in Service: ')
		cursor.execute(query.format(airline_code, years))
	except Exception as e:
		return [(e)]

	return cursor.fetchall()


def query4(cursor):
	query = "select passenger_id from booking natural join flight_time_table where exp_dep_date = '{}' and src_airport_code = '{}' and des_airport_code = '{}';"

	try:
		date = input('Input Date (yy-mm-dd): ')
		src_airport = input('Input Source Airport Code: ')
		dst_airport = input('Input Destination Airport Code: ')
		cursor.execute(query.format(date, src_airport, dst_airport))
	except Exception as e:
		return [(e)]

	return cursor.fetchall()


def query5(cursor):
	query = "select flight_time_table.flight_code from flight_time_table natural join availability_code where {}=true and src_airport_code = '{}' and des_airport_code = '{}';"

	try:
		day = input('Input Day of the week: ')
		src_airport = input('Input Source Airport Code: ')
		dst_airport = input('Input Destination Airport Code: ')
		cursor.execute(query.format(day, src_airport, dst_airport))
	except Exception as e:
		return [(e)]

	return cursor.fetchall()


def query6(cursor):
	query = "select flight_code,class,cost from prices natural join flight_time_table where src_airport_code = '{}' and des_airport_code = '{}' group by (class,flight_code);"

	try:
		src_airport = input('Input Source Airport Code: ')
		dst_airport = input('Input Destination Airport Code: ')
		cursor.execute(query.format(src_airport, dst_airport))
	except Exception as e:
		return [(e)]

	return cursor.fetchall()


def query7(cursor):
	query = "select airport_code,airport_name,mx from (select airport_code,max(check_date) as mx from runway_maintenance group by airport_code)as r natural join airport order by mx desc;"

	try:
		cursor.execute(query)
	except Exception as e:
		return [(e)]

	return cursor.fetchall()


def query8(cursor):
	query = "select count(pnr) from (select * from flight_time_table natural join actual_arr_dep where src_airport_code = '{}' or des_airport_code = 'DEL') as r natural join booking where date(dep_timestamp) >= '{}' and date(dep_timestamp) <= '{}' and date(arr_timestamp) >= '{}' and date(arr_timestamp) >= '{}';"

	try:
		airport_code = input('Input Query Airport Code: ')
		date_l = input('Input Date 1 (yy-mm-dd): ')
		date_r = input('Input Date 2 (yy-mm-dd): ')
	except Exception as e:
		return [(e)]

	cursor.execute(query.format(airport_code, date_l, date_r, date_l, date_r))

	return cursor.fetchall()


def query9(cursor):
	query = "select airlines.airline_name,passenger_name,count(pnr) from booking natural join flight_time_table natural join airlines natural join passenger group by passenger.passenger_id,airlines.airline_code having count(pnr)>{};"

	freq = input('Input Frequency: ')
	try:
		cursor.execute(query.format(freq))
	except Exception as e:
		return [(e)]

	return cursor.fetchall()


def update1(conn, cursor):
	query = "update passenger set passenger_name = '{}' where passenger_id = {};"

	pass_id = input('Input PassengerID: ')
	new_name = input('Input New Name: ')

	try:
		cursor.execute(query.format(new_name, pass_id))
		conn.commit()
	except Exception as e:
		return e

	return 'Passenger Name updated!'

def update2(conn, cursor):
	query = "update prices set cost = {} where flight_code = '{}' AND class = '{}';"

	flight_code = input('Input Flight Code: ')
	class_ = input('Input Class: ')
	new_cost = input('Input New Cost: ')

	try:
		cursor.execute(query.format(new_cost, flight_code, class_))
		conn.commit()
	except Exception as e:
		return e

	return 'Cost Updated!'


def insert1(conn, cursor):
	query = "INSERT INTO runway_maintenance VALUES ({}, '{}', '{}', '{}');"

	officer_name = input('Input Officer Name: ')
	airport_code = input('Input Airport Code: ')
	runway_no = input('Input Runway No: ')
	check_date = input('Input Check Date(yy-mm-dd): ')

	try:
		cursor.execute(query.format(runway_no, officer_name, check_date, airport_code))
		conn.commit()
	except Exception as e:
		return e
	return 'Checking Inserted'


def insert2(conn, cursor):
	query = "INSERT INTO booking VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {});"

	pnr = input('Input PNR: ')
	visa = input('Input Visa Type: ')
	exp_dep_date = input('Input Expected Dep Date(yy-mm-dd): ')
	exp_arr_date = input('Input Expected Arr Date(yy-mm-dd): ')
	class_ = input('Input Class: ')
	flight_code = input('Input Flight Code: ')
	pass_id = input('Input Passenger ID: ')

	try:
		cursor.execute(query.format(pnr, visa, exp_dep_date, exp_arr_date, class_, flight_code, pass_id))
		conn.commit()
	except Exception as e:
		return e
	return 'Booking Inserted'


