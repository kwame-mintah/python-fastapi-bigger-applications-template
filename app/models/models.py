from pydantic import BaseModel, Field


class Example(BaseModel):
    placeholder: str = Field(None)


class Message(BaseModel):
    messageId: int = Field(None, title="Message ID")
    example: Example = Field(None)


class Package(BaseModel):
    version: str = Field(None, title="Package version")
