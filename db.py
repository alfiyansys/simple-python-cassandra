from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from config import db_config

# DB Access
class DBA:
	def __init__(self):
		self.username = db_config['username']
		self.password = db_config['password']
		self.keyspace = db_config['keyspace']

	def connect(self):
		auth_provider = PlainTextAuthProvider(username=self.username,password=self.password)
		cluster = Cluster(auth_provider=auth_provider)
		return cluster.connect(self.keyspace)

	def query(self, query):
		session = self.connect()
		results = session.execute(query)
		return results
