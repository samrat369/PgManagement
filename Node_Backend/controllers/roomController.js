const axios = require("axios");

const createRoom = async (req, res) => {
    try {
        const response = await axios.post("http://localhost:8000/api/rooms/create", req.body);

        res.status(response.status).json(response.data);
    } catch (err) {
        console.error("Error forwarding to FastAPI:", err.message);

        if (err.response) {
            return res.status(err.response.status).json(err.response.data);
        }

        res.status(500).json({ msg: "Server Error communicating with FastAPI" });
    }
};

module.exports = { createRoom };
