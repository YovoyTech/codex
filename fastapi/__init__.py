import inspect
import asyncio

class APIRouter:
    def __init__(self):
        self.routes = {}

    def get(self, path):
        def decorator(func):
            self.routes[("GET", path)] = func
            return func
        return decorator

    def post(self, path, response_model=None):
        def decorator(func):
            self.routes[("POST", path)] = func
            return func
        return decorator

class FastAPI:
    def __init__(self, title=None):
        self.routes = {}
    def include_router(self, router):
        self.routes.update(router.routes)

