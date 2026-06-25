"use client";

import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="bg-white shadow mb-8">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">

        <h1 className="text-2xl font-bold text-blue-600">
          Reality AI
        </h1>

        <div className="flex gap-8">

          <Link
            href="/"
            className="hover:text-blue-600"
          >
            Dashboard
          </Link>

          <Link
            href="/chat"
            className="hover:text-blue-600"
          >
            Chat
          </Link>

          <Link
            href="/timeline"
            className="hover:text-blue-600"
          >
            Timeline
          </Link>

          <Link
            href="/analytics"
            className="hover:text-blue-600"
          >
            Analytics
          </Link>

        </div>

      </div>
    </nav>
  );
}