select *
from reserved_product_payment.order
where month(order_date) = '$month'
    and year(order_date) = '$year'
group by order_id