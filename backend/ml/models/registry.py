"""Model registry for the EVision Telangana ML Infrastructure.

This module provides a centralized registry for looking up and instantiating
supported machine learning models by type identifier.
"""

from typing import Any, Dict, Type

from ml.models.base import BaseModel


class ModelRegistry:
    """Central registry mapping model type strings to their class definitions."""

    _registry: Dict[str, Type[BaseModel]] = {}

    @classmethod
    def register(cls, name: str) -> Any:
        """Decorator to register a BaseModel class in the registry.

        Args:
            name: The model type string (e.g. 'random_forest').
        """
        def decorator(subclass: Type[BaseModel]) -> Type[BaseModel]:
            if not issubclass(subclass, BaseModel):
                raise TypeError(f"Registered class must inherit from BaseModel, got {subclass}")
            cls._registry[name] = subclass
            return subclass

        return decorator

    @classmethod
    def get_model_class(cls, name: str) -> Type[BaseModel]:
        """Retrieve a registered model class by its type name.

        Args:
            name: The registered model type identifier.

        Returns:
            The registered class inheriting from BaseModel.
        """
        if name not in cls._registry:
            raise KeyError(
                f"Model type '{name}' is not registered. "
                f"Available model types: {list(cls._registry.keys())}"
            )
        return cls._registry[name]
