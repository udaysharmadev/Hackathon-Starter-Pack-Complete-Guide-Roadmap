# Database Deep Dive: Choosing and Using the Right Database for Your Hackathon Project

Every application needs somewhere to store data. At a hackathon, choosing the wrong database costs hours of debugging or kills your demo entirely. Choosing the right one saves time, impresses judges, and gives you features you didn't think you'd have time to build.

---

## When to Use SQL vs NoSQL — Decision Framework with Examples

The SQL vs NoSQL debate is one of the oldest in software engineering. At a hackathon, you don't have time for philosophy. You need a practical decision fast.

**The quick decision framework:**

1. **Is your data highly structured with clear relationships?** → SQL
2. **Do you need complex queries with joins?** → SQL
3. **Is your data flexible or semi-structured?** → NoSQL
4. **Do you need to scale horizontally from day one?** → NoSQL
5. **Are you building something with well-defined entities?** → SQL
6. **Is the data model uncertain and might change?** → NoSQL

**SQL (PostgreSQL, MySQL, SQLite):**

SQL databases shine when you have clear entities with defined relationships:

- **E-commerce:** Users have orders, orders have items, items have prices.
- **Social networks:** Users follow users, users post posts, posts have comments.
- **Project management:** Projects contain tasks, tasks have assignees.

SQL gives you ACID transactions, complex queries, schema enforcement, and mature tooling. The downside? Schema changes are painful. If you need to add a column to a table with 10,000 rows on Sunday morning, you're in trouble.

**NoSQL (MongoDB, Firebase, DynamoDB):**

NoSQL shines when data is flexible or you need to move fast:

- **Content management:** Posts have different fields depending on type.
- **Real-time apps:** Chat messages, live feeds, collaborative editing.
- **IoT data:** Sensor readings, device telemetry, event logs.
- **Prototypes:** When your data model is uncertain.

NoSQL gives you flexible schemas, horizontal scaling, developer speed, and JSON-native storage. The downside? No joins, no schema enforcement, and potential data inconsistency.

**The "just use" heuristics:**

- Not sure what to use? **Use PostgreSQL** (via Supabase). It handles 90% of hackathon use cases.
- Building a real-time collaborative app? **Use Firebase.**
- Data model genuinely uncertain? **Use MongoDB.**
- Need offline-first? **Use Firebase or PocketBase.**

---

## Firebase vs Supabase vs PocketBase — Detailed Comparison for Hackathons

**Firebase (Google):**

*Strengths:* Real-time database out of the box, generous free tier (1GB storage, 50K reads/day), excellent documentation, built-in auth with social logins, hosting included, massive community.

*Weaknesses:* Vendor lock-in (migrating away is painful), NoSQL only (no joins), costs can spike, limited query capabilities, tricky data modeling.

*Best for:* Real-time collaborative apps, social features, chat applications, apps where you need auth and database in one platform.

**Supabase:**

*Strengths:* PostgreSQL under the hood (real SQL power), real-time subscriptions, row-level security, generous free tier (500MB database), auto-generated APIs, built-in auth, open source (can migrate to self-hosted).

*Weaknesses:* Newer platform (less community content), real-time less seamless than Firebase, free tier fills up faster than expected, learning curve for row-level security.

*Best for:* Projects needing relational data, teams wanting SQL power with Firebase-like convenience, projects that might migrate to self-hosted later.

**PocketBase:**

*Strengths:* Single binary (download, run, done), SQLite under the hood, built-in admin UI, real-time via SSE, extremely fast setup (under 5 minutes), no vendor lock-in, great for local development.

*Weaknesses:* SQLite limitations (concurrent writes), limited ecosystem, smaller community, single-server architecture, less mature, requires self-hosting.

*Best for:* Solo developers, offline-first projects, hackathons needing zero external dependencies, prototypes that run locally.

**The decision matrix:**

| Feature | Firebase | Supabase | PocketBase |
|---------|----------|----------|------------|
| Setup time | 10 min | 15 min | 5 min |
| Real-time | Excellent | Good | Good |
| Query power | Limited | Excellent | Good |
| Auth | Excellent | Good | Basic |
| Free tier | Generous | Generous | Unlimited |
| Vendor lock-in | High | Low | None |

**The hackathon recommendation:** Use Supabase if unsure — it's the most balanced option.

---

## Schema Design for Hackathons — Keep It Simple, Normalized vs Denormalized

Your schema at a hackathon should be "good enough for now, easy to change later." Over-engineering wastes time. Under-engineering creates bugs.

**The hackathon schema philosophy:**

