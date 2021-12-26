select payment_document_id,
    document_date,
    sum(payed_sum),
    count(payed_sum)
from payment_document
    join order_row on payment_document.payment_document_id = order_row.payment_document
where (payment_document_id = '$payment_document_id')
group by payment_document_id