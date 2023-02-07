def study_time(total_pages, pages_per_session, your_speed, meowth_speed):
    time = 0
    for i in range(1, total_pages + 1, pages_per_session + 1):
        if i + pages_per_session <= total_pages:
            time += pages_per_session * your_speed
        else:
            time += (total_pages - i + 1) * your_speed
        if (i-1) % (pages_per_session + 1) == 0 and i + pages_per_session <= total_pages:
            time += pages_per_session * meowth_speed
    return time

print(study_time(3,14,2,5))