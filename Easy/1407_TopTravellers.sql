select Users.name, coalesce(sum(Rides.distance),0) as travelled_distance
    from Users left join Rides on Users.id=Rides.user_id
    group by rides.user_id
    order by travelled_distance desc , name asc;
    /* name, travelled distance
    where name is the Users name, and travelled distance is the sum of rides from that user
    we get this by joining the tables where the user id matches the rides user id
    then we group them by user_id and order by the travel distance in desc */
