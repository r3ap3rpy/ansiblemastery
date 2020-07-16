### Win - basic authentication

First the basic authentication is demonstrated. 

We are goint to have to install the pywinrm module on the ansible manangement server.

``` bash
sudo python3.6 -m pip install pywinrm --user
```

Then we create our group under the */etc/ansible/hosts* file.

``` bash
[winbasic]
2019A
```

Create a file under the */etc/ansible/group_vars* called *winbasic.yml*.

Add the following content.

``` bash
ansible_user: ansible
ansible_password: Start!123
ansible_connection: winrm
ansible_winrm_transport: basic
ansible_winrm_port: 5985
```

Note that the port *5985* is for http authentication the *5986* is for https authentication.

On the windows machine create the user as shown in the course.

For short you can use these commands, if you open a cmd with admin privileges.

``` bash
net user ansible Start!123 /EXPIRES:NEVER /PASSWORDCHG:NO  /add
net localgroup Administrators ansible /add
winrm set winrm/config/service/auth @{Basic="true"}
winrm set winrm/config/service @{AllowUnencrypted="true"}
```

Then you must be able to issue the following command on the management server.

```bash
ansible -m win_ping 2019A
```