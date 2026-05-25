"""
Ollama 客户端实现
=================

Ollama 使用 OpenAI 兼容 API，本地默认地址为 11434 端口。
"""

from .openai_client import OpenAIClient


class OllamaClient(OpenAIClient):
    """
    Ollama 客户端
    
    继承 OpenAI 客户端，使用 OpenAI 兼容 API。
    """
    
    DEFAULT_BASE_URL = "http://127.0.0.1:11434/v1"
    DEFAULT_MODEL = "llama3.1"
    PROVIDER = "ollama"
