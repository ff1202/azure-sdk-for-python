# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import EntitySearchClientConfiguration
from .operations import EntitiesOperations
from . import models


class EntitySearchClient(SDKClient):
    """The Entity Search API lets you send a search query to Bing and get back search results that include entities and places. Place results include restaurants, hotel, or other local businesses. For places, the query can specify the name of the local business or it can ask for a list (for example, restaurants near me). Entity results include persons, places, or things. Place in this context is tourist attractions, states, countries, etc.

    :ivar config: Configuration for client.
    :vartype config: EntitySearchClientConfiguration

    :ivar entities: Entities operations
    :vartype entities: azure.cognitiveservices.search.entitysearch.operations.EntitiesOperations

    :param endpoint: Supported Cognitive Services endpoints (protocol and
     hostname, for example: "https://westus.api.cognitive.microsoft.com",
     "https://api.cognitive.microsoft.com").
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        self.config = EntitySearchClientConfiguration(endpoint, credentials)
        super(EntitySearchClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.entities = EntitiesOperations(
            self._client, self.config, self._serialize, self._deserialize)
