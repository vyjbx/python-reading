########################################
Tools that make your life easier
########################################

1. ``restview``: restview creates a server and interprets .rst files on default browser. It reflects the changes **real-time**.
    
    ``>>>pip install restview`` 

    ``>>>restview README.rst``

#. Run Jupyter-Notebook server in a docker container. 
    
    *docker-stacks* provides a nice collection of docker files (and images in docker hub). Use ``docker search xxx``, ``docker pull xxx``, ``docker run xxx``, ``docker ps xxx`` and other commands to manipulate one container, use kubernete to orchestrate a collection of containers.
    
    https://github.com/jupyter/docker-stacks
    
    Note you can allocate resource (memory and swap memory) and bind volumens to containers.

    **Note** again, some programs inside containers read resource information from system level despite the memory limit given during container initation at ``docker run``. Those programs will not be aware of the memory limit, and will **crash** at some point. This is not an easy fix on docker end.  

#. *git* explained. This website gives the best explanation on git. Everything is a **DAG**.

    https://git-scm.com/docs

    Another source to look at git under the hood: learning by understanding how it functions, not only the APIs. This is the right way of learning something.

        http://merrigrove.blogspot.com/2014/02/why-heck-is-git-so-hard-places-model-ok.html

    A comparison of git vs. svn.

        https://stackoverflow.com/questions/871/why-is-git-better-than-subversion


#. Can you access mac video in docker container? Short answer: not possible directly. What is the alternative? Stream the video to container.

    https://apple.stackexchange.com/questions/265281/using-webcam-connected-to-macbook-inside-a-docker-container 

#. ``tree``

    ''>>>apt-get install tree``
    ``>>>tree .``
    ``>>>man tree``

#. docker image vs container explained

    http://merrigrove.blogspot.com/2015/10/visualizing-docker-containers-and-images.html

	.. image:: ./media/docker-commands.png

	``docker underhood, not docker all. docker client side is not in this graph``


    docker stop (SIGTERM) vs. docker kill (SIGKILL)

        https://major.io/2010/03/18/sigterm-vs-sigkill/

        ``In fact, the process isn’t even made aware of the SIGKILL signal since the signal goes straight to the kernel init. At that point, init will stop the process. The process never gets the opportunity to catch the signal and act on it.``

#. AWS AMI linux

    https://docs.aws.amazon.com/AmazonECR/latest/userguide/amazon_linux_container_image.html

    1. pull Amazon linux image from docker hub

    ``docker pull amazonlinux``

    ``docker run -it amazonlinux:latest /bin/bash/``

#. Python test modules (almost all of them)

    https://docs.python-guide.org/writing/tests/


