const auth_client = require("../grpc_client/auth_client");
const logger = require("../logger")

module.exports = (req, res, next) => {
    try {
        if (!req.headers.authorization){
            res.status(401).json({
                success: false,
                message: "Missing token"
            });
        } else {
            const token = req.headers.authorization.split(' ')[1];
    
            let request = {
                token: token
            };

            auth_client.validateToken(request, (err, data) => {
                if (err) {
                    logger.error(data)
                    res.status(401).json({
                        success: false,
                        message: "Invalid request"
                    });
                } else {
                    logger.info("token valid", JSON.parse(data.message).ID);
                    res.set("X-USERID", JSON.parse(data.message).ID)
                    next()
                }
            });
        }
    } catch {
        res.status(401).json({
            success: false,
            message: "Invalid request"
        });
    }
};