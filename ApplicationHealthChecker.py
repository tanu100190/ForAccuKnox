import requests
import logging
from datetime import datetime


logging.basicConfig(filename='app_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')


APP_URL = 'http://127.0.0.1:65284/'  

def check_app_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f'Application is UP. Status Code {response.status_code}')
            return 'UP'
        else:
            logging.info(f'Application is DOWN. Status Code {response.status_code}')
            return 'DOWN'
    except requests.exceptions.RequestException as e:
        logging.error(f'Application is DOWN. Error {e}')
        return 'DOWN'

def main():
    status = check_app_health(APP_URL)
    print(f'Application Status {status}')

if __name__ == '__main__':
    main()