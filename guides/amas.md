### Setup

In this guide we will setup ansible user and passwordles authentication.

Let's login to our centos machine. Then issue the following command.

``` bash
useradd ansible
```

Then the following command, to set the password.

``` bash
passwd ansible
```

Then generate some ssh keys.

``` bash
ssh-keygen -b 2048 -t rsa
```
Then edit the */etc/sudoers* file and add the following line.

``` bash
ansible ALL=(ALL) NOPASSWD=ALL
```

We can now copy the keys to localhost.

``` bash
ssh-copy-id localhost
```

Then copy down with winscp to our localhost for reference.

We need to edit our local ssh *config* to have the following content.

``` bash
Host *
	User ansible
	IdentityFile c:\users\r3ap3rpy\.ssh\id_rsa
```

Now we can use the pub-key authentication to login, and have passwordless sudo.
