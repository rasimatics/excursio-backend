from pydantic.generics import GenericModel
from typing import Generic, TypeVar, Optional, Union


Data = TypeVar("Data")

class Response(GenericModel, Generic[Data]):
    is_success: bool
    result: Optional[Data]
    msg: Union[str, dict]