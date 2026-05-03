import pandas as pd


def sla_breach_by_channel(df):
    print("\n📊 SLA Breach by Channel")

    result = df.groupby('channel')['sla_compliance'].apply(
        lambda x: (x == False).mean() * 100
    ).sort_values(ascending=False)

    print(result.round(2))

def csat_correlation(df):
    print("\n📈 CSAT Correlation")

    corr_resolution = df['csat_score'].corr(df['resolution_hours'])
    corr_response = df['csat_score'].corr(df['first_response_hours'])
def csat_correlation(df):
    print("\n📈 CSAT Correlation")

    corr_resolution = df['csat_score'].corr(df['resolution_hours'])
    corr_response = df['csat_score'].corr(df['first_response_hours'])

    print(f"CSAT vs Resolution Time: {round(corr_resolution, 2)}")
    print(f"CSAT vs First Response Time: {round(corr_response, 2)}")
    print(f"CSAT vs Resolution Time: {round(corr_resolution, 2)}")
    print(f"CSAT vs First Response Time: {round(corr_response, 2)}")



def resolution_impact(df):
    print("\n📊 Resolution Speed vs CSAT")

    result = df.groupby('resolution_speed_category')['csat_score'].mean()
    print(result.round(2))


def response_delay_impact(df):
    print("\n📊 Response Delay vs SLA Breach")

    result = df.groupby('response_delay_flag')['sla_compliance'].apply(
        lambda x: (x == False).mean() * 100
    )

    print(result.round(2))