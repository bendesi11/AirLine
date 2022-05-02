from datetime import datetime, timedelta
import random
import string
# pip install names
import names

city_names = ["Aberdeen", "Abilene", "Akron", "Albany", "Albuquerque", "Alexandria", "Allentown", "Amarillo", "Anaheim", "Anchorage", "Ann Arbor", "Antioch", "Apple Valley", "Appleton", "Arlington", "Arvada", "Asheville", "Athens", "Atlanta", "Atlantic City", "Augusta", "Aurora", "Austin", "Bakersfield", "Baltimore", "Barnstable", "Baton Rouge", "Beaumont", "Bel Air", "Bellevue", "Berkeley", "Bethlehem", "Billings", "Birmingham", "Bloomington", "Boise", "Boise City", "Bonita Springs", "Boston", "Boulder", "Bradenton", "Bremerton", "Bridgeport", "Brighton", "Brownsville", "Bryan", "Buffalo", "Burbank", "Burlington", "Cambridge", "Canton", "Cape Coral", "Carrollton", "Cary", "Cathedral City", "Cedar Rapids", "Champaign", "Chandler", "Charleston", "Charlotte", "Chattanooga", "Chesapeake", "Chicago", "Chula Vista", "Cincinnati", "Clarke County", "Clarksville", "Clearwater", "Cleveland", "College Station", "Colorado Springs", "Columbia", "Columbus", "Concord", "Coral Springs", "Corona", "Corpus Christi", "Costa Mesa", "Dallas", "Daly City", "Danbury", "Davenport", "Davidson County", "Dayton", "Daytona Beach", "Deltona", "Denton", "Denver", "Des Moines", "Detroit", "Downey", "Duluth", "Durham", "El Monte", "El Paso", "Elizabeth", "Elk Grove", "Elkhart", "Erie", "Escondido", "Eugene", "Evansville", "Fairfield", "Fargo", "Fayetteville", "Fitchburg", "Flint", "Fontana", "Fort Collins", "Fort Lauderdale", "Fort Smith", "Fort Walton Beach", "Fort Wayne", "Fort Worth", "Frederick", "Fremont", "Fresno", "Fullerton", "Gainesville", "Garden Grove", "Garland", "Gastonia", "Gilbert", "Glendale", "Grand Prairie", "Grand Rapids", "Grayslake", "Green Bay", "GreenBay", "Greensboro", "Greenville", "Gulfport-Biloxi", "Hagerstown", "Hampton", "Harlingen", "Harrisburg", "Hartford", "Havre de Grace", "Hayward", "Hemet", "Henderson", "Hesperia", "Hialeah", "Hickory", "High Point", "Hollywood", "Honolulu", "Houma", "Houston", "Howell", "Huntington", "Huntington Beach", "Huntsville", "Independence", "Indianapolis", "Inglewood", "Irvine", "Irving", "Jackson", "Jacksonville", "Jefferson", "Jersey City", "Johnson City", "Joliet", "Kailua", "Kalamazoo", "Kaneohe", "Kansas City", "Kennewick", "Kenosha", "Killeen", "Kissimmee", "Knoxville", "Lacey", "Lafayette", "Lake Charles", "Lakeland", "Lakewood", "Lancaster", "Lansing", "Laredo", "Las Cruces", "Las Vegas", "Layton", "Leominster", "Lewisville", "Lexington", "Lincoln", "Little Rock", "Long Beach", "Lorain", "Los Angeles",
              "Louisville", "Lowell", "Lubbock", "Macon", "Madison", "Manchester", "Marina", "Marysville", "McAllen", "McHenry", "Medford", "Melbourne", "Memphis", "Merced", "Mesa", "Mesquite", "Miami", "Milwaukee", "Minneapolis", "Miramar", "Mission Viejo", "Mobile", "Modesto", "Monroe", "Monterey", "Montgomery", "Moreno Valley", "Murfreesboro", "Murrieta", "Muskegon", "Myrtle Beach", "Naperville", "Naples", "Nashua", "Nashville", "New Bedford", "New Haven", "New London", "New Orleans", "New York", "New York City", "Newark", "Newburgh", "Newport News", "Norfolk", "Normal", "Norman", "North Charleston", "North Las Vegas", "North Port", "Norwalk", "Norwich", "Oakland", "Ocala", "Oceanside", "Odessa", "Ogden", "Oklahoma City", "Olathe", "Olympia", "Omaha", "Ontario", "Orange", "Orem", "Orlando", "Overland Park", "Oxnard", "Palm Bay", "Palm Springs", "Palmdale", "Panama City", "Pasadena", "Paterson", "Pembroke Pines", "Pensacola", "Peoria", "Philadelphia", "Phoenix", "Pittsburgh", "Plano", "Pomona", "Pompano Beach", "Port Arthur", "Port Orange", "Port Saint Lucie", "Port St. Lucie", "Portland", "Portsmouth", "Poughkeepsie", "Providence", "Provo", "Pueblo", "Punta Gorda", "Racine", "Raleigh", "Rancho Cucamonga", "Reading", "Redding", "Reno", "Richland", "Richmond", "Richmond County", "Riverside", "Roanoke", "Rochester", "Rockford", "Roseville", "Round Lake Beach", "Sacramento", "Saginaw", "Saint Louis", "Saint Paul", "Saint Petersburg", "Salem", "Salinas", "Salt Lake City", "San Antonio", "San Bernardino", "San Buenaventura", "San Diego", "San Francisco", "San Jose", "Santa Ana", "Santa Barbara", "Santa Clara", "Santa Clarita", "Santa Cruz", "Santa Maria", "Santa Rosa", "Sarasota", "Savannah", "Scottsdale", "Scranton", "Seaside", "Seattle", "Sebastian", "Shreveport", "Simi Valley", "Sioux City", "Sioux Falls", "South Bend", "South Lyon", "Spartanburg", "Spokane", "Springdale", "Springfield", "St. Louis", "St. Paul", "St. Petersburg", "Stamford", "Sterling Heights", "Stockton", "Sunnyvale", "Syracuse", "Tacoma", "Tallahassee", "Tampa", "Temecula", "Tempe", "Thornton", "Thousand Oaks", "Toledo", "Topeka", "Torrance", "Trenton", "Tucson", "Tulsa", "Tuscaloosa", "Tyler", "Utica", "Vallejo", "Vancouver", "Vero Beach", "Victorville", "Virginia Beach", "Visalia", "Waco", "Warren", "Washington", "Waterbury", "Waterloo", "West Covina", "West Valley City", "Westminster", "Wichita", "Wilmington", "Winston", "Winter Haven", "Worcester", "Yakima", "Yonkers", "York", "Youngstown"]

