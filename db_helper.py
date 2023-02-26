import mysql.connector


class DB:
    # connect to database
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='amit',
                database='campusx')

            self.mycursor = self.conn.cursor()
            print("connection established")
        except:
            print("Connection error")

    def fetch_cities(self):
        city = []
        self.mycursor.execute("""
        SELECT DISTINCT(SOURCE) FROM flights_cleaned
        UNION
        SELECT DISTINCT(DESTINATION) FROM flights_cleaned
        """)
        data = self.mycursor.fetchall()
        

        for i in data:
            city.append(i[0])

        return city  

    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
        SELECT Airline,Route,Dep_Time,Duration,Price  
        FROM flights_cleaned
        WHERE source = '{}' AND Destination = '{}'
        """.format(source,destination))

        data = self.mycursor.fetchall()

        return data

    def fetch_flight_pie(self):
        self.mycursor.execute("""
        SELECT Airline,COUNT(*) FROM flights_cleaned
        GROUP BY Airline
        """)

        data = self.mycursor.fetchall()

        Airline = []
        Frequency = []
        for item in data:
            Airline.append(item[0])
            Frequency.append(item[1])

        return Airline,Frequency
    

    def most_busiest_aiport(self):
        self.mycursor.execute("""
        SELECT source,count(*) FROM 
        (SELECT Source  FROM flights_cleaned
        UNION ALL
        SELECT Destination FROM flights_cleaned) temp
        GROUP BY source
        ORDER BY count(*) DESC
        """)

        data = self.mycursor.fetchall()

        Airport = []
        Busy = []
        for item in data:
            Airport.append(item[0])
            Busy.append(item[1])

        return Airport,Busy


    def no_of_flights(self):
        self.mycursor.execute("""
        SELECT Date_of_Journey,count(*) FROM flights_cleaned
        GROUP BY Date_of_Journey
        """)

        data = self.mycursor.fetchall()

        Date = []
        Number = []
        for item in data:
            Date.append(item[0])
            Number.append(item[1])

        return Date,Number