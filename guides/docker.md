### Docker

This guide teaches you how to manage docker images, you have a wast amount of standard modules for your disposal.

First demo is a small webapplication which is ran.

You either create a playbook or manually install docker on the remote system.

The *linux_docker_handlers.yaml* is a good starting point, additionally you need to make sure you install *docker* pip module if you are using python above 2.7, if below you need the *docker-py* installed on remote system.

On our target system which is ubuntu we need to issue the *apt install python3-pip* command because by default there is no pip installed alongside the python.

After executing the playbook you should be able to hit the webapp running in the container with your browser.
