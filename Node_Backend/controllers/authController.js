const User = require("../models/Users");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken")


const register = async (req, res) => {
    const { name, email, phoneno, password, role } = req.body;

    try {
        const userExists = await User.findOne({ email });
        if (userExists) {
            return res.status(400).json({ msg: "User already exists" });
        }

        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        const user = await User.create({
            name, email, phoneno, password: hashedPassword, role
        });

        const token = jwt.sign(
            { id: user._id, role: user.role },
            process.env.JWT_SECRET,
            { expiresIn: "7d" }
        );

        res.status(201).json({
            token,
            user_details: {
                id: user._id, name: user.name, email: user.email, role: user.role
            }
        });

    }
    catch (err) {
        return res.status(500).json({ msg: "Internal Server Error" })
    }
}

const login = async (req, res) => {
    const { email, password } = req.body;

    try {
        const user = await User.findOne({ email });
        if (!user) {
            res.status(401).json({ msg: "Invalid Credentials" });
        }
        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
            res.status(401).json({ msg: "Invalid Credentials" });
        }

        const token = jwt.sign(
            { id: user._id, role: user.role },
            process.env.JWT_SECRET,
            { expiresIn: "7d" }
        );

        res.status(200).json({
            token,
            user_details: {
                id: user._id,
                name: user.name,
                email: user.email,
                role: user.role,
            },
        });

    }
    catch (err) {
        res.status(500).json({ msg: "Internal Server Error" });
    }
}

module.exports = { register, login };