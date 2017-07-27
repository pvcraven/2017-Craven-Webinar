Tip 2
=====

Use a good tool-chain

I suggest using:
* PyCharm as an IDE to write the material
* Restructured Text (rst)
* Sphinx - http://www.sphinx-doc.org
* Git
* "Read the Docs" https://readthedocs.org/

(Show building the docs in PyCharm)

Including source snippets:

.. code-block:: python

    print("This will appear in your docs as formatted code.")

Showing longer code samples that are in other files:

.. literalinclude:: ../../examples/bouncing_ball.py
    :caption: bouncing_ball.py
    :linenos:

For arcade, I use this for a lot of samples:
http://arcade.academy/examples/index.html

