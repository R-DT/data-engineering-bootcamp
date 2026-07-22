-- 1. Status count metrics profile lookup
SELECT status, COUNT(*) 
FROM transactions 
GROUP BY status;

-- 2. Top 10 high-value customer whale lookup
SELECT customer_id, SUM(amount) AS total_value 
FROM transactions 
GROUP BY customer_id 
ORDER BY total_value DESC 
LIMIT 10;

-- 1. Verify total records ingested and see transaction statuses
SELECT status, COUNT(*) AS total_transactions
FROM transactions
GROUP BY status;

-- 2. Identify your top 5 highest-spending customer profiles
SELECT customer_id, SUM(amount) AS total_value_usd
FROM transactions
GROUP BY customer_id
ORDER BY total_value_usd DESC
LIMIT 5;

