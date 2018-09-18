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

		In ``shell form``, CMD is ignored when ENTRYPOINT presents; in ``exec form``, if there is no external parameters at ``docker run``, CMD fields will be attached as ENTRYPOINT parameters, otherwise CMD will be ignored and ENTRYPOINT parameter will be used.

		    http://goinbigdata.com/docker-run-vs-cmd-vs-entrypoint/

	#. A few posts about docker

	    http://www.johnzaccone.io/author/john/

	#. docker swarm vs. kubernetes (micro-service orchestration platforms)

	    https://platform9.com/blog/kubernetes-docker-swarm-compared/

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

#. NGINX introduction

    1. General introduction

	    https://medium.freecodecamp.org/an-introduction-to-nginx-for-developers-62179b6a458f

	2. Beginner's guide

	    http://nginx.org/en/docs/beginners_guide.html

	#. Beginner's introduction

		https://waqarafridi.wordpress.com/2017/12/09/introduction-to-nginx/

#. Spark

    1. worker node dependency 

        Install packages on work node by ``--py-files`` pointing to ``*.py`` or ``*.egg`` files or ``ssh`` to worker nodes one by one and do the installation, and setup ``PYSPARK_PYTHON`` path.

        **There must exist a better way to provision the clusters.** 

            https://blog.cloudera.com/blog/2015/09/how-to-prepare-your-apache-hadoop-cluster-for-pyspark-jobs/

#. RPC vs. REST, with examples

    https://blog.jscrambler.com/rpc-style-vs-rest-web-apis/

    
    https://www.smashingmagazine.com/2016/09/understanding-rest-and-rpc-for-http-apis/

	    ``RPC is great for actions (a collection of functions).``

	    ``REST is good for modeling the resource domain with CRUD.``

#. linux filesystem hierarchy

    https://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/
