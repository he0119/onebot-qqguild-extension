from typing import TYPE_CHECKING, Literal, TypedDict

from nonebot.adapters.onebot.v12 import Bot as BaseBot
from nonebot.adapters.onebot.v12 import Message

if TYPE_CHECKING:

    class SendMessageResp(TypedDict):
        message_id: str
        time: float

    class CreateDmsResp(TypedDict):
        guild_id: str
        channel_id: str
        create_time: float

    class Bot(BaseBot):
        async def send_message(
            self,
            *,
            detail_type: Literal["private", "channel"],
            guild_id: str = ...,
            channel_id: str = ...,
            message: Message,
            event_id: str = ...,
        ) -> SendMessageResp:
            """发送消息

            参数:
                detail_type: 发送的类型，可以为 private、channel，和消息事件的 detail_type 字段对应
                guild_id: 私聊临时频道 ID，当 detail_type 为 private 时必须传入
                channel_id: 子频道 ID，当 detail_type 为 channel 时必须传入
                message: 消息内容
                event_id: 事件 ID，当发送被动消息时必须传入
            """
            ...

        def create_dms(self, *, user_id: str, src_guild_id: str) -> CreateDmsResp:
            """创建私信会话

            参数:
                user_id: 用户 ID
                src_guild_id: 源频道 ID
            """
            ...

else:
    Bot = BaseBot
