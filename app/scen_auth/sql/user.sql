SELECT user_id,
    user_group_name
FROM users
where user_login = '$login'
    and user_password = '$password'