from urllib import request
import requests
import os
import bs4
import random
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver


def search_url():
    """ 動画のURLを検索(6分以内)

    @return 動画のURLのリスト
    """

    talk_links = []
    url = "https://www.ted.com/talks?duration=0-6"
    for num in range(8):
        html = request.urlopen(url + "&page=" + str(num + 1))
        soup = bs4.BeautifulSoup(html, "html.parser")
        links = soup.select(".talk-link a.ga-link")
        [talk_links.append(link) for link in [link["href"] for link in links[0::2]]]
    return talk_links


def download_video(url):
    """URLにあるvideoのダウンロード

    @params url ダウンドーロ先のリンク
    @return なし
    """
    name = "sample-name"
    request.urlretrieve(url, filename=os.path.curdir + "/videos/" + name + ".mp4")


def download_audio(url):
    """スクリプトのダウンドーロ

    @params url ダウンドーロ先のリンク
    @return なし
    """
    url = url.replace("-480p.mp4", ".mp3")
    print(url)
    name = "sample-name"
    request.urlretrieve(url, filename=os.path.curdir + "/audio/" + name + ".mp3")


def get_script(url, language):
    """スクリプトのダウンドーロ

    @params url ダウンドーロ先のリンク
    @params langage 言語の指定
    @return 本文の文字列
    """
    script = ""
    url += "/transcript?language=" + language
    html = request.urlopen(url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    body = soup.select(".talk-transcript__fragment")
    for content in body:
        script += (content.string + "\n")
    return script


def get_dl_link(url):
    # proxy超えられない
    browser = webdriver.PhamtomJS("./phantomjs")
    browser.get(url)


def send_mail(to_address, url, script):
    """データをメールで送る
    """

    content = url + "\n" + script
    msg = MIMEText(content)
    msg['Subject'] = 'daily TED'
    msg['From'] = 'ted.com'
    msg['To'] = to_address
    s = smtplib.SMTP()
    s.connect()
    s.sendmail('ted.com', to_address, msg.as_string())
    s.close()


def send_line(url, script):
    """データをLINEで送る
    @params url TEDTalkのリンク
    @params script 本文
    """

    api_url = "https://notify-api.line.me/api/notify"
    title = url[26:].replace("_", " ")
    message = "\n <THEME>\n" + title + \
        " \n\n <URL>\n " + url + \
        "\n\n <SCRIPT>\n" + script
    params = {"message": message}
    token = open("linetoken.txt").read().replace('\n', '')
    header = {"Authorization": "Bearer " + token}
    r = requests.post(api_url, params=params, headers=header)
    print(r.text)


if __name__ == "__main__":

    main_url = "https://www.ted.com"
    # ページに行かないとわからない
    dl_url = "https://download.ted.com"
    apikey = "489b859150fc58263f17110eeb44ed5fba4a3b22"
    dl_link = "/talks/DanAriely_2009-480p.mp4?apikey="
    links = search_url()

    url = main_url + random.choice(links)
    print("--------------\n", url)
    script = get_script(url, "en")
    send_line(url, script)
   # send_mail("okuno.ryo.411@gmail.com", url, script) #動かない
  #  download_video(dl_url)
  #  download_audio(dl_url)
    #os.system("open " + url)
