from typing import Optional
from rest_framework.response import Response


# ERROR is error type
ERROR = Optional[Response]


def validate_error(serialized) -> ERROR:
    """
    response validation error
    """
    return Response(
        {
            'status': 'fail',
            'data': serialized.errors,
        },
        status=400,
    )


def existence_error(object_name: str) -> ERROR:
    """
    response existence error
    """
    return Response(
        {
            'status': 'error',
            'message': 'Object {} does not exist!'.format(object_name),
        },
        status=400,
    )


def response_creator(
    data: Optional[dict, str] = None,
    status_code: int = 200,
    json_type: bool = False,
    status: str = "success",
) -> Response:
    """
    create response
    """
    if json_type:
        return {
            'status': status,
            'data': data,
        }

    return Response(
        {
            'status': status,
            'data': data,
        },
        status=status_code,
    )

