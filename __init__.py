import asyncio
import os
import sys
from configparser import ConfigParser
from urllib import parse
from cprinter import TC
import pandas as pd
import regex
import requests
from kthread_sleep import sleep
import threadingbatch
import random
from a_pandas_ex_horizontal_explode import pd_add_horizontal_explode
from tolerant_isinstance import isinstance_tolerant
from touchtouch import touch
from freeproxydownloader import get_proxies

pd_add_horizontal_explode()
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions

pd_add_apply_ignore_exceptions()
from url_analyzer import get_all_links_from_url, get_url_df, get_all_links_from_html

import numba, windows_filepath, openpyxl, check_if_nan, flatten_any_dict_iterable_or_whatsoever, keyboard, flatten_everything, bs4

site2hddvars = sys.modules[__name__]
site2hddvars.all_dataframes = []

@threadingbatch.thread_capture
def get_url(
    url,
    timeout,
    header,
    howtoconnect,
    proxyDict,
    address,
    header2,
    howtoconnect2,
    proxyDict2,
    address2,
    modus,
    *args,
    **kwargs,
):
    def _get_js_pages(aa_downloadlink, aa_fake_header, aa_timeout, aa_proxyDict):
        return None
        # js rendering - not working yet
        # from requests_html import HTMLSession
        # response = None
        # with HTMLSession() as session:
        #     try:
        #         response = session.get(
        #             url=aa_downloadlink,
        #             headers=aa_fake_header,
        #             timeout=aa_timeout,
        #             proxies=aa_proxyDict,
        #         )
        #         try:
        #             response.html.render()
        #         except Exception as fazx:
        #             print(fazx)
        #     except Exception as Fehler:
        #         print(Fehler)
        # return response

    requestlink1 = regex.sub(
        "^https?://",
        howtoconnect + "://",
        url,
        flags=regex.I,
    )
    try:
        if modus == 0:
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError as e:
                if str(e).startswith("There is no current event loop in thread"):
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                else:
                    pass
            resp = _get_js_pages(
                aa_downloadlink=requestlink1,
                aa_fake_header=header,
                aa_timeout=timeout,
                aa_proxyDict=proxyDict,
            )
        else:
            with requests.get(
                url=requestlink1, timeout=timeout, headers=header, proxies=proxyDict
            ) as response:
                resp = response

        try1 = {
            "aa_response": resp,
            "aa_proxyDict": proxyDict,
            "aa_fake_header": header,
            "aa_downloadlink": requestlink1,
            "aa_timeout": timeout,
            "aa_address": address,
            "aa_downloadlink_original": url,
        }
        try:
            if resp.status_code == 200:
                print(TC(str(resp) + " - " + requestlink1).bg_black.fg_green)
            else:
                print(TC(str(resp) + " - " + requestlink1).bg_black.fg_yellow)
        except Exception as fe:
            pass

    except Exception as fe:
        print(TC(str(fe) + " - " + requestlink1).bg_black.fg_red)
        try1 = {
            "aa_response": None,
            "aa_proxyDict": proxyDict,
            "aa_fake_header": header,
            "aa_downloadlink": requestlink1,
            "aa_timeout": timeout,
            "aa_address": address,
            "aa_downloadlink_original": url,
        }

    requestlink2 = regex.sub(
        "^https?://",
        howtoconnect2 + "://",
        url,
        flags=regex.I,
    )

    try:
        if modus == 0:
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError as e:
                if str(e).startswith("There is no current event loop in thread"):
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                else:
                    pass
            resp2 = _get_js_pages(
                aa_downloadlink=requestlink1,
                aa_fake_header=header,
                aa_timeout=timeout,
                aa_proxyDict=proxyDict,
            )
        else:
            with requests.get(
                url=requestlink2, timeout=timeout, headers=header2, proxies=proxyDict2
            ) as response:
                resp2 = response

        try2 = {
            "aa_response2": resp2,
            "aa_proxyDict2": proxyDict2,
            "aa_fake_header2": header2,
            "aa_downloadlink2": requestlink2,
            "aa_timeout2": timeout,
            "aa_address2": address2,
            "aa_downloadlink_original2": url,
        }
        try:
            if resp.status_code == 200:
                print(TC(str(resp2) + " - " + requestlink2).bg_black.fg_green)
            else:
                print(TC(str(resp2) + " - " + requestlink2).bg_black.fg_yellow)
        except Exception as fe:
            pass

    except Exception as fe:
        print(TC(str(fe) + " - " + requestlink2).bg_black.fg_red)

        try2 = {
            "aa_response2": None,
            "aa_proxyDict2": proxyDict2,
            "aa_fake_header2": header2,
            "aa_downloadlink2": requestlink2,
            "aa_timeout2": timeout,
            "aa_address2": address2,
            "aa_downloadlink_original2": url,
        }

    return list(try1.items()), list(try2.items())


