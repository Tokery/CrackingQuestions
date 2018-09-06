def parens(currentAnswers, depth, n):
    if (depth == n):
        return currentAnswers
    for value in list(currentAnswers):
        currentAnswers['(' + value + ')'] = 'dummy'
        currentAnswers['()' + value] = 'dummy'
        currentAnswers[value + '()'] = 'dummy'
        del currentAnswers[value]
    return parens(currentAnswers, depth + 1, n)

pairs_of_parens = parens({'()': 'dummy'}, 1, 3)

print (list(pairs_of_parens))