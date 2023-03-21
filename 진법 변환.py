{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPTPWOFEXXS9brkDvZyILQq",
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
        "<a href=\"https://colab.research.google.com/github/yunhyeok374/DeliveryAdmin/blob/main/%08%EC%A7%84%EB%B2%95%20%EB%B3%80%ED%99%98.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **테스트 코드**"
      ],
      "metadata": {
        "id": "AHpMJOni4srI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 테스트 코드 작성\n",
        "\n",
        "# q1 < q2\n",
        "\n",
        "def ItFrac(q1, q2):\n",
        "  x1, yㅣ1 = q1\n",
        "  x2, y2 = q2\n",
        "  return x1 * y2 < x2 * y1\n",
        "\n",
        "\n",
        "def test_ItFrac():\n",
        "  assert ItFrac((1,2), (1, 3)) == False\n",
        "  assert ItFrac((3,5), (2, 3)) == True\n",
        "  assert ItFrac((1,4), (1, 4)) == False\n",
        "  assert ItFrac((0,1), (1, 1)) == True\n",
        "  assert ItFrac((5,1), (10, 5)) == False\n",
        "\n",
        "  # 분모가 0인 경우\n",
        "  assert ItFrac((1, 0), (1, 1)) == False\n",
        "  assert ItFrac((1, 1), (0, 0)) == False  \n",
        "\n",
        "\n",
        "test_ItFrac()\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "# q1 > q2\n",
        "def gtFrac(q1, q2):\n",
        "  x1, y1 = q1 \n",
        "  x2, y2 = q2\n",
        "  return x1*y2 > x2*y1\n",
        "\n",
        "def test_gtFrac():\n",
        "  assert gtFrac((1,2), (1, 3)) == True \n",
        "  assert gtFrac((3,5), (2, 3)) == False\n",
        "  assert gtFrac((1,6), (1,7)) == True\n",
        "  assert gtFrac((5,5), (1,1)) == False\n",
        "  assert gtFrac((3,2), (1,2)) == True\n",
        "\n",
        "   # 분모가 0인 경우\n",
        "  assert ItFrac((1, 0), (1, 1)) == False\n",
        "  assert ItFrac((1, 1), (0, 0)) == False \n",
        "\n",
        "\n",
        "test_gtFrac()\n",
        "\n"
      ],
      "metadata": {
        "id": "-NwKHg-nqK9i"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#q1 <= q2  \n",
        "\n",
        "def leFrac(q1, q2):\n",
        "  x1, y1 = q1\n",
        "  x2, y2 = q2\n",
        "  return x1*y2 <= x2*y1\n",
        "\n",
        "\n",
        "def test_leFrac():\n",
        "    # 두 분수가 같은 경우\n",
        "    assert leFrac((1, 2), (1, 2)) == True\n",
        "\n",
        "    # 첫 번째 분수가 두 번째 분수보다 작은 경우\n",
        "    assert leFrac((1, 2), (1, 3)) == False\n",
        "    assert leFrac((2, 3), (3, 4)) == True\n",
        "\n",
        "    # 첫 번째 분수가 두 번째 분수보다 큰 경우\n",
        "    assert leFrac((1, 3), (1, 2)) == True\n",
        "    assert leFrac((3, 4), (2, 3)) == False\n",
        "\n",
        "    # 분모가 0인 경우\n",
        "    assert leFrac((1, 0), (1, 1)) == False\n",
        "    assert leFrac((1, 1), (0, 0)) == True\n",
        "\n",
        "test_leFrac() \n",
        "\n",
        "# q1 >= q2\n",
        "def geFrac(q1, q2):\n",
        "  x1, y1 = q1 \n",
        "  x2, y2 = q2\n",
        "  return x1*y2 >= x2*y1\n",
        "\n",
        "\n",
        "def test_geFrac():\n",
        "    # 두 분수가 같은 경우\n",
        "    assert geFrac((1, 2), (1, 2)) == True\n",
        "\n",
        "    # 첫 번째 분수가 두 번째 분수보다 큰 경우\n",
        "    assert geFrac((1, 2), (1, 3)) == True\n",
        "    assert geFrac((3, 4), (2, 3)) == True\n",
        "\n",
        "    # 첫 번째 분수가 두 번째 분수보다 작은 경우\n",
        "    assert geFrac((1, 3), (1, 2)) == False\n",
        "    assert geFrac((2, 3), (3, 4)) == False\n",
        "\n",
        "    # 분모가 0인 경우\n",
        "    assert geFrac((1, 0), (1, 1)) == True\n",
        "    assert geFrac((1, 1), (0, 0)) == True\n",
        "\n",
        "test_geFrac() \n",
        "\n",
        "\n",
        "# q1 == q2\n",
        "def eqFrac(q1, q2):\n",
        "  x1, y1 = q1 \n",
        "  x2, y2 = q2\n",
        "  return x1*y2 == x2*y1\n",
        "\n",
        "\n",
        "def test_eqFrac():\n",
        "    # 두 분수가 같은 경우\n",
        "    assert eqFrac((1, 2), (1, 2)) == True\n",
        "    assert eqFrac((2, 3), (4, 6)) == True\n",
        "\n",
        "    # 두 분수가 다른 경우\n",
        "    assert eqFrac((1, 2), (1, 3)) == False\n",
        "    assert eqFrac((2, 3), (3, 4)) == False\n",
        "\n",
        "    # 분모가 0인 경우\n",
        "    assert eqFrac((1, 0), (1, 1)) == False\n",
        "    assert eqFrac((1, 1), (0, 0)) == True\n",
        "\n",
        "test_eqFrac() "
      ],
      "metadata": {
        "id": "6A4OtTjYoYq4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **1번**"
      ],
      "metadata": {
        "id": "b3ksFmSW45rM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import math # math.lcm, math.gcd 등등 활용을 위해 import\n",
        "\n",
        "# 통분해서 계산하고 결과는 약분해서\n",
        "def addFrac(q1, q2):\n",
        "  pass\n",
        "\n",
        "# 통분해서 계산하고 결과는 약분해서\n",
        "def subFrac(q1, q2):\n",
        "  pass\n",
        "\n",
        "# q1을 q2로 나눈 몫(정수)과 나머지(유리수)를 순서쌍으로 리턴\n",
        "# 나머지도 유리수이므로 마찬가지로 약분한 결과로\n",
        "def divFrac(q1, q2):\n",
        "  pass"
      ],
      "metadata": {
        "id": "wa7fvHu4vl_B"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "\n",
        "def addFrac(q1, q2):\n",
        "  x1, y1 = q1\n",
        "  x2, y2 = q2\n",
        "\n",
        "\n",
        "  # 최소 공배수 계산\n",
        "\n",
        "  lcm = (y1 * y2) // math.gcd(y1, y2)\n",
        "\n",
        "  # 분자를 공통 분모로 만들어서 더해주기\n",
        "\n",
        "  x = x1 * (lcm // y1) + x2 * (lcm // y2) \n",
        "\n",
        "  gcd = math.gcd(x, lcm)\n",
        "  x //= gcd\n",
        "  lcm //= gcd\n",
        "\n",
        "  return (x, lcm)\n",
        "\n",
        "\n",
        "  # addFrac 테스트 코드\n",
        "\n",
        "#case 1:\n",
        "def test_addFrac1():\n",
        "  q1 = (3, 4)\n",
        "  q2 = (1, 2)\n",
        "  result = addFrac(q1, q2)\n",
        "  return result\n",
        "\n",
        "test_addFrac1()\n",
        "\n",
        "#case 2: (약분이 가능한지 확인)\n",
        "def test_addFrac2():\n",
        "  q1 = (3 ,10)\n",
        "  q2 = (5, 10)\n",
        "  result = addFrac(q1, q2)\n",
        "  return result\n",
        "\n",
        "test_addFrac2()\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "JDVXDT8H0iVc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "def subFrac(q1, q2):\n",
        "  x1, y1 = q1\n",
        "  x2, y2 = q2\n",
        "\n",
        "\n",
        "  # 두 분수의 분모의 최소 공배수를 계산합니다.\n",
        "  lcm = (y1 * y2) // math.gcd(y1, y2)\n",
        "\n",
        "  #분자를 공통 분모로 만들어주고 빼주기\n",
        "  x = x1 * (lcm // y1) - x2 * (lcm // y2)\n",
        "\n",
        "  gcd = math.gcd(x, lcm)\n",
        "  x //= gcd\n",
        "  lcm //= gcd\n",
        "\n",
        "  return (x, lcm)\n",
        "\n",
        "\n",
        "  #subFrac 테스트 코드\n",
        "\n",
        "\n",
        "  #테스트 1: 두 분수의 분자가 같고 분모가 다른 경우\n",
        "\n",
        "  q1 = (3,4)\n",
        "  q2 = (3,8)\n",
        "  result = subFrac(q1,q2)\n",
        "  print(result)\n",
        "\n",
        "\n",
        "  #테스트 2: 두 분수의 분모가 같고 분자가 다른 경우\n",
        "  q1 = (1, 4)\n",
        "  q2 = (3, 4)\n",
        "  result = subFrac(q1, q2)\n",
        "  print(result)\n",
        "\n",
        "  #테스트 3: 두 분수의 분자와 분모가 모두 다른 경우\n",
        "  q1 = (1, 5)\n",
        "  q2 = (3, 7)\n",
        "  result = subFrac(q1, q2)\n",
        "  print(result)\n",
        "\n",
        "\n",
        "  \n",
        "\n"
      ],
      "metadata": {
        "id": "yfD3hv0y2KDd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import  math\n",
        "\n",
        "def divFrac(q1,q2):\n",
        "  #분수 q1과 q2의 분자와 분모를 얻습니다.\n",
        "\n",
        "  x1, y1 = q1\n",
        "  x2, y2 = q2\n",
        "\n",
        "  # 두 분수를 나눈다\n",
        "\n",
        "  x = x1 * y2\n",
        "  y = x2 * y1\n",
        "\n",
        "\n",
        "  #결과 분수를 약분한다.\n",
        "\n",
        "  gcd = math.gcd(x, y)\n",
        "  x //= gcd\n",
        "  y //= gcd\n",
        "\n",
        "  return(x, y)\n",
        "\n",
        "\n",
        "#테스트 코드\n",
        "# 테스트 1: 두 분수의 분자와 분모가 모두 같은 경우\n",
        "\n",
        "q1 = (1, 2)\n",
        "q2 = (1, 2)\n",
        "result = divFrac(q1, q2)\n",
        "print(result)\n",
        "\n",
        "\n",
        "#테스트 2: 첫 번째 분수의 분자가 0인 경우\n",
        "q1 = (0, 3)\n",
        "q2 = (2, 5)\n",
        "result = divFrac(q1, q2)\n",
        "print(result)\n",
        "\n",
        "\n",
        "#테스트 3: 두 분수의 분모가 같고 분자가 서로 다른 경우\n",
        "q1 = (1, 4)\n",
        "q2 = (3, 4)\n",
        "result = divFrac(q1, q2)\n",
        "print(result)\n",
        "\n",
        "\n",
        "#테스트 4: 두 분수의 분자가 분모가 모두 다른 경우\n",
        "q1 = (1, 5)\n",
        "q2 = (3, 7)\n",
        "result = divFrac(q1, q2)\n",
        "print(result)\n",
        "\n"
      ],
      "metadata": {
        "id": "75UwxBAS3W2S",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2b1d9456-c1c1-495f-faf6-c7365dde9f26"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1, 1)\n",
            "(0, 1)\n",
            "(1, 3)\n",
            "(7, 15)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **문제 2번**"
      ],
      "metadata": {
        "id": "gsQKhYKV7DJI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "지금바"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "ogARgtbq-YV0",
        "outputId": "e57e0b8d-5c39-4d12-f324-60930e5d3d8b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'0b101'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 83
        }
      ]
    }
  ]
}