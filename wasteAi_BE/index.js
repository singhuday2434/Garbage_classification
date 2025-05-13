const express=require('express');
const cors=require('cors');

const app=express();
require('dotenv').config;

app.use(express.json())
app.use(express.urlencoded({ extended: true }));
app.use(cors())
//port
const PORT=process.env.PORT||3000;
app.listen(PORT,'0.0.0.0',()=>{
    console.log(`listening at ${PORT}`)
})

//route mounting
const wastedetails=require("./routes/wasteRoute")

app.use('/api/v1',wastedetails)



//DB CONNECT
const dbConnect=require("./config/database");
dbConnect();