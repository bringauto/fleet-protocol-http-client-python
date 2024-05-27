# coding: utf-8

"""
    Fleet v2 HTTP API

    HTTP-based API for Fleet Protocol v2 serving for communication between the External Server and the end users.

    The version of the OpenAPI document: 2.4.0
    Contact: jiri.strouhal@bringauto.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from fleet_http_client_python.models.device_id import DeviceId
from fleet_http_client_python.models.payload import Payload
from typing import Optional, Set
from typing_extensions import Self

class Message(BaseModel):
    """
    Physical device or program located on the car.
    """ # noqa: E501
    timestamp: Optional[StrictInt] = Field(default=None, description="Unix timestamp of the message in milliseconds.")
    device_id: DeviceId
    payload: Payload
    __properties: ClassVar[List[str]] = ["timestamp", "device_id", "payload"]

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
        """Create an instance of Message from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of device_id
        if self.device_id:
            _dict['device_id'] = self.device_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payload
        if self.payload:
            _dict['payload'] = self.payload.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Message from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timestamp": obj.get("timestamp"),
            "device_id": DeviceId.from_dict(obj["device_id"]) if obj.get("device_id") is not None else None,
            "payload": Payload.from_dict(obj["payload"]) if obj.get("payload") is not None else None
        })
        return _obj