airlines = ["Mango", "Middle East Airlines", "Virgin Australia", "Vistara", "Viva Aerobus", "Volaris", "American Airlines", "United Airlines", "Delta Air Lines", "Spirit Airlines", "Cape Air", "Lufthansa", "Aeroflot", "Iberia", "Shanghai Airlines", "Silkair", "Silver", "Singapore Airlines", "Skylanes", "South African Airways", "Southwest", "SpiceJet", "Spirit", "Spring Airlines", "Spring Japan", "SriLankan Airlines", "Sun Country", "Air Baltic",
            "Air Belgium", "Air Canada", "Air Caraibes", "Air China", "Air Corsica", "Air Dolomiti", "Air Europa", "Air France", "Air India", "Air India Express", "TAP Portugal", "THAI", "tigerair Australia", "Transavia Airlines", "TUI UK", "TUIfly", "Cathay Pacific", "Cayman Airways", "CEBU Pacific Air", "China Airlines", "China Eastern", "China Southern", "Condor", "Copa Airlines", "Egyptair", "EL AL", "Emirates", "Ethiopian Airlines", "Etihad", "Eurowings"]

insurers = ["ACORD", "Adler Insurance", "Admiral", "Adrian Flux", "Ageas", "AIG", "Allianz", "Allied World", "Ambant", "AmTrust", "Aon", "Aon Benfield", "Aon Hewitt", "Aon Risk Solutions", "A-Plan", "ARAG", "Arch Insurance", "Argo Group", "Arista", "Ascent", "Aspen", "Assurant", "Aston Lark", "Autonet", "Aviva", "AXA", "AXA XL", "Axiom Underwriting", "AXIS Capital", "Barbican", "Be Wiser", "Beazley", "Beech Underwriting", "Berkley", "Berkshire Hathaway", "Besso", "BGL Group", "Brassington", "Bravo Group", "Brightside", "Brightside", "Broker Direct", "Broker Network", "Bupa", "Camberford", "Canopius", "Carole Nash", "Castel", "CFC Underwriting", "Chubb", "Churchill", "CII", "Citynet", "CNA", "Cobra Network", "Compass", "Co-op", "Covea", "Crawford and Company", "Crawford and Company", "DAS UK", "Direct Line Group", "DUAL", "Ecclesiastical", "Ed Broking", "Endsleigh", "Esure", "Ethos Broking", "First Central", "FM Global", "Gallagher", "General Legal Protection", "Generali", "Geo Underwriting", "Guy Carpenter", "HandR Insurance", "Hastings", "HDI",
            "Henderson", "Hiscox", "Howden", "Hyperion Insurance Group", "Ingenie", "Integro", "Ironshore", "James Hallam", "Jelf", "JLT", "Lancashire", "Legal and General", "Liberty Mutual", "Lloyds", "Lockton Companies", "LV", "Lycetts", "Manchester Underwriting", "Markel Corporation", "Markerstudy", "Marsh", "Marsh McLennan", "MCE", "Mercer", "MetLife", "Miles Smith", "Minova", "More Than", "MS Amlin", "Munich Re", "NFU Mutual", "Obelisk Underwriting", "Octo Telematics", "OPUS Underwriting", "Pardus Underwriting", "Pen Underwriting", "Pioneer Underwriting", "Plum Underwriting", "Portus", "Prudential Plc", "Pulse", "QBE", "Quindell", "RFIB", "RKH Specialty", "RSA", "Sabre Insurance", "Saga", "SCOR", "Sedgwick", "Simply Business", "Sompo", "Sportscover", "Stackhouse Poland", "Starr Companies", "Staysure", "Swiftcover", "Swinton", "Swiss Re", "Tempo Underwriting", "The AA", "Thistle Insurance", "Thomas Carroll", "Tokio Marine", "Touchstone Underwriting", "Towergate Underwriting", "Travelers", "UK General", "UK Insurance", "Willis Towers Watson", "Zurich"]

