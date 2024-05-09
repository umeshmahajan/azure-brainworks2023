import snowflake.connector

class SnowflakeConnector:
    def __init__(self, account, user, password, warehouse, database, schema):
        """AI is creating summary for __init__

        Args:
            account ([type]): [description]
            user ([type]): [description]
            password ([type]): [description]
            warehouse ([type]): [description]
            database ([type]): [description]
            schema ([type]): [description]
        """
        self.account = account
        self.user = user
        self.password = password
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Establish a connection to Snowflake.
        """
        self.connection = snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.account,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        """
        Execute a SQL query.
        """
        if not self.connection or not self.cursor:
            raise Exception("Connection not established. Call connect() method first.")

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        """
        Close the connection.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


