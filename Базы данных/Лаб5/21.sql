SELECT
    product_name AS "Название товара",
    order_date AS "Дата операции",
    quantity AS "Количество",
    SUM(quantity) OVER (PARTITION BY product_id ORDER BY order_date) AS "Промежуточный итог"
FROM
    (SELECT
        p.product_name,
        o.order_date,
        i.quantity,
        i.product_id
    FROM
        orders o
    JOIN
        items i ON o.order_id = i.order_id
    JOIN
        products p ON i.product_id = p.product_id
    WHERE
        o.order_date BETWEEN '2022-01-03' AND '2022-01-09') AS subquery
ORDER BY
    product_name, order_date;
