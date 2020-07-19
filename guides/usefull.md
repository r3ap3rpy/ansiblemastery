### Usefull 

In order to make ansible do some exra lifting for us the following settings were modified in the */etc/ansible/ansible.cfg*

``` bash
host_key_checking = False

stdout_callback = yaml
bin_ansible_callbacks = True

callback_whitelist = timer, log_plays

[callback_log_plays]
log_folder = /etc/ansible/logs

log_path = /var/log/ansible.log
```

This resulted in better structured output in ad-hoc and playbook executions, enabled the timing of the executions.
Added global logging to plays and host based logging.

The */var/log/ansible.log* needs to be created with the appropriate privileges.

``` bash
sudo touch /var/log/ansible.log
sudo chown ansible.ansible /var/log/ansible.log
```