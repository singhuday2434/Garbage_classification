const mongoose=require('mongoose');
require('dotenv').config();
const dbconnect=()=>{
    mongoose.connect(process.env.DATABASE_URL)
    .then(()=>{
           console.log("connect to USER_DB");

    }).catch((e)=>{
        console.log(e.message);
        console.log("failed to connect to USER_DB");
        process.exit(1);

    })

}

module.exports=dbconnect;