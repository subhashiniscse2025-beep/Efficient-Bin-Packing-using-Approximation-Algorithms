def first_fit(items, capacity=1.0):

    bins = []
    bin_contents = []

    for item in items:

        placed = False

        for i in range(len(bins)):

            if bins[i] + item <= capacity:

                bins[i] += item
                bin_contents[i].append(item)

                placed = True
                break

        if not placed:

            bins.append(item)
            bin_contents.append([item])

    return bin_contents


def first_fit_decreasing(items, capacity=1.0):

    sorted_items = sorted(
        items,
        reverse=True
    )

    return first_fit(
        sorted_items,
        capacity
    )


def best_fit_decreasing(items, capacity=1.0):

    sorted_items = sorted(
        items,
        reverse=True
    )

    bins = []
    bin_contents = []

    for item in sorted_items:

        best_index = -1
        minimum_remaining_space = float('inf')


        for i in range(len(bins)):

            remaining_space = capacity - bins[i]

            if (
                remaining_space >= item
                and remaining_space - item
                < minimum_remaining_space
            ):

                minimum_remaining_space = (
                    remaining_space - item
                )

                best_index = i


        if best_index != -1:

            bins[best_index] += item
            bin_contents[best_index].append(item)

        else:

            bins.append(item)
            bin_contents.append([item])


    return bin_contents


def calculate_lower_bound(items, capacity):

    total_weight = sum(items)

    return int(
        -(-total_weight // capacity)
    )


def calculate_utilization(bin_items, capacity):

    return (
        sum(bin_items) / capacity
    ) * 100
