"use client";

import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const searchMemories = async () => {
    setLoading(true);

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/search?q=${query}`
      );

      const data = await response.json();

      console.log("SEARCH DATA:", data);

      setResults(data);
    } catch (error) {
      console.error(error);
    }

    setLoading(false);
  };

  const loadTimeline = async () => {
    setLoading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/timeline"
      );

      const data = await response.json();

      console.log("TIMELINE DATA:", data);

      setResults(data);
    } catch (error) {
      console.error(error);
    }

    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-gray-100">
      <div className="max-w-6xl mx-auto p-8">

        <div className="text-center mb-10">
          <h1 className="text-5xl font-bold">
            Reality Search Engine
          </h1>

          <p className="text-gray-600 mt-3">
            Search your memories, images, goals and experiences
          </p>
        </div>

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
          <div className="text-center mb-4">
            Searching...
          </div>
        )}

        <div className="grid gap-6">

          {results.map((memory, index) => (

            <div
              key={index}
              className="bg-white rounded-xl shadow p-6"
            >

              {memory.image && (
                <img
                  src={`http://127.0.0.1:8000${memory.image}`}
                  alt={memory.title}
                  className="w-full h-64 object-cover rounded-lg mb-4"
                />
              )}

              <h2 className="text-2xl font-bold mb-2">
  {memory.title}
</h2>

<p className="text-red-500">
  {JSON.stringify(memory)}
</p>

              <h2 className="text-2xl font-bold mb-2">
                {memory.title}
              </h2>

              {/* DEBUG */}
              <p className="text-red-500 text-sm">
                {memory.image || "NO IMAGE"}
              </p>

              {memory.date && (
                <p className="text-gray-500">
                  📅 {memory.date}
                </p>
              )}

              {memory.location && (
                <p className="text-gray-500">
                  📍 {memory.location}
                </p>
              )}

              <p className="mt-3 break-words">
                {memory.description}
              </p>

              {memory.objects && (
                <div className="mt-4 flex gap-2 flex-wrap">

                  {memory.objects.map(
                    (obj: string, i: number) => (
                      <span
                        key={i}
                        className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full"
                      >
                        {obj}
                      </span>
                    )
                  )}

                </div>
              )}

            </div>

          ))}

        </div>

      </div>
    </main>
  );
}