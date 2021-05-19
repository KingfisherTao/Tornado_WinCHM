# coding=utf-8
from handler.Request import IndexHandler, HelpFrameHandler, HelpTopHandler, HelpLeftHandler, HelpToolBarHandler, \
    HelpContentsHnadler, HelpIndexHandler, HelpSearchHandler, HelpBookmarkHandler

TornadoHandler = \
    [
        (r'/index', IndexHandler),
        (r'/webhelpframe.htm', HelpFrameHandler),
        (r'/webhelptop.htm', HelpTopHandler),
        (r'/webhelpleft.htm', HelpLeftHandler),
        (r'/webhelptoolbar.htm', HelpToolBarHandler),
        (r'/webhelpcontents.htm', HelpContentsHnadler),
        (r'/webhelpindex.htm', HelpIndexHandler),
        (r'/webhelpsearch.htm', HelpSearchHandler),
        (r'/webhelpbookmark.htm', HelpBookmarkHandler),
    ]

__all__ = ['TornadoHandler']