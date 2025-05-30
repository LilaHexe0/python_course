# (C) 2025 A.Voß, a.voss@fh-aachen.de, info@codebasedlearning.dev

"""
This snippet discusses class level methods.

Teaching focus
  - use cases for class level methods
"""

from typing import Self                     # from Python 3.11


class Temperature:
    """ temperature class with class level methods """
    def __init__(self, fahrenheit: float) -> None:
        self.fahrenheit = fahrenheit

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """ converts Celsius to Fahrenheit """
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """ converts Fahrenheit to Celsius """
        return (fahrenheit - 32) * 5 / 9

    @classmethod
    def from_celsius(cls, celsius: float) -> Self:     # Temperature not defined yet
        """ factory method to create Temperature instance from Celsius """
        fahrenheit = cls.celsius_to_fahrenheit(celsius)
        return cls(fahrenheit)

    def __str__(self):
        return f"{self.fahrenheit}°F"


class OptimizedTemperature(Temperature):
    pass                                    # a nop


def show_class_level_functions():
    """ show class level functions """
    print("\nshow_class_level_functions\n==========================")

    # using static methods for conversion
    freeze_c = 0
    freeze_f = Temperature.celsius_to_fahrenheit(freeze_c)
    body_f = 98.6
    body_c = Temperature.fahrenheit_to_celsius(body_f)
    print(f" 1| Freeze: {freeze_c}°C={freeze_f}°F")
    print(f" 2| Body:   {body_f}°F={body_c}°C")

    # using class method to create an instance from Celsius
    boil_f = Temperature.from_celsius(100)
    print(f" 3| Boil:   {boil_f}, {boil_f.__dict__}")
    print(f" 4| {Temperature.__dict__=}")

    # note the type
    boil_opt = OptimizedTemperature.from_celsius(100)
    print(f" 5| {boil_opt}, {type(boil_opt)=}")


if __name__ == '__main__':
    show_class_level_functions()


###############################################################################


"""
Summary

Topics
  - @staticmethod
  - @classmethod

Static Methods:
  - `celsius_to_fahrenheit` and `fahrenheit_to_celsius` convert temperature 
    values but don’t depend on any class or instance.
  - These are utility methods grouped logically within the `Temperature` class.
  - Use `@staticmethod` for utility/helper methods that don’t need class or 
    instance context (e.g., mathematical functions, converters, etc.).

Class Method:
  - `from_celsius` creates a `Temperature` instance using Celsius instead 
    of Fahrenheit.
  - It uses the `cls` parameter to create the class instance and calls the 
    static method `celsius_to_fahrenheit` for conversion.
  - Use `@classmethod` for methods that need class-level context (e.g., 
    factory methods, altering class variables, polymorphic behavior).
  - If you replace `cls` with the hard-coded class name (`Temperature`), 
    the method will always use `Temperature` for instantiation, even when 
    invoked from a subclass. This breaks the principle of polymorphism and 
    can lead to incorrect behavior in multiple inheritance scenarios.

See also
  - https://docs.python.org/3/library/functions.html
  - https://de.wikipedia.org/wiki/Grad_Celsius
"""
