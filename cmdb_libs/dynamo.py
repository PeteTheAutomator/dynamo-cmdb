import boto3
from boto3.dynamodb.conditions import Key


class DynamoHandler:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')

    def post_audit(self, instance_id, results):
        table = self.dynamodb.Table('audits')
        response = table.put_item(
            Item={
                'instance_id': instance_id,
                'rpm_packages': results['rpm_packages'],
                'facts': results['facts'],
            }
        )
        return response

    def query(self, instance_id):
        table = self.dynamodb.Table('audits')
        response = table.query(
            KeyConditionExpression=Key('rpm_packages.name').eq(instance_id)
        )
        return response