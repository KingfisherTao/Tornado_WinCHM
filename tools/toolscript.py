# coding=utf-8
from os.path import abspath, dirname
from bs4 import BeautifulSoup as BS


def makeDataJS(templateFile: str, outFilePath: str):
    """使用 bs4 库 对 WinCHM 生成的 htm 进行解析，提取 a 的 title 和 href 并生成data.js"""
    _jsDataStrLst = []
    try:
        with open(f'{dirname(dirname(abspath(__file__)))}{templateFile}', 'r', encoding='utf-8') as t:
            _template = BS(t.read(), 'html.parser')
            for a in _template.find_all('a'):
                try:
                    if a["href"] != '#':
                        _jsDataStrLst.append(f'"", "{a["title"]}", "{a["href"]}",')
                except KeyError:
                    pass
            with open(f'{dirname(dirname(abspath(__file__)))}{outFilePath}', 'w+', encoding='utf-8') as f:
                f.write(f'var contents = new Array({"".join(_jsDataStrLst)});')
    except FileNotFoundError as e:
        print('templateFile 参数错误, 此文件不存在:', e)

