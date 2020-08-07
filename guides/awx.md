### Ansible Tower

This guide let's you brind up the AWX container farm.

The following commands should be executed with sudo.

``` bash
dnf install epel-release -y
dnf install git gcc gcc-c++ nodejs gettext device-mapper-persistent-data lvm2 bzip2 python3-pip
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
dnf install docker-ce
systemctl start docker
systemctl enable --now docker.service
alternatives --set python /usr/bin/python3
pip3 install docker-compos
git clone https://github.com/ansible/awx.git
```

Now you should edit the */root/awx/installer/inventory* file and customize these parameters.

``` yaml
pg_admin_password
admin_password
secret_key
```

For the secret key you can use the following one to generate it.

``` bash
openssl rand -base64 30
```

Now you can build your container with the following command.

``` bash
ansible-playbook -i inventory install.yml
```

You can login to the *http://centos* port with the configured credentials.

If you want to shutdown the containers use the following commands.

``` bash
cd /root/.awx/awxcompose
docker-compose stop
```

Starting it back up is just as easy.

``` bash
cd /root/.awx/awxcompose
docker-compose up -d
```

You can check the logs with the following commands.

``` bash
cd /root/.awx/awxcompose
docker-compose logs -f
```