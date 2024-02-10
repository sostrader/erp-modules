16.0.1.0.2 (2023-10-09)
~~~~~~~~~~~~~~~~~~~~~~~

**Bugfixes**

- Avoid config error when using the webdav protocol. The auth option is expected
  to be a tuple not a list. Since our config is loaded from a json file, we
  cannot use tuples. The fix converts the list to a tuple when the config is
  related to a webdav protocol and the auth option is into the confix. (`#285 <https://github.com/OCA/storage/issues/285>`_)
