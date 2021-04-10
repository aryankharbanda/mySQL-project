#!/usr/bin/python
import pymysql

tables = {'0': 'team', '1': 'coaches', '2': 'player',
		  '3': 'match', '4': 'stadium', '5': 'umpire', 
		  '6': 'ground_staff', '7': 'team_management'}

# Open database connection
db = pymysql.connect("localhost", "sqlaryan", "aryansql", "ipl")
# db = pymysql.connect("localhost", "root", "aryansql", "TEST3")

def get_code(cursor):
	print("Select the table : ")
	print("Enter\n0 for team\n1 for coaches\n2 for player\n3 for match\n4 for stadium\n5 for umpire\n6 for ground_staff\n7 for team_management")
	code = input()

	if code < '0' or code > '7':
		print("Error : invalid input")
		return -1

	return code

def view():
	cursor = db.cursor()

	code = get_code(cursor)
	if code == -1:
		return

	sql_query = "SELECT * FROM " + tables[code]
 
	try :
		cursor.execute(sql_query)
		
		results = cursor.fetchall()
		for entry in results:
			print(entry)

	except Exception as e:
		print("Error ", str(e))
		db.rollback()

def insert():
	cursor = db.cursor()

	print("Enter:\n0 for player\n1 for umpire")
	inp = input()

	if inp == '0':
		player_id = input("Enter player_id : ")
		name = input("Enter name : ")
		nationality = input("Enter nationality: ")
		team_name = input("Enter team : ")
		player_type = input("Enter player type (0 for bowler; 1 for batsman; 2 for wicketkeeper) : ")
		
		if player_type == '0':
			wickets = input("Enter wickets : ")
			economy = input("Enter economy : ")

			cursor = db.cursor()
			try:
				cursor.execute(
					"""INSERT INTO player(player_id,name,nationality,team_name) VALUES (%s,%s,%s,%s)""",
							   (player_id,name,nationality,team_name))
				cursor.execute(
					"""INSERT INTO bowler(player_id,wickets,economy) VALUES (%s,%s,%s)""",
							   (player_id,wickets,economy))
				db.commit()

			except Exception as e:
				print("Error ", str(e))
				db.rollback()

			cursor.close()

		if player_type == '1':
			runs = input("Enter runs : ")
			average = input("Enter average : ")

			cursor = db.cursor()
			try:
				cursor.execute(
					"""INSERT INTO player(player_id,name,nationality,team_name) VALUES (%s,%s,%s,%s)""",
							   (player_id,name,nationality,team_name))
				cursor.execute(
					"""INSERT INTO batsman(player_id,runs,average) VALUES (%s,%s,%s)""",
							   (player_id,runs,average))
				db.commit()

			except Exception as e:
				print("Error ", str(e))
				db.rollback()

			cursor.close()

		if player_type == '2':
			stumps = input("Enter stumps : ")
			caughts = input("Enter caughts : ")

			cursor = db.cursor()
			try:
				cursor.execute(
					"""INSERT INTO player(player_id,name,nationality,team_name) VALUES (%s,%s,%s,%s)""",
							   (player_id,name,nationality,team_name))
				cursor.execute(
					"""INSERT INTO bowler(player_id,stumps,caughts) VALUES (%s,%s,%s)""",
							   (player_id,stumps,caughts))
				db.commit()

			except Exception as e:
				print("Error ", str(e))
				db.rollback()

			cursor.close()

	elif inp == '1':
		umpire_id = input("Enter umpire_id : ")
		name = input("Enter name : ")
		salary = input("Enter salary : ")

		cursor = db.cursor()
		try:
			cursor.execute(
				"""INSERT INTO umpire(umpire_id,name,salary) VALUES (%s,%s,%s)""", (umpire_id,name,salary))
			db.commit()

		except Exception as e:
			print("Error ", str(e))
			db.rollback()

		cursor.close()

	else:
		print("Error: more insertion queries will be supported in future updates xP")

