{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO9sf6Ou8UOdZXS6Jx5kwZr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JhonTroyeMartinez/PLNG211-QC/blob/main/Lab_Activity_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "id": "svqe1AnwJlad",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6dce9b3d-6504-4609-d3d9-fd31dc9852b4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name: Troye Martinez\n",
            "Enter your student number: 2210001107\n",
            "Enter your age: 19\n",
            "Enter your course: BSCS 2-YA-1\n",
            " \n",
            "Name:                   Troye Martinez\n",
            "Student_No:             2210001107\n",
            "Age:                    19\n",
            "School and Course:      BSCS 2-YA-1\n"
          ]
        }
      ],
      "source": [
        "class Student:\n",
        "  def info(myself):\n",
        "    print(\" \")\n",
        "    print(\"Name:                  \",myself.name)\n",
        "    print(\"Student_No:            \",myself.SN)\n",
        "    print(\"Age:                   \",myself.age)\n",
        "    print(\"School and Course:     \",myself.course) \n",
        "r1 = Student()\n",
        "r1.name = input(\"Enter your name: \")\n",
        "r1.SN = int(input(\"Enter your student number: \"))\n",
        "r1.age = int(input(\"Enter your age: \"))\n",
        "r1.course = input(\"Enter your course: \")\n",
        "\n",
        "r1.info()"
      ]
    }
  ]
}