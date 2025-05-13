const mongoose=require("mongoose")
const wDetails=new mongoose.Schema(
    {
        category:{
            type:String,
            required:true
        },
        impact:{
            type:Array,
            required:true
        },
        disposal:{
            type:Array,
            required:true
        },
        eco_friendly_alternatives:{
            type:Array,
            required:true,
        },
        toxicity:{
            type:Number,
            required:true
        },
        v_id:{
            type:String,
        }

    }
);
module.exports=mongoose.model("wasteDetail",wDetails);