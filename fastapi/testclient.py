import inspect
import asyncio

class Response:
    def __init__(self, data):
        self.status_code = 200
        self._data = data

    def json(self):
        if hasattr(self._data, "dict"):
            return self._data.dict()
        return self._data

class TestClient:
    def __init__(self, app):
        self.app = app

    def _call(self, method, path, json=None):
        func = self.app.routes[(method, path)]
        if json is not None:
            sig = inspect.signature(func)
            params = list(sig.parameters.values())
            if params:
                anno = params[0].annotation
                if anno is inspect.Parameter.empty:
                    arg = json
                else:
                    arg = anno(**json)
                result = func(arg)
            else:
                result = func()
        else:
            result = func()
        if inspect.iscoroutine(result):
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            result = loop.run_until_complete(result)
        return Response(result)

    def get(self, path):
        return self._call('GET', path)

    def post(self, path, json):
        return self._call('POST', path, json=json)
