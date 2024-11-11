const express = require('express');
const cors=require('cors');

require('dotenv').config({path:"./config.env"})

const app=express();
const port=process.env.PORT || 5000;

// using middlewares
app.use(cors());
app.use(express.json());

// using Routes
app.use(require('./routes/route'));


app.listen(port,()=>{
    console.log(`Server is running on: http://localhost:${port}`)
})