from dataclasses import dataclass


@dataclass
class Vulnerability:
    id: int | None = None
    title: str = ""
    description: str = ""
