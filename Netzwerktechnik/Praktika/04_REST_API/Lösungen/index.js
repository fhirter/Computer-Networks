/**
 * @swagger
 * /users:
 *   get:
 *     summary: Returns a list of users
 *     responses:
 *       200:
 *         description: A list of users
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 type: object
 *                 properties:
 *                   name:
 *                     type: string
 *                   email:
 *                     type: string
 *   post:
 *     summary: create a new user
 *     responses:
 *       201:
 *         description: A new user has been created
 */

const express = require('express');
const app = express();
const port = 8080;

const swaggerJsdoc = require("swagger-jsdoc");
const swaggerUi = require("swagger-ui-express");

const user = {
    name: "John Doe"
}

const options = {
    definition: {
        openapi: '3.0.0',
        info: {
            title: 'My API',
            version: '1.0.0',
            description: 'A simple Express API',
        },
    },
    apis: ['./index.js'], // paths to files containing OpenAPI definitions
};

const specs = swaggerJsdoc(options);
app.use(
    "/api-docs",
    swaggerUi.serve,
    swaggerUi.setup(specs)
);

app.get('/users', (req, res) => {
    res.status(200);
    res.send([user]);
})

app.post('/users/{user}', (req, res) => {
    res.status(201);
    res.send();
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})