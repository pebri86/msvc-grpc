import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
    let headersList = {
        headers: {
            "Accept": "*/*",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDA4ODI3MDcsImlkIjoxLCJ1c2VybmFtZSI6IiJ9.fmU_pSnFLHF6zZ-jwQLbrPrPadh57fVVNMI1WJXlniM"
        }
    }
    http.get('http://localhost:5000/api/user/todos', headersList);
    sleep(1);
}
