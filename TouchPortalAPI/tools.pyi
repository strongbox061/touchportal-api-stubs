from types import SimpleNamespace
from typing import Any, Literal

class Tools:
    @staticmethod
    def convertImage_to_base64(
        image: str,
        type: Literal["Auto", "Web", "Local"] = ...,
        image_formats: list[str] = ...,
    ) -> str: ...
    @staticmethod
    def updateCheck(name: str, repository: str) -> str: ...
    @staticmethod
    def nested_conversion(value: Any) -> Any | SimpleNamespace: ...
