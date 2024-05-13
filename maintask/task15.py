def gross(a,b):
    gross=a+b
    return gross
salary=int(input("enter sal"))
benefits=int(input("enter benefits"))
grosssalary=float(gross(salary,benefits))
print(grosssalary)
#  use the gross salary to calc nhif
def calc_nhif(grss):
            if (grss > 0 and grss <= 5999) :
                nhif_contribution = 150
            elif (grss > 6000 and grss <= 7999) :
                nhif_contribution = 300
            elif (grss > 8000 and grss <= 12000) :
                nhif_contribution = 400
            elif (grss > 12000 and grss <= 14999) :
                nhif_contribution = 500
            elif (grss >= 15000 and grss <= 19999) :
                nhif_contribution = 600
            elif (grss >= 20000 and grss <= 24999) :
                nhif_contribution = 750
            elif (grss >= 25000 and grss <= 29999) :
                nhif_contribution = 850
            elif (grss >= 30000 and grss <= 34999) :
                nhif_contribution = 900
            elif (grss >= 35000 and grss <= 39999) :
                nhif_contribution = 950
            elif (grss >= 40000 and grss <= 44999) :
                nhif_contribution = 1000
            elif (grss >= 45000 and grss <= 49999) :
                nhif_contribution = 1100
            elif (grss >= 50000 and grss <= 59999) :
                nhif_contribution = 1200
            elif (grss >= 60000 and grss <= 69999) :
                nhif_contribution = 1300
            elif (grss >= 70000 and grss <= 79999) :
                nhif_contribution = 1400
            elif (grss >= 80000 and grss <= 89999) :
                nhif_contribution = 1500
            elif (grss >= 90000 and grss <= 99999) :
                nhif_contribution = 1600
            else :
                nhif_contribution = 1700
            
            return nhif_contribution
        
NHIF = float(calc_nhif(grosssalary))
print(NHIF, "nhif")

# Continue with the program above, then use  the gross salary to find the NSSF. 
#  To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MAXIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
def calc_nssf(x, rate = 0.06) :
            if (x > 0 and x <= 18000) :
                nssf_contri = x * rate
            else :
                nssf_contri = 18000 * 0.06
            
            return nssf_contri
        
NSSF =float(calc_nssf(grosssalary))
print(NSSF, "nssf")
        # Continue with the same program and calculate an individual’s NHDF using:
        #   i.e NHDF = gross_salary *  0.015
def calc_nhdf(y) :
            nhdf_contri = y * 0.015
            return nhdf_contri
        
NHDF = float(calc_nhdf(grosssalary))
print(NHDF, "nhdf")

        # Calculate the taxable income.
        #  i.e taxable_income = gross salary - (NSSF + NHDF) 
def calc_taxable_income(a, b, c) :
            taxable_income = a - (b + c)
            return taxable_income
        
taxable_income =float(calc_taxable_income(grosssalary, NSSF, NHDF))
print(taxable_income, "taxable_income")
        # //Continue with the same program and find the person's PAYEE using the taxable income above.
def calc_payee(tax) :
            payee = 0
            relief = 2400
            if (tax >= 0 and tax <= 24000) :
                payee = (24000 * 0.1) - relief
            elif (tax > 24000 and tax <= 32333) :
                payee = (24000 * 0.1) + ((tax - 24000) * 0.25) - relief
            elif (tax > 32333 and tax <= 500000) :
                payee = (24000 * 0.1) + (8333 * 0.25) + ((tax - 24000) * 0.3) - relief
            elif (tax > 500000 and tax <= 800000) :
                payee = (24000 * 0.1) + (8333 * 0.25) + (467667 * 0.3) + ((tax - 24000) * 0.325) - relief
            elif (tax > 800000 and tax <= 800000) :
                payee = (24000 * 0.1) + (8333 * 0.25) + (467667 * 0.3) + (300000 * 0.325) + ((tax - 24000) * 0.35) - relief
            return payee
        
PAYEE = float(calc_payee(taxable_income))
print(PAYEE, "payee")
        # //Continue with the same program and calculate an individual’s Net Salary using:
        # //  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
def calc_netsalary(a, b, c, d, e) :
            net_salary = float(a - (b+c+d+e))
            return net_salary
        
net_pay = calc_netsalary(grosssalary, NHIF, NSSF, NHDF, PAYEE)
print('net-pay', net_pay)