# Next.js + Supabase Hackathon Boilerplate

A quick-start template for hackathons using Next.js 14 (App Router) and Supabase for auth and database.

## Quick Start

```bash
# 1. Install dependencies
npm install

# 2. Set up environment variables
cp .env.local.example .env.local
# Edit .env.local with your Supabase credentials

# 3. Run the dev server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Setup Steps

### 1. Create a Supabase Project

Go to [supabase.com](https://supabase.com) and create a free project.

### 2. Get Your Credentials

In your Supabase dashboard:
- Go to **Project Settings** → **API**
- Copy the **Project URL** and **anon/public key**
- Paste them into `.env.local`

### 3. Enable Auth Providers (Optional)

In Supabase dashboard:
- Go to **Authentication** → **Providers**
- Enable Google, GitHub, or any provider you want
- Add the callback URL: `http://localhost:3000/auth/callback`

### 4. Create Database Tables (Optional)

In Supabase dashboard, go to **SQL Editor** and run:

```sql
-- Example: Create a todos table
create table todos (
  id uuid default gen_random_uuid() primary key,
  user_id uuid references auth.users(id) on delete cascade,
  title text not null,
  completed boolean default false,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Enable RLS
alter table todos enable row level security;

-- Create policy: Users can only see their own todos
create policy "Users can view own todos" on todos
  for select using (auth.uid() = user_id);

create policy "Users can insert own todos" on todos
  for insert with check (auth.uid() = user_id);

create policy "Users can update own todos" on todos
  for update using (auth.uid() = user_id);

create policy "Users can delete own todos" on todos
  for delete using (auth.uid() = user_id);
```

## Project Structure

```
├── app/
│   ├── layout.tsx          # Root layout with Supabase provider
│   ├── page.tsx            # Landing page
│   └── login/
│       └── page.tsx        # Login page
├── components/
│   └── Navbar.tsx          # Navigation bar with auth state
├── lib/
│   └── supabase.ts         # Supabase client setup
├── .env.local.example      # Environment variable template
├── package.json
└── README.md
```

## Tech Stack

- **Framework:** Next.js 14 (App Router)
- **Auth/Database:** Supabase
- **Styling:** Tailwind CSS
- **Language:** TypeScript

## What's Included

- Supabase client setup (browser + server)
- Email/password authentication
- Protected routes
- Auth state management
- Basic landing page with login/logout
- Tailwind CSS for styling

## Deploy to Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Add environment variables in Vercel dashboard
# Or use CLI:
vercel env add NEXT_PUBLIC_SUPABASE_URL
vercel env add NEXT_PUBLIC_SUPABASE_ANON_KEY
```

## License

MIT — use this for any hackathon, no strings attached.
