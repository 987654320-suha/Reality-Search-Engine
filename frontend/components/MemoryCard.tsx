"use client";

import Link from "next/link";

type Memory = {
  id: string;
  title: string;
  description: string;
  image?: string;
  date?: string;
  location?: string;
  objects?: string[];
};

export default function MemoryCard({
  memory,
}: {
  memory: Memory;
}) {
  return (
    <Link href={`/memory/${memory.id}`}>

      <div className="bg-white rounded-xl shadow p-6 hover:shadow-lg transition cursor-pointer">

        {memory.image && (

          <img
            src={
              memory.image.startsWith("/uploads")
                ? `http://127.0.0.1:8000${memory.image}`
                : memory.image
            }
            alt={memory.title}
            loading="lazy"
            className="w-full max-h-[300px] object-cover rounded-lg mb-4"
          />

        )}

        <h2 className="text-2xl font-bold mb-2">

          {memory.title}

        </h2>

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

          <div className="mt-4 flex flex-wrap gap-2">

            {memory.objects.map((obj, index) => (

              <span
                key={index}
                className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full"
              >
                {obj}
              </span>

            ))}

          </div>

        )}

      </div>

    </Link>
  );
}