def fetch_urls(domain, link):

    df3 = get_all_links_from_url(link)

    df3 = df3.loc[df3.aa_domain_w_tl.str.lower() == domain].reset_index(drop=True)
    return df3


def double_download_links_from_list(
    dfproxy,
    urls,
    threadtlimit=100,
    timeout_requests=5,
    timeout=12,
    sleepafterkill=0.02,
    sleepafterstart=0.02,
    ignore_exceptions=False,
    verbose=False,
    modus=1,
    save_as_tmp_dataframe=False
):
    flist = []
    urls = list(set(urls))
    for ini, k in enumerate(urls):  # creating 20 function calls
        randomch = dfproxy.sample(2, weights=dfproxy.aa_weights)
        header = randomch.aa_fake_header.iloc[0]
        howtoconnect = randomch.aa_howtoconnect.iloc[0]
        proxyDict = randomch.aa_proxyDict.iloc[0]
        address = randomch.aa_address.iloc[0]
        header2 = randomch.aa_fake_header.iloc[1]
        howtoconnect2 = randomch.aa_howtoconnect.iloc[1]
        proxyDict2 = randomch.aa_proxyDict.iloc[1]
        address2 = randomch.aa_address.iloc[1]

        flist.append(
            [
                get_url,  # function
                (),  # args
                {
                    "url": k,
                    "timeout": timeout_requests,
                    "header": header,
                    "howtoconnect": howtoconnect,
                    "proxyDict": proxyDict,
                    "address": address,
                    "header2": header2,
                    "howtoconnect2": howtoconnect2,
                    "proxyDict2": proxyDict2,
                    "address2": address2,
                    "modus": modus,
                },  # kwargs
                f"{k}",  # key in threadingbatch.results (must be unique and type str), the key can't have the name "done"
            ]
        )

    flistt = threadingbatch.start_all_threads(
        flist,
        threadtlimit=threadtlimit,
        timeout=timeout,
        sleepafterkill=sleepafterkill,
        sleepafterstart=sleepafterstart,
        ignore_exceptions=ignore_exceptions,
        verbose=verbose,
    )
    #
    while not threadingbatch.results[
        "done"
    ]:  # when all threads are done, threadingbatch.results['done'] changes to True
        sleep(0.1)
    print(TC("Batch done - writing files to HDD ...").bg_black.fg_lightcyan)
    df = pd.DataFrame(threadingbatch.results).T.drop("done").dropna()
    df["url"] = df.index.__array__().copy()
    df = df.reset_index(drop=True)
    exploded = df.results.ds_horizontal_explode()
    firstresults = exploded["0_0"].ds_horizontal_explode()
    secondresults = exploded["0_1"].ds_horizontal_explode()
    secondresults = secondresults.drop(columns=[0])
    firstresults = firstresults.drop(columns=[0])
    secondresults = secondresults.apply(
        lambda x: [x[col][1] for col in secondresults.columns],
        axis=1,
        result_type="expand",
    )
    firstresults = firstresults.apply(
        lambda x: [x[col][1] for col in firstresults.columns],
        axis=1,
        result_type="expand",
    )
    secondresults.columns = [
        "aa_response",
        "aa_proxyDict",
        "aa_fake_header",
        "aa_downloadlink",
        "aa_timeout",
        "aa_address",
        "aa_downloadlink_original",
    ]

    firstresults.columns = [
        "aa_response",
        "aa_proxyDict",
        "aa_fake_header",
        "aa_downloadlink",
        "aa_timeout",
        "aa_address",
        "aa_downloadlink_original",
    ]
    df = pd.concat([firstresults, secondresults], ignore_index=True).copy()
    df["aa_size_of_response"] = df.aa_response.ds_apply_ignore(
        -1, lambda x: sys.getsizeof(x.content)
    )
    df["aa_success"] = df.aa_response.ds_apply_ignore(
        False, lambda x: True if x.status_code == 200 else False
    )
    if save_as_tmp_dataframe:
        site2hddvars.all_dataframes.append(df.copy())
    return df


