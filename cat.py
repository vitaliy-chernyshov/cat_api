from dataclasses import dataclass, field


@dataclass
class CatImage:
    url: str
    weight: int
    height: int
    breeds: list = field(default_factory=list)