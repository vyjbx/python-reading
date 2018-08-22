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


#. Can you access mac video in docker container? Short answer: not possible directly. What is the alternative? Stream the video to container.

    https://apple.stackexchange.com/questions/265281/using-webcam-connected-to-macbook-inside-a-docker-container 