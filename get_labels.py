import requests
import re
import json
from core.config import LABELS_FILENAME, IGNORES_FILENAME


def get_tag_name(address):
    url = f"https://etherscan.io/address/{address}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_content = response.text
        match = re.search(
            r"(?<=<span class='hash-tag text-truncate'>)([^<]*)(?=<\/span>)",
            html_content,
        )
        if match:
            return match.group(1)
    return None


def read_labels():
    try:
        with open(LABELS_FILENAME, "r") as file:
            return json.load(file)
    except:
        return {}


def get_tag_names(addresses):
    with open(IGNORES_FILENAME, "r") as file:
        ignore = file.read().splitlines()
    address_tag_map = {}
    existing_data = read_labels()
    for address in addresses:
        if address in ignore or address in existing_data:
            continue
        tag_name = get_tag_name(address)
        if not tag_name:
            with open(IGNORES_FILENAME, "a") as file:
                file.write(address + "\n")
            continue
        address_tag_map[address] = tag_name.replace(" ", "_")
    return address_tag_map


def append_to_labels(data):
    existing_data = read_labels()
    existing_data.update(data)
    with open(LABELS_FILENAME, "w") as file:
        json.dump(existing_data, file, indent=4)
