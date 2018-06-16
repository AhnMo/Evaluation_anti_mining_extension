#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from time import sleep
# pip install selenium
# http://selenium-python.readthedocs.io/
# http://chromedriver.chromium.org/getting-started // must be setting up path
# https://www.blazemeter.com/blog/6-easy-steps-testing-your-chrome-extension-selenium

class StopIteration(Exception):
    pass

class AutomatedTest:
  def __init__(self, path=''):
    self.driver = None
    self.setExtensionPath(path)
    self.sleep_time = 3

  def __del__(self):
    self.clean()

  def init(self):
    assert self.ext_path != ''

    desired = DesiredCapabilities.CHROME
    desired['loggingPrefs'] = {
      'browser': 'ALL'
    }

    options = webdriver.ChromeOptions()
    options.add_extension(self.getExtensionPath())

    self.driver = webdriver.Chrome(
      chrome_options=options,
      desired_capabilities=desired
    )

  def clean(self):
    if self.driver != None:
      self.driver.close()
      self.driver = None

  def setExtensionPath(self, path):
    self.ext_path = path

  def getExtensionPath(self):
    return self.ext_path

  def getLogs(self):
    return self.driver.get_log('browser')

  def start(self, urls, callback):
    self.init()

    try:
      for i in urls:
        self.driver.get(i)
        #sleep(1)
        try:
          self.driver.find_element(By.XPATH, '//button[text()="Continue"]').click()
        except:
          pass

        sleep(10)
        callback(i, self.getLogs())
        #exit(1)
    except StopIteration, e:
      print "ITER END"
    except Exception, e:
      print "UNKNOWN ERROR", e
      pass

    self.clean()


class SiteIter:
  def __init(self):
    pass

  def __iter__(self):
    self.idx = 0
    self.max = 1000
    return self

  def __next__(self):
    if self.idx == self.max:
      raise StopIteration
    ret = self.idx
    self.idx += 1
    return 'https://wsp02.pagez.kr/%04d/' % (ret)

  def next(self):
    return self.__next__()

if __name__ == '__main__':
  #exts = ['is511', 'NoMiner', 'NoCoin', 'MinerBlock', 'CoinHive-blocker']
  exts = ['CoinHive-blocker']
  for ext in exts:
    a = AutomatedTest('%s.crx' % (ext))
    def output(url, result):
      with open('result_%s.txt' % (ext), 'ab+') as f:
        x = 'IS511-DETECTED' in (str(result))
        print url, x
        f.write(str(x) + '\r\n')
    a.start(SiteIter(), output)
