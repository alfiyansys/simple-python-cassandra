from db import DBA

dbp = DBA()

rows = dbp.query("select * from foo")

for row in rows:
	print row
