SELECT seller_id,
    sum(price) as TotalRevenue,
    count(DISTINCT t1.order_id) as qtSalles

FROM tb_order_items as t1
LEFT JOIN tb_orders as t2
on t1.order_id = t2.order_id

GROUP BY t1.seller_id


