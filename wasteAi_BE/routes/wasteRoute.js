const express=require("express")
const router=express.Router();


const{getInfo}=require("../controllers/wasteController");




router.post('/get',getInfo);



module.exports=router;
