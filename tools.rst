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

        Dockerfile as a wrapper on docker run + docker commit

            https://stackoverflow.com/questions/17891981/docker-run-cd-does-not-work-as-expected 

	#. A few posts about docker

	    http://www.johnzaccone.io/author/john/

	#. docker swarm vs. kubernetes (micro-service orchestration platforms)

	    https://platform9.com/blog/kubernetes-docker-swarm-compared/

    #. docker -v vs --mount

        ''Mounting into a non-empty directory on the container
        If you bind-mount into a non-empty directory on the container, the directory’s existing contents are obscured by the bind mount. This can be beneficial, such as when you want to test a new version of your application without building a new image. However, it can also be surprising and this behavior differs from that of docker volumes.

        This example is contrived to be extreme, but replaces the contents of the container’s /usr/ directory with the /tmp/ directory on the host machine. In most cases, this would result in a non-functioning container.''

        https://docs.docker.com/storage/bind-mounts/#mounting-into-a-non-empty-directory-on-the-container

    #. docker container to host communication

        mac: host.docker.internal from 18.03

        linux: host

        https://dev.to/bufferings/access-host-from-a-docker-container-4099

    #. docker resource change dynamically: through docer, or systemd, or cgroup config files

        https://goldmann.pl/blog/2014/09/11/resource-management-in-docker/#_changing_the_shares_value_for_a_running_container

            ``sudo systemctl set-property docker-4be96b853089bc6044b29cb873cac460b429cfcbdd0e877c0868eb2a901dbf80.scope CPUShares=512``

        https://forums.docker.com/t/dynamic-changing-memory-limitation/14460/2

        The docker update command dynamically updates container configuration.

            ``The docker update command dynamically updates container configuration.``

        linux cgroups

            https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/ch01

    #. ENV vs ARG
        
        https://stackoverflow.com/questions/41916386/arg-or-env-which-one-to-use-in-this-case

            The ARG instruction defines a variable that users can pass at build-time to the builder with the docker build command using the --build-arg <varname>=<value> flag.

            The ENV instruction sets the environment variable <key> to the value <value>. The environment variables set using ENV will persist when a container is run from the resulting image.

        

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

#. how to build an AI sandbox

    https://blog.prolego.io/how-to-build-an-ai-sandbox-3a95e9507379

#. **CHEAT SHEETS!** a good collection of cheat sheets covers pyspark, pandas, sklearn, scipy, matplotlib, keras, neural nets, with link to orginal resources, image + reading.

    https://startupsventurecapital.com/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5

#. zeppelin

    **zeppelin is good**

