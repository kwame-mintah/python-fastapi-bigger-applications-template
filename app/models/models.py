from pydantic import BaseModel, Field


class Example(BaseModel):
    placeholder: str = Field(None)


class Message(BaseModel):
    messageId: int = Field(title="Message ID", examples=[1])
    example: Example = Field(None)


class Package(BaseModel):
    version: str = Field(None, title="Package version", examples=["0.109.0"])
