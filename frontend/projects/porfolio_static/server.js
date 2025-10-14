import express from "express";
import fs from "fs";
import path from "path";

const app = express();
const PORT = 3000;

// Middleware to parse JSON
app.use(express.json());
app.use(express.static(".")); // serve your HTML/JS files

// Handle form submission
app.post("/submit", (req, res) => {
  const { name, email, message } = req.body;

  // Save as CSV line
  const line = `${name},${email},${message}\n`;

  fs.appendFileSync("/submissions.csv", line, "utf8");
  console.log("✅ Data saved:", line.trim());
  res.status(200).send("Data saved successfully");
});

app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));
