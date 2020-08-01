## Windows setup

#### Basic authentication

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

#### Certificate authentication

Let's generate a self signed certificated, on our centos machine.
``` bash
# Set the name of the local user that will have the key mapped to

cat > openssl.conf << EOL
distinguished_name = req_distinguished_name
[req_distinguished_name]
[v3_req_client]
extendedKeyUsage = clientAuth
subjectAltName = otherName:1.3.6.1.4.1.311.20.2.3;UTF8:ansible@localhost
EOL

export OPENSSL_CONF=openssl.conf

openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -out cert.pem -outform PEM -keyout cert_key.pem -subj "/CN=ansible" -extensions v3_req_client
```

Import the certificate to the certificate store, Trusted People and Trusted root CA

Generate a selfsigned cert on the windows machine!

``` powershell
New-SelfSignedCertificate -DnsName 2019A -KeyLocation Cert:\LocalMachine\My\
```

Configure the winrm listener.

``` bash
winrm create winrm/config/Listener?Address=*+Transport=HTTPS @{Hostname="2019A";CertificateThumbprint="828F238786FE722A55420BE9209A93B996B8CEDF"}

winrm enumerate winrm/config/Listener
```

Map the user to the credentials.

``` cmd
winrm create winrm/config/service/certmapping?Issuer=50988BCCAF7371814D722E34CDC77A0FF0DE212A+Subject=ansible@localhost+URI=* @{UserName = "ansible";Password="*********************"}
```

Last setting on windows is to enable certificate based authentication.

``` cmd
winrm set winrm/config/service/Auth @{Certificate="true"}
```

You need to create the user on the windows machine and add it to the *Administrators* localgroup.

On the ansible server you need to modify some stuff.

Create a folder called */etc/ansible/certs*, move the *cert.pem* and *cert_key.pem* in there.

Now create the file */etc/ansible/group_vars/wincert.yaml* with the following content.

``` yaml
---
ansible_connection: winrm
ansible_winrm_transport: certificate
ansible_winrm_cert_pem: /etc/ansible/certs/cert.pem
ansible_winrm_cert_key_pem: /etc/ansible/certs/cert_key.pem
ansible_port: 5986
ansible_winrm_scheme: https
ansible_winrm_server_cert_validation: ignore
```

Now add the following lines to the */etc/ansible/hosts* file.

``` yaml
[wincert]
2019A
```

If all went wenn the *ansible -m win_ping 2019A* should return green!

#### NTLM Authentication

You need to have a domain based environment with an account with appropriate privileges to do this.

I have created the *ansible* user and added it to the *Domain Admins* group, not secure and not advised either.

On the centos machine i have added this to the */etc/ansible/hosts* file

``` yaml
[winntlm]
2019A
```

I have created the following file under group_vars: */etc/ansible/group_vars/winntlm.yml* with this content.

``` yaml
---
ansible_winrm_transport: ntlm
ansible_winrm_port: 5985
ansible_user: ansible
ansible_password: Start!123
ansible_connection: winrm
```

The following command should work.

``` bash
ansible -m win_ping 2019A
```

#### Kerberos Authentication

On the centos machine you need these packages installed.

``` bash
yum install python3-devel krb5-devel krb5-workstation krb5-libs gcc -y 
```

Then you need to install the following python module.

``` bash
python3 -m pip install pywinrm[kerberos]
```

Then create the */etc/ansible/group_vars/winkerberos.yml* with the following content.

``` yaml
---
ansible_user: ansible@REDWOOD.LOCAL
ansible_password: Start!123
ansible_connection: winrm
ansible_winrm_port: 5985
ansible_winrm_transport: kerberos
```

Add the group that holds the server to the */etc/ansible/hosts*

``` yaml
[winkerberos]
2019A
```

You need to make sure that both the domain and the domain controllers are resolvable by the centos host.

Add the following to your */etc/hosts*

``` bash
192.168.56.5 2019A
192.168.56.5 REDWOOD.LOCAL
```

You also need to edit the kerberos configuration file under */etc/krb5.conf*

``` bash
[realms]
 REDWOOD.LOCAL = {
     kdc = 2019A
     admin_server = 2019A
 }
```

If you have to create a user and adjust the configuration, but the following command should work if you went video by video.

``` bash
ansible -m win_ping 2019A
```

#### CredSSP Authentication

On the windows machine you need to open a powershell console and issue the following command.

``` powershell
Enable-WSManCredSSP -Role Server -Force
```

This configured the WSman for CredSSP authentication.

Now on the centos machine you need to create the */etc/ansible/group_vars/wincredssp.yml* with the following content.

``` yaml
---
ansible_user: ansible
ansible_password: Start!123
ansible_port: 5985
ansible_connection: winrm
ansible_winrm_transport: credssp
```

Then add your host to the appropriate group.

``` yaml
[wincredssp]
2019A
```

You should be able to ping your windows machine with the following command.

``` bash
ansible -m win_ping 2019A
```

#### Authentication overview

|     Type    | Local Accounts | Active Directory Accounts | Client Delegation | HTTPS Encryption |
|:-----------:|:--------------:|:-------------------------:|:-----------------:|:----------------:|
|    BASIC    |       YES      |             NO            |         NO        |        NO        |
| CERTIFICATE |       YES      |             NO            |         NO        |        NO        |
|   KERBEROS  |       NO       |            YES            |        YES        |        YES       |
|     NTLM    |       YES      |            YES            |         NO        |        YES       |
|   CREDSSP   |       YES      |            YES            |        YES        |        YES       |


### Dem playbooks

The first playbook is about gathering disk information from windows systems. Check out the *win_disk_facts.yaml* for further reference.

The second playbook to work you need to edit the */etc/ansible/group_vars/all.yaml* file and add these lines.

``` yaml
default_users:
  - sdagent
  - bqaagent
  - monitoring
  - tshoot
```

Then you can execute the playbook *win_local_user.yaml* to provision your users.

