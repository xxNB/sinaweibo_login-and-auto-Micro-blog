from spiderman.cnbeta import CnbetaParser
from spiderman.cnblog import CnblogParser
from spiderman.miaopai import MiaopaParser
from spiderman.myBlog import MyBlogParser
from spiderman.techweb import TechwebParser
from spiderman.tuicool import TuicoolParser

spiders = [ 
          MyBlogParser(),
          CnbetaParser(),
          CnblogParser(),
          MiaopaParser(),
          MyBlogParser(),
          TechwebParser(),
          TuicoolParser() 
        ]

currentIndex = 0
count = len(spiders)

def nextSpider():
      global currentIndex
      spider = spiders[currentIndex]
      currentIndex = (currentIndex + 1) % count
      return spider
