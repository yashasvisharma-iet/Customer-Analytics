import pandas as pd


def sla_breach_rate(df: pd.DataFrame):
    total = len(df)
    breached = df['sla_compliance'].value_counts().get(False, 0)

    rate = (breached / total) * 100
    return round(rate, 2)


def avg_resolution_time(df: pd.DataFrame):
    return round(df['resolution_hours'].mean(), 2)


def avg_csat(df: pd.DataFrame):
    return round(df['csat_score'].mean(), 2)


def kpi_summary(df: pd.DataFrame):
    print("\n📊 KPI SUMMARY")

    print(f"SLA Breach Rate: {sla_breach_rate(df)}%")
    print(f"Avg Resolution Time: {avg_resolution_time(df)} hrs")
    print(f"Avg CSAT Score: {avg_csat(df)}")

# analysis

def performance_by_channel(df: pd.DataFrame):
    print("\n📊 Performance by Channel")

    result = df.groupby('channel').agg({
        'resolution_hours': 'mean',
        'sla_compliance': lambda x: (x == False).mean() * 100,
        'csat_score': 'mean'
    }).rename(columns={
        'resolution_hours': 'avg_resolution_time',
        'sla_compliance': 'sla_breach_rate',
        'csat_score': 'avg_csat'
    })

    print(result.round(2))


def performance_by_region(df: pd.DataFrame):
    print("\n📊 Performance by Region")

    result = df.groupby('region').agg({
        'resolution_hours': 'mean',
        'sla_compliance': lambda x: (x == False).mean() * 100,
        'csat_score': 'mean'
    })

    print(result.round(2))


def top_agents(df: pd.DataFrame):
    print("\n🏆 Top Agents")

    result = df.groupby('agent_id').agg({
        'resolution_hours': 'mean',
        'csat_score': 'mean'
    }).sort_values(by='csat_score', ascending=False)

    print(result.head(5).round(2))