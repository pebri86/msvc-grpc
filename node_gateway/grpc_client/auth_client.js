const PROTO_PATH = __dirname + "/../protos/auth.proto";

const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");

var packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    arrays: true
});

const auth = grpc.loadPackageDefinition(packageDefinition).auth;
const auth_client = new auth.AuthService(
    "localhost:9000",
    grpc.credentials.createInsecure()
);

module.exports = auth_client;