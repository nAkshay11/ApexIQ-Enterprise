/*
=========================================================
ApexIQ Enterprise
Enterprise Sales Analytics Platform
SQL Query Book

Author : Akshay Chandra N
Database : PostgreSQL

Description:
This file contains 50 business SQL queries for executive KPIs,
sales analysis, customer insights, product analysis, inventory,
payments, employee analysis, and business reporting.
=========================================================
*/

-- 1. Total Revenue
SELECT SUM(final_amount) AS total_revenue
FROM sales.orders;

-- 2. Total Orders
SELECT COUNT(*) AS total_orders
FROM sales.orders;

-- 3. Total Customers
SELECT COUNT(*) AS total_customers
FROM customer.customers;

-- 4. Total Products
SELECT COUNT(*) AS total_products
FROM inventory.products;

-- 5. Total Employees
SELECT COUNT(*) AS total_employees
FROM common.employees;

-- 6. Top 10 Customers by Revenue
SELECT
c.customer_id,
c.first_name,
c.last_name,
SUM(o.final_amount) AS total_revenue
FROM customer.customers c
JOIN sales.orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_revenue DESC
LIMIT 10;

-- 7. Monthly Revenue
SELECT
DATE_TRUNC('month', order_date) AS month,
SUM(final_amount) AS revenue
FROM sales.orders
GROUP BY month
ORDER BY month;

-- 8. Top 10 Best Selling Products
SELECT
p.product_name,
SUM(oi.quantity) AS total_quantity
FROM inventory.products p
JOIN sales.order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC
LIMIT 10;

-- 9. Revenue by State
SELECT
c.state,
SUM(o.final_amount) AS revenue
FROM customer.customers c
JOIN sales.orders o
ON c.customer_id = o.customer_id
GROUP BY c.state
ORDER BY revenue DESC;

-- 10. Payment Status Count
SELECT
payment_status,
COUNT(*) AS total_payments
FROM finance.payments
GROUP BY payment_status;

-- 11. Top 10 Highest Spending Customers
SELECT
c.customer_id,
c.first_name,
c.last_name,
SUM(o.final_amount) AS total_spent
FROM customer.customers c
JOIN sales.orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spent DESC
LIMIT 10;

-- 12. Average Order Value
SELECT ROUND(AVG(final_amount),2) AS average_order_value
FROM sales.orders;

-- 13. Revenue by Payment Method
SELECT
payment_method,
SUM(final_amount) AS revenue
FROM sales.orders
GROUP BY payment_method
ORDER BY revenue DESC;

-- 14. Orders by Status
SELECT
order_status,
COUNT(*) AS total_orders
FROM sales.orders
GROUP BY order_status;

-- 15. Top 10 Cities by Revenue
SELECT
c.city,
SUM(o.final_amount) AS revenue
FROM customer.customers c
JOIN sales.orders o
ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY revenue DESC
LIMIT 10;

-- 16. Top 10 Brands by Revenue
SELECT
p.brand,
SUM(oi.total_price) AS revenue
FROM inventory.products p
JOIN sales.order_items oi
ON p.product_id = oi.product_id
GROUP BY p.brand
ORDER BY revenue DESC
LIMIT 10;

-- 17. Average Employee Salary
SELECT ROUND(AVG(salary),2) AS average_salary
FROM common.employees;

-- 18. Employees by Department
SELECT
department_id,
COUNT(*) AS employees
FROM common.employees
GROUP BY department_id
ORDER BY department_id;

-- 19. Average Product Price
SELECT ROUND(AVG(unit_price),2) AS average_product_price
FROM inventory.products;

-- 20. Total Discount Given
SELECT SUM(discount) AS total_discount
FROM sales.orders;

-- 21. Monthly Order Count
SELECT
DATE_TRUNC('month', order_date) AS month,
COUNT(*) AS total_orders
FROM sales.orders
GROUP BY month
ORDER BY month;

-- 22. Monthly Average Order Value
SELECT
DATE_TRUNC('month', order_date) AS month,
ROUND(AVG(final_amount),2) AS avg_order_value
FROM sales.orders
GROUP BY month
ORDER BY month;

-- 23. Revenue by Customer Segment
SELECT
c.customer_segment,
SUM(o.final_amount) AS revenue
FROM customer.customers c
JOIN sales.orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_segment
ORDER BY revenue DESC;

-- 24. Orders by Customer Segment
SELECT
c.customer_segment,
COUNT(o.order_id) AS total_orders
FROM customer.customers c
JOIN sales.orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_segment
ORDER BY total_orders DESC;

-- 25. Profit by Product
SELECT
p.product_name,
SUM((oi.unit_price - p.cost_price) * oi.quantity - oi.discount) AS profit
FROM sales.order_items oi
JOIN inventory.products p
ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY profit DESC
LIMIT 10;

