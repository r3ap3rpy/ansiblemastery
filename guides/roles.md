### Roles

Roles allow you to group together tasks in one place and apply it to achieve your desired state, it allows you to reduce playbook size and simplify your infrastructure.

You need to create a new folder structure.

``` bash
mkdir -p /etc/ansible/roles/linux/texteditor/tasks
```

Then populate the *main.yml* file with the following content.

``` yaml
- name: "Install nano text editor!"
  apt:
    name: nano
    state: present

- name: "Install multiple packages!"
  apt:
    pkg:
      - apache2
      - nginx
    state: present
```

Then you can use the *test_roles.yaml* playbook to try out the example.