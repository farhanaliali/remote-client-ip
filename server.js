const express = require("express");

const app = express();

app.set("trust proxy", true); // Enable trusted proxy

app.get("/", (req, res) => {
    const clientIp = req.ip; // Express will automatically get the right IP
    console.log(`Client IP: ${clientIp}`);
    res.send(`Client IP: ${clientIp}`);
});

app.listen(3000, () => {
    console.log("Server is running on port 3000");
});
