### Linux clients

First we need a user on our ubuntu machine.

``` bash
adduser ansible
```

We specify the password *Start!123*, and accept everything on the default.

We setup passwordless sudo access with editing the */etc/sudoers* file with the *sudo visudo -f /etc/sudoers*.

Add the following line.

``` bash
ansible ALL=(ALL) NOPASSWD: ALL
```

Now logoff and login to test it.

On the management server we have two options the first one is like this.

Create a new folder with the following command.

``` bash
mkdir /etc/ansible/group_vars
```

Then create the */etc/ansible/group_vars/all.yml* file with the following content.

``` bash
---
ansible_user: ansible
ansible_password: Start!123
```

Now you need to edit the file */etc/ansible/ansible.cfg*

Uncomment the following line *host_key_checking = False*

This will allow you to issue the following command with success.

``` bash
ansible -m ping ubuntu
```

The other option is to remove the *all.yml* restore the *ansibéle.cfg* content.

THen issue the following command.

``` bash
ssh-copy-id ubuntu
```

Insert password,  then try to ping it. It must succeed.