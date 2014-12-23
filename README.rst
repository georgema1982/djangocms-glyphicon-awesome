===========================
djangocms-glyphicon-awesome
===========================

A django app that eases the incorporation of the two ckeditor plugins (http://ckeditor.com/addon/glyphicons and http://ckeditor.com/addon/fontawesome) into djangocms's ckeditor.

Installation
============

To get started using ``djangocms-glyphicon-awesome``:

- install it with ``pip``::

    $ pip install djangocms-glyphicon-awesome

- add the app to ``INSTALLED_APPS`` and make sure it's before ``djangocms_text_ckeditor``::

    INSTALLED_APPS = (
        ...
        'djangocms_glyphicon_awesome',
        'djangocms_text_ckeditor',
        ...
    )

Configuration
=============

You need a ``CKEDITOR_SETTINGS`` in ``settings.py`` that has ``toolbar_CMS`` attribute containing ``Glyphicons``

You can copy the following configuration into your ``settings.py``::

    CKEDITOR_SETTINGS = {
        'language': '{{ language }}',
        'extraPlugins': 'cmsplugins,glyphicons,lineutils,widget',
        'toolbar_CMS': [
            [ 'Source', 'Maximize' ],
            [ 'cmsplugins', '-', 'ShowBlocks' ],
            [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ],
            [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ],
            [ 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField' ],
            [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ],
            [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ],
            [ 'Link', 'Unlink', 'Anchor' ],
            [ 'Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe' ],
            [ 'Styles', 'Format', 'Font', 'FontSize' ],
            [ 'TextColor', 'BGColor'],
            [ 'Glyphicons' ],
        ],
        'contentsCss': 'http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css',
        'skin': 'moono',
    }

Now when you edit any text plugin with ckeditor, you will see a red cross button. Click the button and you will find all the Glyphicons.

Todo
====

Although the app's name suggests that Font Awesome should be included in this app, it's not done in the first release. Would add it in the future release.
