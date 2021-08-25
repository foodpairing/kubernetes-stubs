import datetime
import typing

import kubernetes.client

class V1beta1APIServiceSpec:
    ca_bundle: typing.Optional[str]
    group: typing.Optional[str]
    group_priority_minimum: int
    insecure_skip_tls_verify: typing.Optional[bool]
    service: typing.Optional[kubernetes.client.ApiregistrationV1beta1ServiceReference]
    version: typing.Optional[str]
    version_priority: int
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[str] = ...,
        group: typing.Optional[str] = ...,
        group_priority_minimum: int,
        insecure_skip_tls_verify: typing.Optional[bool] = ...,
        service: typing.Optional[
            kubernetes.client.ApiregistrationV1beta1ServiceReference
        ] = ...,
        version: typing.Optional[str] = ...,
        version_priority: int
    ) -> None: ...
    def to_dict(self) -> V1beta1APIServiceSpecDict: ...

class V1beta1APIServiceSpecDict(typing.TypedDict, total=False):
    caBundle: typing.Optional[str]
    group: typing.Optional[str]
    groupPriorityMinimum: int
    insecureSkipTLSVerify: typing.Optional[bool]
    service: typing.Optional[
        kubernetes.client.ApiregistrationV1beta1ServiceReferenceDict
    ]
    version: typing.Optional[str]
    versionPriority: int
