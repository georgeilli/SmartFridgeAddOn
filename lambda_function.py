import json
import boto3

s3 = boto3.client('s3')
bucket = "fridgedata-s3"
key = 'FridgeContents.json'

def lambda_handler(event, context):
    # TODO implement
    
    if "ProductName" in event:
        list = event['ProductName']
    else:
        list = ""
        
    products = get_s3_bucket(bucket, key)
    
    #print(products['Name'])
    print(list)
    plist = []

    for record in products:
        print(plist.append(record['Name']))
        
    
    response =""
    #tt = products['Data']['Items'][event['ProductName']]
    for record in products:
        
        if record['Name'] == list:
            print("Found: " + record['Name'])
            response = {
                "found": True,
                "message": "Found: " + record['Name']
            }
            break;
        else:
            response = {
                "found": False,
                "message": "This item is not in the Fridge  "
            }
     
           
    if list == "":
        return {
            'statusCode': 200,
            'body': products
        }
    else:    
        return {
            'statusCode': 200,
            'body': response
        }

def get_s3_bucket(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    Product = json.loads(content.read())
    print("Product Json loaded:",Product)
    return Product

# def item(product, itemname):
  #  item = product['Data']['Items'][itemname]
   # return item
    