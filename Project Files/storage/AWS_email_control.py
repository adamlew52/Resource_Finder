import boto3 
import json 

def lambda_handler( event, context ):
    
    #grab the to, from , subject and body 
    to_address = event['theceresapp@gmail.com']
    subject = event['subject']
    body = event['body']
    from_address = event['theceresapp@gmail.com']
    
    #load the ses client 
    client = boto3.client('ses')
    
    response = client.send_email(
        Source= from_address, 
        Destination={
            'ToAddresses':[
                    to_address
                ]            
        }, 
        Message={
            'Subject': {
                'Data': subject
            }, 
            'Body':{
                'Text':{
                    'Data': body 
                }
            }
        }
    )
    
    return {'status': 200, 'body': json.dumps( response ) }
    
    
    
    