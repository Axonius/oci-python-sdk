# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateExternalExadataStorageConnectorDetails(object):
    """
    The connector details of the storage server to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateExternalExadataStorageConnectorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connector_name:
            The value to assign to the connector_name property of this UpdateExternalExadataStorageConnectorDetails.
        :type connector_name: str

        :param connection_uri:
            The value to assign to the connection_uri property of this UpdateExternalExadataStorageConnectorDetails.
        :type connection_uri: str

        :param credential_info:
            The value to assign to the credential_info property of this UpdateExternalExadataStorageConnectorDetails.
        :type credential_info: oci.database_management.models.RestCredential

        """
        self.swagger_types = {
            'connector_name': 'str',
            'connection_uri': 'str',
            'credential_info': 'RestCredential'
        }

        self.attribute_map = {
            'connector_name': 'connectorName',
            'connection_uri': 'connectionUri',
            'credential_info': 'credentialInfo'
        }

        self._connector_name = None
        self._connection_uri = None
        self._credential_info = None

    @property
    def connector_name(self):
        """
        Gets the connector_name of this UpdateExternalExadataStorageConnectorDetails.
        The connector name if OCI connector is created.


        :return: The connector_name of this UpdateExternalExadataStorageConnectorDetails.
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """
        Sets the connector_name of this UpdateExternalExadataStorageConnectorDetails.
        The connector name if OCI connector is created.


        :param connector_name: The connector_name of this UpdateExternalExadataStorageConnectorDetails.
        :type: str
        """
        self._connector_name = connector_name

    @property
    def connection_uri(self):
        """
        Gets the connection_uri of this UpdateExternalExadataStorageConnectorDetails.
        The unique connection string of the connection. For example, \"https://slcm21celadm02.us.oracle.com:443/MS/RESTService/\".


        :return: The connection_uri of this UpdateExternalExadataStorageConnectorDetails.
        :rtype: str
        """
        return self._connection_uri

    @connection_uri.setter
    def connection_uri(self, connection_uri):
        """
        Sets the connection_uri of this UpdateExternalExadataStorageConnectorDetails.
        The unique connection string of the connection. For example, \"https://slcm21celadm02.us.oracle.com:443/MS/RESTService/\".


        :param connection_uri: The connection_uri of this UpdateExternalExadataStorageConnectorDetails.
        :type: str
        """
        self._connection_uri = connection_uri

    @property
    def credential_info(self):
        """
        Gets the credential_info of this UpdateExternalExadataStorageConnectorDetails.

        :return: The credential_info of this UpdateExternalExadataStorageConnectorDetails.
        :rtype: oci.database_management.models.RestCredential
        """
        return self._credential_info

    @credential_info.setter
    def credential_info(self, credential_info):
        """
        Sets the credential_info of this UpdateExternalExadataStorageConnectorDetails.

        :param credential_info: The credential_info of this UpdateExternalExadataStorageConnectorDetails.
        :type: oci.database_management.models.RestCredential
        """
        self._credential_info = credential_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other