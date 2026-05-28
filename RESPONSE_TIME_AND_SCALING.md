# Response Time and Scaling

## 1. Expected time from farmer question to answer

For simple farmer-facing scenarios, the expected response time is **1–3 minutes**.

| Step | Expected time |
|---|---:|
| WhatsApp message received | 1–3 seconds |
| AI intake and scenario planning | 5–15 seconds |
| Weather and soil preparation | 5–20 seconds |
| APSIM simulations | 30–120 seconds |
| Validation and advisory generation | 5–20 seconds |
| WhatsApp reply | 1–5 seconds |

## 2. Factors affecting time

The response time depends on:

- Number of scenarios
- Number of weather years
- Number of locations
- Server CPU capacity
- APSIM model complexity
- Whether weather/soil data are cached
- Whether simulations run sequentially or in parallel

## 3. Recommended operating modes

### Fast advisory mode

Use for farmers.

- 3–6 scenarios
- 5–10 weather years
- Cached weather and soil files
- Parallel APSIM execution
- Expected time: 1–3 minutes

### Detailed research mode

Use for scientists and project teams.

- Many locations
- 20–30 weather years
- Full factorial management scenarios
- Expected time: 10–30 minutes or more

### Precomputed lookup mode

Use for national scaling.

- Pre-run APSIM simulations by governorate/grid
- Farmer request only queries database
- Expected time: less than 30 seconds

## 4. Scaling recommendations

To scale to many farmers:

1. Precompute common scenarios.
2. Cache weather files by location and year.
3. Cache soil profiles by grid cell/governorate.
4. Run APSIM jobs in parallel.
5. Add Redis queue and Celery workers.
6. Store all simulation outputs in PostgreSQL.
7. Use fallback advisory messages if APSIM queue is overloaded.

## 5. Suggested performance target

For national pilot deployment:

| Metric | Target |
|---|---:|
| Simple WhatsApp query | less than 3 minutes |
| Cached recommendation | less than 30 seconds |
| Failed simulation rate | less than 2% |
| Arabic response quality | agronomist-reviewed |
| Farmer satisfaction | measured during pilot |
