# coding=utf-8
from abc import ABC
from tornado.web import RequestHandler


# index
class IndexHandler(RequestHandler, ABC):
    def get(self):
        self.render(
            'index.htm',
        )


class HelpFrameHandler(RequestHandler, ABC):
    def get(self):
        self.render(
            'webhelpframe.htm',
        )


class HelpTopHandler(RequestHandler, ABC):
    def get(self):
        self.render(
            'webhelptop.htm',
        )


class HelpLeftHandler(RequestHandler, ABC):
    def get(self):
        self.render(
            'webhelpleft.htm',
        )


class HelpToolBarHandler(RequestHandler, ABC):
    def get(self):
        self.render(
            'webhelptoolbar.htm',
        )


class HelpContentsHnadler(RequestHandler, ABC):
    def get(self):
        self.render(
            'webhelpcontents.htm',
        )


class HelpIndexHandler(RequestHandler, ABC):
    def get(self):
        self.render(
            'webhelpindex.htm',
        )


class HelpSearchHandler(RequestHandler, ABC):
    def get(self):
        self.render(
            'webhelpsearch.htm',
        )

    def post(self):
        self.render(
            'webhelpsearch.htm',
        )


class HelpBookmarkHandler(RequestHandler, ABC):
    def get(self):
        self.render(
            'webhelpbookmark.htm',
        )
