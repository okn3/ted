from urllib import request
import os


def search_url(keyword):
    """ 動画の検索
    キーワードが無い場合はランダムで検索を行う

    @params 検索キーワード
    @return 動画のURL
    """
    if keyword:
        # serch video in url
        return url
    else:
        # random
        return url


def download_video(url):
    """URLにあるvideoのダウンロード

    @params url ダウンドーロ先のリンク
    @return なし
    """
    name = "sample-name"
    request.urlretrieve(url, filename=os.path.curdir + "/videos/" + name + ".mp4")


def download_script(url, language):
    """スクリプトのダウンドーロ

    @params url ダウンドーロ先のリンク
    @params langage 言語の指定
    @return なし
    """


def download_audio(url):
    """スクリプトのダウンドーロ

    @params url ダウンドーロ先のリンク
    @return なし
    """
    url = url.replace("-480p.mp4", "mp3")
    name = "sample-name"
    request.urlretrieve(url, filename=os.path.curdir + "/audio/" + name + ".mp3")


if __name__ == "__main__":

    #url = search_url()
    url = "https://download.ted.com/talks/DanAriely_2009-480p.mp4?apikey=489b859150fc58263f17110eeb44ed5fba4a3b22"
    download_video(url)
  #  download_audio(url)
