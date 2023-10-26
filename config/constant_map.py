# -*- coding: utf-8 -*-
# @Time:  23:20
# @Author: tk
# @File：model_maps
from aigc_zoo.constants.define import (TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING,
                                       TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING)

__all__ = [
    "TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING",
    "TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING",
    "MODELS_MAP"
]




MODELS_MAP = {
    'detr-resnet-50': {
        'model_type': 'detr',
        'model_name_or_path': '/data/nlp/pre_models/torch/detr/detr-resnet-50',
        'config_name': '/data/nlp/pre_models/torch/detr/detr-resnet-50/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/detr/detr-resnet-50',
    },

    'detr-resnet-101': {
        'model_type': 'detr',
        'model_name_or_path': '/data/nlp/pre_models/torch/detr/detr-resnet-101',
        'config_name': '/data/nlp/pre_models/torch/detr/detr-resnet-101/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/detr/detr-resnet-101',
    },
    
    'yolos-base': {
        'model_type': 'yolos',
        'model_name_or_path': '/data/nlp/pre_models/torch/yolos/yolos-base',
        'config_name': '/data/nlp/pre_models/torch/yolos/yolos-base/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/yolos/yolos-base',
    },

    'yolos-small': {
        'model_type': 'yolos',
        'model_name_or_path': '/data/nlp/pre_models/torch/yolos/yolos-small',
        'config_name': '/data/nlp/pre_models/torch/yolos/yolos-small/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/yolos/yolos-small',
    },

    'yolos-tiny': {
        'model_type': 'yolos',
        'model_name_or_path': '/data/nlp/pre_models/torch/yolos/yolos-tiny',
        'config_name': '/data/nlp/pre_models/torch/yolos/yolos-tiny/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/yolos/yolos-tiny',
    },

    'table-transformer': {
        'model_type': 'table-transformer',
        'model_name_or_path': '/data/nlp/pre_models/torch/table-transformer/table-transformer-detection',
        'config_name': '/data/nlp/pre_models/torch/table-transformer/table-transformer-detection/config.json',
        'tokenizer_name': '/data/nlp/pre_models/torch/table-transformer/table-transformer-detection',
    },




}


# 按需修改
# TRANSFORMERS_MODELS_TO_LORA_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_ADALORA_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_IA3_TARGET_MODULES_MAPPING
# TRANSFORMERS_MODELS_TO_IA3_FEEDFORWARD_MODULES_MAPPING




