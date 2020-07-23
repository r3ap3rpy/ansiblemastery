### Group Variables

In this guide the group variables and their inheritance is on the menu.

We all know how important it is to create flexible playbooks accepting arguments.

These arguments can come either from command line or variables defined under */etc/ansible/group_vars* folder.

You will need to adjust the */etc/ansible/hosts* file to make these work.

``` bash
[lin]
ubuntu

[ans]
centos

[secret:children]
ans

[lin:vars]
specialvar=Whatever
anotherspecial=Whenever
thirdspecial=Wherever
```

These are the playbooks at your disposal to try out.

* test_all_group.yaml
* test_ans_group_.yaml
* test_hosts_inherit.yaml

You need to create the following files under *group_vars* aswell.

*/etc/ansible/group_vars/all.yml* 

``` yaml
---
prod_user: ansible
prod_password: ansible
```

*/etc/ansible/group_vars/ans.yml*

``` yaml
---
packages: "ansible, epel-release, python3-devel"
editor: "nano, vi, vim"
```

*/etc/ansible/group_vars/secret.yml*


``` yaml
---
classified: I dont like comedy!
```

Happy coding!