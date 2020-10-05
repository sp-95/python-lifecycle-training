============
EditorConfig
============

What is EditorConfig?
---------------------

EditorConfig helps maintain consistent coding styles for multiple developers working on
the same project across various editors and IDEs. The EditorConfig project consists of
**a file format** for defining coding styles and a collection of **text editor plugins**
that enable editors to read the file format and adhere to defined styles. EditorConfig
files are easily readable and they work nicely with version control systems.

When opening a file, EditorConfig plugins look for a file named ``.editorconfig`` in the
directory of the opened file and in every parent directory. A search for
``.editorconfig`` files will stop if the root filepath is reached or an EditorConfig
file with ``root=true`` is found.

EditorConfig files are read top to bottom and the most recent rules found take
precedence. Properties from matching EditorConfig sections are applied in the order they
were read, so properties in closer files take precedence.

**For Windows Users**: To create an ``.editorconfig`` file within Windows Explorer, you
need to create a file named ``.editorconfig.``, which Windows Explorer will
automatically rename to ``.editorconfig``.

For further details visit https://editorconfig.org/

Instructions
------------

1. Create a ``.editorconfig`` file and add the following:

   .. code-block:: RST

        # top-most EditorConfig file
        root = true

        # Unix-style newlines with a newline ending every file
        [*]
        end_of_line = lf
        insert_final_newline = true

        # Matches multiple files with brace expansion notation
        # Set default charset
        [*.{js,py}]
        charset = utf-8

        # 4 space indentation
        [*.py]
        indent_style = space
        indent_size = 4

        # Tab indentation (no size specified)
        [Makefile]
        indent_style = tab
