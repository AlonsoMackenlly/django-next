from pathlib import Path

from decouple import AutoConfig

# Build paths inside the project like this: BASE_DIR.joinpath('some')
# `pathlib` is better than writing: dirname(dirname(dirname(__file__)))
BASE_DIR = Path(__file__).parent.parent

# Loading `.env` files
# See docs: https://gitlab.com/mkleehammer/autoconfig
env = AutoConfig(search_path=BASE_DIR)
