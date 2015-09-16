Title: command alias workflow on mac x
Date: 2015-09-15
Category: technology
Tags:
Slug: 
Author:
Summary: 

I have several linux box which is located in different place. Every time I login in using an anonoying long commmand such as :

> ssh pch@xxxxx  

Especially my password is really long and comlexity. I use the following ways  to figure this out. 
The final output is that when a type 'do' (abbreviation of my Digital Ocean server), it automatially login into the server without password.

# command alias of on-my-zsh
Because I am using the iterm2+on-my-zsh, i edit the ~/.zashrc, add the following lines.

> alias do="ssh pch@x.x.x.x"
alias a="ssh pch@x.x.x.x"
alias b="ssh pch@x.x.x.x"

# automatic login using the key-gen

Note that a@A login to b@B
> a@A:~> ssh-keygen -t rsa
cat .ssh/id_rsa.pub | ssh b@B 'cat >> .ssh/authorized_keys'

enter b's password for the last time.

The reference is [alias](http://computers.tutsplus.com/tutorials/speed-up-your-terminal-workflow-with-command-aliases-and-profile--mac-30515) and [ssh login without password](http://www.linuxproblem.org/art_9.html)  