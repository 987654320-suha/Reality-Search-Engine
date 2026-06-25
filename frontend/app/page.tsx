"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import StatsCards from "@/components/StatsCards";
import MemoryCard from "@/components/MemoryCard"; // Add this import

export default function Home() {
  const [stats, setStats] = useState({
    total: 0,
    images: 0,
    pdfs: 0,
    docx: 0,
  });

  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [aiQuestion, setAiQuestion] = useState("");
  const [aiAnswer, setAiAnswer] = useState("");
  const [sources, setSources] = useState<any[]>([]);
  const [aiLoading, setAiLoading] = useState(false);

  const searchMemories = async () => {
    console.log("BUTTON CLICKED");
    console.log("QUERY =", query);

    setLoading(true);

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/search?q=${encodeURIComponent(query)}`
      );

      console.log("STATUS =", response.status);

      const data = await response.json();

      console.log("DATA =", data);

      setResults(data);
    } catch (error) {
      console.error("SEARCH ERROR:", error);
    } finally {
      setLoading(false);
    }
  };

  const loadStats = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/stats");
      const data = await response.json();
      setStats(data);
    } catch (error) {
      console.error(error);
    }
  };

  const loadTimeline = async () => {
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/timeline");
      const data = await response.json();

      console.log("TIMELINE DATA:", data);

      setResults(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const uploadPDF = async () => {
    if (!selectedFile) {
      alert("Please select a PDF");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload/pdf", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      alert(data.message || "PDF uploaded successfully!");
      loadStats();
      setSelectedFile(null);
      loadTimeline();
    } catch (error) {
      console.error(error);
      alert("Upload failed");
    }
  };

  const askAI = async () => {
    if (!aiQuestion.trim()) return;

    setAiLoading(true);
    setAiAnswer("");
    setSources([]);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: aiQuestion,
        }),
      });

      const data = await response.json();

      setAiAnswer(data.answer);
      setSources(data.sources || []);
    } catch (error) {
      console.error(error);
      setAiAnswer("Something went wrong.");
      setSources([]);
    } finally {
      setAiLoading(false);
    }
  };

  useEffect(() => {
    loadStats();
  }, []);

  return (
    <main className="min-h-screen bg-gray-100">
      <div className="max-w-6xl mx-auto p-8">
        <div className="text-center mb-10">
          <h1 className="text-5xl font-bold">Reality Search Engine</h1>
          <p className="text-gray-600 mt-3">
            Search your memories, images, PDFs, goals and experiences
          </p>
          
          {/* StatsCards component */}
          <StatsCards stats={stats} />
        </div>

        {/* PDF Upload */}
        <div className="bg-white rounded-xl shadow p-6 mb-8">
          <h2 className="text-xl font-bold mb-4">Upload PDF</h2>

          <div className="flex gap-3 items-center">
            <input
              type="file"
              accept=".pdf"
              onChange={(e) => setSelectedFile(e.target.files?.[0] || null)}
            />

            <button
              onClick={uploadPDF}
              className="bg-purple-600 text-white px-5 py-2 rounded-lg"
            >
              Upload PDF
            </button>
          </div>
        </div>

        {/* AI Assistant */}
        <div className="bg-white rounded-xl shadow p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">
            🤖 AI Memory Assistant
          </h2>

          <div className="flex gap-3">
            <input
              className="flex-1 border rounded-lg p-4"
              placeholder="Ask anything about your memories..."
              value={aiQuestion}
              onChange={(e) => setAiQuestion(e.target.value)}
            />

            <button
              onClick={askAI}
              className="bg-black text-white px-6 rounded-lg"
            >
              Ask AI
            </button>
          </div>

          {aiLoading && (
            <p className="mt-4 text-blue-600">
              🤖 Thinking...
            </p>
          )}

          {aiAnswer && (
            <div className="mt-6 bg-gray-100 rounded-lg p-4">
              <h3 className="font-bold mb-2">
                AI Answer
              </h3>

              <p className="whitespace-pre-wrap">
                {aiAnswer}
              </p>

              {/* Sources Section */}
              {sources.length > 0 && (
                <div className="mt-6">
                  <h3 className="font-bold mb-2">Sources</h3>
                  <div className="space-y-2">
                    {sources.map((source, index) => (
                      <div
                        key={index}
                        className="bg-white rounded border p-3"
                      >
                        <p className="font-semibold">
                          📄 {source.title}
                        </p>
                        <p className="text-sm text-gray-500 break-all">
                          {source.source}
                        </p>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Search */}
        <div className="bg-white rounded-xl shadow p-6 mb-8">
          <div className="flex gap-3">
            <input
              className="flex-1 border rounded-lg p-4"
              placeholder="Search memories..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
            />

            <button
              onClick={searchMemories}
              className="bg-blue-600 text-white px-6 rounded-lg"
            >
              Search
            </button>

            <button
              onClick={loadTimeline}
              className="bg-green-600 text-white px-6 rounded-lg"
            >
              Timeline
            </button>
          </div>
        </div>

        {loading && (
          <div className="text-center mb-6 text-lg">Loading...</div>
        )}

        {!loading && (
          <>
            <div className="mb-4 text-gray-600">
              Results Found: {results.length}
            </div>

            {results.length === 0 ? (
              <div className="bg-white rounded-xl shadow p-12 text-center text-gray-500">
                No memories found. Try searching or uploading some content!
              </div>
            ) : (
              <div className="grid gap-6">
                {results.map((memory) => (
                  <MemoryCard
                    key={memory.id}
                    memory={memory}
                  />
                ))}
              </div>
            )}
          </>
        )}
      </div>
    </main>
  );
}