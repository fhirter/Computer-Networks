const request = require('supertest');
const {describe, expect, it, beforeEach, afterAll} = require('@jest/globals');

const url = "http://localhost:8080";

describe('GET /users', () => {
    let getUsers;
    beforeEach(() => {
        getUsers = request(url)
            .get('/users');
    });

    afterAll(() => {
        getUsers.end();
    });

    it('should return json data', (done) => {
        getUsers.expect('Content-Type', /json/, done);
    });

    it('should return HTTP code 200', (done) => {
        getUsers.expect(200, done)
    });

    it('should return a user array', (done) => {
        getUsers.then(response => {
            expect(response.body).toContainEqual(expect.anything());
            done();
        });
    });
});

describe('POST /user', () => {
    it('should return 201 created', (done) => {
        request(url)
            .post("/users")
            .expect(201, done)
    });
});


