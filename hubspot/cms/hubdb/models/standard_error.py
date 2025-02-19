# coding: utf-8

"""
    HubDB endpoints

    HubDB is a relational data store that presents data as rows, columns, and cells in a table, much like a spreadsheet. HubDB tables can be added or modified [in the HubSpot CMS](https://knowledge.hubspot.com/cos-general/how-to-edit-hubdb-tables), but you can also use the API endpoints documented here. For more information on HubDB tables and using their data on a HubSpot site, see the [CMS developers site](https://designers.hubspot.com/docs/tools/hubdb). You can also see the [documentation for dynamic pages](https://designers.hubspot.com/docs/tutorials/how-to-build-dynamic-pages-with-hubdb) for more details about the `useForPages` field.  HubDB tables support `draft` and `published` versions. This allows you to update data in the table, either for testing or to allow for a manual approval process, without affecting any live pages using the existing data. Draft data can be reviewed, and published by a user working in HubSpot or published via the API. Draft data can also be discarded, allowing users to go back to the published version of the data without disrupting it. If a table is set to be `allowed for public access`, you can access the published version of the table and rows without any authentication by specifying the portal id via the query parameter `portalId`.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.cms.hubdb.configuration import Configuration


class StandardError(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "status": "str",
        "id": "str",
        "category": "object",
        "sub_category": "object",
        "message": "str",
        "errors": "list[ErrorDetail]",
        "context": "dict[str, list[str]]",
        "links": "dict[str, str]",
    }

    attribute_map = {"status": "status", "id": "id", "category": "category", "sub_category": "subCategory", "message": "message", "errors": "errors", "context": "context", "links": "links"}

    def __init__(self, status=None, id=None, category=None, sub_category=None, message=None, errors=None, context=None, links=None, local_vars_configuration=None):  # noqa: E501
        """StandardError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._id = None
        self._category = None
        self._sub_category = None
        self._message = None
        self._errors = None
        self._context = None
        self._links = None
        self.discriminator = None

        self.status = status
        if id is not None:
            self.id = id
        self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        self.message = message
        self.errors = errors
        self.context = context
        self.links = links

    @property
    def status(self):
        """Gets the status of this StandardError.  # noqa: E501


        :return: The status of this StandardError.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StandardError.


        :param status: The status of this StandardError.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def id(self):
        """Gets the id of this StandardError.  # noqa: E501


        :return: The id of this StandardError.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StandardError.


        :param id: The id of this StandardError.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def category(self):
        """Gets the category of this StandardError.  # noqa: E501


        :return: The category of this StandardError.  # noqa: E501
        :rtype: object
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this StandardError.


        :param category: The category of this StandardError.  # noqa: E501
        :type category: object
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def sub_category(self):
        """Gets the sub_category of this StandardError.  # noqa: E501


        :return: The sub_category of this StandardError.  # noqa: E501
        :rtype: object
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """Sets the sub_category of this StandardError.


        :param sub_category: The sub_category of this StandardError.  # noqa: E501
        :type sub_category: object
        """

        self._sub_category = sub_category

    @property
    def message(self):
        """Gets the message of this StandardError.  # noqa: E501


        :return: The message of this StandardError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this StandardError.


        :param message: The message of this StandardError.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def errors(self):
        """Gets the errors of this StandardError.  # noqa: E501


        :return: The errors of this StandardError.  # noqa: E501
        :rtype: list[ErrorDetail]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this StandardError.


        :param errors: The errors of this StandardError.  # noqa: E501
        :type errors: list[ErrorDetail]
        """
        if self.local_vars_configuration.client_side_validation and errors is None:  # noqa: E501
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def context(self):
        """Gets the context of this StandardError.  # noqa: E501


        :return: The context of this StandardError.  # noqa: E501
        :rtype: dict[str, list[str]]
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this StandardError.


        :param context: The context of this StandardError.  # noqa: E501
        :type context: dict[str, list[str]]
        """
        if self.local_vars_configuration.client_side_validation and context is None:  # noqa: E501
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def links(self):
        """Gets the links of this StandardError.  # noqa: E501


        :return: The links of this StandardError.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this StandardError.


        :param links: The links of this StandardError.  # noqa: E501
        :type links: dict[str, str]
        """
        if self.local_vars_configuration.client_side_validation and links is None:  # noqa: E501
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StandardError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StandardError):
            return True

        return self.to_dict() != other.to_dict()
