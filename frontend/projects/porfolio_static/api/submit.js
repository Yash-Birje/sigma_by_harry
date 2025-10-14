import fs from "fs";
import path from "path";

export default function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ message: "Only POST allowed" });
  }

  const { name, email, message } = req.body;
  const line = `${name},${email},${message}\n`;

  // write to file inside /tmp (Vercel only allows writing here)
  const filePath = path.join("/tmp", "submissions.csv");
  fs.appendFileSync(filePath, line, "utf8");

  console.log("✅ Data saved:", line.trim());
  alert(`Data saved on server ${data.name}`);
  res.status(200).json({ message: "Saved temporarily on server." });
}
