import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const uploadDocument = async () => {
    if (!file) {
      alert("Wybierz plik!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/documents/upload", {
      method: "POST",
      body: formData,
    });

    if (res.ok) {
      alert("Plik został przesłany!");
    } else {
      alert("Błąd podczas przesyłania pliku.");
    }
  };

  const askQuestion = async () => {
    if (!question.trim()) {
      alert("Wpisz pytanie!");
      return;
    }

    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        session_id: "frontend",
        query: question,
      }),
    });

    const data = await res.json();
    setAnswer(data.answer);
  };

  return (
    <div style={{ padding: 40, fontFamily: "Arial" }}>
      <h1>AI Knowledge Assistant</h1>

      <h2>📄 Upload dokumentu</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadDocument}>Wyślij</button>

      <h2>💬 Zapytaj AI</h2>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        style={{ width: "300px" }}
      />
      <button onClick={askQuestion}>Wyślij pytanie</button>

      <h3>Odpowiedź:</h3>
      <p>{answer}</p>
    </div>
  );
}

export default App;
