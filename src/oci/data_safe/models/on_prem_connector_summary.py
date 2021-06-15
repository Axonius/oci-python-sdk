# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OnPremConnectorSummary(object):
    """
    Summary of a Data Safe on-premises connector.
    """

    #: A constant which can be used with the lifecycle_state property of a OnPremConnectorSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OnPremConnectorSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OnPremConnectorSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OnPremConnectorSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OnPremConnectorSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OnPremConnectorSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OnPremConnectorSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OnPremConnectorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OnPremConnectorSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OnPremConnectorSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OnPremConnectorSummary.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this OnPremConnectorSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this OnPremConnectorSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OnPremConnectorSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OnPremConnectorSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OnPremConnectorSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OnPremConnectorSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OnPremConnectorSummary.
        :type system_tags: dict(str, dict(str, object))

        :param created_version:
            The value to assign to the created_version property of this OnPremConnectorSummary.
        :type created_version: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'created_version': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'created_version': 'createdVersion'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._created_version = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OnPremConnectorSummary.
        The OCID of the on-premises connector.


        :return: The id of this OnPremConnectorSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OnPremConnectorSummary.
        The OCID of the on-premises connector.


        :param id: The id of this OnPremConnectorSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OnPremConnectorSummary.
        The display name of the on-premises connector.


        :return: The display_name of this OnPremConnectorSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OnPremConnectorSummary.
        The display name of the on-premises connector.


        :param display_name: The display_name of this OnPremConnectorSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OnPremConnectorSummary.
        The OCID of the compartment that contains the on-premises connector.


        :return: The compartment_id of this OnPremConnectorSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OnPremConnectorSummary.
        The OCID of the compartment that contains the on-premises connector.


        :param compartment_id: The compartment_id of this OnPremConnectorSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this OnPremConnectorSummary.
        The description of the on-premises connector.


        :return: The description of this OnPremConnectorSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OnPremConnectorSummary.
        The description of the on-premises connector.


        :param description: The description of this OnPremConnectorSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this OnPremConnectorSummary.
        The date and time the on-premises connector was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this OnPremConnectorSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OnPremConnectorSummary.
        The date and time the on-premises connector was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this OnPremConnectorSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OnPremConnectorSummary.
        The current state of the on-premises connector.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OnPremConnectorSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OnPremConnectorSummary.
        The current state of the on-premises connector.


        :param lifecycle_state: The lifecycle_state of this OnPremConnectorSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this OnPremConnectorSummary.
        Details about the current state of the on-premises connector.


        :return: The lifecycle_details of this OnPremConnectorSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OnPremConnectorSummary.
        Details about the current state of the on-premises connector.


        :param lifecycle_details: The lifecycle_details of this OnPremConnectorSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OnPremConnectorSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this OnPremConnectorSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OnPremConnectorSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this OnPremConnectorSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OnPremConnectorSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this OnPremConnectorSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OnPremConnectorSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this OnPremConnectorSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OnPremConnectorSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OnPremConnectorSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OnPremConnectorSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OnPremConnectorSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def created_version(self):
        """
        Gets the created_version of this OnPremConnectorSummary.
        Created version of the on-premises connector.


        :return: The created_version of this OnPremConnectorSummary.
        :rtype: str
        """
        return self._created_version

    @created_version.setter
    def created_version(self, created_version):
        """
        Sets the created_version of this OnPremConnectorSummary.
        Created version of the on-premises connector.


        :param created_version: The created_version of this OnPremConnectorSummary.
        :type: str
        """
        self._created_version = created_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