- **Start denormalized.** Duplicate data freely. Easier to normalize later than to denormalize under time pressure.
- **Keep it flat.** Deep nesting creates complex queries. Two levels of relationships is usually enough.
- **Use sensible defaults.** If a field can have a default value, give it one.
- **Nullable over required.** Make fields nullable unless absolutely sure they're required.

**Example: Hackathon team finder**

Over-engineered (don't do this):
```sql
-- 5+ tables with complex relationships
CREATE TABLE users (...);
CREATE TABLE skills (...);
CREATE TABLE user_skills (...);
-- ... and so on
```

Hackathon version (do this):
```sql
-- Two tables, simple relationships
CREATE TABLE users (
  id UUID PRIMARY KEY,
  name TEXT,
  skills TEXT[],  -- Array, no separate table
  bio TEXT,
  looking_for TEXT
);

CREATE TABLE projects (
  id UUID PRIMARY KEY,
  name TEXT,
  owner_id UUID REFERENCES users(id),
  members UUID[],
  skills_needed TEXT[]
);
```

The hackathon version is simpler, faster to query, and easier to modify. Yes, it's denormalized. But it works in minutes instead of hours.

**Patterns that work:**

1. **Everything in one table.** For simple apps, a single table with JSONB columns works.
2. **Array references.** Use arrays instead of junction tables for many-to-many relationships.
3. **Soft delete.** Add `deleted_at` instead of deleting records. Makes undo easier.
4. **Status field.** Use one `status` column with values like 'draft', 'published', 'archived'.

**When to normalize:** Lots of updates to the same data, need data consistency, approaching demo time and want clean data.

**When to denormalize:** Lots of reads and few writes, need to show data quickly, prototyping and unsure about your model.

---

## Real-Time Patterns — When You Need WebSockets, When You Don't

Real-time features impress judges but are complex and error-prone. Use them when they add genuine value, not just for the cool factor.

**When you actually need real-time:**

- Collaborative editing
- Chat and messaging
- Live dashboards (stocks, IoT, analytics)
- Multiplayer games
- Live notifications

**When you don't:**

- Forms and CRUD operations (standard form submission works)
- Reporting and analytics (batch processing is fine)
- Content management (publishing doesn't need real-time)
- Read-heavy apps (polling or cache invalidation is fine)

**Implementation options:**

**Firebase:** Easiest for hackathons. Set up listeners, data syncs automatically:
```javascript
onSnapshot(doc(db, "messages", chatId), (doc) => {
  displayMessage(doc.data());
});
```

**Supabase Realtime:** Subscribe to table changes:
```javascript
supabase.channel('messages')
  .on('postgres_changes', 
    { event: '*', schema: 'public', table: 'messages' }, 
    (payload) => displayMessage(payload.new))
  .subscribe();
```

**Socket.IO:** For custom real-time features that don't fit database-level real-time.

**The polling alternative:**

Before jumping into WebSockets, consider polling. It's simpler, more reliable, and often good enough:
```javascript
setInterval(async () => {
  const response = await fetch('/api/messages');
  const messages = await response.json();
  updateUI(messages);
}, 5000);
```

Polling is easier to implement, more reliable, easier to debug, and good enough for most demos. Use WebSockets when you need sub-second updates.

**Real-time gotchas:** Connection management (need reconnection logic), state synchronization, scaling (100 connections fine, 10K is not), demo reliability (have fallback plan).

---

## Offline-First Strategies — Service Workers, Local Storage, Sync Patterns

Offline-first apps work everywhere — even in demo rooms with terrible WiFi. They also demonstrate sophisticated engineering judges appreciate.

**The offline-first stack:**

**Level 1: Local Storage.** Simplest offline storage. 5-10MB limit, synchronous API, good for small data:
```javascript
localStorage.setItem('user-preferences', JSON.stringify({ theme: 'dark' }));
```

**Level 2: IndexedDB.** More powerful. Handles larger datasets and complex queries. More complex but much more capable.

**Level 3: Service Workers.** Gold standard. Intercept network requests, serve cached content:
```javascript
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
```

**Level 4: Full sync engine.** Libraries like PouchDB or RxDB handle automatic sync between local and remote databases.

**The hackathon offline strategy:**

For most hackathons, you don't need Level 4:

1. **Cache API responses.** Store last known good response locally.
2. **Queue writes.** Save locally when offline, sync when online.
3. **Show connectivity status.** Let users know when offline.
4. **Use localStorage for small data.** Preferences, recent items, form drafts.
5. **Use IndexedDB for medium data.** User records, cached API responses.

**The offline demo:** Turn off WiFi → show app works → make changes → turn WiFi back on → show syncing. Impressive and shows real-world utility.

---

## "The Database That Kills Your Demo" — Common Failure Modes and Prevention

**Failure mode 1: Empty database.** You forgot to seed data. App looks dead. *Prevention: Seed before the hackathon. Use realistic data.*

**Failure mode 2: Connection timeout.** Too many people on WiFi. *Prevention: Cache responses, use connection pooling, test with slow network.*

**Failure mode 3: Schema mismatch.** Changed schema locally but not in production. *Prevention: Use migrations, test production after changes.*

**Failure mode 4: Race condition.** Two updates overwrite each other. *Prevention: Use optimistic locking, database transactions.*

**Failure mode 5: Query performance bomb.** Works with 10 records, dies with 1,000. *Prevention: Add indexes, test with realistic volumes.*

**Failure mode 6: Credential leak.** Hardcoded API keys in frontend code. *Prevention: Environment variables, .env files, server-side API routes.*

**Failure mode 7: Migration rollback failure.** Migration fails and you can't roll back. *Prevention: Write rollback migrations, test both directions.*

---

## Migration Strategy — What to Do When Your Schema Needs to Change Mid-Hackathon

Schema changes happen at every hackathon. Here's how to handle them.

**The migration workflow:**

1. Create the migration file (timestamp-named)
2. Write the forward migration SQL
3. Write the rollback migration SQL
4. Test locally
5. Deploy to production
6. Verify the change

**Common mid-hackathon migrations:**

```sql
-- Adding a column
ALTER TABLE users ADD COLUMN avatar_url TEXT;

-- Adding an index
CREATE INDEX idx_users_email ON users(email);

-- Changing column type
ALTER TABLE posts ALTER COLUMN content TYPE TEXT;
```

**The zero-downtime approach:** Add column with default → backfill data → add constraints → remove old column.

**The "no time for migrations" approach:** Export data to JSON → drop and recreate tables → import transformed data → test everything. Risky but works in a pinch. Back up first.

---

## Backup and Recovery — Protecting User Data During a Hackathon

**The backup strategy:**

1. **Automated backups.** Enable if your platform supports it (Firebase and Supabase do).
2. **Manual exports.** Before major changes, export to JSON or SQL file.
3. **Version control your schema.** Migration files ARE your schema backup.
4. **Seed data as backup.** Seed scripts recreate data from scratch.

**The recovery plan:**

1. Don't panic
2. Assess the damage
3. Check backups
4. Restore from most recent good backup
5. Re-enter recent changes if needed
6. Test everything

**The "everything is on my laptop" problem:** If using PocketBase or SQLite, back up your file regularly. Use cloud storage or a USB drive. Or use a cloud database if data loss is unacceptable.

---

## Performance Basics — Indexing, Query Optimization, Connection Pooling

**Indexing:**

An index is like a book's table of contents. Without it, the database scans every row. With it, it jumps directly to the right row.

```sql
-- Index on frequently queried columns
CREATE INDEX idx_users_email ON users(email);

-- Index on multiple columns
CREATE INDEX idx_posts_user_date ON posts(user_id, created_at);
```

Add indexes to columns you filter on, join on, sort on, or search on. Skip them for small tables, rarely-queried columns, or write-heavy tables.

**Query optimization:**

```sql
-- Use EXPLAIN to check query plans
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';

-- Select only what you need
SELECT id, name, email FROM users WHERE active = true;

-- Avoid N+1 queries — use JOINs
SELECT posts.*, users.name FROM posts JOIN users ON posts.user_id = users.id;

-- Always LIMIT results
SELECT * FROM posts ORDER BY created_at DESC LIMIT 20;
```

**Connection pooling:**

Most database clients create a new connection per query. That's slow. Supabase handles pooling automatically. Firebase uses long-lived connections. For self-hosted databases, use PgBouncer.

---

## "Database Decision Tree" — Flowchart for Choosing the Right Database

```
Is your app real-time collaborative?
├── Yes → Firebase (Firestore)
└── No ↓

Do you need complex queries with joins?
├── Yes → PostgreSQL (Supabase)
└── No ↓

Is your data highly structured?
├── Yes → PostgreSQL (Supabase)
└── No ↓

Do you need offline-first?
├── Yes → PocketBase or Firebase
└── No ↓

Is your data model uncertain?
├── Yes → Firebase or MongoDB
└── No ↓

Do you want zero vendor lock-in?
├── Yes → PocketBase
└── No ↓

Default: Supabase
```

**The "still not sure" rule:** Use Supabase. It handles 90% of hackathon projects well.

**The "switch later" option:** Export data → transform to new schema → import → update application code → test. Painful but possible. Keep database logic isolated in a service layer to make switching easier.

---

*Quick Reference: For structured relational data — Supabase. For real-time collaborative — Firebase. For offline-first simplicity — PocketBase. The best database is the one you know well. The worst is one you don't understand.*
