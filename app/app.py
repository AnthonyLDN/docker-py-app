#!/usr/bin/python
import mysql.connector, os, sys, re, time

version_table_name = 'versionTable'
version_column_name = 'version'

def connect(host, db, user, password):
	"Connect to the database"
	try:
		return mysql.connector.connect(host=host, db=db, user=user, passwd=password)
	except mysql.connector.Error as err:
		print("Could not connect to database: {}".format(err))

def get_db_version(cursor):
	if cursor:
		cursor.execute(
			"SELECT {:s} FROM {:s}".format(
				version_column_name, version_table_name
			)
		)
		version = cursor.fetchone()
	
		return version[0]

def update_db_version(conn, cursor, script_version):
	"Update versionTable.version"
	cursor.execute(
		"UPDATE {:s} SET {:s} = '{:s}'".format(
			version_table_name, version_column_name, script_version
		)
	)
	
	print('Database Version: {:s}\n'.format(script_version))

	conn.commit()

def get_script_version(script):
	"Given a script, return the version."
	return re.search(r'\d+', script).group()

def execute_script(conn, cursor, dir_path, script):
	"Executes a given script and updates the table version number."
	if conn and cursor:
		current_db_version = get_db_version(cursor)
		script_version =  get_script_version(script)
		if script_version > current_db_version:
			print('Executing {:s}'.format(script))
			# Read the .sql file and exectute each statement.
			file = open(dir_path + script)
			sql = file.read().strip()
			commands = sql.split(';')
			# Remove any empty strings
			commands = list(filter(None, commands))

			for command in commands:
				print('statement -> {:s}'.format(command))
				cursor.execute(command)
				result = cursor.fetchone()
				print('output -> {:s}'.format(result[0]))
				conn.commit()

			print('')
			update_db_version(conn, cursor, script_version)

def main():
	if len(sys.argv) != 6:
		exit("Invalid script parameters. Usage: \"python ecsd.py <script directory> <DB host> <DB name> <DB username> <DB password>\"")

	# These params should be parsed better but I ran out of time!
	script_dir = sys.argv[1]
	db_host = sys.argv[2]
	db_name = sys.argv[3]
	db_username = sys.argv[4]
	db_password = sys.argv[5]

	while True:
		conn = connect(db_host, db_name, db_username, db_password)
		if conn is None:
			print("Could not make database connection. Attempting again in 30 seconds.")
			time.sleep(30)
		else:
			break
  			
	cursor = conn.cursor()
	scripts = []

	if os.path.isdir(script_dir):
		for file in os.listdir(script_dir):
			if file.endswith(".sql"):
				scripts.append(file)
	
	# Sort the list of scripts into asscending order.
	scripts_ascending_version = sorted(scripts)

	db_version = get_db_version(cursor)

	# Compile a subset of scripts for execution
	scripts_filtered = [script for script in scripts_ascending_version if get_script_version(script) > db_version]

	# If there are either no scripts in the directory or no new scripts to execute.
	if not scripts_filtered:
		sys.exit('No new scripts to execute, exiting.')

	print('\nInitial Database Version: {:s}\n'.format(db_version))

	# Print out all .sql scripts found in the directory provided.
	print('Scripts Found:\n' + '\n'.join(scripts_ascending_version) + '\n')
	
	# Execute the scripts and update versionTable.version.
	for script in scripts_filtered:
		execute_script(conn, cursor, script_dir, script)

if __name__ == "__main__":
	main()