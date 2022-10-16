from typing import Tuple, Optional, Dict
from internals.toolkit import validate_error, ERROR
from apps.example.serializers import ExampleSerializer


class ExampleRepository:

    def create(data: Dict) -> Tuple[Optional[Dict], ERROR]:
        example_serialized = ExampleSerializer(data=data)
        if not example_serialized.is_valid():
            err = validate_error(example_serialized.errors)
            return None, err
        example_serialized.save()

        return example_serialized.data, None
