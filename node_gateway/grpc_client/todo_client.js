const PROTO_PATH = __dirname + "/../protos/todo.proto";

const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");

var packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    arrays: true
});

const todo = grpc.loadPackageDefinition(packageDefinition).todo;
const todo_client = new todo.TodoService(
    "localhost:3000",
    grpc.credentials.createInsecure()
);

module.exports = todo_client;