import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("API_KEY")

endpoints = {
    "https://api.etherscan.io/api?module=account&action=txlist&address=0xc5102fE9359FD9a28f877a67E36B0F050d81a3CC&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=YourApiKeyToken"
}


def get_acc_txns(address, offset):
    return f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset={offset}&sort=asc&apikey={API_KEY}"


def requester(address, offset):
    return requests.get(get_acc_txns(address, offset)).json()
