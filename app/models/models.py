import json

from pydantic import BaseModel, Field, field_validator


class Example(BaseModel):
    placeholder: str = Field(title="Example message returned")


class Message(BaseModel):
    messageId: int = Field(title="Message ID", examples=[1])
    example: Example = Field(title="Example Model inheriting another model")


class MessageFormData(BaseModel):
    messageId: int = Field(title="Message ID", examples=[1])
    example: Example = Field(title="Example Model inheriting another model")

    @field_validator("example", mode="before")
    @classmethod
    def validate_example_field(cls, value):
        if isinstance(value, str):
            return json.loads(value)
        return value


class Package(BaseModel):
    version: str = Field(default="", title="Package version", examples=["0.115.0"])
