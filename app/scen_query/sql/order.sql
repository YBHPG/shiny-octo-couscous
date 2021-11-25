SELECT *
FROM `order`
WHERE order_date BETWEEN DATE('$begin') AND DATE('$end')
    /* все закаы в диапазоне дат */