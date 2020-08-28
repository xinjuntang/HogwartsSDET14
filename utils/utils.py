#! /user/bin/env python
# encoding: utf-8
import yaml


def yamlload(path):
    """
    提供yaml文件路径，加载yaml数据文件
    :param path: yaml文件路径
    :return: 返回加载后的数据内容
    """
    file_data = open(path, 'r', encoding='utf-8').read()
    yaml_data = yaml.load(file_data, Loader=yaml.FullLoader)
    return yaml_data
