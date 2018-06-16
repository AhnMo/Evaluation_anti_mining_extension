#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
# pip install selenium
# http://selenium-python.readthedocs.io/
# http://chromedriver.chromium.org/getting-started // must be setting up path
# https://www.blazemeter.com/blog/6-easy-steps-testing-your-chrome-extension-selenium

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

    for i in urls:
      self.driver.get(i)
      sleep(self.sleep_time)
      callback(i, self.getLogs())

    self.clean()

class SiteIter:
  def __init(self):
    pass

  def __iter__(self):
    self.idx = 0
    self.max = 10000
    return self

  def __next__(self):
    if self.idx == self.max:
      raise StopIteration
    ret = self.idx
    self.idx += 1
    return 'https://peter.pagez.kr/%04d/' % (ret)

  def next(self):
    return self.__next__()

if __name__ == '__main__':
  a = AutomatedTest('ext\\MinerBlock.crx')
  def output(url, result):
    with open('result_MinerBlock.txt', 'ab+') as f:
      x = 'IS511-DETECTED' in (str(result))
      print url, x
      f.write(str(x) + '\r\n')
  a.start(SiteIter(), output)
