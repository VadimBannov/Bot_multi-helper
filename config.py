BOT_TOKEN = ""  # подставь свой токен

GPT_LOCAL_URL = ""  # подставь свой локальный url-адрес
HEADERS = {"Content-Type": "application/json"}
MAX_TOKENS = 200

LINK_IMAGE = {
    0: "https://ibb.co/NNrHCwZ"
}


PROMPTS_TEMPLATES = {
    'Russian language': {
        'beginner': "Ты помощник по русскому языку, давая простые ответы",
        'advanced': "Ты помощник по русскому языку, давая сложные ответы"
    },
    'maths': {
        'beginner': "Ты помощник по математике, давая простые ответы",
        'advanced': "Ты помощник по математике, давая сложные ответы"
    },
    'history': {
        'beginner': "Ты помощник по истории, давая простые ответы",
        'advanced': "Ты помощник по истории, давая сложные ответы"
    }
}
