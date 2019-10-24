const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const app = express()

const chk = require('./check-json')

app.use(express.static(__dirname + '/public'));
app.use(bodyParser.urlencoded({ extended: 'true', limit: '5mb' }));
app.use(bodyParser.json({ limit: '5mb' }));
app.use(bodyParser.json({ type: 'application/vnd.api+json', limit: '5mb' }));
app.use(function (req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header("Access-Control-Allow-Methods", "GET, POST");
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});


app.post('/create', function (req, res) {
    console.log(req.body);
    console.log(chk.checkjson(req.body));
    
    axios.post("http://localhost:5001/rate", req.body)
        .then(function (response) {
            console.log(response.data)
            res.status(200)
            res.send({});
        })
        .catch(function (error) {
            console.log(error);
            res.status(400)
            res.send();
        });
    

});


app.listen(9000);
console.log("Server started");