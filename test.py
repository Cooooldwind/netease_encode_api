from netease_encode_api import EncodeSession
es = EncodeSession()
# 加密获取歌曲下载链接
url = "https://music.163.com/weapi/song/enhance/player/url/v1"
data = {"ids":"[1462389992]",
        "level":"exhigh",
        "encodeType":"mp3"}
responses = es.encoded_post(url, data)
download_url = responses["data"][0]["url"]
download_responses = es.get(download_url)
with open(test.mp3, "wb") as f: f.write(download_responses.content)