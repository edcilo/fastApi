from typing import Any, Callable

from fastapi import HTTPException, status

from ..repositories.repository import Repository


def getEntity(repository: Repository):
    def decorator(func: Callable):
        def wrapper(self, id: Any, *args, **kwargs):
            repo = repository()
            entity = repo.get_by_id(id)
            if entity is None:
                raise HTTPException(status_code=404, detail="Not Found")
            return func(self, entity, *args, **kwargs)
        return wrapper
    return decorator
