def investment_val(amount, annualRate, years):
    monthRate = annualRate / 12.0 / 100.0
    months = years * 12
    futureInvestmentValue = amount * ((1 + monthRate) ** months)
    return round(futureInvestmentValue,2)