def uri_validator(x):
    try:
        result = parse.urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False


def download_all_urls(
    proxypickl,
    stilltodownload,
    urlsatonce,
    domainname,
    domainlink,
    threadtlimit,
    timeout_requests,
    timeout,
    sleepafterkill,
    sleepafterstart,
    ignore_exceptions,
    verbose,
    conf,
    savefolder,
    alreadydownloaded,
    modus,
    save_config_on_hdd=True,
save_as_tmp_dataframe=False
):
    dfx = pd.read_pickle(proxypickl)
    if isinstance_tolerant(stilltodownload, str):
        if os.path.exists(stilltodownload):
            with open(stilltodownload, mode="r", encoding="utf-8") as f:
                urls = [x.strip() for x in f.readlines()]
    else:
        if isinstance_tolerant(stilltodownload, str):
            urls = [stilltodownload]
        else:
            urls = stilltodownload.copy()
    random.shuffle(urls)
    if save_config_on_hdd:
        urls = urls[:urlsatonce]
    if not any(urls):
        if save_config_on_hdd:
            dfurls = fetch_urls(domain=domainname, link=domainlink)
            urls = dfurls.drop_duplicates().aa_url_noquery.to_list()

    df = double_download_links_from_list(
        dfproxy=dfx,
        urls=urls,
        threadtlimit=threadtlimit,
        timeout_requests=timeout_requests,
        timeout=timeout,
        sleepafterkill=sleepafterkill,
        sleepafterstart=sleepafterstart,
        ignore_exceptions=ignore_exceptions,
        verbose=verbose,
        modus=modus, save_as_tmp_dataframe=save_as_tmp_dataframe
    )
    goodresults = []
    for name, group in df.groupby("aa_downloadlink_original"):
        vac = group.aa_success.value_counts()
        if True in vac.index:
            if (vac[True]) == 2:
                if (
                    abs(
                        group.aa_size_of_response.iloc[0]
                        - group.aa_size_of_response.iloc[1]
                    )
                    <= group.aa_size_of_response.iloc[0] // 100
                ):
                    goodresults.append(group.copy())

    dfgood = pd.concat(goodresults)
    dfx.loc[dfx.aa_address.isin(dfgood.aa_address), "aa_weights"] += 1

    dfnotasgood = df.loc[dfgood.index.symmetric_difference(df.index)]

    confp = dfx.loc[
        dfx.aa_address.isin(dfnotasgood.aa_address) & (dfx.aa_weights >= conf)
    ].aa_address
    dfx.to_pickle(proxypickl)
    accept = dfnotasgood.loc[dfnotasgood.aa_address.isin(confp)].copy()
    accept = accept.dropna(subset="aa_response").copy()
    dfgood = pd.concat([dfgood, accept]).copy()

    dfgood = dfgood.drop_duplicates(subset="aa_downloadlink_original")
    dfhddgood = get_url_df(dfgood.aa_downloadlink_original.drop_duplicates().to_list())
    dffileconfig = dfhddgood[
        ["aa_url_noquery", "aa_folder_on_hdd", "aa_filetype"]
    ].copy()
    dffileconfig.loc[
        dffileconfig.aa_filetype.str.contains(r"^\s*$"), "aa_folder_on_hdd"
    ] = (
        dffileconfig.loc[
            dffileconfig.aa_filetype.str.contains(r"^\s*$", na=False, regex=True)
        ]
        .aa_folder_on_hdd.apply(
            lambda x: os.path.normpath(os.path.join(x, "index.html"))
        )
        .__array__()
        .copy()
    )
    dfsave = pd.merge(
        dfgood,
        dffileconfig,
        left_on="aa_downloadlink_original",
        right_on="aa_url_noquery",
    ).copy()

    for key, item in dfsave.iterrows():
        try:
            cont = item.aa_response.content
            savep = os.path.join(savefolder, item.aa_folder_on_hdd)
            touch(savep)
            sleep(0.001)
            with open(savep, mode="wb") as f:
                f.write(cont)
        except Exception as fe:
            print(fe)
            continue

    if not save_config_on_hdd:
        return dfsave

    downloadedlinks = list(
        set(
            dfsave.aa_url_noquery.to_list()
            + dfsave.aa_downloadlink.to_list()
            + dfsave.aa_downloadlink_original.to_list()
        )
    )
    with open(alreadydownloaded, mode="r", encoding="utf-8") as f:
        da = [x.strip() for x in f.readlines()]

    downloadedlinks = list(set(da + downloadedlinks))
    with open(alreadydownloaded, mode="w", encoding="utf-8") as f:
        for _ in downloadedlinks:
            f.write(str(_))
            f.write("\n")

    dfgood["aa_is_text"] = dfgood.aa_response.apply(
        lambda x: "text" in (g := str(x.headers)) or "charset" in g or "utf-8" in g
    )

    newurls = dfgood.apply(
        lambda x: get_all_links_from_html(
            x["aa_downloadlink_original"], x["aa_response"].content
        ),
        axis=1,
    )
    dfnewlinks = (
        pd.concat(newurls.to_list(), ignore_index=True)
        .drop_duplicates()
        .reset_index(drop=True)
    )
    dfnewlinks = dfnewlinks.loc[
        ~(
            dfnewlinks.aa_unquoted_noquery.isin(downloadedlinks)
            | dfnewlinks.aa_url_query.isin(downloadedlinks)
            | dfnewlinks.aa_unquoted_noquery.isin(downloadedlinks)
        )
    ].reset_index(drop=True)
    try:
        dfnewlinks = dfnewlinks.loc[
            dfnewlinks.aa_fragment.str.contains(r"^\s*$")
            & (dfnewlinks.aa_domain_w_tl.str.lower() == domainname)
            & (~dfnewlinks.aa_url_noquery.isin(downloadedlinks))
        ].reset_index(drop=True)
        stilld = dfnewlinks.aa_url_noquery.to_list()
    except Exception as fe:
        print(fe)
    with open(stilltodownload, mode="r", encoding="utf-8") as f:
        urlsn = f.read()

    urlsn = urlsn.splitlines()
    stilld = [u for u in stilld if uri_validator(u)]
    stilld.extend(urlsn)
    stilld = set(stilld) - set(downloadedlinks)
    stilld = list(stilld)
    random.shuffle(stilld)
    with open(stilltodownload, mode="w", encoding="utf-8") as f:
        f.write("\n".join(stilld).strip())


