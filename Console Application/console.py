import psycopg2, sys, os
import my_queries

db_name = '201701073'
db_user = '201701073'
db_host = '10.100.71.21'
db_pass = 'purvilpm@6'
db_port = '5432'

conn = psycopg2.connect(database = db_name, user = db_user, password = db_pass, host = db_host, port = db_port)
my_cur = conn.cursor()

my_cur.execute('SET SEARCH_PATH TO airport_atc;')
print("You're currently in the airport database!")
print('-----------------------------------------')
print("Option 1) Write Your Own Query")
print()
print("Option 2) Pre-written Queries/Stored Procedures")
with open('queries_doc.txt', 'r') as f:
	print(f.read())
print()
print("Option 3) Inserts")
with open('inserts_doc.txt', 'r') as f:
	print(f.read())
print()
print("Option 4) Updates")
with open('updates_doc.txt', 'r') as f:
	print(f.read())
print()
print("Option 5) Exit")
print()


while True:
	option = int(input('Enter option: '))
	if option == 5:
		break
	elif option == 2:
		query_id = int(input('Enter Query ID: '))
		
		if query_id == 1:
			results = my_queries.query1(my_cur)
			print('---- Results ----')
			for result in results:
				print(result)
		
		elif query_id == 2:
			results = my_queries.query2(my_cur)
			print('---- Results ----')
			for result in results:
				print(*result)
		
		elif query_id == 3:
			results = my_queries.query3(my_cur)
			print('---- Results ----')
			for result in results:
				print(*result)
		
		elif query_id == 4:
			results = my_queries.query4(my_cur)
			print('---- Results ----')
			for result in results:
				print(*result)
		
		elif query_id == 5:
			results = my_queries.query5(my_cur)
			print('---- Results ----')
			for result in results:
				print(*result)
		
		elif query_id == 6:
			results = my_queries.query6(my_cur)
			print('---- Results ----')
			for result in results:
				print(*result)
		
		elif query_id == 7:
			results = my_queries.query7(my_cur)
			print('---- Results ----')
			for result in results:
				print(*result)
		
		elif query_id == 8:
			results = my_queries.query8(my_cur)
			print('---- Results ----')
			for result in results:
				print(*result)
		
		elif query_id == 9:
			results = my_queries.query9(my_cur)
			print('---- Results ----')
			for result in results:
				print(*result)
		
		else:
			print('Invalid Query ID')
	
	elif option == 4:
		update_id = int(input('Enter Update ID: '))

		if update_id == 1:
			print(my_queries.update1(conn, my_cur))

		elif update_id == 2:
			print(my_queries.update2(conn, my_cur))

		else:
			print('Invalid Update ID')

	elif option == 3:
		insert_id = int(input('Enter Insert ID: '))

		if insert_id == 1:
			print(my_queries.insert1(conn, my_cur))

		elif insert_id == 2:
			print(my_queries.insert2(conn, my_cur))

		else:
			print('Invalid Update ID')

	elif option == 1:
		my_queries.executeQuery(conn, my_cur)
	
	else:
		print('Invalid Option')





	print('\n')
conn.close()