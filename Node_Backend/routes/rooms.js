const express = require("express");
const router = express.Router();
const { createRoom } = require("../controllers/roomController");
const { verifyToken } = require("../middleware/authMiddleware");

router.post("/create", verifyToken, createRoom);

module.exports = router;
