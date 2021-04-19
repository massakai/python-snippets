import json
import logging
import urllib.error
import urllib.request

logging.basicConfig(
    format='%(asctime)-15s %(levelname)s %(message)s',
    level=logging.INFO)


def main():
    data = {
        'data': {
            'key': 'value'
        }
    }

    request = urllib.request.Request(
        'http://localhost:8080/json',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(data).encode('utf-8'))

    try:
        with urllib.request.urlopen(request, timeout=1) as response:
            response_data = json.loads(response.read())
        logging.info(response_data)
    # エラーハンドリング
    except urllib.error.HTTPError as e:
        logging.exception(
            f'Server returned error: '
            f'status = {e.code} reason = {e.reason}')
    except urllib.error.URLError as e:
        logging.exception(
            f'Handler returned error: '
            f'reason = {e.reason}')


if __name__ == '__main__':
    main()
