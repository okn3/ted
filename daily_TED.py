from urllib import request
import os
import bs4


def search_url(keyword):
    """ 動画の検索
    キーワードが無い場合はランダムで検索を行う

    @params 検索キーワード
    @return 動画のURL
    """
    if keyword:
        # serch video in url
        return
    else:
        # random
        return


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


def download_script(url, language):
    """スクリプトのダウンドーロ

    @params url ダウンドーロ先のリンク
    @params langage 言語の指定
    @return 本文の文字列
    """
    script = ""
    url += "transcript?language=" + language
    html = request.urlopen(url)
    soup = bs4.BeautifulSoup(html)
    body = soup.select(".talk-transcript__fragment")
    for content in body:
        script += (content.string + "\n")
    return script

if __name__ == "__main__":

    #url = search_url()
    main_url = "https://www.ted.com/talks/dan_ariely_on_our_buggy_moral_code/"
    dl_url = "https://download.ted.com/talks/DanAriely_2009-480p.mp4?apikey=489b859150fc58263f17110eeb44ed5fba4a3b22"
    print(download_script(main_url, "en"))
  #  download_video(dl_url)
  #  download_audio(dl_url)
