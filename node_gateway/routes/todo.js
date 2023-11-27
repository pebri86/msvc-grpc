const todo_client = require("../grpc_client/todo_client");
const express = require('express');
const logger = require("../logger");
const router = express.Router()

router.get('/todos', async (req, res) => {
    userId = parseInt(res.get('X-USERID'))
    let request = {
        userID: userId
    };

    console.log(request)
    todo_client.getTodos(request, (err, data) => {
        if (err) {
            logger.error(err)
            res.status(401).json({
                success: false,
                message: "Failed to get todos"
            });
        } else {
            logger.info("get todos succeeded", data);
            data.data = JSON.parse(data.data)
            res.status(200).json(data)
        }
    });
})

router.get('/todo/:id', async (req, res) => {
    userId = parseInt(res.get('X-USERID'))
    let request = {
        itemID: parseInt(req.params.id),
        userID: userId
    };

    todo_client.getTodo(request, (err, data) => {
        if (err) {
            logger.error(err)
            res.status(500).json({
                success: false,
                message: "Failed to get todo"
            });
        } else {
            logger.info("register succeeded", data);
            data.data = JSON.parse(data.data)
            res.status(200).json(data)
        }
    });
})

router.post('/todo', async (req, res) => {
    userId = parseInt(res.get('X-USERID'))
    let request = {
        title: req.body.title,
        description: req.body.description,
        userID: userId
    };

    todo_client.createTodo(request, (err, data) => {
        if (err) {
            logger.error(err)
            res.status(500).json({
                success: false,
                message: "Failed to create todo"
            });
        } else {
            logger.info("create todo succeeded", data);
            res.status(200).json(data)
        }
    });
})

router.put('/todo', async (req, res) => {
    let request = {
        title: req.body.title,
        description: req.body.description,
        id: req.body.id
    };

    todo_client.updateTodo(request, (err, data) => {
        if (err) {
            logger.error(err)
            res.status(500).json({
                success: false,
                message: "Failed to update todo"
            });
        } else {
            logger.info("update todo succeeded", data);
            res.status(200).json(data)
        }
    });
})

router.delete('/todo', async (req, res) => {
    let request = {
        id: req.body.id
    };

    todo_client.deleteTodo(request, (err, data) => {
        if (err) {
            logger.error(err)
            res.status(500).json({
                success: false,
                message: "Failed to delete todo"
            });
        } else {
            data.id = req.body.id
            logger.info("delete todo succeeded", data);
            res.status(200).json(data)
        }
    });
})

module.exports = router;