def download_webpage(
    ProxyPickleFile: str,
    DomainName: str,
    DomainLink: str,
    SaveFolder=os.path.join(os.getcwd(), "__webpage"),
    ProxyConfidenceLimit: int = 10,
    UrlsAtOnce: int = 100,
    ThreadLimit: int = 50,
    RequestsTimeout: int = 10,
    ThreadTimeout: int = 12,
    SleepAfterKillThread: float = 0.1,
    SleepAfterStartThread: float = 0.1,
    IgnoreExceptions: bool = True,
    proxy_http_check_timeout: int = 10,
    proxy_threads_httpcheck: int = 20,
    proxy_threads_ping: int = 10,
    proxy_silent: bool = False,
    proxy_max_proxies_to_check: int = 1000,
    starturls=None,
):

    if not os.path.exists(ProxyPickleFile):
        print("Downloading Proxies")
        touch(ProxyPickleFile)

        xlsxfile, ProxyPickleFile = get_proxies(
            save_path_proxies_all_filtered=ProxyPickleFile,
            http_check_timeout=proxy_http_check_timeout,
            threads_httpcheck=proxy_threads_httpcheck,
            threads_ping=proxy_threads_ping,
            silent=proxy_silent,
            max_proxies_to_check=proxy_max_proxies_to_check,
        )
    di = {}
    di["GENERAL"] = {
        "ProxyPickleFile": ProxyPickleFile,
        "ProxyConfidenceLimit": ProxyConfidenceLimit,
        "UrlsAtOnce": UrlsAtOnce,
        "ThreadLimit": ThreadLimit,
        "RequestsTimeout": RequestsTimeout,
        "ThreadTimeout": ThreadTimeout,
        "SleepAfterKillThread": SleepAfterKillThread,
        "SleepAfterStartThread": SleepAfterStartThread,
        "IgnoreExceptions": str(IgnoreExceptions),
        "SaveFolder": SaveFolder,
        "DomainName": DomainName,
        "DomainLink": DomainLink,
    }
    if starturls:
        alreadydownloaded = os.path.normpath(
            os.path.join(SaveFolder, f"saveddata{os.sep}alreadydownloaded.txt")
        )
        touch(alreadydownloaded)

        stilltodownload = os.path.normpath(
            os.path.join(SaveFolder, f"saveddata{os.sep}stilltodownload.txt")
        )
        touch(stilltodownload)
        with open(stilltodownload, mode="a", encoding="utf-8") as f:
            f.write("\n".join(starturls))
    main(configfile=di, useconfigfile=False)


