
import cx_Oracle
from flask import Flask, jsonify, request, session
import json
from flask_cors import CORS, cross_origin


dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe')
conn = cx_Oracle.connect(user=r'system', password='oracle', dsn=dsn_tns)
app = Flask(__name__)
app.secret_key = "adatb"

CORS(app)


def query_db(query, args=(), one=False):
    with conn.cursor() as cursor:
        cursor.execute(query, args)
        r = [dict((cursor.description[i][0], value)
                  for i, value in enumerate(row)) for row in cursor.fetchall()]
    return (r[0] if r else None) if one else r


def autoIncrement(table):
    lastId = query_db("select * from (select * from " +
                      table + " order by id desc) where rownum = 1")
    return lastId[0]["ID"] + 1


@app.route('/<table>', methods=["DELETE"])
@cross_origin()
def delete(table):
    if table == "ticket":
        user_id = request.get_json()["user_id"]
        trip_id = request.get_json()["trip_id"]
        queryStr = "delete from ticket where user_id={} and trip_id={}".format(
            user_id,
            trip_id
        )
    else:
        id = request.get_json()["id"]
        queryStr = "delete from " + table + " where id = " + id
        
    with conn.cursor() as cursor:
        cursor.execute(queryStr)
        conn.commit()
    return "", 200


@app.route('/<table>', methods=["PUT"])
@cross_origin()
def put(table):
    if(table[0:5] == "edit-"):
        id = 0
        requestData = request.get_json()
        vesszo_index = 0
        queryStr = "UPDATE " + table[5:] + " SET "
        for k, v in requestData.items():
            if k == "id":
                id = v
            else:
                if(vesszo_index > 0):
                    queryStr += ','
                queryStr += k + " = '" + v + "' "
                vesszo_index += 1

        queryStr += "WHERE id='" + id+"'"
        print(queryStr)

        with conn.cursor() as cursor:
            cursor.execute(queryStr)
            conn.commit()
        return "", 200
    else:
        requestData = request.get_json()

        id = autoIncrement(table)

        queryStr = "insert into " + table + " values('" + str(id) + "',"
        for k, v in requestData.items():
            queryStr += "'" + v + "'" + ","
        queryStr = queryStr[0:-1]
        queryStr += ")"
        print(queryStr)

        with conn.cursor() as cursor:
            cursor.execute(queryStr)
            conn.commit()
        return "", 200


@app.route("/<table>", methods=["GET"])
def listTables(table):
    if table == "trip":
        my_query = query_db("""select id, from_city_id, to_city_id, base_price, airplane_id, has_food, 
            TO_CHAR(takeoff_time,'MM.DD HH24:MM') as takeoff_time, 
            TO_CHAR(landing_time,'MM.DD HH24:MM') as landing_time 
            from trip""")
    elif table == "ticket":
        my_query = query_db("select * from " + table )
        print(my_query)
    else:
        my_query = query_db("select * from " + table + " order by id")

    resp = json.dumps(my_query)
    return resp, 200, {"Access-Control-Allow-Origin": "*"}


@app.route("/timetable", methods=["GET"])
@cross_origin()
def timetable():
    my_query = query_db("""
    select * from(
        select from_city, to_city, 
        TO_CHAR(takeoff_time,'MM.DD HH24:MM') as takeoff_time, 
        TO_CHAR( landing_time,'MM.DD HH24:MM') as landing_time, 
        base_price as price, 
        name as airline_name
        from(
            select city.name as to_city, inner_query.*
            from city, (
                select city.name as from_city, trip.*, airline.name
                from trip, airplane, airline, city 
                where trip.airplane_id = airplane.id 
                and airplane.airline_id = airline.id 
                and city.id = trip.from_city_id 
            ) inner_query where city.id = inner_query.to_city_id
        ) order by takeoff_time, landing_time
    ) where ROWNUM <= 10
    """)
    resp = json.dumps(my_query)
    return resp, 200


@app.route("/popular", methods=["GET"])
@cross_origin()
def popular():
    myQuery = query_db("""
    select * from 
        (select city.name, count(*) as num
        from ticket, trip, city 
        where ticket.trip_id = trip.id 
        and trip.to_city_id = city.id 
        group by city.name 
        order by count(*) desc)
    where ROWNUM <= 10""")
    resp = json.dumps(myQuery)
    return resp, 200


@app.route("/stat", methods=["GET"])
@cross_origin()
def stat():
    myQuery = query_db("""
    select avg_age, sum_trips_price, travellers_num from dual, (
        select count(*) as travellers_num from (
            select  ticket.user_id
            from ticket, customuser 
            where ticket.user_id = customuser.id
            group by ticket.user_id)
    )
    """)
    resp = json.dumps(myQuery)
    return resp, 200


@app.route("/registration", methods=["POST"])
@cross_origin()
def registration():
    requestData = request.get_json()

    pwd = requestData["password"]
    pwd2 = requestData["password2"]

    print(pwd, pwd2, email)
    if pwd == pwd2:
        my_query = query_db(
            """
                insert into customuser values('','{}','{}','{}','{}',0,'{}')
            """.format(
                requestData["email"],
                requestData["age"],
                requestData["firstname"],
                requestData["lastname"],
                pwd)
        )

    return "0", 200


@app.route("/login", methods=["POST"])
@cross_origin()
def login():
    requestData = request.get_json()

    my_query = query_db("""
        select password from customuser where customuser.email = '{}'
    """.format(requestData["email"]))

    if my_query != []:
        password = my_query[0]["PASSWORD"]
        if password == requestData["password"]:
            session["user"] = requestData["email"]
            print("login siker:", session["user"])

            return "1", 200
        else:
            print("failos")

    return "0", 200


@app.route("/top-insurer", methods=["GET"])
@cross_origin()
def topInsurer():
    myQuery = query_db("""
        select * from (
        select insurer.name, count(*) as taken_insurance, sum(price) as revenue
        from insurance,recommended_insurance, insurer
        where insurance.rec_insurance_id = recommended_insurance.id
        and recommended_insurance.insurer_id = insurer.id
        group by insurer.name
        order by count(*) desc
        ) where ROWNUM <= 10
    """)
    resp = json.dumps(myQuery)
    return resp, 200
