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
module: clc_network_fact
short_description: Get facts about networks in the Centurylink Cloud
description:
  - An Ansible module to retrieve facts about networks in the Centurylink Cloud
version_added: "2.3"
options:


requirements:
  - python >= 2.7
author: "CLC Runner (@clc-runner)"
notes:
  - To use this module, it is required to set the below environmental variables which enable access to CLC
      - CLC_V2_API_USERNAME: the account login id for CLC
      - CLC_V2_API_PASSWORD: the password for the CLC account
  - Alternatively, the module accepts the API token and account alias. The API token can be generated using the CLC
    account login and password via the HTTP api call @ https://api.ctl.io/v2/authentication/login
      - CLC_V2_API_TOKEN: the API token generated from https://api.ctl.io/v2/authentication/login
      - CLC_ACCT_ALIAS: the account alias associated with CLC
  - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment
'''

EXAMPLES = '''
# NOTE - You must set the CLC_V2_API_USERNAME and CLC_V2_API_PASSWD Environment variables before running examples

- name: Retrieve network facts
  clc_network_fact:
    id: Blah
    location: CA3

  clc_network_fact:
    id: f759b60eb31d4a33a3d63ffe713de019
    location: CA3

  clc_network_fact:
    id: 10.101.236.0/24
    location: CA3
'''

RETURN = '''
changed:
  description: a flag indicating if any change was made or not
  returned: success
  type: boolean
  sample: True
network:
  description: The retrieved network info
  returned: success
  type: dict
  sample:
    "network": {
        "changed": false,
        "network": {
            "cidr": "10.101.236.0/24",
            "description": "vlan_736_10.101.236",
            "gateway": "10.101.236.1",
            "id": "f759b60eb31d4a33a3d63ffe713de019",
            "links": [
                {
                    "href": "/v2-experimental/networks/wfti/ca3/f759b60eb31d4a33a3d63ffe713de019",
                    "rel": "self",
                    "verbs": [
                        "GET",
                        "PUT"
                    ]
                },
                {
                    "href": "/v2-experimental/networks/wfti/ca3/f759b60eb31d4a33a3d63ffe713de019/ipAddresses",
                    "rel": "ipAddresses",
                    "verbs": [
                        "GET"
                    ]
                },
                {
                    "href": "/v2-experimental/networks/wfti/ca3/f759b60eb31d4a33a3d63ffe713de019/release",
                    "rel": "release",
                    "verbs": [
                        "POST"
                    ]
                }
            ],
            "name": "Ansible Network",
            "netmask": "255.255.255.0",
            "type": "private",
            "vlan": 736
        }
    }
}
'''

__version__ = '{version}'


class ClcNetworkFact(object):

    module = None

    def __init__(self, module):
        """
        Construct module
        """
        self.clc_auth = {}
        self.module = module
        self.networks = None

    def process_request(self):
        """
        Process the request - Main code path
        :return: Returns with either an exit_json or fail_json
        """
        result = None
        params = self.module.params

        self.clc_auth = clc_common.authenticate(self.module)
        # Network operations use v2-experimental, so over-ride default
        self.clc_auth['v2_api_url'] = self.clc_auth['v2_api_url'].replace(
            '/v2/', '/v2-experimental/', 1)

        location = params.get('location')
        self.networks = clc_common.networks_in_datacenter(
            self.module, self.clc_auth, location)
        requested = params.get('id', None)
        if requested is None:
            self.module.exit_json(
                networks=[n.data for n in self.networks])
        else:
            network = clc_common.find_network(
                self.module, self.clc_auth, location,
                network_id_search=requested, networks=self.networks)
            if network is None:
                return self.module.fail_json(
                    msg='Network: {network} does not exist in location: '
                        '{location}.'.format(
                            network=requested, location=location))
            self.module.exit_json(network=network.data)

    @staticmethod
    def _define_module_argument_spec():
        """
        Define the argument spec for the ansible module
        :return: argument spec dictionary
        """
        argument_spec = dict(
            id=dict(required=False),
            location=dict(required=True)
        )
        return argument_spec


def main():
    """
    The main function.  Instantiates the module and calls process_request.
    :return: none
    """
    module = AnsibleModule(
        argument_spec=ClcNetworkFact._define_module_argument_spec(),
        supports_check_mode=False)
    clc_network = ClcNetworkFact(module)
    clc_network.process_request()

from ansible.module_utils.basic import *  # pylint: disable=W0614
import ansible.module_utils.clc as clc_common  # pylint: disable=W0614
if __name__ == '__main__':
    main()
