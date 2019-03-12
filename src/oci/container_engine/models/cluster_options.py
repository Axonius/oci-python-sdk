# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClusterOptions(object):
    """
    Options for creating or updating clusters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClusterOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kubernetes_versions:
            The value to assign to the kubernetes_versions property of this ClusterOptions.
        :type kubernetes_versions: list[str]

        """
        self.swagger_types = {
            'kubernetes_versions': 'list[str]'
        }

        self.attribute_map = {
            'kubernetes_versions': 'kubernetesVersions'
        }

        self._kubernetes_versions = None

    @property
    def kubernetes_versions(self):
        """
        Gets the kubernetes_versions of this ClusterOptions.
        Available Kubernetes versions.


        :return: The kubernetes_versions of this ClusterOptions.
        :rtype: list[str]
        """
        return self._kubernetes_versions

    @kubernetes_versions.setter
    def kubernetes_versions(self, kubernetes_versions):
        """
        Sets the kubernetes_versions of this ClusterOptions.
        Available Kubernetes versions.


        :param kubernetes_versions: The kubernetes_versions of this ClusterOptions.
        :type: list[str]
        """
        self._kubernetes_versions = kubernetes_versions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other