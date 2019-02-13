.. Python Project Proto documentation master file, created by
   sphinx-quickstart on Mon Feb 11 09:39:02 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

====================
Python Project Proto
====================

----------
Annotation
----------

This documentation covers simple python project which can be used to grab
links from web page and represent them in one of supported view variants.

--------------
How to install
--------------

Install with ``pip`` from ``github``::

   pip install git+https://github.com/schipiga/ppp.git

----------
How to use
----------

**as user**::

   $ links -h
   usage: links [-h] [--as {text,html,json,yaml}] [--enum] uri

   $ links https://pipedrive.com 
   https://app.pipedrive.com?return_url=https%3A%2F%2Fapp.pipedrive.com%2Fsettings%2Fpersonal%2Fcompanies
   https://www.pipedrive.com/et/terms-of-service
   #signup-form
   https://www.pipedrive.com/et/blog
   ...
   https://www.pipedrive.com/et/pricing

   $ links https://pipedrive.com --enum
   1. https://app.pipedrive.com?return_url=https%3A%2F%2Fapp.pipedrive.com%2Fsettings%2Fpersonal%2Fcompanies
   2. https://www.pipedrive.com/et/terms-of-service
   3. #signup-form
   4. https://www.pipedrive.com/et/blog
   ...
   27. https://www.pipedrive.com/et/pricing

**as developer**::

   >>> import ppp
   >>> print(ppp.links_as_text("https://pipedrive.com", enum=True))
   1. https://www.pipedrive.com/et/features
   2. https://www.pipedrive.com/et/resources
   3. https://www.pipedrive.com/et/blog
   ...
   27. https://www.pipedrive.com/et/sitemap

--------
Packages
--------

.. toctree::
   :maxdepth: 1

   ppp
   loader
   parser
   view
