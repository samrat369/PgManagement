const mongoose = require("mongoose");
const bedSchema = require("./Bed");

const roomSchema = new mongoose.Schema({
    roomId: {
        type: Number,
        required: true,
        unique: true
    },
    roomType: {
        type: String,
        enum: ["single", "double", "triple", "quad"],
        required: true,
    },
    beds: [bedSchema], // embed array of beds
    utilities: {
        wifi: { type: Boolean, default: false },
        ac: { type: Boolean, default: false },
        geyser: { type: Boolean, default: false }
    },
    rent: {
        type: Number,

    }
}, { timestamps: true });

module.exports = mongoose.model("Room", roomSchema);