SELECT
    Department,
    JobRole,
    COUNT(CASE
        WHEN Attrition_Flag = 1 AND PerformanceRating >= 3 THEN 1
    END) AS Regrettable_Losses,
    ROUND(AVG(Comp
_Parity_Index), 2) AS Avg_Comp_Parity,
    ROUND(AVG(Flight_Risk_Score), 1) AS Avg_Flight_Risk
FROM enterprise_hr_data
GROUP BY Department, JobRole
HAVING Regrettable_Losses > 0
ORDER BY Regrettable_Losses DESC;

SELECT
    OverTime,
    COUNT(EmployeeNumber) AS Total_Employees,
    ROUND(AVG(Flight_Risk_Score), 2) AS Avg_Risk_Score,
    ROUND(AVG(Attrition_Flag) * 100, 2) AS Attrition_Rate_Pct
FROM enterprise_hr_data
GROUP BY OverTime;
