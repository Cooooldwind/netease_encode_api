# 网易云 weapi 汇总

最后的更新日期：`2024/07/12`

## 歌曲

### 歌曲信息

#### URL

`https://music.163.com/weapi/v3/song/detail`

#### 请求头

```json
{
    "c": [{"id": "479223413"}]
}
```

#### 返回示例

```json
{
    "songs": [
        {
            "name": "I Like Me Better",
            "id": 479223413,
            "pst": 0,
            "t": 0,
            "ar": [
                {
                    "id": 1057226,
                    "name": "Lauv",
                    "tns": [],
                    "alias": []
                }
            ],
            "alia": [],
            "pop": 100.0,
            "st": 0,
            "rt": "None",
            "fee": 1,
            "v": 48,
            "crbt": "None",
            "cf": "",
            "al": {
                "id": 35536102,
                "name": "I Like Me Better",
                "picUrl": "https://p1.music.126.net/IfnA0aQfZVilERliWbjt_g==/109951167966295520.jpg",
                "tns": [],
                "pic_str": "109951167966295520",
                "pic": 109951167966295520
            },
            "dt": 197436,
            "h": {
                "br": 320000,
                "fid": 0,
                "size": 7900517,
                "vd": -52535.0,
                "sr": 44100
            },
            "m": {
                "br": 192000,
                "fid": 0,
                "size": 4740328,
                "vd": -49948.0,
                "sr": 44100
            },
            "l": {
                "br": 128000,
                "fid": 0,
                "size": 3160233,
                "vd": -48327.0,
                "sr": 44100
            },
            "sq": {
                "br": 884654,
                "fid": 0,
                "size": 21832898,
                "vd": -52535.0,
                "sr": 44100
            },
            "hr": "None",
            "a": "None",
            "cd": "1",
            "no": 1,
            "rtUrl": "None",
            "ftype": 0,
            "rtUrls": [],
            "djId": 0,
            "copyright": 1,
            "s_id": 0,
            "mark": 17180139520,
            "originCoverType": 1,
            "originSongSimpleData": "None",
            "tagPicList": "None",
            "resourceState": "True",
            "version": 48,
            "songJumpInfo": "None",
            "entertainmentTags": "None",
            "awardTags": "None",
            "single": 0,
            "noCopyrightRcmd": "None",
            "mv": 5620023,
            "rtype": 0,
            "rurl": "None",
            "mst": 9,
            "cp": 1416336,
            "publishTime": 1495123200000
        }
    ],
    "privileges": [
        {
            "id": 479223413,
            "fee": 1,
            "payed": 1,
            "st": 0,
            "pl": 999000,
            "dl": 999000,
            "sp": 7,
            "cp": 1,
            "subp": 1,
            "cs": "False",
            "maxbr": 999000,
            "fl": 0,
            "toast": "False",
            "flag": 260,
            "preSell": "False",
            "playMaxbr": 999000,
            "downloadMaxbr": 999000,
            "maxBrLevel": "lossless",
            "playMaxBrLevel": "lossless",
            "downloadMaxBrLevel": "lossless",
            "plLevel": "lossless",
            "dlLevel": "lossless",
            "flLevel": "none",
            "rscl": "None",
            "freeTrialPrivilege": {
                "resConsumable": "False",
                "userConsumable": "False",
                "listenType": "None",
                "cannotListenReason": "None",
                "playReason": "None"
            },
            "rightSource": 0,
            "chargeInfoList": [
                {
                    "rate": 128000,
                    "chargeUrl": "None",
                    "chargeMessage": "None",
                    "chargeType": 1
                },
                {
                    "rate": 192000,
                    "chargeUrl": "None",
                    "chargeMessage": "None",
                    "chargeType": 1
                },
                {
                    "rate": 320000,
                    "chargeUrl": "None",
                    "chargeMessage": "None",
                    "chargeType": 1
                },
                {
                    "rate": 999000,
                    "chargeUrl": "None",
                    "chargeMessage": "None",
                    "chargeType": 1
                }
            ],
            "code": 0,
            "message": "None"
        }
    ],
    "code": 200
}
```

#### 备注

1. 这是仿 **请求歌单内歌曲详细信息的请求方式** 的请求方式。需要歌曲信息在返回的字典里面的 `["songs"][0]` 里面

2. 返回示例内可能需要的内容：

    ```json
    {
        "songs": [
            {
                "name": "I Like Me Better",
                "id": 479223413,
                "ar": [
                    {
                        "id": 1057226,
                        "name": "Lauv",
                        "tns": []
                    }
                ],
                "al": {
                    "id": 35536102,
                    "name": "I Like Me Better",
                    "picUrl": "https://p1.music.126.net/IfnA0aQfZVilERliWbjt_g==/109951167966295520.jpg",
                    "tns": [],
                    "pic_str": "109951167966295520",
                    "pic": 109951167966295520
                },
                "h": {
                    "br": 320000,
                    "size": 7900517
                },
                "m": {
                    "br": 192000,
                    "size": 4740328
                },
                "l": {
                    "br": 128000,
                    "size": 3160233
                },
                "sq": {
                    "br": 884654,
                    "size": 21832898
                },
                "mv": 5620023,
                "publishTime": 1495123200000
            }
        ],
        "code": 200
    }
    ```

    1. 状态：`["code"]`；

    2. 歌曲名称：`["songs"][0]["name"]`；

    3. 歌手：`["songs"][0]["ar"]`；

    4. 专辑：`["songs"][0]["al"]["name"]`；

    5. 专辑封面：`["songs"][0]["al"]["picUrl"]`；

    6. 发行时间：`["songs"][0]["publishTime"]`，这是 **以毫秒为单位** 的时间戳；

    7. ......

3. 这是一个 **老旧的API** ，可能会失效。

### 歌词
