def arithmetic_arranger(problems, show_results=False):

    problems_list = []
    for p in problems:
        problems_list += p.split(" ")

    problems_digits = [pr.replace("+", '1') for pr in problems_list]
    problems_digits = [pr.replace("-", '-1') for pr in problems_digits]

    test_total = 0

    # Test too many problems - ttmp -
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        test_total += 1

    # Test Incorrect Operator - tio -
    count_pl = 1
    tio = 0

    while count_pl < len(problems_list):

        count_ele = problems_list[count_pl]

        if count_ele == "+":
            count_ele = count_ele.replace("+", "0")
        if count_ele == "-":
            count_ele = count_ele.replace("-", "0")
        if count_ele.isdigit():
            tio += 1

        count_pl += 3

    if tio < len(problems):
        arranged_problems = "Error: Operator must be '+' or '-'."
        test_total += 1

    # Test Only Digits - tod -
    count_pl = 0
    tod = 0

    while count_pl < len(problems_list):
        count_ele = problems_list[count_pl]
        count_ele2 = problems_list[count_pl + 2]
        if count_ele.isnumeric() and count_ele2.isnumeric():
            tod += 1
        count_pl += 3

    if tod < len(problems):
        arranged_problems = "Error: Numbers must only contain digits."
        test_total += 1

    # Test Too Many Digits - ttmd -
    ttmd = 0
    for pd in problems_digits:
        if len(pd) > 4:
            ttmd += 1
    if ttmd > 0:
        arranged_problems = "Error: Numbers cannot be more than four digits."
        test_total += 1

    if test_total == 0:
        tt = 0
        first_row = ""
        second_row = ""
        underline_row = ""
        results = ""

        while tt < len(problems_digits):

            if len(problems_digits[tt]) > len(problems_digits[tt + 2]):
                longest_digit = len(problems_digits[tt])
            else:
                longest_digit = len(problems_digits[tt + 2])

            # First numbers row
            first_row_spaces = longest_digit - len(problems_digits[tt])
            first_row_formatted = (' ' * first_row_spaces) + problems_digits[tt]
            first_row += "  " + first_row_formatted + "    "

            # Second numbers row
            second_row += problems_list[tt + 1]
            second_row_spaces = longest_digit - len(problems_digits[tt + 2])
            second_row_formatted = (' ' * second_row_spaces) + problems_digits[tt + 2]
            second_row += " " + second_row_formatted + "    "

            # Underline row
            underline_row_spaces = longest_digit
            underline_formatted = ('-' * underline_row_spaces)
            underline_row += "--" + underline_formatted + "    "

            # Results row
            add = int(problems_digits[tt]) + int(problems_digits[tt + 1]) * int(problems_digits[tt + 2])
            result_spaces = (2 + longest_digit) - len(str(add))
            result_formatted = (' ' * result_spaces) + str(add)
            results += result_formatted + "    "

            tt += 3

        test_arrangement = first_row[:-4] + "\n" + second_row[:-4] + "\n" + underline_row[:-4]
        test_solutions = test_arrangement + "\n" + results[:-4]

        if show_results:
            arranged_problems = test_solutions
        else:
            arranged_problems = test_arrangement

    return arranged_problems
