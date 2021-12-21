# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Country(object):
    """
    Country details model
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Country object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param country_id:
            The value to assign to the country_id property of this Country.
        :type country_id: float

        :param country_code:
            The value to assign to the country_code property of this Country.
        :type country_code: str

        :param country_name:
            The value to assign to the country_name property of this Country.
        :type country_name: str

        :param language_id:
            The value to assign to the language_id property of this Country.
        :type language_id: float

        :param ascii3_country_code:
            The value to assign to the ascii3_country_code property of this Country.
        :type ascii3_country_code: str

        """
        self.swagger_types = {
            'country_id': 'float',
            'country_code': 'str',
            'country_name': 'str',
            'language_id': 'float',
            'ascii3_country_code': 'str'
        }

        self.attribute_map = {
            'country_id': 'countryId',
            'country_code': 'countryCode',
            'country_name': 'countryName',
            'language_id': 'languageId',
            'ascii3_country_code': 'ascii3CountryCode'
        }

        self._country_id = None
        self._country_code = None
        self._country_name = None
        self._language_id = None
        self._ascii3_country_code = None

    @property
    def country_id(self):
        """
        Gets the country_id of this Country.
        Indentifier of the country. This is a DB side unique id which was generated when the entity was created in the table


        :return: The country_id of this Country.
        :rtype: float
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """
        Sets the country_id of this Country.
        Indentifier of the country. This is a DB side unique id which was generated when the entity was created in the table


        :param country_id: The country_id of this Country.
        :type: float
        """
        self._country_id = country_id

    @property
    def country_code(self):
        """
        Gets the country_code of this Country.
        Country code in ISO-3166-1 2-letter format


        :return: The country_code of this Country.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this Country.
        Country code in ISO-3166-1 2-letter format


        :param country_code: The country_code of this Country.
        :type: str
        """
        self._country_code = country_code

    @property
    def country_name(self):
        """
        Gets the country_name of this Country.
        Name of the country


        :return: The country_name of this Country.
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """
        Sets the country_name of this Country.
        Name of the country


        :param country_name: The country_name of this Country.
        :type: str
        """
        self._country_name = country_name

    @property
    def language_id(self):
        """
        Gets the language_id of this Country.
        Language identifier


        :return: The language_id of this Country.
        :rtype: float
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id):
        """
        Sets the language_id of this Country.
        Language identifier


        :param language_id: The language_id of this Country.
        :type: float
        """
        self._language_id = language_id

    @property
    def ascii3_country_code(self):
        """
        Gets the ascii3_country_code of this Country.
        Country code in ISO-3166-1 3-letter format


        :return: The ascii3_country_code of this Country.
        :rtype: str
        """
        return self._ascii3_country_code

    @ascii3_country_code.setter
    def ascii3_country_code(self, ascii3_country_code):
        """
        Sets the ascii3_country_code of this Country.
        Country code in ISO-3166-1 3-letter format


        :param ascii3_country_code: The ascii3_country_code of this Country.
        :type: str
        """
        self._ascii3_country_code = ascii3_country_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other