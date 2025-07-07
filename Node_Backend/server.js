const express = require("express");
const dotenv = require("dotenv");
const connectDB = require("./config/db");
const cors = require("cors");

const authRoutes = require("./routes/auth");
const roomRoutes = require("./routes/rooms");

dotenv.config();        // Load env variables

connectDB();            // Connect MongoDB

const app = express();

app.use(cors());        // Allow cross-origin requests
app.use(express.json()); // Parse JSON bodies
app.use("/api/auth", authRoutes);
app.use("/api/rooms", roomRoutes);

app.get("/", (req, res) => {
    res.send("PG backend is running 🚀");
});


const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`);
});
