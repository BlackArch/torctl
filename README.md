## Description

Script to redirect all traffic through tor network

## Installation

`pacman -S torctl`

## Usage

```
$ torctl
--==[ torctl.sh by blackarch.org ]==--

usage:

  torctl.sh start | stop | status | restart | ip | change | version

options:

  start   - start tor and redirect all traffic through tor
  stop    - stop tor and redirect all traffic through clearnet
  status  - get tor service status
  restart - restart tor and traffic rules
  ip      - get remote ip
  change  - change tor identity
  version - print version of torctl and exit

```

## Get Involved

You can get in touch with the BlackArch Linux team. Just check out the following:

**Please, send us pull requests!**

**Web:** https://www.blackarch.org/

**Mail:** team@blackarch.org

**IRC:** [irc://irc.freenode.net/blackarch](irc://irc.freenode.net/blackarch)
