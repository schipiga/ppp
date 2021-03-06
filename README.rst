====================
Python Project Proto
====================

----------
Annotation
----------

It is simple python project which can be used to grab
links from web page and represent them in one of supported view variants.

--------------
How to install
--------------

**for usage**::

   pip install git+https://github.com/schipiga/ppp.git

**for contribution**::

   git clone https://github.com/schipiga/ppp.git
   cd ppp
   make install
   . .venv/bin/activate

----------
How to use
----------

**as user**::

   $ links -h
   usage: links [-h] [--as {text,html,json,yaml}] [--enum] uri

   Grab web links

   positional arguments:
     uri                   URI to retrieve links from

   optional arguments:
     -h, --help            show this help message and exit
     --as {text,html,json,yaml}
                           Result format type (text by default)
     --enum                Add enumation for links (for text and html only)

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