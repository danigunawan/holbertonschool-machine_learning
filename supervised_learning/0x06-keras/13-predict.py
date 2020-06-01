#!/usr/bin/env python3
"""Contains the test_model function"""

import tensorflow as tf


def predict(network, data, verbose=False):
    """
    makes a prediction using a neural network
    :param network:  network model to make the prediction with
    :param data: input data to make the prediction with
    :param verbose: boolean that determines if output
        should be printed during the prediction process
    :return:  prediction for the data
    """
    result = network.predict(data, verbose=verbose)
    return result
