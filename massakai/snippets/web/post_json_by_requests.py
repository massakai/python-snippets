import json
import logging
import requests

logging.basicConfig(
    format='%(asctime)-15s %(levelname)s %(message)s',
    level=logging.INFO)


def main():
    data = {
        'data': {
            'key': 'value'
        }
    }

    try:
        response = requests.post(
            'http://localhost:8080/json',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(data),
            timeout=1  # seconds
        )
        # ステータスコード4XX, 5XX時に例外を発生させる
        response.raise_for_status()

        logging.info(response.json())
    except requests.exceptions.HTTPError as e:
        logging.exception(
            f'Server returned error: '
            f'status = {e.response.status_code} '
            f'reason = {e.response.reason}')
    except requests.exceptions.ConnectionError:
        logging.exception('Connection error')
    except requests.exceptions.Timeout:
        logging.exception('Timeout')


if __name__ == '__main__':
    main()
