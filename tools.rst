########################################
Tools that make your life easier
########################################

1. ``restview``: restview creates a server and interprets .rst files on default browser. It reflects the changes **real-time**.
    
    ``>>>pip install restview`` 

    ``>>>restview README.rst``

#. Run Jupyter-Notebook server in a docker container. 
    
    1. *docker-stacks* provides a nice collection of docker files (and images in docker hub). Use ``docker search xxx``, ``docker pull xxx``, ``docker run xxx``, ``docker ps xxx`` and other commands to manipulate one container, use kubernete to orchestrate a collection of containers.
    
	    https://github.com/jupyter/docker-stacks
    
    2. Note you can allocate resource (memory and swap memory) and bind volumens to containers.

	    **Note** again, some programs inside containers read resource information from system level despite the memory limit given during container initation at ``docker run``. Those programs will not be aware of the memory limit, and will **crash** at some point. This is not an easy fix on docker end.  

#. *git* explained. This website gives the best explanation on git. Everything is a **DAG**.

    https://git-scm.com/docs

    1. Another source to look at git under the hood: learning by understanding how it functions, not only the APIs. This is the right way of learning something.

        http://merrigrove.blogspot.com/2014/02/why-heck-is-git-so-hard-places-model-ok.html

    2. A comparison of git vs. svn.

        https://stackoverflow.com/questions/871/why-is-git-better-than-subversion

    3. A **very nice** git cheat sheet

        .. image:: ./media/git-cheat-sheet.png
          :width: 600px


        http://www.ndpsoftware.com/git-cheatsheet.html#loc=workspace 


#. Can you access mac video in docker container? Short answer: not possible directly. What is the alternative? Stream the video to container.

    https://apple.stackexchange.com/questions/265281/using-webcam-connected-to-macbook-inside-a-docker-container 

#. ``tree``

    ''>>>apt-get install tree``
    ``>>>tree .``
    ``>>>man tree``

#. docker

    1. docker image vs container explained

        http://merrigrove.blogspot.com/2015/10/visualizing-docker-containers-and-images.html

	    .. image:: ./media/docker-commands.png

	    ``docker underhood, not docker all. docker client side is not in this graph``


    2. docker stop (SIGTERM) vs. docker kill (SIGKILL)

        https://major.io/2010/03/18/sigterm-vs-sigkill/

        ``In fact, the process isn’t even made aware of the SIGKILL signal since the signal goes straight to the kernel init. At that point, init will stop the process. The process never gets the opportunity to catch the signal and act on it.``

    #. docker ``RUN`` vs ``CMD`` vs ``ENTRYPOINT``

        ``1. RUN executes commands in a new layer and creates a new image.``

        ``2. CMD sets default command and/or parameters which can be overwritten from command line when **docker run**.``

        ``3. ENTRYPOINT configures a container that will run as an executable, and can take parameters.``

        http://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/

    #. another docker ``CMD`` vs ``ENTRYPOINT`` difference

        https://medium.freecodecamp.org/docker-entrypoint-cmd-dockerfile-best-practices-abc591c30e21 

    #. docker ``exec form`` vs ``shell form``: ``exec form`` makes it possible to avoid shell string munging, and to run commands with an image without specified shell executable.

	    ``exec form`` example
	    
	        ``CMD ["python", "helloworld.py", "username"]``

	        ``CMD ["python", "helloworld.py", "$NAME"]``

	        Notice the **double quotes** as ``exec form`` processes the command line as JSON array. Also in the last example, as a shell is not evoked, "$NAME" will be recognized as ``$HOME``, instead of environment variable substitution.

	    ``shell form`` example

	        ``CMD python helloworld.py username``

	        ``CMD ["python", "-c", "helloworld.py", "username"]``

		https://stackoverflow.com/questions/42805750/dockerfile-cmd-shell-versus-exec-form

		A bit of more details
		
			http://www.johnzaccone.io/entrypoint-vs-cmd-back-to-basics/

	#. A few posts about docker

	    http://www.johnzaccone.io/author/john/

#. AWS AMI linux

    https://docs.aws.amazon.com/AmazonECR/latest/userguide/amazon_linux_container_image.html

    1. pull Amazon linux image from docker hub

	    ``docker pull amazonlinux``

	    ``docker run -it amazonlinux:latest /bin/bash/``

	    It is a CentOS/RH descendent instead of Debian. Use ``yum`` instead of ``apt`` or ``apt-get``, and ``which yum`` will fail because ``which`` is not defined :).

#. Mesos vs YARN

    https://www.oreilly.com/ideas/a-tale-of-two-clusters-mesos-and-yarn

#. Sparkling water: H2O+Spark

    https://github.com/h2oai/sparkling-water/blob/master/README.rst

#. **tmux**, multiple window, session sharing
    
    minimal introduction to get started

    https://medium.com/actualize-network/a-minimalist-guide-to-tmux-13675fb160fa
