.. image:: https://media.githubusercontent.com/media/aeroxis/gypse/master/images/logo.png
    :target: https://pypi.org/project/gypse/

.. image:: https://travis-ci.org/aeroxis/gypse.svg?branch=master
   :target: https://travis-ci.org/aeroxis/gypse

What is Gypse?
--------------

Have you ever tried looking for interesting things like URLs, E-Mails or Phone numbers in a bunch of text files? 
That is going to get really tough, really fast. It can be downright painful. 

Gypse is here to help. You simply install 'gypsy' with 'pip', and have Gypse look at your text files.

.. image:: https://media.githubusercontent.com/media/aeroxis/gypse/master/images/gypsy_screen_grab.gif
    :target: https://pypi.org/project/gypse/

Requirements
------------

You will need Python 3.4 or higher for Gypse to work properly

Getting Started
---------------

    pip install gypse

Usage
-----

Gypsy comes with some sample data that you can clone and play with.

    git clone https://github.com/aeroxis/gypse /tmp/gypsy
    cd /tmp/gypsy
    gypse url-extractor ./samples/ --margins 5

This will yield something like the following: