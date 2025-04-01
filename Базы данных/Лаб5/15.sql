SELECT 
    product_id, 
    product_name,
	product_price,
    ROW_NUMBER() OVER (ORDER BY product_price DESC) AS rn,
    RANK() OVER (ORDER BY product_price DESC) AS r,
    DENSE_RANK() OVER (ORDER BY product_price DESC) AS dr
FROM products;
