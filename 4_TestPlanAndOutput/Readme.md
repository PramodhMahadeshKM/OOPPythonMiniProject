# TEST PLAN:

## Table: High level test plan

| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|HLT01     | Test various code quality checks | .py files,,Implementation folder | Pass | Pass | Technical |
|HLT02     | Test various user inputs | User inputs | Success | Success | Scenario/Technical

## Table: Low level test plan

| **Test ID** | **HLT ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** |**Type Of Test**  |    
|-------------|-----|--------------------------------------------------------------|------------|-------------|----------------|------------------|
| LLT01 | HLT02 | Check for boundary conditions of balance | float value of balance | self.balance | self.balance | Scenario/Technical |
| LLT02 | HLT02 | Check for passing correct values from .txt files | Approppriate values in .txt file | 0 | 0 | Scenario/Technical |
| LLT03 | HLT02 | Check for boundary conditions of bill | float value of bill | self.bill | self.bill | Scenario/Technical |
| LLT04 | HLT02 | Check for passing wrong values from .txt files | Wrong values in .txt file | -1 | -1 | Scenario/Technical |
| LLT05 | HLT02 | Check for wrong input variable for choosing feature | user inputs | stay in loop | stay in loop | Scenario/Technical |
| LLT06 | HLT02 | pylint score check | .py file | Pass | Pass | Technical |
