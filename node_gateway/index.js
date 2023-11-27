const express = require("express");
const bodyParser = require("body-parser");
const cors = require('cors');

const auth = require("./routes/auth");
const todo = require("./routes/todo");
const authMiddleware = require("./middleware/auth");
const logger = require("./logger");

const app = express();
var corsOptions = {
    origin: '*',
    optionsSuccessStatus: 200
}
app.use(cors(corsOptions));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use('/api', auth);
app.use('/api/user', authMiddleware, todo);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    logger.info(`Server running at port ${PORT}`);
});