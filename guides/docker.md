### Docker

This guide teaches you how to manage docker images, you have a wast amount of standard modules for your disposal.

First demo is a small webapplication which is ran.

You either create a playbook or manually install docker on the remote system.

### Ubuntu 20.04 LTS

The *linux_docker_handlers.yaml* is a good starting point, additionally you need to make sure you install *docker* pip module if you are using python above 2.7, if below you need the *docker-py* installed on remote system.

On our target system which is ubuntu we need to issue the *apt install python3-pip* command because by default there is no pip installed alongside the python.

After executing the playbook you should be able to hit the webapp running in the container with your browser.

The second example is about gathering hostin information from the docker instance with the *docker_host_info.yaml* playbook.

The third one is about how you can gather information about a specific container of your choice. Check out the *container_info.yaml*

The last one is about volume management, check out this playbook *container_volumes.yaml*