-- 26. Low Stock Products
SELECT
product_id,
product_name,
stock_quantity,
reorder_level
FROM inventory.products
WHERE stock_quantity <= reorder_level
ORDER BY stock_quantity ASC;

-- 27. Revenue by Warehouse
SELECT
warehouse_id,
SUM(final_amount) AS revenue
FROM sales.orders
GROUP BY warehouse_id
ORDER BY revenue DESC;

-- 28. Cancelled Orders Count
SELECT COUNT(*) AS cancelled_orders
FROM sales.orders
WHERE order_status = 'Cancelled';

-- 29. Pending Payments Count
SELECT COUNT(*) AS pending_payments
FROM finance.payments
WHERE payment_status = 'Pending';

-- 30. Payment Success Rate
SELECT
ROUND(
COUNT(*) FILTER (WHERE payment_status = 'Completed') * 100.0 / COUNT(*), 2
) AS payment_success_rate
FROM finance.payments;

-- 31. Top 10 Employees by Sales
SELECT
e.employee_id,
e.first_name,
e.last_name,
SUM(o.final_amount) AS total_sales
FROM common.employees e
JOIN sales.orders o
ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
ORDER BY total_sales DESC
LIMIT 10;

-- 32. Average Revenue Per Customer
SELECT
ROUND(SUM(final_amount) / COUNT(DISTINCT customer_id),2) AS average_customer_revenue
FROM sales.orders;

-- 33. Top 10 Customers by Number of Orders
SELECT
customer_id,
COUNT(*) AS total_orders
FROM sales.orders
GROUP BY customer_id
ORDER BY total_orders DESC
LIMIT 10;

-- 34. Highest Value Order
SELECT *
FROM sales.orders
ORDER BY final_amount DESC
LIMIT 1;

-- 35. Lowest Value Order
SELECT *
FROM sales.orders
ORDER BY final_amount ASC
LIMIT 1;

-- 36. Product Count by Brand
SELECT
brand,
COUNT(*) AS total_products
FROM inventory.products
GROUP BY brand
ORDER BY total_products DESC;

-- 37. Average Stock by Brand
SELECT
brand,
ROUND(AVG(stock_quantity),2) AS average_stock
FROM inventory.products
GROUP BY brand
ORDER BY average_stock DESC;

-- 38. Customer Distribution by State
SELECT
state,
COUNT(*) AS total_customers
FROM customer.customers
GROUP BY state
ORDER BY total_customers DESC;

-- 39. Employee Performance Rating Distribution
SELECT
performance_rating,
COUNT(*) AS employees
FROM common.employees
GROUP BY performance_rating
ORDER BY performance_rating DESC;

-- 40. Total Quantity Sold by Product
SELECT
p.product_name,
SUM(oi.quantity) AS quantity_sold
FROM inventory.products p
JOIN sales.order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY quantity_sold DESC
LIMIT 10;

-- 41. Top 10 Most Ordered Products
SELECT
p.product_name,
COUNT(DISTINCT oi.order_id) AS total_orders
FROM inventory.products p
JOIN sales.order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_orders DESC
LIMIT 10;

-- 42. Average Quantity Per Order Item
SELECT
ROUND(AVG(quantity),2) AS average_quantity
FROM sales.order_items;

-- 43. Total Revenue by Brand
SELECT
p.brand,
SUM(oi.total_price) AS revenue
FROM inventory.products p
JOIN sales.order_items oi
ON p.product_id = oi.product_id
GROUP BY p.brand
ORDER BY revenue DESC;

-- 44. Top 10 Products by Revenue
SELECT
p.product_name,
SUM(oi.total_price) AS revenue
FROM inventory.products p
JOIN sales.order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;

-- 45. Customer Loyalty Points Ranking
SELECT
customer_id,
first_name,
last_name,
loyalty_points
FROM customer.customers
ORDER BY loyalty_points DESC
LIMIT 10;

-- 46. Employee Salary Ranking
SELECT
employee_id,
first_name,
last_name,
salary
FROM common.employees
ORDER BY salary DESC
LIMIT 10;

-- 47. Product Inventory Value
SELECT
SUM(stock_quantity * cost_price) AS inventory_value
FROM inventory.products;

-- 48. Average Profit Per Product
SELECT
ROUND(AVG(unit_price - cost_price),2) AS average_profit
FROM inventory.products;

-- 49. Total Tax Collected
SELECT
SUM(tax) AS total_tax
FROM sales.orders;

-- 50. Overall Business Summary
SELECT
(SELECT COUNT(*) FROM customer.customers) AS customers,
(SELECT COUNT(*) FROM common.employees) AS employees,
(SELECT COUNT(*) FROM inventory.products) AS products,
(SELECT COUNT(*) FROM sales.orders) AS orders,
(SELECT SUM(final_amount) FROM sales.orders) AS revenue;

/*
=========================================================
END OF SQL QUERY BOOK
Total Queries: 50
=========================================================
*/