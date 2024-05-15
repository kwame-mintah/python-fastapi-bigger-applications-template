from pydantic import BaseModel, Field


class Example(BaseModel):
    placeholder: str = Field(title="Example message returned")


class Message(BaseModel):
    messageId: int = Field(title="Message ID", examples=[1])
    example: Example = Field(title="Example Model inheriting another model")


class Package(BaseModel):
    version: str = Field(default="", title="Package version", examples=["0.109.0"])
