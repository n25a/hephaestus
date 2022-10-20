def make_repository(project_name: str) -> None:
    """
    Make repository.

    :param project_name: project name
    """
    with open(f"{project_name}/internals/repositories/example.py", "w") as repository:
        repository.write("from typing import Tuple, Optional, Dict\n")
        repository.write("from internals.toolkit import validate_error, ERROR\n")
        repository.write("from apps.example.serializers import ExampleSerializer\n\n\n")
        repository.write("class ExampleRepository:\n\n")
        repository.write("    def create(self, data: Dict) -> Tuple[Optional[Dict], ERROR]:\n")
        repository.write("        example_serialized = ExampleSerializer(data=data)\n")
        repository.write("        if not example_serialized.is_valid():\n")
        repository.write("            err = validate_error(example_serialized.errors)\n")
        repository.write("            return None, err\n")
        repository.write("        example_serialized.save()\n\n")
        repository.write("        return example_serialized.data, None\n")
