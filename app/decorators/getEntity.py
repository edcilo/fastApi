from fastapi import HTTPException, status


def getEntity(repository):
    def decorator(func):
        def wrapper(self, id, *args, **kwargs):
            repo = repository()
            entity = repo.get_by_id(id)
            if entity is None:
                raise HTTPException(status_code=404, detail="Not Found")
            return func(self, entity, *args, **kwargs)
        return wrapper
    return decorator
