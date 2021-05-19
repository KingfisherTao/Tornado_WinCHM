# coding=utf-8
from os.path import join, dirname
from tornado import ioloop
from tornado.web import Application, StaticFileHandler
from tornado.options import define, options
from handler import *
from tools import *

if __name__ == '__main__':
    define('port', default='8000', type=int, help="listening port")
    options.parse_command_line()

    # 创建路由 handler 动态添加需要路由的页面
    _handlers = []
    for item in TornadoHandler:
        _handlers.append(item)

    # setting
    _settings = {
        'debug': True,
        'static_path': join(dirname(__file__), 'static'),
        'template_path': join(dirname(__file__), "template"),
        'static_url_prefix': '/static/',
    }

    # 制作 data.js 为了使用 WinCHM 框架的 搜索功能
    makeDataJS(r'./template/webhelpcontents.htm', r'./static/js/data.js')

    # 初始化 app 并启动
    _app = Application(handlers=_handlers, **_settings)
    _app.listen(options.port)
    print(f'starting tornado on port {options.port}')
    ioloop.IOLoop.current().start()