def main(configfile=None, useconfigfile=True):
    if len(sys.argv) < 2 and not configfile:
        return
    if useconfigfile:
        config = ConfigParser()
        if configfile is None:
            if os.path.exists(sys.argv[1]):
                configfile = sys.argv[1]
            else:
                return
        config.read(configfile, encoding="utf-8")
    else:
        config = configfile
    verbose = False
    proxypickl = os.path.normpath(str(config["GENERAL"]["ProxyPickleFile"]))
    conf = int(config["GENERAL"]["ProxyConfidenceLimit"])
    urlsatonce = int(config["GENERAL"]["UrlsAtOnce"])
    threadtlimit = int(config["GENERAL"]["ThreadLimit"])
    timeout_requests = int(config["GENERAL"]["RequestsTimeout"])
    timeout = int(config["GENERAL"]["ThreadTimeout"])
    sleepafterkill = float(config["GENERAL"]["SleepAfterKillThread"])
    sleepafterstart = float(config["GENERAL"]["SleepAfterStartThread"])
    ignore_exceptions = (
        False if len(config["GENERAL"]["IgnoreExceptions"].strip()) == 5 else True
    )
    modus = 1
    savefolder = os.path.normpath(str(config["GENERAL"]["SaveFolder"]))
    domainname = str(config["GENERAL"]["DomainName"])
    domainlink = str(config["GENERAL"]["DomainLink"])
    # dfx = pd.read_pickle(proxypickl)
    alreadydownloaded = os.path.normpath(
        os.path.join(savefolder, f"saveddata{os.sep}alreadydownloaded.txt")
    )
    touch(alreadydownloaded)

    stilltodownload = os.path.normpath(
        os.path.join(savefolder, f"saveddata{os.sep}stilltodownload.txt")
    )
    touch(stilltodownload)

    while True:
        try:
            download_all_urls(
                proxypickl,
                stilltodownload,
                urlsatonce,
                domainname,
                domainlink,
                threadtlimit,
                timeout_requests,
                timeout,
                sleepafterkill,
                sleepafterstart,
                ignore_exceptions,
                verbose,
                conf,
                savefolder,
                alreadydownloaded,
                modus,
            )
        except Exception as fe:
            print(fe)
            continue
        sleep(1)


def download_url_list(
    urls,
    ProxyPickleFile: str,
    SaveFolder=os.path.join(os.getcwd(), "__webpage"),
    try_each_url_n_times: int = 5,
    ProxyConfidenceLimit: int = 10,
    ThreadLimit: int = 50,
    RequestsTimeout: int = 10,
    ThreadTimeout: int = 12,
    SleepAfterKillThread: float = 0.1,
    SleepAfterStartThread: float = 0.1,
    IgnoreExceptions: bool = True,
save_as_tmp_dataframe:bool=False
):

    counter_ = 0
    while counter_ < try_each_url_n_times and any(urls):
        try:
            df = download_all_urls(
                proxypickl=ProxyPickleFile,
                stilltodownload=urls,
                urlsatonce=len(urls),
                domainname="XXXXAACCBBS.com",
                domainlink="https://XXXXAACCBBS.com",
                threadtlimit=ThreadLimit,
                timeout_requests=RequestsTimeout,
                timeout=ThreadTimeout,
                sleepafterkill=SleepAfterKillThread,
                sleepafterstart=SleepAfterStartThread,
                ignore_exceptions=IgnoreExceptions,
                verbose=False,
                conf=ProxyConfidenceLimit,
                savefolder=SaveFolder,
                alreadydownloaded="",
                modus=1,
                save_config_on_hdd=False, save_as_tmp_dataframe=save_as_tmp_dataframe
            )
            urls = [_ for _ in urls if not _ in df.aa_downloadlink_original.to_list()]
        except Exception as fe:
            print(fe)
        finally:
            counter_ += 1


if __name__ == "__main__":
    main()
