#!/user/bin/python

import requests
import bs4
from bs4 import BeautifulSoup
import csv

HscSchoolRanking_TblTag = {
    "TableId": "ctl00_ContentPlaceHolder1_GridView1",   #"class="table table-striped table-bordered table-hover dataTable no-footer""
}

class log(object):
    _logLevelEnum = ( "DEBUG", "INFO", "ERROR")
    def __init__(self):
        self._logLevel = "INFO"

    def setLogLevel(self, lvl):
        assert lvl in self._logLevelEnum
        self._logLevel = lvl

    def logInfo(self, msg):
        if self._logLevel in ("DEBUG", "INFO"):
            print(msg)

def LOG(msg):
    lg = log()
    lg.logInfo(msg)


class WebScraper(object):

    def __init__(self):
        self._webName = None
        self._baseUrl = None
        self._data = None
        self.dataFileName = "web-data.csv"

    def run(self):
        LOG("Scraper run...")
        pass

    # retrive data from the web
    def getData(self):
        pass

    # export data to csv
    def exportToCsv(self):
        LOG("exportToCsv...")
        if self._data == None:
            return None

        if type(self._data) is not list:
            raise Exception("The data to export should be a list")

        with open(self.dataFileName, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            for row in self._data:
                writer.writerow(row)


class BetterEduWebScraper(WebScraper):
    _urls = {
        "HscSchoolRanking": 'https://bettereducation.com.au/results/hsc.aspx',
    }

    def __init__(self):
        super(BetterEduWebScraper, self).__init__()
        self._webName = "BetterEducation"
        self._baseUrl = 'https://bettereducation.com.au'


    def run(self):
        super(BetterEduWebScraper, self).run()

        self._data = self._pickHscSchoolRank()
        print(self._data)
        self.exportToCsv()

    def getData(self):
        #
        pass

    def _pickHscSchoolRank(self):
        http_resp = requests.get(self._urls["HscSchoolRanking"])
        #print(http_resp.text)

        # To solve the 'UnicodeEncodeError': Gbk Codec Can't Encode Character '\xa0'
        # Cause: the 'space' character in html is "&nbsp" which "\xc2 \xa0" as its utf-8 coding which is converted to "\xa0" as unicode character.
        # When displaying it to terminal (which use GBK), "\xa0" does not exist in GBK character set.
        # Solution: TO replace unicode '\xa0' with u' '
        #content_txt = http_resp.text.replace(u'\xa0', u' ')
        print(http_resp.encoding)
        http_resp.text.encode(encoding='utf-8', errors='ignore')
        print(http_resp.text)

        bs = BeautifulSoup(http_resp.text)
        #print(bs)

        data = []

        table = bs.find('table', attrs={"id" : HscSchoolRanking_TblTag["TableId"]})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')

            betterEduRank = cols[1].a.find(text=True)
            schoolName = cols[2].a.find(text=True)
            percent = cols[3].find(text=True)
            studentMum = cols[4].find(text=True)
            examsSat = cols[5].span.find(text=True)
            da = cols[6].find(text=True)
            print(type(da))
            category = cols[7].find(text=True).encode(encoding='utf-8')
            print(type(category))
            region = cols[8].find(text=True).encode(encoding='utf-8')

            rec = [betterEduRank, schoolName, percent, studentMum, examsSat, da, category, region]
            data.append(rec)
            #print(rec)
            #print('-'*40)

        return data





if __name__ == '__main__':
    scraper = BetterEduWebScraper()
    scraper.run()



