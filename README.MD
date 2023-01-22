```python
$pip install site2hdd
from site2hdd import download_url_list,get_proxies,download_webpage
```

### This video in Portuguese might help you: https://www.youtube.com/watch?v=FuLikrVCVeY

```python
xlsxfile,pklfile = get_proxies(
  save_path_proxies_all_filtered='c:\\newfilepath\\myproxiefile\\proxy', #  path doesn't have to exist, it will be created, last 
 # part (proxy) is the name of the file - pkl and xlsx will be added
 # important: There will be 2 files, in this case: c:\\newfilepath\\myproxiefile\\proxy.pkl and c:\\newfilepath\\myproxiefile\\proxy.xlsx

  http_check_timeout=4, # if proxy can't connect within 4 seconds to wikipedia, it is invalid

  threads_httpcheck=50, # threads to check if the http connection is working

  threads_ping=100 ,  # before the http test, there is a ping test to check if the server exists

  silent=False, # show results when a working server has been found

  max_proxies_to_check=2000, # stops the search at 2000
)
```

## Downloading lists of free proxy servers

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/site2hdd/site2hdd00000000.png" alt="">

## Checking if the ip exists

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/site2hdd/site2hdd00000001.png" alt="">

## Checking if http works and own IP is hidden

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/site2hdd/site2hdd00000004.png" alt="">

```python
urls = [r'''https://pandas.pydata.org/docs/#''', r'''https://pandas.pydata.org/docs/getting_started/index.html''',
       r'''https://pandas.pydata.org/docs/user_guide/index.html''',
       r'''https://pandas.pydata.org/docs/reference/index.html''',
       r'''https://pandas.pydata.org/docs/development/index.html''',
       r'''https://pandas.pydata.org/docs/whatsnew/index.html''', r'''https://pandas.pydata.org/docs/dev/index.html''',
       r'''https://pandas.pydata.org/docs/index.html''',
       r'''https://pandas.pydata.org/pandas-docs/version/1.4/index.html''',
       r'''https://pandas.pydata.org/pandas-docs/version/1.3/index.html''',
       r'''https://pandas.pydata.org/pandas-docs/version/1.2/index.html''',
       r'''https://pandas.pydata.org/pandas-docs/version/1.1/index.html''',
       r'''https://pandas.pydata.org/pandas-docs/version/1.0/index.html''',
       r'''https://github.com/pandas-dev/pandas''', r'''https://twitter.com/pandas_dev''',
       r'''https://pandas.pydata.org/docs/#pandas-documentation''', r'''https://pandas.pydata.org/docs/pandas.zip''',
       r'''https://pandas.pydata.org/''', r'''https://pypi.org/project/pandas''',
       r'''https://github.com/pandas-dev/pandas/issues''', r'''https://stackoverflow.com/questions/tagged/pandas''',
       r'''https://groups.google.com/g/pydata''', r'''https://pandas.pydata.org/docs/#module-pandas''',
       r'''https://www.python.org/''',
       r'''https://pandas.pydata.org/docs/getting_started/index.html#getting-started''',
       r'''https://pandas.pydata.org/docs/user_guide/index.html#user-guide''',
       r'''https://pandas.pydata.org/docs/reference/index.html#api''',
       r'''https://pandas.pydata.org/docs/development/index.html#development''',
       r'''https://pandas.pydata.org/docs/_sources/index.rst.txt''', r'''https://numfocus.org/''',
       r'''https://www.ovhcloud.com/''', r'''http://sphinx-doc.org/''', ]

download_url_list(urls, ProxyPickleFile='c:\\newfilepath\\myproxiefile\\proxyn.pkl',
   # The file you created using the function: get_proxies 
   SaveFolder='f:\\testdlpandaslinks',  # where should the files be saved
   try_each_url_n_times=5,  # maximum retries for each url
   ProxyConfidenceLimit=10,
   # each link will be downloaded twice and then compared. If only one result is positive, it counts as a not successful download. But if     the ProxyConfidenceLimit is higher, then it will be accepted
   ThreadLimit=50,  # downloads at the same time
   RequestsTimeout=10,  # Timeout for requests
   ThreadTimeout=12,  # Should be a little higher than RequestsTimeout
   SleepAfterKillThread=0.1,  # Don't put 0.0 here - it will use too much CPU
   SleepAfterStartThread=0.1,  # Don't put 0.0 here - it will use too much CPU
   IgnoreExceptions=True, )
```

