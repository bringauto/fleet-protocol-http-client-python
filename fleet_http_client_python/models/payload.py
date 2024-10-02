# coding: utf-8

"""
    Fleet v2 HTTP API

    HTTP-based API for Fleet Protocol v2 serving for communication between the External Server and the end users.

    The version of the OpenAPI document: 2.7.0
    Contact: jiri.strouhal@bringauto.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from fleet_http_client_python.models.payload_data import PayloadData
from typing import Optional, Set
from typing_extensions import Self

class Payload(BaseModel):
    """
    Payload of the message, containing message type (status or command), encoding and data.
    """ # noqa: E501
    message_type: Annotated[str, Field(strict=True)] = Field(description="Type of the payload")
    encoding: Annotated[str, Field(strict=True)] = Field(description="Encoding of the payload")
    data: PayloadData
    __properties: ClassVar[List[str]] = ["message_type", "encoding", "data"]

    @field_validator('message_type')
    def message_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(STATUS)|(COMMAND)|(STATUS_ERROR)$", value):
            raise ValueError(r"must validate the regular expression /^(STATUS)|(COMMAND)|(STATUS_ERROR)$/")
        return value

    @field_validator('encoding')
    def encoding_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(JSON)|(BASE64)$", value):
            raise ValueError(r"must validate the regular expression /^(JSON)|(BASE64)$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Payload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Payload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message_type": obj.get("message_type"),
            "encoding": obj.get("encoding"),
            "data": PayloadData.from_dict(obj["data"]) if obj.get("data") is not None else None
        })
        return _obj


