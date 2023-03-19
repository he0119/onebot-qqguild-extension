## `message.channel` 频道消息

=== "事件字段"

    字段名 | 数据类型 | 说明
    --- | --- | ---
    `detail_type` | string | 必须为 `channel`
    `message_id` | string | 消息唯一 ID
    `message` | message | 消息内容
    `alt_message` | string | 消息内容的替代表示, 可以为空
    `guild_id` | string | 群组 ID
    `channel_id` | string | 频道 ID
    `user_id` | string | 用户 ID
    `qqguild.author` | map[string]any | 消息创建者
    `qqguild.author` | map[string]any | 消息创建者的成员信息

=== "示例"

    ```json
    {
        "id": "b6e65187-5ac0-489c-b431-53078e9d2bbb",
        "self": {
            "platform": "qq",
            "user_id": "123234"
        },
        "time": 1632847927.599013,
        "type": "message",
        "detail_type": "channel",
        "sub_type": "",
        "message_id": "6283",
        "message": [
            {
                "type": "text",
                "data": {
                    "text": "OneBot is not a bot"
                }
            },
            {
                "type": "image",
                "data": {
                    "file_id": "e30f9684-3d54-4f65-b2da-db291a477f16"
                }
            }
        ],
        "alt_message": "OneBot is not a bot[图片]",
        "guild_id": "12345",
        "channel_id": "12",
        "user_id": "123456788",
        "qqguild.author": {
            "id": 123456788,
            "username": "uy/sun",
            "avatar": "https://qqchannel-profile-123456788.file.myqcloud.com/123456788",
            "bot": false,
            "union_openid": null,
            "union_user_account": null
        },
        "qqguild.member": {
            "user": null,
            "nick": "uy/sun",
            "roles": [4, 15],
            "joined_at": 1678111157.0
        }
    }
    ```
