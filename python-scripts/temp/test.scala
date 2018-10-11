#! /bin/sh
exec scala "$0" "$@"
!#

object Hello {
  def main(args: Array[String]) {
    println("hello world") }
}

Hello.main(args)
