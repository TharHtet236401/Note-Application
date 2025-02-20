# HTTP Success Status Codes
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_204_NO_CONTENT = 204

# HTTP Client Error Status Codes
HTTP_400_BAD_REQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404
HTTP_409_CONFLICT = 409

# HTTP Server Error Status Codes
HTTP_500_INTERNAL_SERVER_ERROR = 500

status_codes = {
    'success': 200, # Success
    'created': 201, # Created
    'bad_request': 400, # Bad Request
    'not_found': 404, # Not Found
    'internal_server_error': 500, # Internal Server Error
    'unauthorized': 401, # Unauthorized
    'forbidden': 403, # Forbidden
    'not_acceptable': 406, # Not Acceptable
    'request_timeout': 408, # Request timeout
    'conflict': 409, # Conflict
    'gone': 410, # Gone
    'length_required': 411, # Length Required
    'precondition_failed': 412, # Precondition Failed
    'payload_too_large': 413, # Payload Too Large
    'uri_too_long': 414, # URI Too Long
    'unsupported_media_type': 415, # Unsupported Media Type
    'range_not_satisfiable': 416, # Range Not Satisfiable
    'expectation_failed': 417, # Expectation Failed
    'teapot': 418, # I'm a teapot
    'misdirected_request': 421, # Misdirected Request
    'unprocessable_entity': 422, # Unprocessable Entity
    'locked': 423, # Locked
    'failed_dependency': 424, # Failed Dependency
    
}
