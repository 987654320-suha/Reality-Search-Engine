"use client";

import { use } from "react";
import { useEffect, useState } from "react";

export default function MemoryPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {

  const { id } = use(params);

  const [memory, setMemory] =
    useState<any>(null);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {
    const loadMemory = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:8000/memory/${id}`
        );

        const data =
          await response.json();

        setMemory(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

    loadMemory();
  }, [id]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center text-xl">
        Loading Memory...
      </div>
    );
  }

  if (!memory) {
    return (
      <div className="min-h-screen flex items-center justify-center text-xl text-red-500">
        Memory Not Found
      </div>
    );
  }

  return (
    <main className="min-h-screen bg-gray-100 p-8">

      <div className="max-w-4xl mx-auto bg-white rounded-xl shadow p-8">

        <h1 className="text-4xl font-bold mb-4">
          {memory.title}
        </h1>

        {memory.file_type && (
          <p className="text-gray-500 mb-2">
            📄 Type: {memory.file_type}
          </p>
        )}

        {memory.source && (
          <p className="text-gray-500 mb-6 break-all">
            📁 Source: {memory.source}
          </p>
        )}

        {memory.image && (
          <img
            src={
              memory.image.startsWith("/uploads")
                ? `http://127.0.0.1:8000${memory.image}`
                : memory.image
            }
            alt={memory.title}
            className="w-full rounded-xl mb-6"
          />
        )}

        {memory.objects &&
          memory.objects.length > 0 && (
            <div className="mb-6">

              <h2 className="text-xl font-bold mb-2">
                Detected Objects
              </h2>

              <div className="flex gap-2 flex-wrap">

                {memory.objects.map(
                  (
                    obj: string,
                    index: number
                  ) => (
                    <span
                      key={index}
                      className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full"
                    >
                      {obj}
                    </span>
                  )
                )}

              </div>

            </div>
          )}

        <div>

          <h2 className="text-xl font-bold mb-2">
            Description
          </h2>

          <div className="whitespace-pre-wrap text-gray-700">
            {memory.description}
          </div>

        </div>

      </div>

    </main>
  );
}