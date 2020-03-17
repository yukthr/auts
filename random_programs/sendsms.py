import telnyx
import json

def function():
    telnyx.api_key = "xxxxxx"

    your_telnyx_number = "+xxxx"
    destination_number = "+xxxx"

    telnyx.Message.create(
        from_=your_telnyx_number,
        to=destination_number,
        text="I need some water!",
     )

def lambda_handler(event, context):
    # TODO implement
    function()
    return {
        'statusCode': 200,
        'body': json.dumps('Executed!')
    }
