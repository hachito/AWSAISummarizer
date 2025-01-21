import json
import boto3
import requests as req
from bs4 import BeautifulSoup as bs
import os

def lambda_handler(event, context):
    ModelID = "Insert AI model"
    bedrock = boto3.client(service_name="bedrock-runtime", region_name="Insert Region")
    link = event["link"]

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Insert Table")
    response = table.get_item(Key={"link": link})

    link_string = get_text(link)
    messages = 
    [
        {
            "role": "user",
            "content": 
            [
                {"text": f"You are an article simplifier. Simplify this text within a paragraph:{link_string}."},
            ],
        }
    ]

    response = bedrock.converse
    (
        modelId=ModelID,
        messages=messages,
    )

    responsetext = response["output"]["message"]["content"][0]["text"]
    table.put_item(Item={"link": link, "text": responsetext})
    print(responsetext)


def get_text(link):
    html = req.get(link)
    soup = bs(html.text, 'html.parser')
    text = soup.find_all("p", class_="")
    return text
