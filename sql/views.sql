-- High-level financial metric summary view
CREATE OR REPLACE VIEW view_transaction_summary AS
SELECT 
    status, 
    COUNT(*) AS total_count,
    COALESCE(SUM(amount), 0.00) AS total_volume_usd,
    COALESCE(AVG(amount), 0.00) AS average_transaction_value
FROM transactions
GROUP BY status;

-- Top 10 high-value customer whale tracking profile view
CREATE OR REPLACE VIEW view_top_customers AS
SELECT 
    customer_id,
    SUM(amount) AS total_value_spent,
    COUNT(*) AS total_transactions
FROM transactions
GROUP BY customer_id
ORDER BY total_value_spent DESC
LIMIT 10;
