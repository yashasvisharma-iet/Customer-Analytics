from data_cleaning import clean_data, save_data
from kpi_analysis import kpi_summary, performance_by_channel, performance_by_region, top_agents
from insights import (
    sla_breach_by_channel,
    csat_correlation,
    resolution_impact,
    response_delay_impact
)
def main():
    input_file = "support_tickets.csv"
    output_file = "cleaned_support_tickets.csv"

    print("🔄 Starting data cleaning...")
    df = clean_data(input_file)

    save_data(df, output_file)

    print("\n✅ Data cleaning complete")

    # 👉 KPI Analysis
    kpi_summary(df)
    performance_by_channel(df)
    performance_by_region(df)
    top_agents(df)
    print("\n🔍 Running Insight Analysis...")

    sla_breach_by_channel(df)
    csat_correlation(df)
    resolution_impact(df)
    response_delay_impact(df)

if __name__ == "__main__":
    main()