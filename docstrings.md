# Docstrings

## Sections

- [Docstrings](#docstrings)
  - [Sections](#sections)
  - [Method docstring](#method-docstring)
  - [Class docstring](#class-docstring)
  - [Module docstring](#module-docstring)

## Method docstring

```python
r"""Summarize the function in one line.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    *args : iterable
        Other arguments.
    long_var_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.
    **kwargs : dict
        Keyword arguments.

    Returns
    -------
    type
        Explanation of anonymous return value of type ``type``.
    describe : type
        Explanation of return value named `describe`.
    out : type
        Explanation of `out`.
    type_without_description

    Other Parameters
    ----------------
    only_seldom_used_keywords : type
        Explanation.
    common_parameters_listed_above : type
        Explanation.

    Raises
    ------
    BadException
        Because you shouldn't have done that.

    See Also
    --------
    numpy.array : Relationship (optional).
    numpy.ndarray : Relationship (optional), which could be fairly long, in
                    which case the line wraps here.
    numpy.dot, numpy.linalg.norm, numpy.eye

    Notes
    -----
    Notes about the implementation algorithm (if needed).

    This can have multiple paragraphs.

    You may include some math:

    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

    And even use a Greek symbol like :math:`\omega` inline.

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> a = [1, 2, 3]
    >>> print([x + 3 for x in a])
    [4, 5, 6]
    >>> print("a\nb")
    a
    b
    """
```

Source: https://gist.github.com/jakevdp/3808292

## Class docstring

```python
r"""The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes
    ----------
    attr1 : str
        Description of `attr1`.
    attr2 : :obj:`int`, optional
        Description of `attr2`.

    Parameters
    ----------
    attr1 : str
        Description of `attr1`.
    attr2 : :obj:`int`, optional
        Description of `attr2`.

    Methods
    ----------
    method_name(c='rgb')
        Description of public `method_name`.
    method_name(signature)
        Description of public `method_name`.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> from view_api.models import APIInfo
    >>> a1 = APIInfo(
    ...     name = "APOD",
    ...     description = "Astronomy Picture of the Day",
    ...     link = "https://api.nasa.gov/planetary/apod",
    ...     image = "img/1.jpg",
    ... )
    >>> a1.save()
    asyncio - 2020-10-18 05:53:05,483-5384-DEBUG-Using proactor: IocpProactor
    >>> a2 = APIInfo(
    ...     name = "EPIC",
    ...     description = "Latest Images from Earth Polychromatic Imaging Camera",
    ...     link = "https://api.nasa.gov/EPIC/api/natural",
    ...     image = "img/2.png",
    ... )
    >>> ...
    >>> a2.save()
    """
```

Source: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html

## Module docstring

```python
r"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
```
