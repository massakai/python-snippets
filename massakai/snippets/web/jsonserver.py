import json
import logging

import tornado.ioloop
import tornado.web

logging.basicConfig(
    format='%(asctime)-15s %(levelname)s %(message)s',
    level=logging.INFO)


class JsonHandler(tornado.web.RequestHandler):
    async def post(self):
        # JSON以外のリクエストは400 Bad Requestにする
        if (self.request.headers.get('Content-Type')
                != 'application/json'):
            raise tornado.web.HTTPError(400)

        # JSONをパースする
        data = json.loads(self.request.body)

        # ここで処理を実施する
        logging.info(f'data = {data}')

        # レスポンスを書き込む
        self.write({'result': 'OK'})


def main():
    app = tornado.web.Application([
        (r'/json', JsonHandler),
    ])
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
