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
            vehicle_id = event['queryStringParameters']['id']
            sql = "DELETE FROM vehiculos WHERE id = %s"
            cursor.execute(sql, (vehicle_id,))
            connection.commit()
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS',
                },
                'body': json.dumps({'message': 'Vehicle deleted successfully'})
            }
    finally:
        connection.close()
