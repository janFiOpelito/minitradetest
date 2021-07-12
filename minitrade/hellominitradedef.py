# Copyright © 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""A function hello minitrade  and addition for crypto.

test coverage -> pytest -v --cov=minitrade --cov-report=html
"""

def hello_minitrade():
    """ hello mini trade function

    :param : none
    :type : none

    :return: hello_mini_trade
    :rtype: string
    """
    return "hello_mini_trade"

def add_crypto_trade(a,b):
    """ addition

    :param : a
    :type : int
    :param : b
    :type : int

    :return: a+b
    :rtype: int
    """
    return a+b
