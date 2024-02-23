{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "name": ""
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "TAX_RATE = 0.06\ndef calculate_tax(total):\n    tax = total * TAX_RATE\n    return round(tax, 2)\ndef calculate_total_after_tax(total):\n    tax = calculate_tax(total)\n    total_after_tax = total + tax\n    return round(total_after_tax, 2)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}