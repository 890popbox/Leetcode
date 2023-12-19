select sell_date, 
COUNT(distinct product) as num_sold,
GROUP_CONCAT(distinct product order by product ASC separator ',') as products
From Activities group by sell_date order by sell_date
