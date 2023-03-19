## `send_message` 发送消息

=== "请求参数"

    字段名 | 数据类型 | 默认值 | 说明
    --- | --- | --- | ---
    `detail_type` | string | - | 发送的类型，可以为 `private`、`channel`，和**消息事件**的 `detail_type` 字段对应
    `event_id` | string | - | 事件 ID，当发送被动消息时必须传入
    `guild_id` | string | - | 私聊临时频道 ID，当 `detail_type` 为 `private` 时必须传入
    `channel_id` | string | - | 子频道 ID，当 `detail_type` 为 `channel` 时必须传入
    `message` | message | - | 消息内容

=== "响应数据"

    字段名 | 数据类型 | 说明
    --- | --- | ---
    `message_id` | string | 消息 ID
    `time` | float64 | 消息成功发出的时间（Unix 时间戳），单位：秒

=== "请求示例"

    ```json
    {
        "action": "send_message",
        "params": {
            "detail_type": "channel",
            "event_id": "11111",
            "channel_id": "12467",
            "message": [
                {
                    "type": "text",
                    "data": {
                        "text": "我是文字巴拉巴拉巴拉"
                    }
                }
            ]
        }
    }
    ```

=== "响应示例"

    ```json
    {
        "status": "ok",
        "retcode": 0,
        "data": {
            "message_id": "2452352435",
            "time": 1632847927.599013
        },
        "message": ""
    }
    ```

## `create_dms` 创建私信会话

=== "请求参数"

    字段名 | 数据类型 | 默认值 | 说明
    --- | --- | --- | ---
    `user_id` | string | - | 用户 ID
    `src_guild_id` | string | - | 源频道 ID

=== "响应数据"

    字段名 | 数据类型 | 说明
    --- | --- | ---
    `guild_id` | string | 私信会话关联的临时频道 ID
    `channel_id` | string | 私信会话关联的子频道 ID
    `create_time` | float64 | 创建私信会话时间（Unix 时间戳），单位：秒

=== "请求示例"

    ```json
    {
        "action": "create_dms",
        "params": {
            "user_id": "11111",
            "src_guild_id": "12467",
        }
    }
    ```

=== "响应示例"

    ```json
    {
        "status": "ok",
        "retcode": 0,
        "data": {
            "guild_id": "2452352435",
            "channel_id": "233333333",
            "time": 1632847927.599013
        },
        "message": ""
    }
    ```