## Downloading a url list

### Never close the app when this is the last message that was printed: "Batch done - writing files to HDD ..."

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/site2hdd/site2hdd00000007.png" alt="">

```python
# downloads only links from one domain! All others are ignored!
starturls=[r'''https://pydata.org/upcoming-events/''',  # if it can't find links on the starting page, pass a list of links from the site. 
r'''https://pydata.org/past-events/''',
r'''https://pydata.org/organize-a-conference/''',
r'''https://pydata.org/start-a-meetup/''',
r'''https://pydata.org/volunteer/''',
r'''https://pydata.org/code-of-conduct/''',
r'''https://pydata.org/diversity-inclusion/''',
r'''https://pydata.org/wp-content/uploads/2022/03/PyData-2022-Sponsorship-Prospectus-v4-1.pdf''',
r'''https://pydata.org/sponsor-pydata/#''',
r'''https://pydata.org/faqs/''',
r'''https://pydata.org/''',
r'''https://pydata.org/about/''',
r'''https://pydata.org/sponsor-pydata/''',
r'''https://pydata.org/wp-content/uploads/2022/03/PyData-2022-Sponsorship-Prospectus-v4.pdf''',]
download_webpage(
      ProxyPickleFile='c:\\newfilepath\\myproxiefile\\proxyn.pkl',
      DomainName="pydata.org",
      DomainLink="https://pydata.org/",
      SaveFolder=r"f:\pandashomepagetest",
      ProxyConfidenceLimit=10,
      UrlsAtOnce=100,
      ThreadLimit=50,
      RequestsTimeout=10,
      ThreadTimeout=12,
      SleepAfterKillThread=0.1,
      SleepAfterStartThread=0.1,
      IgnoreExceptions=True,
      proxy_http_check_timeout=4,
      proxy_threads_httpcheck=65,
      proxy_threads_ping=100,
      proxy_silent=False,
      proxy_max_proxies_to_check=1000,
      starturls=starturls,
  )
```

## Downloading a whole page

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/site2hdd/site2hdd00000007.png" alt="">

```python
# Command line also works, but you can't use starturls, and the proxy.pkl has to exist already! 
# Best usage is to continue a download that hasn't been finished yet. 
# Existing files won't be downloaded again! 

import subprocess
import sys

subprocess.run(
    [
        sys.executable,
        r"C:\Users\USERNAME\anaconda3\envs\ENVNAME\Lib\site-packages\site2hdd\__init__.py",
        r"C:\Users\USERNAME\anaconda3\envs\ENVNAME\pandaspyd.ini",
    ]
)

# This is how ini files should look like 

r"""
[GENERAL]
ProxyPickleFile = c:\newfilepath\myproxiefile\proxyn.pkl
ProxyConfidenceLimit = 10
UrlsAtOnce = 100
; ThreadLimit - 50% of UrlsAtOnce is a good number 
ThreadLimit = 50  
RequestsTimeout = 10 
; ThreadTimeout - Should be a little higher than RequestsTimeout
ThreadTimeout = 12 
; SleepAfterKillThread - Don't put 0.0 here
SleepAfterKillThread = 0.1 
; SleepAfterStartThread - Don't put 0.0 here
SleepAfterStartThread = 0.1 
IgnoreExceptions = True
SaveFolder = f:\pythonsite
DomainName = python.org
DomainLink = https://www.python.org/
"""
```

## Downloading a whole page using the command line

<img title="" src="https://github.com/hansalemaos/screenshots/raw/main/site2hdd/site2hdd00000009.png" alt="">
