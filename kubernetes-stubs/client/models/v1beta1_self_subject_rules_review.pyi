import datetime
import typing

import kubernetes.client

class V1beta1SelfSubjectRulesReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1beta1SelfSubjectRulesReviewSpec
    status: typing.Optional[kubernetes.client.V1beta1SubjectRulesReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1beta1SelfSubjectRulesReviewSpec,
        status: typing.Optional[kubernetes.client.V1beta1SubjectRulesReviewStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1SelfSubjectRulesReviewDict: ...

class V1beta1SelfSubjectRulesReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: kubernetes.client.V1beta1SelfSubjectRulesReviewSpecDict
    status: typing.Optional[kubernetes.client.V1beta1SubjectRulesReviewStatusDict]
