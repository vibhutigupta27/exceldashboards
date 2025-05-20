import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Filter Dashboard", layout="wide")
st.title("📊 Excel Dashboard: Filter by Spend")

# Step 1: Upload Excel File
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        st.success("File uploaded successfully!")
        st.write("### Preview of Uploaded Data")
        st.dataframe(df)

        # Clean and normalize column names
        df.columns = df.columns.str.strip().str.lower()

        # Now check for 'spend'
        if "spend" in df.columns:
            min_spend = st.number_input(
                "Enter minimum spend to filter rows",
                min_value=0.0,
                value=300.0,
                step=50.0
            )

            total_rows = len(df)

            # Step 3: Filter the dataframe
            filtered_df = df[df["spend"] >= min_spend]
            remaining_rows = len(filtered_df)
            removed_rows = total_rows - remaining_rows

            # Feedback message
            st.info(
                f"🔍 Filter applied: Kept {remaining_rows:,} out of {total_rows:,} rows "
                f"(Filtered out {removed_rows:,} rows below spend {min_spend})."
            )

            st.write(f"### Filtered Data (spend ≥ {min_spend})")
            st.dataframe(filtered_df)

            st.write("### Basic Stats on Filtered Data")
            st.write(filtered_df.describe())
        else:
            st.error("⚠️ The uploaded file does not contain a 'Spend' column.")
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
else:
    st.info("Please upload an Excel file to get started.")

