def maximumTime(time):
    output = []
    # Individual comparison checks, assume the whole timestring is valid
    # Check the hour left and right
    if time[0] == "?":
        if time[1] != "?" and int(time[1]) > 3:
            output.append("1")
        else:
            output.append("2")
    else:
        output.append(time[0])
    # Using the knowledge from the first append
    if time[1] == "?":
        if output[0] == "2":
            output.append("3")
        else:
            output.append("9")
    else:
        output.append(time[1])
    # The inbetween must have a colon
    output.append(":")
    # Now the minutes should be easier
    if time[3] == "?":
        output.append("5")
    else:
        output.append(time[3])
    if time[4] == "?":
        output.append("9")
    else:
        output.append(time[4])
    # Return the output, O(N) To make it a string
    return ''.join(output)