airplane_types = ["Airbus A300", "Airbus A310", "Airbus A330", "Airbus A340", "Airbus A350 XWB", "Airbus A380", "Airbus A400M", "Airbus A3xx sorozat", "Airbus A320", "An–38", "An–140", "An–148", "Szu–80", "Szuhoj Superjet 100", "Tu–204", "Tu–334", "Tu–70", "Tu–104", "Tu–110", "Tu–114", "Tu–124", "Tu–134",
                  "Tu–144", "Tu–154", "McDonnell Douglas DC–8", "McDonnell Douglas DC–9", "McDonnell Douglas DC–10", "McDonnell Douglas MD–11", "McDonnell Douglas MD–12", "McDonnell Douglas MD–80", "McDonnell Douglas MD–90", "Convair 990", "Convair CV–240", "Convair 880", "DC–3", "DC–4", "DC–6", "Piper PA–46 Malibu"]


hotels = ["The Venetian", "Spotlight Hotel", "The Mississippi Hotel", "Green Tortoise Hostel", "The Orchard Hotel", "Spring Brook", "Hotel Agoura", "Wonder Hill Inn", "The New Yorker", "Beachwalk Resort", "Etiquette Suites", "Water Vibe Resorts", "Consulate Hotel", "Quaint Motel", "Cape Grace", "Fountain Fun", "Element", "The New View", "White Season Resort", "Hotel Occazia", "Purple Orchid", "Prestige proga Inn", "The Manhattan", "Lime Wood", "Parallel Shine",
          "The Glory Hotel", "The Mutiny Hotel", "The Huntington Hotel", "Towne Place Suites", "Cosmopolitan Hotel", "Eden Roc", "Coastal bay hotel", "Dream Connect", "Purple Orchid", "The Palazzo Resort", "The White Rock Hotel", "The Hot Springs Hotel", "Venture Hotel", "The Lakefront", "The Peninsula", "The Lakefront", "Always Welcome", "Tower Hotel", "Sunny Canopy", "Royal Galaxy", "The Watson Hotel", "Treebones Resort", "Waypoint", "The Eternity Resort"]
