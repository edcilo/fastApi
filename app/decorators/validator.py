import logging

from fastapi import HTTPException, status


def validator(schema):
    def decorator(fnc):
        def wrapper(self, params, *args, **kwargs):
            try:
                params = schema(**params)
                return fnc(self, params, *args, **kwargs)
            except Exception as e:
                logging.warning(
                    msg=f'{self.request.client.host}:{self.request.client.port} - {e.errors()}')
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=e.errors())
        return wrapper
    return decorator
