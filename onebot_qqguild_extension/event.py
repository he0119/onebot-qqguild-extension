from datetime import datetime
from typing import List, Optional

from nonebot.adapters.onebot.v12 import ChannelMessageEvent as BaseChannelMessageEvent
from nonebot.adapters.onebot.v12 import PrivateMessageEvent as BasePrivateMessageEvent
from pydantic import BaseModel


class User(BaseModel):
    """消息创建者"""

    id: str
    username: str
    avatar: str
    bot: bool
    union_openid: Optional[str]
    union_user_account: Optional[str]


class Member(BaseModel):
    """消息创建者的成员信息"""

    user: Optional[User]
    nick: str
    roles: List[int]
    joined_at: datetime


class PrivateMessageExtension(BaseModel):
    """私聊消息扩展"""

    guild_id: str
    src_guild_id: str
    author: User
    member: Member


class PrivateMessageEvent(BasePrivateMessageEvent):
    """私聊消息"""

    qqguild: PrivateMessageExtension


class ChannelMessageExtension(BaseModel):
    """频道消息扩展"""

    author: User
    member: Member


class ChannelMessageEvent(BaseChannelMessageEvent):
    """频道消息"""

    qqguild: ChannelMessageExtension


__all__ = [
    "PrivateMessageEvent",
    "ChannelMessageEvent",
]
