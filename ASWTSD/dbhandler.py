import os


def init_db():
		"""This function creates a empty database"""
		inited = open("temp.sdb", "w")
		inited.close()


def rename_temp_db(name):
		"""This function renames the TEMP database"""
		os.rename('temp.sdb', name)


def delete_db(path):
		"""This deletes a database"""
		os.remove(path)


def move_db(name, newpath):
		"""This function moves a db using os.rename"""
		os.rename(name, newpath)
