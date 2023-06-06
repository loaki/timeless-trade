import logging
import requests
from pydantic import BaseSettings
from typing import List
from selenium import webdriver
from bs4 import BeautifulSoup
from scrapping import scrap_url

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)


class Settings(BaseSettings):
    SEED_URL: str

    class Config:
        env_file = "env"


if __name__ == "__main__":
    settings = Settings()
    r = scrap_url(settings.SEED_URL)
