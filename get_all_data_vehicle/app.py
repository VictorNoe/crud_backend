import pymysql
import json

def lambda_handler(event, context):
    connection = pymysql.connect(
        host='integradora.cf00oc48ct9r.us-east-1.rds.amazonaws.com',
        user='root',
        password='superroot',
        database='victor'
    )

    vehicles = []

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM vehiculos"
            cursor.execute(sql)
            result = cursor.fetchall()

            for row in result:
                car = {
                    'id_rate': row[0],
                    'value': row[1],
                    'comment': row[2],
                    'id_auto': row[3],
                    'id_user': row[4]
                }
                vehicles.append(car)

    finally:
        connection.close()

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS',
        },
        "body": json.dumps({vehicles}),
    }