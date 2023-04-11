# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddmDbSchemaObjectCollection(object):
    """
    Summarizes Schema Objects over specified time period
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddmDbSchemaObjectCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this AddmDbSchemaObjectCollection.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this AddmDbSchemaObjectCollection.
        :type time_interval_end: datetime

        :param database_details_items:
            The value to assign to the database_details_items property of this AddmDbSchemaObjectCollection.
        :type database_details_items: list[oci.opsi.models.DatabaseDetails]

        :param items:
            The value to assign to the items property of this AddmDbSchemaObjectCollection.
        :type items: list[oci.opsi.models.AddmDbSchemaObjectSummary]

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'database_details_items': 'list[DatabaseDetails]',
            'items': 'list[AddmDbSchemaObjectSummary]'
        }

        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'database_details_items': 'databaseDetailsItems',
            'items': 'items'
        }

        self._time_interval_start = None
        self._time_interval_end = None
        self._database_details_items = None
        self._items = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this AddmDbSchemaObjectCollection.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this AddmDbSchemaObjectCollection.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this AddmDbSchemaObjectCollection.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this AddmDbSchemaObjectCollection.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this AddmDbSchemaObjectCollection.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this AddmDbSchemaObjectCollection.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this AddmDbSchemaObjectCollection.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this AddmDbSchemaObjectCollection.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def database_details_items(self):
        """
        **[Required]** Gets the database_details_items of this AddmDbSchemaObjectCollection.
        List of database details data


        :return: The database_details_items of this AddmDbSchemaObjectCollection.
        :rtype: list[oci.opsi.models.DatabaseDetails]
        """
        return self._database_details_items

    @database_details_items.setter
    def database_details_items(self, database_details_items):
        """
        Sets the database_details_items of this AddmDbSchemaObjectCollection.
        List of database details data


        :param database_details_items: The database_details_items of this AddmDbSchemaObjectCollection.
        :type: list[oci.opsi.models.DatabaseDetails]
        """
        self._database_details_items = database_details_items

    @property
    def items(self):
        """
        **[Required]** Gets the items of this AddmDbSchemaObjectCollection.
        List of Schema Objects


        :return: The items of this AddmDbSchemaObjectCollection.
        :rtype: list[oci.opsi.models.AddmDbSchemaObjectSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this AddmDbSchemaObjectCollection.
        List of Schema Objects


        :param items: The items of this AddmDbSchemaObjectCollection.
        :type: list[oci.opsi.models.AddmDbSchemaObjectSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other