# repcsi típusok ülőhellyel együtt
airplane_types_seats = {}
for v in airplane_types:
    airplane_types_seats[v] = random.randint(100, 500)

NUM_OF_USERS = 50
NUM_OF_TRIPS = 50
MIN_SEAT = 50
NUM_OF_REC_INSURANCE = 50
NUM_OF_AIRPLANES = 50


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


def random_time_interval():
    start_time = datetime.now() + timedelta(days=random.randint(1, 100),
                                            hours=random.randint(0, 24), minutes=random.randint(0, 60))
    end_time = start_time + \
        timedelta(hours=random.randint(3, 20), minutes=random.randint(0, 60))
    return start_time.strftime("%d/%m/%Y %H:%M:%S"), end_time.strftime("%d/%m/%Y %H:%M:%S")


# user
for i in range(NUM_OF_USERS):
    print("INSERT INTO CUSTOMUSER VALUES('{}','{}','{}','{}', '{}', '{}', '{}');"
          .format(i,
                  random_char(10)+"@gmail.com",
                  random.randint(5, 80),
                  names.get_first_name(),
                  names.get_last_name(),
                  "0",
                  # "trips",
                  random_char(8)))


# city
for i, v in enumerate(city_names):
    print("INSERT INTO CITY VALUES('{}','{}');".format(i, v))


# airline
for i, v in enumerate(airlines):
    print("INSERT INTO AIRLINE VALUES('{}','{}');".format(i, v))


# insurer
for i, v in enumerate(insurers):
    print("INSERT INTO INSURER VALUES('{}','{}');".format(i, v))


# hotel
for i, v in enumerate(hotels):
    print("INSERT INTO HOTEL VALUES('{}','{}','{}','{}');"
          .format(i,
                  v,
                  random.randint(1, 5),
                  random.randint(0, len(city_names)-1)))


# airplane
for i in range(NUM_OF_AIRPLANES):
    type = random.choice(airplane_types)
    print("INSERT INTO AIRPLANE VALUES('{}','{}','{}','{}');"
          .format(i,
                  type,
                  random.randint(0, len(airlines)-1),
                  airplane_types_seats[type]))

# trip
for i in range(NUM_OF_TRIPS):
    start_time, end_time = random_time_interval()
    print("INSERT INTO TRIP VALUES('{}','{}','{}','{}', '{}', '{}', TO_DATE('{}', 'DD/MM/YYYY HH24:MI:SS'), TO_DATE('{}', 'DD/MM/YYYY HH24:MI:SS'));"
          .format(i,
                  random.randint(0, len(city_names)-1),
                  random.randint(0, len(city_names)-1),
                  random.randint(40000, 300000),
                  random.randint(0, NUM_OF_AIRPLANES-1),
                  random.choice([0, 1]),
                  start_time,
                  end_time
                  ))

# ticket
for i in range(500):
    print("INSERT INTO TICKET VALUES('{}','{}','{}');"
          .format(random.randint(0, NUM_OF_USERS-1),
                  random.randint(0, NUM_OF_TRIPS-1),
                  random.randint(0, MIN_SEAT-1)))


# rec insurance
for i in range(NUM_OF_REC_INSURANCE):
    print("INSERT INTO RECOMMENDED_INSURANCE VALUES('{}','{}','{}','{}','{}');"
          .format(i,
                  random.randint(0, len(insurers)-1),
                  random.randint(0, NUM_OF_TRIPS-1),
                  "Valamilyen biztosítás",
                  random.randint(10000, 100000)))


# insurance
for i in range(50):
    print("INSERT INTO INSURANCE VALUES('{}','{}','{}','{}');"
          .format(i,
                  random.randint(0, NUM_OF_USERS-1),
                  random.randint(0, NUM_OF_REC_INSURANCE-1),
                  random.randint(10000, 100000),
                  ))
