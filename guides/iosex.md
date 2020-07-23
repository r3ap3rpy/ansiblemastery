## IOS playbook examples

This guide holds all the related playbooks and edits necessary to reproduce the contents of the video.

#### Basic troubleshooting

The task is simple, you need a playbook which executes a set of commands on remote targets and saves the output to the local machine.

First the */etc/ansible/group_vars/cisco.yml* add the following 2 lines.

``` yaml
ansible_become_method: enable
ansible_become_password: Start123
```

This is only necessary if you want to execute commands which need *enable* privileges.

Then we can create the playbook called *network_tshoot.yaml*, refer to it in the sources.

#### Dynamic troubleshooting

We need to improve our playbook, and detach two dependencies, one is the hardcoded *hosts*, the other is the hardcoded commands.

The *network_tshoot_v2.yaml* playbook reflects these changes, only the */etc/ansible/group_vars/cisco.yml* needs to be expanded with the following values.

``` yaml
cisco_tshoot_commands:
  - "show version"
  - "show ip int brief"
  - "show run"
```

Now the depenencies are detached from the playbook.