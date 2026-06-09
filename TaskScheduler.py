"""
Problem 2: Event Scheduler

Logic and Approach:
For `can_attend_all`: If we sort the events by when they start, we just need 
to loop through once. If any event starts before the previous one finishes, 
there is an overlap.

For `min_rooms_required`: I used a two-pointer approach. By splitting the start 
and end times into their own sorted lists, we can treat them like a timeline. 
When we hit a start time, a room is taken. When we hit an end time, a room 
opens up. We just keep a running tally and record the maximum rooms needed.
"""

def can_attend_all(events: list[tuple[int, int]]) -> bool:
    if not events:
        return True
    # Sort events based on start time
    events.sort()
    for i in range(1, len(events)):
        # If current event starts before the previous one ends, it overlaps
        if events[i][0] < events[i-1][1]:
            return False
    return True

def min_rooms_required(events: list[tuple[int, int]]) -> int:
    if not events:
        return 0
    # Separate and sort start times and end times
    start_times = sorted([event[0] for event in events])
    end_times = sorted([event[1] for event in events])
    rooms_in_use = 0
    max_rooms = 0
    # Pointers for our start and end time lists
    s = 0 
    e = 0 

    while s < len(events):
        # A meeting is starting before the current earliest meeting ends
        if start_times[s] < end_times[e]:
            rooms_in_use += 1
            s += 1
        # A meeting has ended
        else:
            rooms_in_use -= 1
            e += 1
        max_rooms = max(max_rooms, rooms_in_use)
    return max_rooms