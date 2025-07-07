const mongoose = require("mongoose");

const bedSchema = new mongoose.Schema({

    bedNumber: {
        type: Number,
        required: true,
    },
    status: {
        type: String,
        enum: ["vacant", "occupied"],
        default: "vacant"
    },
    tenant: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "User",
        default: null,
    },

});

module.exports = bedSchema;