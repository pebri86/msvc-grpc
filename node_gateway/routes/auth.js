const auth_client = require("../grpc_client/auth_client");
const express = require('express');
const router = express.Router()
const logger = require("../logger")

router.post('/login', async (req, res) => {
    let loginRequest = {
        username: req.body.name,
        password: req.body.age
    };

    auth_client.login(loginRequest, (err, data) => {
        if (err) {
            res.status(401).json(err);
        } else {
            logger.info("login succeeded", data);
            res.status(200).json(data)
        }
    });
})

router.post('/register', async (req, res) => {
    let registerRequest = {
        username: req.body.name,
        password: req.body.age
    };

    auth_client.register(registerRequest, (err, data) => {
        if (err) {
            res.status(500).json(err);
        } else {
            logger.info("register succeeded", data);
            res.status(200).json(data)
        }
    });
})

module.exports = router;