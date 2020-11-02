from bs4 import BeautifulSoup
import requests
import lxml
import datetime
import pandas as pd


from database import db_session
from models import Data


def get_udemy_info():
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text, "lxml")
    name = soup.select(
        "body > div.row > div > div:nth-child(2) > div > div > div.card-image > span")[0].string
    jukousei = soup.select(
        "body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.subscribers")[0].string
    jukousei = int(jukousei.split('：')[1])
    reviewes = soup.select(
        "body > div.row > div > div:nth-child(2) > div > div > div.card-action > p.reviews")[0].string
    reviewes = int(reviewes.split('：')[1])

    results = {
        'name': name,
        'jukousei': jukousei,
        'reviewes': reviewes,
    }
    return results


def write_data():
    # 読み込むデータ
    _results = get_udemy_info()
    # 書き込むデータ
    date = datetime.date.today()
    subscribers = _results['n_subscribers']
    reviews = _results['n_subscribers']

    row = Data(date=date, subscribers=subscribers, reviews=reviews)

    db_session.add(row)
    db_session.commit()
