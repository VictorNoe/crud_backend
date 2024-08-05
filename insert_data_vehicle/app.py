import pymysql
import json

def lambda_handler(event, context):
    connection = pymysql.connect(
        host='integradora.cf00oc48ct9r.us-east-1.rds.amazonaws.com',
        user='root',
        password='superroot',
        database='victor'
    )

    try:
        with connection.cursor() as cursor:
            body = json.loads(event['body'])
            sql = "INSERT INTO vehiculos (marca, modelo, velocidadMaxima, autonomia) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (body['marca'], body['modelo'], body['velocidadMaxima'], body['autonomia']))
            connection.commit()
            return {
                'statusCode': 201,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS',
                },
                'body': json.dumps({'message': 'Vehicle inserted successfully', 'id': cursor.lastrowid})
            }
    finally:
        connection.close()
