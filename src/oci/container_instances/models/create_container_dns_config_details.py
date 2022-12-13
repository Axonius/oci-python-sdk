# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerDnsConfigDetails(object):
    """
    Allow customers to define DNS settings for containers. If this is not provided, the containers will use
    the default DNS settings of the subnet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerDnsConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param nameservers:
            The value to assign to the nameservers property of this CreateContainerDnsConfigDetails.
        :type nameservers: list[str]

        :param searches:
            The value to assign to the searches property of this CreateContainerDnsConfigDetails.
        :type searches: list[str]

        :param options:
            The value to assign to the options property of this CreateContainerDnsConfigDetails.
        :type options: list[str]

        """
        self.swagger_types = {
            'nameservers': 'list[str]',
            'searches': 'list[str]',
            'options': 'list[str]'
        }

        self.attribute_map = {
            'nameservers': 'nameservers',
            'searches': 'searches',
            'options': 'options'
        }

        self._nameservers = None
        self._searches = None
        self._options = None

    @property
    def nameservers(self):
        """
        Gets the nameservers of this CreateContainerDnsConfigDetails.
        IP address of a name server that the resolver should query, either an IPv4 address
        (in dot notation), or an IPv6 address in colon (and possibly dot) notation. If null, we will use
        nameservers from subnet dhcpDnsOptions.


        :return: The nameservers of this CreateContainerDnsConfigDetails.
        :rtype: list[str]
        """
        return self._nameservers

    @nameservers.setter
    def nameservers(self, nameservers):
        """
        Sets the nameservers of this CreateContainerDnsConfigDetails.
        IP address of a name server that the resolver should query, either an IPv4 address
        (in dot notation), or an IPv6 address in colon (and possibly dot) notation. If null, we will use
        nameservers from subnet dhcpDnsOptions.


        :param nameservers: The nameservers of this CreateContainerDnsConfigDetails.
        :type: list[str]
        """
        self._nameservers = nameservers

    @property
    def searches(self):
        """
        Gets the searches of this CreateContainerDnsConfigDetails.
        Search list for host-name lookup. If null, we will use searches from subnet dhcpDnsOptios.


        :return: The searches of this CreateContainerDnsConfigDetails.
        :rtype: list[str]
        """
        return self._searches

    @searches.setter
    def searches(self, searches):
        """
        Sets the searches of this CreateContainerDnsConfigDetails.
        Search list for host-name lookup. If null, we will use searches from subnet dhcpDnsOptios.


        :param searches: The searches of this CreateContainerDnsConfigDetails.
        :type: list[str]
        """
        self._searches = searches

    @property
    def options(self):
        """
        Gets the options of this CreateContainerDnsConfigDetails.
        Options allows certain internal resolver variables to be modified. Options are a list of objects in
        https://man7.org/linux/man-pages/man5/resolv.conf.5.html. Examples: [\"ndots:n\", \"edns0\"]


        :return: The options of this CreateContainerDnsConfigDetails.
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this CreateContainerDnsConfigDetails.
        Options allows certain internal resolver variables to be modified. Options are a list of objects in
        https://man7.org/linux/man-pages/man5/resolv.conf.5.html. Examples: [\"ndots:n\", \"edns0\"]


        :param options: The options of this CreateContainerDnsConfigDetails.
        :type: list[str]
        """
        self._options = options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other