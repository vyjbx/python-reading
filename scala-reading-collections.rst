#####################################
Good Things about Scala, everything
#####################################

1. Define actor props 

    https://blog.codecentric.de/en/2017/03/akka-best-practices-defining-actor-props/

    .. code:: scala

        def apply[T <: Actor: ClassTag](creator: => T): Props

    ``the creator parameter is passed by-name instead of by-value. Scala is lazy evaluation, plus the concurrency, the value of the parameter could have changed when it is actually evaluated``