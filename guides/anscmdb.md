### Ansible CMDB

This guide shows you how you can create a simple cmdb from your ansible inventory.

This shows you how you can generate a HTML file about the stats of your ansible clients.

You need to install the *ansible-cmdb* module of python.

``` bash
sudo python3.6 -m pip install ansible-cmdb
```

Then execute the following commands.

``` bash
mkdir out
ansible -m setup all --tree out
```

Then compile the output to an html file.

``` bash
ansible-cmdb out/ > index.html
```

Finally serve the output via python.

``` bash
python3.6 -m http.server
```

Then visit the following site.

``` bash
http://centos:8000
```

The following should be visible.

![cmdb](/pics/cmdb.PNG)