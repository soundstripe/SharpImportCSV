==============
SharpImportCSV
==============

This tool can be used to import a CSV file of names and contact information into a Sharp copier.

It uses the built-in web interface on the Sharp.

Currently it does not handle login, as the address book is publicly editable by default.

This tool *does not check for duplicate entries*; if you run it twice you *will* have duplicate entries. Use the ``-s`` flag to simulate a run, without adding any entries to the copier.

========
Usage
========


Run ``sharpimportcsv.py -h`` to view help.

To build an executable, run ``python setup.py py2exe``

To run that exe you may need to install `Microsoft Visual C++ 2008 Redistributable Package`_ (not the SP1 version).

Modify, use, and distribute as you like.

.. _Microsoft Visual C++ 2008 Redistributable Package: http://www.microsoft.com/downloads/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en
