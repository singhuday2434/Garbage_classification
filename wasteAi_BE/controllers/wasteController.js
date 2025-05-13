const wasteModel=require("../models/wasteModel")

exports.getInfo =async (req,res)=>{
    try {
        const {category_}=req.body
        const data=await wasteModel.findOne({category:category_})
        console.log(data);
        res.json({success:true,message:"data fetched",details:data},
            )
    } catch (error) {
        console.log(error);
       
        return  (res.json({success:false, message:error.message}))
    }
}