def update():
	cursor = db.cursor()

	player_id = input("Enter player_id whose stats are to be updated : ");

	player_type = input("Enter player type whose stats are to be updated:\n0 for bowler; 1 for batsman; 2 for wicketkeeper")
		
	if player_type == '0':
		upd = input("0 for wickets; 1 for economy")

		if upd == '0':
			wickets = input("Enter wickets : ")

			cursor = db.cursor()
			try:
				cursor.execute(
					"""UPDATE bowler SET wickets=%s WHERE player_id=%s""",(wickets,player_id))
				db.commit()

			except Exception as e:
				print("Error ", str(e))
				db.rollback()

			cursor.close()

		if upd == '1':
			economy = input("Enter economy : ")

			cursor = db.cursor()
			try:
				cursor.execute(
					"""UPDATE bowler SET economy=%s WHERE player_id=%s""",(economy,player_id))
				db.commit()

			except Exception as e:
				print("Error ", str(e))
				db.rollback()

			cursor.close()

	if player_type == '1':
		upd = input("0 for runs; 1 for average")

		if upd == '0':
			runs = input("Enter runs : ")

			cursor = db.cursor()
			try:
				cursor.execute(
					"""UPDATE bowler SET runs=%s WHERE player_id=%s""",(runs,player_id))
				db.commit()

			except Exception as e:
				print("Error ", str(e))
				db.rollback()

			cursor.close()

		if upd == '1':
			average = input("Enter average : ")

			cursor = db.cursor()
			try:
				cursor.execute(
					"""UPDATE bowler SET average=%s WHERE player_id=%s""",(average,player_id))
				db.commit()

			except Exception as e:
				print("Error ", str(e))
				db.rollback()

			cursor.close()

	if player_type == '2':
		upd = input("0 for stumps; 1 for caughts")

		if upd == '0':
			stumps = input("Enter stumps : ")

			cursor = db.cursor()
			try:
				cursor.execute(
					"""UPDATE bowler SET stumps=%s WHERE player_id=%s""",(stumps,player_id))
				db.commit()

			except Exception as e:
				print("Error ", str(e))
				db.rollback()

			cursor.close()

		if upd == '1':
			caughts = input("Enter caughts : ")

			cursor = db.cursor()
			try:
				cursor.execute(
					"""UPDATE bowler SET caughts=%s WHERE player_id=%s""",(caughts,player_id))
				db.commit()

			except Exception as e:
				print("Error ", str(e))
				db.rollback()

			cursor.close()

	else:
		print("Error: more updation queries will be supported in future updates xP")	

def delete():
	cursor = db.cursor()

	umpire_id = input("Enter umpire_id which is retiring : ");

	# DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
	try:
		cursor.execute(
			"""DELETE FROM umpire WHERE umpire_id=%s""",(umpire_id))
		db.commit()

	except Exception as e:
		print("Error ", str(e))
		db.rollback()

	cursor.close()

def analysis():
	cursor = db.cursor()

	print("ANALYSIS REPORT : teams ordered by descending popularity")

	report = "SELECT team.name as team_name FROM team, match WHERE team.name = match.home_team OR team.name = match.away_team GROUP BY team.name ORDER BY AVG(match.audience) DESC"
	# report = "SELECT team.name FROM team CROSS JOIN match WHERE team.name = match.home_team OR team.name = match.away_team GROUP BY team.name ORDER BY AVG(match.audience) DESC"

	try :
		cursor.execute(report)
		results = cursor.fetchall()
		for entry in results:
			print(entry)

	except Exception as e:
		print("Error ", str(e))
		db.rollback()

def queries():
	cursor = db.cursor()

	print("Enter query number :")
	q = input("1 - project teams with win rate > 0.7\n2 - select all players in a team\n3 - retreive max(wickets) by bowlers\n4 - search players with partial text\n")

	if q == '1':
		
		report = "SELECT * FROM team WHERE winrate > '0.7'"
		
		try :
			cursor.execute(report)
			results = cursor.fetchall()
			for entry in results:
				print(entry)

		except Exception as e:
			print("Error ", str(e))
			db.rollback()

	# INCOMPLETE
	if q == '2':
		
		tem = input("Enter team name : ")

		try :
			cursor.execute("""SELECT * FROM player WHERE team_name = %s""",(tem))
			results = cursor.fetchall()
			for entry in results:
				print(entry)

		except Exception as e:
			print("Error ", str(e))
			db.rollback()

	if q == '3':
		
		report = "SELECT MAX(wickets) AS MaxWick FROM bowler"
		
		try :
			cursor.execute(report)
			results = cursor.fetchall()
			for entry in results:
				print(entry)

		except Exception as e:
			print("Error ", str(e))
			db.rollback()

	if q == '4':
		# search
		playa = input("Enter player to search : ")

		try :
			cursor.execute("""SELECT * FROM player WHERE name LIKE %s""",("%" + playa + "%"))
			results = cursor.fetchall()
			for entry in results:
				print(entry)

		except Exception as e:
			print("Error ", str(e))
			db.rollback()
			
	

def loop():
	while(1):
		print("\nSelect query :\n0 - view\n1 - insertion\n2 - updation\n3 - deletion\n4 - analysis\n5 - queries\n6 - exit")

		inp = input()

		if inp == '0':
			view()
		elif inp == '1':
			insert()
		elif inp == '2':
			update()
		elif inp == '3':
			delete()
		elif inp == '4':
			analysis()
		elif inp == '5':
			queries()
		if inp == '6':
			return

loop()