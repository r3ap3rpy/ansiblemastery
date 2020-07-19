### Fact caching

There are many modules provided in this guide. In this tutorial we will use the *jsonfile* and the *redis* plugins.

In order to configure the *jsonfile* module you can edit the file */etc/ansible/ansible.cfg*

``` bash
fact_caching = jsonfile
fact_caching_connection=/tmp
```

After this executing the following command.

Gives you a file under the */tmp* folder called ubuntu.

It is going to hold the gathered facts.

Now we can configure the *redis* module, first we install it and enable it and remove the firewall protection.

``` bash
sudo yum install redis -y
sudo systemctl enable redis
sudo systemctl stop firewalld
sudo systemctl disable firewalld
```

Now we need to edit the */etc/redis.conf* file
Replace the bind address with your IP.

``` bash
bind 192.168.56.2
```

Now you can install the redis module for python.

``` bash
sudo python3 -m pip install redis 
```

Now you can start the *redis* process.

``` bash
sudo systemctl start redis
```

You can download the [redisinsight](https://redislabs.com/redisinsight/) to watch the changes happen to your redis instance.

In our case the redis showed the following on the console after executing *ansible -m setup ubuntu*

![ubuntu](/pics/redis.PNG)

You also need to check the *test_redis.yaml* playbook to see it in action.


