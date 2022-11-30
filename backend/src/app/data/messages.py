"""
    Appellation: messages
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from datetime import datetime
from pydantic import BaseModel


class Message(BaseModel):
    message: iter
    timestamp: str = str(datetime.now())

class Status(BaseModel):
    message: str
