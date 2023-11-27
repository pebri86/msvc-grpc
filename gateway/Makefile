proto:
	python -m grpc_tools.protoc -I. --python_out=./auth --grpc_python_out=./auth ./auth.proto
	python -m grpc_tools.protoc -I. --python_out=./todo --grpc_python_out=./todo ./todo.proto
run:
	ENV=dev python3 server.py --reload