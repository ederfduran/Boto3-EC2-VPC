import boto3

class ClientLocator:
    def __init__(self,client):
        self._client= boto3.client(client,region_name='us-west-2')
    
    def get_client(self):
        return self._client

class EC2Client(ClientLocator):
    def __init__(self):
        super().__init__('ec2')