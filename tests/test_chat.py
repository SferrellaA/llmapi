import pytest
from src.chat.complete import complete
from src.client.client import Client
from src.chat.message import Message, MessageHistory
from tests.test_client import client

@pytest.fixture
def chat_mock(requests_mock):
    # From https://platform.openai.com/docs/api-reference/chat/object
    requests_mock.post("https://api.example.com/v1/chat/completions", json={
        "id": "chatcmpl-B9MBs8CjcvOU2jLn4n570S5qMJKcT",
        "object": "chat.completion",
        "created": 1741569952,
        "model": "gpt-4.1-2025-04-14",
        "choices": [
            {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Hello! How can I assist you today?",
                "refusal": None,
                "annotations": []
            },
            "logprobs": None,
            "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 19,
            "completion_tokens": 10,
            "total_tokens": 29,
            "prompt_tokens_details": {
            "cached_tokens": 0,
            "audio_tokens": 0
            },
            "completion_tokens_details": {
            "reasoning_tokens": 0,
            "audio_tokens": 0,
            "accepted_prediction_tokens": 0,
            "rejected_prediction_tokens": 0
            }
        },
        "service_tier": "default"
        }
    )

@pytest.fixture
def chat_history():
    mh = MessageHistory()
    mh.System("You are a helpful assistant")
    mh.User("Hello!")
    return mh

# TODO - make this better
def test_asdf(chat_mock, chat_history, client):
    c = complete(client, chat_history, "asdf")
    assert type(c) == Message
    assert str(c) == "assistant: Hello! How can I assist you today?"