#. Art of model deployment: covering blue-green, canary, and A/B testing (basically adding a router before the model endpoint) and using 

    https://medium.com/@julsimon/mastering-the-mystical-art-of-model-deployment-c0cafe011175

    What is Blue-Green model deployment

        https://docs.cloudfoundry.org/devguide/deploy-apps/blue-green.html

    Sagemaker ML model deployment

        From Sagemaker documents (https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-dg.pdf#gs)
            
            ``You can deploy multiple variants of a model to the same Amazon SageMaker HTTPS endpoint. This is useful for testing variations of a model in production. For example, suppose that you've deployed a model into production. You want to test a variation of the model by directing a small amount of traffic, say 5%, to the new model. To do this, create an endpoint configuration that describes both variants of the model. You specify the ProductionVariant in your request to the CreateEndPointConfig. For more information, see ProductionVariant (p. 461).``


#. SageMaker, Lambda to make a quick ML demo framework

    https://aws.amazon.com/blogs/machine-learning/build-a-serverless-frontend-for-an-amazon-sagemaker-endpoint/

#. send data to server through HTML: form, application/json, application/x-www-form-urlencoded

    https://medium.com/@mohamedraja_77/content-type-x-www-form-urlencoded-form-data-and-json-e17c15926c69

    https://stackoverflow.com/questions/26723467/what-is-the-difference-between-form-data-x-www-form-urlencoded-and-raw-in-the-p/26730839

#. Microservice mesh: Istio

    ``Using Istio’s traffic management model essentially decouples traffic flow and infrastructure scaling, letting you specify via Pilot what rules they want traffic to follow rather than which specific pods/VMs should receive traffic - Pilot and intelligent Envoy proxies look after the rest.``

    https://istio.io/docs/concepts/traffic-management/

    https://blog.envoyproxy.io/service-mesh-data-plane-vs-control-plane-2774e720f7fc

    https://www.abhishek-tiwari.com/a-sidecar-for-your-service-mesh/

#. Protobuf: with python examples (metaprogramming, ``protoc``, etc.)

    https://developers.google.com/protocol-buffers/docs/overview

    https://www.datadoghq.com/blog/engineering/protobuf-parsing-in-python/

#. what is k8s?

    ``Kubernetes and containers are here to stay.``

    https://itnext.io/what-is-kubernetes-c9c5bedb51f0

#. cassandra compaction

    https://www.datastax.com/dev/blog/leveled-compaction-in-apache-cassandra

    read, write to cassandra

        https://docs.datastax.com/en/cassandra/3.0/cassandra/dml/dmlAboutReads.html

    sstable (sorted string table) storage format

        http://distributeddatastore.blogspot.com/2013/08/cassandra-sstable-storage-format.html

    difference between ``UDPATE`` and ``INSERT`` in cassandra

        https://stackoverflow.com/questions/16532227/difference-between-update-and-insert-in-cassandra

#. about kafka (not franz kafka)
    
    kafka assigner

        https://medium.com/@anyili0928/what-i-have-learned-from-kafka-partition-assignment-strategy-799fdf15d3ab

    kafka consumers and rebalancing

        https://www.oreilly.com/library/view/kafka-the-definitive/9781491936153/ch04.html

    kafka partitions

#. kubernetes

    what are pods? they share the same namespace, but not necessarily the same cgroup. (containers are not containers in a box. they are processes isolated from each other using linux namespace and cgroups. both can be used independently. such as, two containers can have the same namespace, so that they are "local" to each other, while they have different cgroups which grant them different limits to the system.)

        https://www.ianlewis.org/en/what-are-kubernetes-pods-anyway

#. SQL server: server side cursor vs. client side cursor

    https://msdn.microsoft.com/en-us/library/aa266531(v=vs.60).aspx

    https://www.sqlservercentral.com/Forums/Topic416894-8-1.aspx

    https://stackoverflow.com/questions/33704316/im-confused-about-mysqldb-server-side-cursor-and-client-cursor

#. s3cmd ls, get, put, sync; single file vs. directory ``s3cmd put dir1/ s3://something`` vs ``s3cmd put dir1 s3://something``

    https://s3tools.org/s3cmd-howto

    https://s3tools.org/usage

#. s3cmd, bot, aws cli comparison

    https://stackoverflow.com/questions/26326408/difference-between-s3cmd-boto-and-aws-cli

    s3cmd access multiple buckets with different confidentials

        ``s3cmd --configure -c .s3cfg_bucketname`` to set up a configuration file
        ``s3cmd -c .s3cfg_bucketname ls/put/get/sync s3_bucketname`` to use the specified configuration file to display or apply on the s3 bucket

        https://stackoverflow.com/questions/18495329/access-multiple-buckets-in-s3

#. linux cgroups (subsystems, hierarchies, cgroups, and tasks)

    https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/resource_management_guide/ch01

        cgorups are orgnized heirarchically, just like processes. Child cgroups inherit from parent cgroups when initialized. 

        The four rulls:

            1. a single hierarchy can have one or more subsystems (resource).

            2. if a single subsystem is attached to multiple hierarchies, it cannot co-exist with another subsystem.

            3. in one hierarchy, one task can only exist in one cgroup. 

            4. when a process spawns a child process, the child process inherits the cgroups from the parent initially. The two process then become independent of each other and can be mounted to different cgroups.


#. dask

    https://towardsdatascience.com/why-every-data-scientist-should-use-dask-81b2b850e15b 

    http://docs.dask.org/en/latest/_downloads/daskcheatsheet.pdf

#. linux && vs ; vs &

    The && operator is a boolean AND operator: if the left side returns a non-zero exit status, the operator returns that status and does not evaluate the right side (it short-circuits), otherwise it evaluates the right side and returns its exit status. This is commonly used to make sure that command2 is only run if command1 ran successfully. While & causes the command to be run in the background.

#. postgres vs mysql

    https://blog.panoply.io/postgresql-vs.-mysql

#. WSL windows subsystem linux

    https://blogs.msdn.microsoft.com/wsl/2016/06/15/wsl-file-system-support/

#. linux EA (Extended file Attributes)

    http://www.linux-mag.com/id/8741/
