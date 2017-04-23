# python-colornames

A Python library for finding the names of colors.

The `colornames` library gives you the name of any RGB color. If the exact color you're looking for doesn't have a name, it'll find the closest match instead.


## Usage

A single function, `find`, is exposed by the library. It finds the name of a given color.

```python
>>> import colornames
>>> colornames.find(255, 255, 255)   # Decimal RGB
'White'
>>> colornames.find('#3e3e3e')       # Hexadecimal notation
'Dune'
>>> colornames.find('#abc')          # Shorthand hexadecimal
'Cadet Blue'
>>> colornames.find('f5f5f5')        # Optional '#' prefix
'Wild Sand'
>>> colornames.find((123, 12, 1))    # Decimal RGB as a tuple
'Dark Burgundy'
```


## License

The code is licensed under the MIT license.
Certain parts are licensed under CC BY 2.5 (see [acknowledgements](#acknowledgements)).


## Acknowledgements

The list of color names is based on Chirag Mehta's [ntc js](http://chir.ag/projects/ntc), licensed under [CC BY 2.5](https://creativecommons.org/licenses/by/2.5/).
