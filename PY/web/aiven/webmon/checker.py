# website checker
# The tool to check a website's availability 


import logging
import re
import requests


class WebChecker(object):
    """Check the availability of a webstie. """
    
    def __init__(self, url:str, pattern:str='') -> None:
        """init the website checker.

        Args:
          url: the target website (URL)
          reg_pattern:  the regex pattern used to check the website, optional.   
        """
        self.url = url
        self.pattern = pattern

    def check(self) -> dict:
        """Check the website and return the result in dict().
           
           The result is in form of:
            {
                'url':'http://a.url',
                'success':True,   # the result for the availability check (True/False)
                'errcode':'200',  # the status_code or other Error info (str)
                'rsptime':'0:00:00.719604'  # the HTTP respond time of the website (str)
            }
            success = True if both bolow condition are met:
            1) http response status_code = 200
            2) regex pattern match found (if pattern provided).
        Return:
            A dict with the check result
        """

        metrics = {
           'url':self.url,
           'success':False,
           'errcode':'Unknown',
           'rsptime':'0',
        }

        try:
            rsp = requests.get(self.url)
        except Exception as e:
            logging.warning(f'HTTP request Error: {e}')
            metrics['success'] = False
            metrics['errcode'] = f'{e}'
            metrics['rsptime'] = str(0)
        else:        
            metrics['errcode'] = str(rsp.status_code)
            metrics['rsptime'] = str(rsp.elapsed)
            success = True
            if self.pattern:
                result = re.search(self.pattern, rsp.text)   
                success = True if result else False
            success &= rsp.status_code==200
            metrics['success'] = success

        return metrics