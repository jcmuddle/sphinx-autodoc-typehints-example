
from pydantic import BaseModel
from pydantic.networks import AnyHttpUrl


class Website(BaseModel):
    """Website model."""
    name: str
    url: AnyHttpUrl
