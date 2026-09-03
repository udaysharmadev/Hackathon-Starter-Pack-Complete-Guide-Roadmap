import Navbar from "@/components/Navbar";

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50">
      <Navbar />
      <div className="max-w-4xl mx-auto px-4 py-16">
        <div className="text-center">
          <h1 className="text-5xl font-bold text-gray-900 mb-6">
            Hackathon Starter
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Next.js + Supabase boilerplate. Get building in minutes.
          </p>
          <div className="flex gap-4 justify-center">
            <a
              href="https://supabase.com/docs"
              target="_blank"
              rel="noopener noreferrer"
              className="bg-green-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-green-700 transition"
            >
              Read the Docs
            </a>
            <a
              href="https://github.com"
              target="_blank"
              rel="noopener noreferrer"
              className="bg-gray-800 text-white px-6 py-3 rounded-lg font-medium hover:bg-gray-900 transition"
            >
              View on GitHub
            </a>
          </div>
        </div>

        <div className="mt-16 grid md:grid-cols-3 gap-8">
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
            <div className="text-3xl mb-3">⚡</div>
            <h3 className="font-semibold text-gray-900 mb-2">Fast Setup</h3>
            <p className="text-gray-600 text-sm">
              Supabase auth, database, and storage ready to go. No boilerplate
              to write.
            </p>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
            <div className="text-3xl mb-3">🔒</div>
            <h3 className="font-semibold text-gray-900 mb-2">Auth Built In</h3>
            <p className="text-gray-600 text-sm">
              Email/password, Google, GitHub, and 20+ providers with Row Level
              Security.
            </p>
          </div>
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
            <div className="text-3xl mb-3">🚀</div>
            <h3 className="font-semibold text-gray-900 mb-2">Deploy Anywhere</h3>
            <p className="text-gray-600 text-sm">
              Vercel, Netlify, or your own server. Works everywhere.
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}
