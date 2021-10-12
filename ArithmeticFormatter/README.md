### Arithmetic Formatter

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
```
  235
+  52
-----
```

Inside `arithmetic_arranger.py` file, there is a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function optionally takes a second argument. When the second argument is set to `True`, the answers are displayed.

### For example

Function Call:
```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:
```py
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

### Program Output

The function returns the correct conversion if the supplied problems are properly formatted, otherwise, it **returns** a **string** that describes an error that is meaningful to the user.  


* Situations that will return an error:
  * If there are **too many problems** supplied to the function. The limit is **five**, anything more will return:
    `Error: Too many problems.`
  * The appropriate operators the function will accept are **addition** and **subtraction**. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
    `Error: Operator must be '+' or '-'.`
  * Each number (operand) can only contain digits. Otherwise, the function will return:
    `Error: Numbers must only contain digits.`
  * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
    `Error: Numbers cannot be more than four digits.`
*  If the user supplied the correct format of problems, the conversion returned will follow these rules:
    * There shall be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
    * Numbers shall be right-aligned.
    * There shall be four spaces between each problem.
    * There shall be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
    

### Testing 

The unit tests for this project are in `test_module.py`. The tests have been imported from `test_module.py` to `main.py`. The tests will run automatically whenever the "run" button is clicked.
