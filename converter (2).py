{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "def feet_to_meters(feet):\n    meters = feet / 0.3048\n    return round(meters, 2)\ndef meters_to_feet(meters):\n    feet = meters * 0.3048\n    return round(feet, 2)\ndef display_title():\n    print('Feet and Meters Converter')\ndef display_menu():\n    print(\"Conversions Menu:\")\n    print(\"a. Feet to Meters\")\n    print(\"b. Meters to Feet\")\ndef main():\n    while True:\n        display_title()\n        display_menu()\n        choice = input()\n        if choice == 'a':\n            feet = float(input(\"Enter feet: \"))\n            result = feet_to_meters(feet)\n            print(f\"{feet} feet is {result} meters.\")\n        elif choice == 'b':\n            meters = float(input(\"Enter meters: \"))\n            result = meters_to_feet(meters)\n            print(f\"{meters} meters is {result} feet.\")\n        another_conversion = input(\"Would you like to perform another conversion? (y/n): \")\n        if another_conversion != 'y':\n            break\nif __name__ == \"__main__\":\n    main()",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}