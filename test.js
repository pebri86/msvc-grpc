import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
    http.post('http://localhost:5000/api/login', JSON.stringify({ "username": "test_user@yopmail.com", "password": "userpassword" }));
    sleep(1);
}