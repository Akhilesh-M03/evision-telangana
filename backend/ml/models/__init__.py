"""Models package initialization.

Exposes base classes and model registry mechanisms.
"""

from ml.models.base import BaseModel
from ml.models.registry import ModelRegistry

__all__ = ["BaseModel", "ModelRegistry"]
