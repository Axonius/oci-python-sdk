# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerInstance(object):
    """
    A ContainerInstance for hosting Containers.

    If this ContainerInstance is DELETED, the record will remain visible for a short period
    of time before being permanently removed.
    """

    #: A constant which can be used with the lifecycle_state property of a ContainerInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ContainerInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ContainerInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ContainerInstance.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ContainerInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ContainerInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ContainerInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the container_restart_policy property of a ContainerInstance.
    #: This constant has a value of "ALWAYS"
    CONTAINER_RESTART_POLICY_ALWAYS = "ALWAYS"

    #: A constant which can be used with the container_restart_policy property of a ContainerInstance.
    #: This constant has a value of "NEVER"
    CONTAINER_RESTART_POLICY_NEVER = "NEVER"

    #: A constant which can be used with the container_restart_policy property of a ContainerInstance.
    #: This constant has a value of "ON_FAILURE"
    CONTAINER_RESTART_POLICY_ON_FAILURE = "ON_FAILURE"

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ContainerInstance.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ContainerInstance.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ContainerInstance.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ContainerInstance.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ContainerInstance.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ContainerInstance.
        :type system_tags: dict(str, dict(str, object))

        :param availability_domain:
            The value to assign to the availability_domain property of this ContainerInstance.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this ContainerInstance.
        :type fault_domain: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ContainerInstance.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ContainerInstance.
        :type lifecycle_details: str

        :param volumes:
            The value to assign to the volumes property of this ContainerInstance.
        :type volumes: list[oci.container_instances.models.ContainerVolume]

        :param volume_count:
            The value to assign to the volume_count property of this ContainerInstance.
        :type volume_count: int

        :param containers:
            The value to assign to the containers property of this ContainerInstance.
        :type containers: list[oci.container_instances.models.ContainerInstanceContainer]

        :param container_count:
            The value to assign to the container_count property of this ContainerInstance.
        :type container_count: int

        :param time_created:
            The value to assign to the time_created property of this ContainerInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ContainerInstance.
        :type time_updated: datetime

        :param shape:
            The value to assign to the shape property of this ContainerInstance.
        :type shape: str

        :param shape_config:
            The value to assign to the shape_config property of this ContainerInstance.
        :type shape_config: oci.container_instances.models.ContainerInstanceShapeConfig

        :param vnics:
            The value to assign to the vnics property of this ContainerInstance.
        :type vnics: list[oci.container_instances.models.ContainerVnic]

        :param dns_config:
            The value to assign to the dns_config property of this ContainerInstance.
        :type dns_config: oci.container_instances.models.ContainerDnsConfig

        :param graceful_shutdown_timeout_in_seconds:
            The value to assign to the graceful_shutdown_timeout_in_seconds property of this ContainerInstance.
        :type graceful_shutdown_timeout_in_seconds: int

        :param image_pull_secrets:
            The value to assign to the image_pull_secrets property of this ContainerInstance.
        :type image_pull_secrets: list[oci.container_instances.models.ImagePullSecret]

        :param container_restart_policy:
            The value to assign to the container_restart_policy property of this ContainerInstance.
            Allowed values for this property are: "ALWAYS", "NEVER", "ON_FAILURE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type container_restart_policy: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'availability_domain': 'str',
            'fault_domain': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'volumes': 'list[ContainerVolume]',
            'volume_count': 'int',
            'containers': 'list[ContainerInstanceContainer]',
            'container_count': 'int',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'shape': 'str',
            'shape_config': 'ContainerInstanceShapeConfig',
            'vnics': 'list[ContainerVnic]',
            'dns_config': 'ContainerDnsConfig',
            'graceful_shutdown_timeout_in_seconds': 'int',
            'image_pull_secrets': 'list[ImagePullSecret]',
            'container_restart_policy': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'availability_domain': 'availabilityDomain',
            'fault_domain': 'faultDomain',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'volumes': 'volumes',
            'volume_count': 'volumeCount',
            'containers': 'containers',
            'container_count': 'containerCount',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'shape': 'shape',
            'shape_config': 'shapeConfig',
            'vnics': 'vnics',
            'dns_config': 'dnsConfig',
            'graceful_shutdown_timeout_in_seconds': 'gracefulShutdownTimeoutInSeconds',
            'image_pull_secrets': 'imagePullSecrets',
            'container_restart_policy': 'containerRestartPolicy'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._availability_domain = None
        self._fault_domain = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._volumes = None
        self._volume_count = None
        self._containers = None
        self._container_count = None
        self._time_created = None
        self._time_updated = None
        self._shape = None
        self._shape_config = None
        self._vnics = None
        self._dns_config = None
        self._graceful_shutdown_timeout_in_seconds = None
        self._image_pull_secrets = None
        self._container_restart_policy = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ContainerInstance.
        Unique identifier that is immutable on creation


        :return: The id of this ContainerInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContainerInstance.
        Unique identifier that is immutable on creation


        :param id: The id of this ContainerInstance.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ContainerInstance.
        Display name for the ContainerInstance. Can be renamed.


        :return: The display_name of this ContainerInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ContainerInstance.
        Display name for the ContainerInstance. Can be renamed.


        :param display_name: The display_name of this ContainerInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ContainerInstance.
        Compartment Identifier


        :return: The compartment_id of this ContainerInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ContainerInstance.
        Compartment Identifier


        :param compartment_id: The compartment_id of this ContainerInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ContainerInstance.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ContainerInstance.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ContainerInstance.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ContainerInstance.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ContainerInstance.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ContainerInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ContainerInstance.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ContainerInstance.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ContainerInstance.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ContainerInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ContainerInstance.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ContainerInstance.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ContainerInstance.
        Availability Domain where the ContainerInstance is running.


        :return: The availability_domain of this ContainerInstance.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ContainerInstance.
        Availability Domain where the ContainerInstance is running.


        :param availability_domain: The availability_domain of this ContainerInstance.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this ContainerInstance.
        Fault Domain where the ContainerInstance is running.


        :return: The fault_domain of this ContainerInstance.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this ContainerInstance.
        Fault Domain where the ContainerInstance is running.


        :param fault_domain: The fault_domain of this ContainerInstance.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ContainerInstance.
        The current state of the ContainerInstance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ContainerInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ContainerInstance.
        The current state of the ContainerInstance.


        :param lifecycle_state: The lifecycle_state of this ContainerInstance.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ContainerInstance.
        A message describing the current state in more detail. For example, can be used to provide
        actionable information for a resource in Failed state.


        :return: The lifecycle_details of this ContainerInstance.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ContainerInstance.
        A message describing the current state in more detail. For example, can be used to provide
        actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this ContainerInstance.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def volumes(self):
        """
        Gets the volumes of this ContainerInstance.
        A Volume represents a directory with data that is accessible across multiple containers in a
        ContainerInstance.


        :return: The volumes of this ContainerInstance.
        :rtype: list[oci.container_instances.models.ContainerVolume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this ContainerInstance.
        A Volume represents a directory with data that is accessible across multiple containers in a
        ContainerInstance.


        :param volumes: The volumes of this ContainerInstance.
        :type: list[oci.container_instances.models.ContainerVolume]
        """
        self._volumes = volumes

    @property
    def volume_count(self):
        """
        Gets the volume_count of this ContainerInstance.
        The number of volumes that attached to this Instance


        :return: The volume_count of this ContainerInstance.
        :rtype: int
        """
        return self._volume_count

    @volume_count.setter
    def volume_count(self, volume_count):
        """
        Sets the volume_count of this ContainerInstance.
        The number of volumes that attached to this Instance


        :param volume_count: The volume_count of this ContainerInstance.
        :type: int
        """
        self._volume_count = volume_count

    @property
    def containers(self):
        """
        **[Required]** Gets the containers of this ContainerInstance.
        The Containers on this Instance


        :return: The containers of this ContainerInstance.
        :rtype: list[oci.container_instances.models.ContainerInstanceContainer]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """
        Sets the containers of this ContainerInstance.
        The Containers on this Instance


        :param containers: The containers of this ContainerInstance.
        :type: list[oci.container_instances.models.ContainerInstanceContainer]
        """
        self._containers = containers

    @property
    def container_count(self):
        """
        **[Required]** Gets the container_count of this ContainerInstance.
        The number of containers on this Instance


        :return: The container_count of this ContainerInstance.
        :rtype: int
        """
        return self._container_count

    @container_count.setter
    def container_count(self, container_count):
        """
        Sets the container_count of this ContainerInstance.
        The number of containers on this Instance


        :param container_count: The container_count of this ContainerInstance.
        :type: int
        """
        self._container_count = container_count

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ContainerInstance.
        The time the the ContainerInstance was created. An RFC3339 formatted datetime string


        :return: The time_created of this ContainerInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ContainerInstance.
        The time the the ContainerInstance was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this ContainerInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ContainerInstance.
        The time the ContainerInstance was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this ContainerInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ContainerInstance.
        The time the ContainerInstance was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this ContainerInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this ContainerInstance.
        The shape of the Container Instance. The shape determines the resources available to the Container Instance.


        :return: The shape of this ContainerInstance.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this ContainerInstance.
        The shape of the Container Instance. The shape determines the resources available to the Container Instance.


        :param shape: The shape of this ContainerInstance.
        :type: str
        """
        self._shape = shape

    @property
    def shape_config(self):
        """
        **[Required]** Gets the shape_config of this ContainerInstance.

        :return: The shape_config of this ContainerInstance.
        :rtype: oci.container_instances.models.ContainerInstanceShapeConfig
        """
        return self._shape_config

    @shape_config.setter
    def shape_config(self, shape_config):
        """
        Sets the shape_config of this ContainerInstance.

        :param shape_config: The shape_config of this ContainerInstance.
        :type: oci.container_instances.models.ContainerInstanceShapeConfig
        """
        self._shape_config = shape_config

    @property
    def vnics(self):
        """
        **[Required]** Gets the vnics of this ContainerInstance.
        The virtual networks available to containers running on this Container Instance.


        :return: The vnics of this ContainerInstance.
        :rtype: list[oci.container_instances.models.ContainerVnic]
        """
        return self._vnics

    @vnics.setter
    def vnics(self, vnics):
        """
        Sets the vnics of this ContainerInstance.
        The virtual networks available to containers running on this Container Instance.


        :param vnics: The vnics of this ContainerInstance.
        :type: list[oci.container_instances.models.ContainerVnic]
        """
        self._vnics = vnics

    @property
    def dns_config(self):
        """
        Gets the dns_config of this ContainerInstance.

        :return: The dns_config of this ContainerInstance.
        :rtype: oci.container_instances.models.ContainerDnsConfig
        """
        return self._dns_config

    @dns_config.setter
    def dns_config(self, dns_config):
        """
        Sets the dns_config of this ContainerInstance.

        :param dns_config: The dns_config of this ContainerInstance.
        :type: oci.container_instances.models.ContainerDnsConfig
        """
        self._dns_config = dns_config

    @property
    def graceful_shutdown_timeout_in_seconds(self):
        """
        Gets the graceful_shutdown_timeout_in_seconds of this ContainerInstance.
        Duration in seconds processes within a Container have to gracefully terminate. This applies whenever a Container must be halted, such as when the Container Instance is deleted. Processes will first be sent a termination signal. After this timeout is reached, the processes will be sent a termination signal.


        :return: The graceful_shutdown_timeout_in_seconds of this ContainerInstance.
        :rtype: int
        """
        return self._graceful_shutdown_timeout_in_seconds

    @graceful_shutdown_timeout_in_seconds.setter
    def graceful_shutdown_timeout_in_seconds(self, graceful_shutdown_timeout_in_seconds):
        """
        Sets the graceful_shutdown_timeout_in_seconds of this ContainerInstance.
        Duration in seconds processes within a Container have to gracefully terminate. This applies whenever a Container must be halted, such as when the Container Instance is deleted. Processes will first be sent a termination signal. After this timeout is reached, the processes will be sent a termination signal.


        :param graceful_shutdown_timeout_in_seconds: The graceful_shutdown_timeout_in_seconds of this ContainerInstance.
        :type: int
        """
        self._graceful_shutdown_timeout_in_seconds = graceful_shutdown_timeout_in_seconds

    @property
    def image_pull_secrets(self):
        """
        Gets the image_pull_secrets of this ContainerInstance.
        The image pull secrets for accessing private registry to pull images for containers


        :return: The image_pull_secrets of this ContainerInstance.
        :rtype: list[oci.container_instances.models.ImagePullSecret]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """
        Sets the image_pull_secrets of this ContainerInstance.
        The image pull secrets for accessing private registry to pull images for containers


        :param image_pull_secrets: The image_pull_secrets of this ContainerInstance.
        :type: list[oci.container_instances.models.ImagePullSecret]
        """
        self._image_pull_secrets = image_pull_secrets

    @property
    def container_restart_policy(self):
        """
        **[Required]** Gets the container_restart_policy of this ContainerInstance.
        The container restart policy is applied for all containers in container instance.

        Allowed values for this property are: "ALWAYS", "NEVER", "ON_FAILURE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The container_restart_policy of this ContainerInstance.
        :rtype: str
        """
        return self._container_restart_policy

    @container_restart_policy.setter
    def container_restart_policy(self, container_restart_policy):
        """
        Sets the container_restart_policy of this ContainerInstance.
        The container restart policy is applied for all containers in container instance.


        :param container_restart_policy: The container_restart_policy of this ContainerInstance.
        :type: str
        """
        allowed_values = ["ALWAYS", "NEVER", "ON_FAILURE"]
        if not value_allowed_none_or_none_sentinel(container_restart_policy, allowed_values):
            container_restart_policy = 'UNKNOWN_ENUM_VALUE'
        self._container_restart_policy = container_restart_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other