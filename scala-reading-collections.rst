#####################################
Good Things about Scala, everything
#####################################

1. Define actor props 

    https://blog.codecentric.de/en/2017/03/akka-best-practices-defining-actor-props/

    .. code:: scala

        def apply[T <: Actor: ClassTag](creator: => T): Props

    ``the creator parameter is passed by-name instead of by-value. Scala is lazy evaluation, plus the concurrency, the value of the parameter could have changed when it is actually evaluated``

2. Scala type inference
 
    https://dzone.com/articles/introduction-to-scala-type-system

3. Scala type parameter lower, upper and view (implicit conversions) bounds (variances)

    https://www.journaldev.com/9609/scala-typebounds-upper-lower-and-view-bounds

    .. code:: scala

        class myClass1[T <: S] # upper bound
        class myClass2[T >: S] # lower bound
        class myClass3[T <% S] # view bound
4. Type erasure in Scala (JVM)

    https://blog.knoldus.com/type-erasure-in-scala/

5. high kind types (following the scala type erasure)

    https://typelevel.org/blog/2016/08/21/hkts-moving-forward.html

6. defunctionalization: This is not specifically about Scala

    http://www.brics.dk/RS/01/23/BRICS-RS-01-23.pdf

#. scala object vs. class 

    https://blog.knoldus.com/class-and-object-keyword-in-scala-programming/

#. identify which ``main`` to use in ``sbt run`` in build.sbt

    https://alvinalexander.com/scala/sbt-how-specify-main-method-class-to-run-in-project

    add a line like this to your build.sbt file

    .. code:: scala

        mainClass in (Compile, run) := Some("com.module.object")

#. actor vs future for concurrency using threading

    https://www.chrisstucchio.com/blog/2013/actors_vs_futures.html