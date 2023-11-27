const request = require('supertest');
request("http://localhost:8080")
    .get('/users')
    .expect('Content-Type', /json/)
    .expect(200)
    .end(function (err, res) {
        if (err) throw err;
    });