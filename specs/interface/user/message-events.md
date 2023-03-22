## `message.private` 私聊消息

=== "事件字段"

    字段名 | 数据类型 | 说明
    --- | --- | ---
    `detail_type` | string | 必须为 `private`
    `message_id` | string | 消息唯一 ID
    `message` | message | 消息内容
    `alt_message` | string | 消息内容的替代表示, 可以为空
    `user_id` | string | 用户 ID
    `qqguild.guild_id` | string | 临时频道 ID
    `qqguild.src_guild_id` | string | 源频道 ID
    `qqguild.author` | map[string]any | 消息创建者
    `qqguild.member` | map[string]any | 消息创建者的成员信息

    对于 `user_id` 字段，如果存在匿名用户或群内系统自身发送的消息，应指定为固定值并在文档中告知用户。

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
        "detail_type": "private",
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
        "user_id": "123456788",
        "qqguild.guild_id": "2222222",
        "qqguild.src_guild_id": "33333333",
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
