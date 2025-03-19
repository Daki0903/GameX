# gamex/__init__.py

from .core import GameEngine
from .sprites import Sprite
from .sound import Sound
from .images import load_image
from .physics import Physics

__version__ = "0.1.0"
__all__ = ["GameEngine", "Sprite", "Sound", "load_image", "Physics"]
