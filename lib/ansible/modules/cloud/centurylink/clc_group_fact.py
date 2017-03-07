#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2017 CenturyLink
#
# This file is part of Ansible.
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>
#

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'version': '1.0'}

DOCUMENTATION = '''
module: clc_group_fact
short_description: Get facts about groups in CenturyLink Cloud.
description:
  - An Ansible module to retrieve facts about groups in CenturyLink Cloud.
version_added: "2.3"
options:
  group_id:
    description:
      - The group id to retrieve facts for.
    required: False
  group_name:
    description:
      - The group name to retrieve facts for.
    required: False
  location:
    description:
      - Datacenter to create the group in. If location is not provided,
        the group gets created in the default datacenter
        associated with the account
    required: False
requirements:
    - python = 2.7
author: "CLC Runner (@clc-runner)"
notes:
    - To use this module, it is required to set the below environment variables which enables access to the
      Centurylink Cloud
          - CLC_V2_API_USERNAME, the account login id for the centurylink cloud
          - CLC_V2_API_PASSWORD, the account password for the centurylink cloud
    - Alternatively, the module accepts the API token and account alias. The API token can be generated using the
      CLC account login and password via the HTTP api call @ https://api.ctl.io/v2/authentication/login
          - CLC_V2_API_TOKEN, the API token generated from https://api.ctl.io/v2/authentication/login
          - CLC_ACCT_ALIAS, the account alias associated with the centurylink cloud
    - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment.
'''

EXAMPLES = '''
# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

- name: Retrieve Group Facts
  clc_group_fact:
    group_id: 31d13f501459411ba59304f3d47486eb

'''

RETURN = '''
changed:
    description: A flag indicating if any change was made or not
    returned: success
    type: boolean
    sample: True
server:
    description: The retrieved group facts.
    returned: success
    type: dict
    sample:
        "group": {
                "changeInfo": {
                    "createdBy": "mark.ramach.wfas",
                    "createdDate": "2016-04-07T23:37:15Z",
                    "modifiedBy": "mark.ramach.wfas",
                    "modifiedDate": "2016-04-07T23:37:15Z"
                },
                "customFields": [],
                "description": "K8S",
                "groups": [],
                "id": "479857c65d6a42d8b2523fab58c4c3cb",
                "links": [
                    {
                        "href": "/v2/groups/wfad",
                        "rel": "createGroup",
                        "verbs": [
                            "POST"
                        ]
                    },
                    {
                        "href": "/v2/servers/wfad",
                        "rel": "createServer",
                        "verbs": [
                            "POST"
                        ]
                    },
                    {
                        "href": "/v2/groups/wfad/479857c65d6a42d8b2523fab58c4c3cb",
                        "rel": "self",
                        "verbs": [
                            "GET",
                            "PATCH",
                            "DELETE"
                        ]
                    },
                    {
                        "href": "/v2/groups/wfad/a319873a32e84c17aa76306a477b9a22",
                        "id": "a319873a32e84c17aa76306a477b9a22",
                        "rel": "parentGroup"
                    },
                    {
                        "href": "/v2/groups/wfad/479857c65d6a42d8b2523fab58c4c3cb/defaults",
                        "rel": "defaults",
                        "verbs": [
                            "GET",
                            "POST"
                        ]
                    },
                    {
                        "href": "/v2/groups/wfad/479857c65d6a42d8b2523fab58c4c3cb/billing",
                        "rel": "billing"
                    },
                    {
                        "href": "/v2/groups/wfad/479857c65d6a42d8b2523fab58c4c3cb/archive",
                        "rel": "archiveGroupAction"
                    },
                    {
                        "href": "/v2/groups/wfad/479857c65d6a42d8b2523fab58c4c3cb/statistics",
                        "rel": "statistics"
                    },
                    {
                        "href": "/v2/groups/wfad/479857c65d6a42d8b2523fab58c4c3cb/upcomingScheduledActivities",
                        "rel": "upcomingScheduledActivities"
                    },
                    {
                        "href": "/v2/groups/wfad/479857c65d6a42d8b2523fab58c4c3cb/horizontalAutoscalePolicy",
                        "rel": "horizontalAutoscalePolicyMapping",
                        "verbs": [
                            "GET",
                            "PUT",
                            "DELETE"
                        ]
                    },
                    {
                        "href": "/v2/groups/wfad/479857c65d6a42d8b2523fab58c4c3cb/scheduledActivities",
                        "rel": "scheduledActivities",
                        "verbs": [
                            "GET",
                            "POST"
                        ]
                    },
                    {
                        "href": "/v2/servers/wfad/uc1wfadk8sm16",
                        "id": "UC1WFADK8SM16",
                        "rel": "server"
                    },
                    {
                        "href": "/v2/servers/wfad/uc1wfadk8sn46",
                        "id": "UC1WFADK8SN46",
                        "rel": "server"
                    },
                    {
                        "href": "/v2/servers/wfad/uc1wfadk8sm17",
                        "id": "UC1WFADK8SM17",
                        "rel": "server"
                    },
                    {
                        "href": "/v2/servers/wfad/uc1wfadk8sn45",
                        "id": "UC1WFADK8SN45",
                        "rel": "server"
                    }
                ],
                "locationId": "UC1",
                "name": "K8S",
                "servers": [
                    "UC1WFADK8SM16",
                    "UC1WFADK8SN46",
                    "UC1WFADK8SM17",
                    "UC1WFADK8SN45"
                ],
                "serversCount": 4,
                "status": "active",
                "type": "default"
            }
'''

__version__ = '${version}'


class ClcGroupFact(object):

    def __init__(self, module):
        """
        Construct module
        """
        self.clc_auth = {}
        self.module = module

    def process_request(self):
        """
        Process the request - Main Code Path
        :return: Returns with either an exit_json or fail_json
        """
        group_id = self.module.params.get('group_id')
        group_name = self.module.params.get('group_name')
        if not group_id and not group_name:
            return self.module.fail_json(
                msg='Must specify either group_id or group_name parameter.')

        self.clc_auth = clc_common.authenticate(self.module)

        if group_id:
            group = clc_common.find_group_by_id(self.module, self.clc_auth,
                                                group_id)
        elif group_name:
            location = self.module.params.get('location')
            root_group = clc_common.group_tree(self.module, self.clc_auth,
                                               datacenter=location)
            group = clc_common.find_group(self.module, root_group,
                                          group_name)

        group.data['servers'] = [obj['id'] for obj in group.data['links'] if
                                 obj['rel'] == 'server']

        return self.module.exit_json(changed=False, group=group.data)

    @staticmethod
    def _define_module_argument_spec():
        """
        Define the argument spec for the ansible module
        :return: argument spec dictionary
        """

        argument_spec = dict(
            group_id=dict(default=None),
            group_name=dict(default=None),
            location=dict(default=None)
        )

        mutually_exclusive = [['group_id', 'group_name']]

        return {"argument_spec": argument_spec,
                "mutually_exclusive": mutually_exclusive}


def main():
    """
    The main function.  Instantiates the module and calls process_request.
    :return: none
    """
    argument_dict = ClcGroupFact._define_module_argument_spec()
    module = AnsibleModule(supports_check_mode=True, **argument_dict)
    clc_group_fact = ClcGroupFact(module)
    clc_group_fact.process_request()

from ansible.module_utils.basic import *  # pylint: disable=W0614
import ansible.module_utils.clc as clc_common  # pylint: disable=W0614
if __name__ == '__main__':
    main()
