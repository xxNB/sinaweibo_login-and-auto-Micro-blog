import bs4

from spiderman.spider import Spider
from weibo_process.weibo_message import WeiboMessage

HOME_URL = "http://www.cnbeta.com"

class CnbetaParser(Spider):
      def __init__(self):
            super(CnbetaParser, self).__init__(HOME_URL)

      def get_weibo_message(self):
            html = self.download_text()
            soup = bs4.BeautifulSoup( html, "html.parser" )
            items = soup.find_all( attrs={"class": "item"} )
            msg = ''
            if len( items ) > 0:
                  topItem = items[0]
                  title = topItem.h3.text.strip()
                  path = topItem.a.get( 'href' )
                  url = HOME_URL + path
                  # infodiv = topItem.find( attrs={"class": "newsinfo"} )
                  # content = infodiv.get_text()
                  msg = "%s %s" % ( title, url )
            return WeiboMessage( msg )
