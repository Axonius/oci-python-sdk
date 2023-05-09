# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DisasterRecoveryConfiguration(object):
    """
    Configurations of a Disaster Recovery.
    """

    #: A constant which can be used with the disaster_recovery_type property of a DisasterRecoveryConfiguration.
    #: This constant has a value of "ADG"
    DISASTER_RECOVERY_TYPE_ADG = "ADG"

    #: A constant which can be used with the disaster_recovery_type property of a DisasterRecoveryConfiguration.
    #: This constant has a value of "BACKUP_BASED"
    DISASTER_RECOVERY_TYPE_BACKUP_BASED = "BACKUP_BASED"

    def __init__(self, **kwargs):
        """
        Initializes a new DisasterRecoveryConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param disaster_recovery_type:
            The value to assign to the disaster_recovery_type property of this DisasterRecoveryConfiguration.
            Allowed values for this property are: "ADG", "BACKUP_BASED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type disaster_recovery_type: str

        :param time_snapshot_standby_enabled_till:
            The value to assign to the time_snapshot_standby_enabled_till property of this DisasterRecoveryConfiguration.
        :type time_snapshot_standby_enabled_till: datetime

        :param is_snapshot_standby:
            The value to assign to the is_snapshot_standby property of this DisasterRecoveryConfiguration.
        :type is_snapshot_standby: bool

        """
        self.swagger_types = {
            'disaster_recovery_type': 'str',
            'time_snapshot_standby_enabled_till': 'datetime',
            'is_snapshot_standby': 'bool'
        }

        self.attribute_map = {
            'disaster_recovery_type': 'disasterRecoveryType',
            'time_snapshot_standby_enabled_till': 'timeSnapshotStandbyEnabledTill',
            'is_snapshot_standby': 'isSnapshotStandby'
        }

        self._disaster_recovery_type = None
        self._time_snapshot_standby_enabled_till = None
        self._is_snapshot_standby = None

    @property
    def disaster_recovery_type(self):
        """
        Gets the disaster_recovery_type of this DisasterRecoveryConfiguration.
        Indicates the disaster recovery (DR) type of the Shared Autonomous Database.
        Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover.
        Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.

        Allowed values for this property are: "ADG", "BACKUP_BASED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The disaster_recovery_type of this DisasterRecoveryConfiguration.
        :rtype: str
        """
        return self._disaster_recovery_type

    @disaster_recovery_type.setter
    def disaster_recovery_type(self, disaster_recovery_type):
        """
        Sets the disaster_recovery_type of this DisasterRecoveryConfiguration.
        Indicates the disaster recovery (DR) type of the Shared Autonomous Database.
        Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover.
        Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.


        :param disaster_recovery_type: The disaster_recovery_type of this DisasterRecoveryConfiguration.
        :type: str
        """
        allowed_values = ["ADG", "BACKUP_BASED"]
        if not value_allowed_none_or_none_sentinel(disaster_recovery_type, allowed_values):
            disaster_recovery_type = 'UNKNOWN_ENUM_VALUE'
        self._disaster_recovery_type = disaster_recovery_type

    @property
    def time_snapshot_standby_enabled_till(self):
        """
        Gets the time_snapshot_standby_enabled_till of this DisasterRecoveryConfiguration.
        Time and date stored as an RFC 3339 formatted timestamp string. For example, 2022-01-01T12:00:00.000Z would set a limit for the snapshot standby to be converted back to a cross-region standby database.


        :return: The time_snapshot_standby_enabled_till of this DisasterRecoveryConfiguration.
        :rtype: datetime
        """
        return self._time_snapshot_standby_enabled_till

    @time_snapshot_standby_enabled_till.setter
    def time_snapshot_standby_enabled_till(self, time_snapshot_standby_enabled_till):
        """
        Sets the time_snapshot_standby_enabled_till of this DisasterRecoveryConfiguration.
        Time and date stored as an RFC 3339 formatted timestamp string. For example, 2022-01-01T12:00:00.000Z would set a limit for the snapshot standby to be converted back to a cross-region standby database.


        :param time_snapshot_standby_enabled_till: The time_snapshot_standby_enabled_till of this DisasterRecoveryConfiguration.
        :type: datetime
        """
        self._time_snapshot_standby_enabled_till = time_snapshot_standby_enabled_till

    @property
    def is_snapshot_standby(self):
        """
        Gets the is_snapshot_standby of this DisasterRecoveryConfiguration.
        Indicates if user wants to convert to a snapshot standby. For example, true would set a standby database to snapshot standby database. False would set a snapshot standby database back to regular standby database.


        :return: The is_snapshot_standby of this DisasterRecoveryConfiguration.
        :rtype: bool
        """
        return self._is_snapshot_standby

    @is_snapshot_standby.setter
    def is_snapshot_standby(self, is_snapshot_standby):
        """
        Sets the is_snapshot_standby of this DisasterRecoveryConfiguration.
        Indicates if user wants to convert to a snapshot standby. For example, true would set a standby database to snapshot standby database. False would set a snapshot standby database back to regular standby database.


        :param is_snapshot_standby: The is_snapshot_standby of this DisasterRecoveryConfiguration.
        :type: bool
        """
        self._is_snapshot_standby = is_snapshot_standby

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
