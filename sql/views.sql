-- ====================================================================
-- FINTECH DATA PLATFORM - PERMANENT ANALYTICAL REPORTING VIEWS
-- ====================================================================

-- 1. High-Level Core Operations Performance View
-- Computes volume metrics, ticket size totals, and status distributions
CREATE OR REPLACE VIEW view_transaction_summary AS
SELECT 
    status, 
    COUNT(*) AS total_transaction_count,
    ROUND(SUM(amount), 2) AS gross_volume_usd,
    ROUND(AVG(amount), 2) AS average_ticket_size_usd
FROM transactions
GROUP BY status;

-- 2. Processing Channel Speed and Velocity View
-- Ranks performance, aggregate values, and processing system metrics
CREATE OR REPLACE VIEW view_channel_velocity AS
SELECT 
    channel,
    COUNT(*) AS absolute_transaction_hits,
    ROUND(SUM(amount), 2) AS cumulative_volume_processed,
    ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM transactions)), 2) AS channel_volume_market_share
FROM transactions
GROUP BY channel;

-- 3. Top High-Value Account Whale View
-- Flags accounts driving the highest transaction values across the platform
CREATE OR REPLACE VIEW view_top_customer_profiles AS
SELECT 
    customer_id,
    COUNT(*) AS gross_execution_count,
    ROUND(SUM(amount), 2) AS gross_spend_volume_usd
FROM transactions
GROUP BY customer_id
ORDER BY gross_spend_volume_usd DESC;
