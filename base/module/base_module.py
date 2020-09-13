#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File     : base_module
# @Author   : 张志毅
# @Time     : 2020/9/12 19:14

import abc
import torch.nn as nn


class BaseModule(nn.Module, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        super(BaseModule, self).__init__()

    @abc.abstractmethod
    def forward(self, dict_: dict) -> dict:
        pass
