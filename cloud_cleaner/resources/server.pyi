from .resource import Resource

class Server(Resource):
    def __init__(self, *args, **kwargs): ...

    def register(self, config: CloudCleanerConfig): ...

    def process(self): ...

    def clean(self): ...

    def __process_dates(self): ...

    def __process_names(self): ...

    def __right_name(self, target: Munch) -> bool: ...

    def __right_age(self, target: Munch) -> bool: ...