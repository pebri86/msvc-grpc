# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import todo_pb2 as todo__pb2


class TodoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTodo = channel.unary_unary(
                '/todo.TodoService/CreateTodo',
                request_serializer=todo__pb2.CreateTodoRequest.SerializeToString,
                response_deserializer=todo__pb2.CreateTodoResponse.FromString,
                )
        self.GetTodos = channel.unary_unary(
                '/todo.TodoService/GetTodos',
                request_serializer=todo__pb2.GetTodosRequest.SerializeToString,
                response_deserializer=todo__pb2.GetTodosResponse.FromString,
                )
        self.GetTodo = channel.unary_unary(
                '/todo.TodoService/GetTodo',
                request_serializer=todo__pb2.GetTodoRequest.SerializeToString,
                response_deserializer=todo__pb2.GetTodoResponse.FromString,
                )
        self.UpdateTodo = channel.unary_unary(
                '/todo.TodoService/UpdateTodo',
                request_serializer=todo__pb2.UpdateTodoRequest.SerializeToString,
                response_deserializer=todo__pb2.UpdateTodoResponse.FromString,
                )
        self.DeleteTodo = channel.unary_unary(
                '/todo.TodoService/DeleteTodo',
                request_serializer=todo__pb2.DeleteTodoRequest.SerializeToString,
                response_deserializer=todo__pb2.DeleteTodoResponse.FromString,
                )


class TodoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTodos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTodo,
                    request_deserializer=todo__pb2.CreateTodoRequest.FromString,
                    response_serializer=todo__pb2.CreateTodoResponse.SerializeToString,
            ),
            'GetTodos': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodos,
                    request_deserializer=todo__pb2.GetTodosRequest.FromString,
                    response_serializer=todo__pb2.GetTodosResponse.SerializeToString,
            ),
            'GetTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTodo,
                    request_deserializer=todo__pb2.GetTodoRequest.FromString,
                    response_serializer=todo__pb2.GetTodoResponse.SerializeToString,
            ),
            'UpdateTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTodo,
                    request_deserializer=todo__pb2.UpdateTodoRequest.FromString,
                    response_serializer=todo__pb2.UpdateTodoResponse.SerializeToString,
            ),
            'DeleteTodo': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTodo,
                    request_deserializer=todo__pb2.DeleteTodoRequest.FromString,
                    response_serializer=todo__pb2.DeleteTodoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todo.TodoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TodoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.TodoService/CreateTodo',
            todo__pb2.CreateTodoRequest.SerializeToString,
            todo__pb2.CreateTodoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTodos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.TodoService/GetTodos',
            todo__pb2.GetTodosRequest.SerializeToString,
            todo__pb2.GetTodosResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.TodoService/GetTodo',
            todo__pb2.GetTodoRequest.SerializeToString,
            todo__pb2.GetTodoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.TodoService/UpdateTodo',
            todo__pb2.UpdateTodoRequest.SerializeToString,
            todo__pb2.UpdateTodoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.TodoService/DeleteTodo',
            todo__pb2.DeleteTodoRequest.SerializeToString,
            todo__pb2.DeleteTodoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
