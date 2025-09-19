class HttpError(Exception):
    """Exception raised for HTTP errors during API requests"""
    
    # Error message mapping
    ERROR_MESSAGES = {
        # 400 series - Client errors
        400: "Bad request: The request was malformed or invalid",
        401: "Authentication failed: Token may be invalid or expired",
        403: "Permission denied: Token does not have access to this resource",
        404: "Not found: The requested resource does not exist",
        405: "Method not allowed: The HTTP method is not supported for this resource",
        408: "Request timeout: The server timed out waiting for the request",
        429: "Too many requests: Rate limit exceeded",
        
        # 500 series - Server errors
        500: "Internal server error: Something went wrong on the server",
        502: "Bad gateway: The server received an invalid response from the upstream server",
        503: "Service unavailable: The server is currently unavailable",
        504: "Gateway timeout: The upstream server failed to respond in time"
    }
    
    def __init__(self, status_code, response=None):
        self.status_code = status_code
        self.response = response
        self.message = self.ERROR_MESSAGES.get(status_code, "HTTP Error occurred")
        super().__init__(f"HTTP Error {status_code}: {self.message}")