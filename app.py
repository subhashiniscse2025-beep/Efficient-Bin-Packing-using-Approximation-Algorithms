import streamlit as st

from PROGRAM import (
    first_fit,
    first_fit_decreasing,
    best_fit_decreasing,
    calculate_lower_bound,
    calculate_utilization
)


st.set_page_config(

    page_title="Bin Packing Approximation",

    page_icon="📦"

)


st.title(

    "Efficient Bin Packing using Approximation Algorithms"

)


st.write(

    """
    This application compares three Bin Packing approximation algorithms:
    First Fit (FF), First Fit Decreasing (FFD), and Best Fit Decreasing (BFD).
    """

)


st.subheader("Input Configuration")


items_input = st.text_input(

    "Enter item weights separated by commas",

    "0.5,0.7,0.3,0.9,0.2,0.6,0.8,0.4,0.1,0.5"

)


capacity = st.number_input(

    "Bin Capacity",

    min_value=0.1,

    value=1.0,

    step=0.1

)


if st.button("Compare Algorithms"):


    items = list(

        map(

            float,

            items_input.split(",")

        )

    )


    lower_bound = calculate_lower_bound(

        items,

        capacity

    )


    ff_bins = first_fit(

        items,

        capacity

    )


    ffd_bins = first_fit_decreasing(

        items,

        capacity

    )


    bfd_bins = best_fit_decreasing(

        items,

        capacity

    )


    st.success(

        f"Theoretical Lower Bound: {lower_bound} bins"

    )


    st.subheader("Algorithm Comparison")


    comparison_data = [

        [

            "First Fit (FF)",

            len(ff_bins),

            len(ff_bins) - lower_bound

        ],

        [

            "First Fit Decreasing (FFD)",

            len(ffd_bins),

            len(ffd_bins) - lower_bound

        ],

        [

            "Best Fit Decreasing (BFD)",

            len(bfd_bins),

            len(bfd_bins) - lower_bound

        ]

    ]


    st.table(

        comparison_data

    )


    st.divider()


    st.subheader("First Fit (FF)")


    for i, bin_items in enumerate(

        ff_bins,

        1

    ):

        used = sum(bin_items)


        st.write(

            f"Bin {i}: {bin_items} | "

            f"Used: {used:.2f} / {capacity}"

        )


    st.divider()


    st.subheader("First Fit Decreasing (FFD)")


    for i, bin_items in enumerate(

        ffd_bins,

        1

    ):

        used = sum(bin_items)


        st.write(

            f"Bin {i}: {bin_items} | "

            f"Used: {used:.2f} / {capacity}"

        )


    st.divider()


    st.subheader("Best Fit Decreasing (BFD)")


    for i, bin_items in enumerate(

        bfd_bins,

        1

    ):

        used = sum(bin_items)


        st.write(

            f"Bin {i}: {bin_items} | "

            f"Used: {used:.2f} / {capacity}"

        )
