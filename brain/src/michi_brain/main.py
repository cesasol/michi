from jsonrpcserver import method, serve, Success

@method
def ping():
    return Success("pong")

if __name__ == "__main__":
    serve()

