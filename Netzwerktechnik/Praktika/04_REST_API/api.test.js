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

    it('should return a user object', (done) => {
        getUsers.then(response => {
            expect(response.body.name).toBeDefined();
            done();
        });
    });
});


