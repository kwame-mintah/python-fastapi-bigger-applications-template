from typing import List

from app.models.models import Message, Example


class DemoService:
    """
    Example class to return mock / stubbed data.
    """

    stub_data = [
        Message(
            messageId=1,
            example=Example(
                placeholder="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                "sed do eiusmod tempor incididuntut labore et dolore magna aliqua."
            ),
        )
    ]

    def return_stub_data(self) -> List[Message]:
        """
        Example data returned from an endpoint
        :return: Message
        """
        return self.stub_data

    def create_additional_stub_data(self, message: Message) -> List[Message]:
        """
        Example post request returning results from an endpoint
        :return: Message
        """
        self.stub_data.append(message)
        return self.stub_data

    def remove_stub_data(self, message_id: int) -> None:
        """
        Example delete request returning nothing back
        :param message_id:
        """
        for message in self.stub_data:
            if message.messageId == message_id:
                self.stub_data.remove(message)
