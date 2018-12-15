gypsy
#############################


.. image:: https://travis-ci.org/aeroxis/gypsy.svg?branch=master
   :target: https://travis-ci.org/aeroxis/gypsy

What is Gypse?
--------------

Gypse analyzes and reveals information of the text files that you have. It identifies things like URLs, E-Mails and Phone Numbers, which are difficult to extract 

.. image:: https://media.githubusercontent.com/media/aeroxis/gypse/master/images/gypsy_screen_grab.gif
    :target: https://pypi.org/project/gypse/

License
-------

This code is licensed under the `MIT License`_.

.. _`MIT License`: https://github.com/aeroxis/gypsy/blob/master/LICENSE


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