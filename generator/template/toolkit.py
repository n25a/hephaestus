
def make_toolkit(project_name: str) -> None:
    """
    Make toolkit folder.

    :param project_name: project name in string type (e.g. my_project)
    """

    with open(f'{project_name}/internals/toolkit/toolkit.py', 'w') as toolkit:
        toolkit.write('from typing import Optional')
        toolkit.write('from rest_framework.response import Response\n\n')

        toolkit.write('# ERROR is error type')
        toolkit.write('ERROR = Optional[Response]\n\n\n')

        toolkit.write('def validate_error(serialized) -> ERROR:\n')
        toolkit.write('    """\n')
        toolkit.write('    response validation error\n')
        toolkit.write('    """\n')
        toolkit.write('    return Response(\n')
        toolkit.write('        {\n')
        toolkit.write("            'status': 'fail',\n")
        toolkit.write("            'data': serialized.errors,\n")
        toolkit.write('        },\n')
        toolkit.write('        status=400,\n')
        toolkit.write('    )\n\n\n')
        toolkit.write('def existence_error(object_name: str) -> ERROR:\n')
        toolkit.write('    """\n')
        toolkit.write('    response existence error\n')
        toolkit.write('    """\n')
        toolkit.write('    return Response(\n')
        toolkit.write('        {\n')
        toolkit.write("            'status': 'error',\n")
        toolkit.write("            'message': 'Object {} does not exist!'.format(object_name),\n")
        toolkit.write('        },\n')
        toolkit.write('        status=400,\n')
        toolkit.write('    )\n\n\n')
        toolkit.write('def response_creator(\n')
        toolkit.write('    data: Optional[dict, str] = None,\n')
        toolkit.write('    status_code: int = 200,\n')
        toolkit.write('    json_type: bool = False,\n')
        toolkit.write('    status: str = "success",\n')
        toolkit.write(') -> Response:\n')
        toolkit.write('    """\n')
        toolkit.write('    create response\n')
        toolkit.write('    """\n')
        toolkit.write('    if json_type:\n')
        toolkit.write('        return {\n')
        toolkit.write("            'status': status,\n")
        toolkit.write("            'data': data,\n")
        toolkit.write('        }\n\n')
        toolkit.write('    return Response(\n')
        toolkit.write('        {\n')
        toolkit.write("            'status': status,\n")
        toolkit.write("            'data': data,\n")
        toolkit.write('        },\n')
        toolkit.write('        status=status_code,\n')
        toolkit.write('    )\n\n')

    with open(f'{project_name}/internals/toolkit/__init__.py', 'w') as toolkit_init:
        toolkit_init.write('from toolkit import validate_error, response_creator, existence_error, ERROR\n\n')

