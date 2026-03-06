from slowapi import Limiter
from slowapi.util import get_remote_address

# This protects your Groq/OpenAlex limits
limiter = Limiter(key_func=get_remote_address)
