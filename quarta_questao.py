from math import pi, trunc, e, sqrt

def truncate(number, digits) -> float:
    nbDecimals = len(str(number).split('.')[1]) 
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return trunc(stepper * number) / stepper

def error_calculator(p, p2):
    relat_error = 0
    abs_error = abs(p-p2)
    if p == 0:
        print(f'Relative error from {p} and {p2} cannot be calculated')
    else:
        relat_error = abs(p-p2)/abs(p)
    return abs_error, relat_error
    
## Truncamento de 3 dígitos
digits_to_truncate = 3
digits_to_round = 3

def question_4_letter_a(digits_to_truncate, digits_to_round):
    exactly_result = -10*pi+6*e-0.327
    truncate_result = -10*truncate(pi, digits_to_truncate)+6*truncate(e, digits_to_truncate)-0.327
    round_result = -10*round(pi, digits_to_round)+6*round(e, digits_to_round)-0.327
    
    abs_error_trunc, relat_error_trunc = error_calculator(exactly_result, truncate_result)
    abs_error_round, relat_error_round = error_calculator(exactly_result, round_result)
    
    print('Letter a)')
    print(f'{digits_to_truncate} digits truncate: Absolute error: {abs_error_trunc}, Relative error: {relat_error_trunc}')
    print(f'{digits_to_round} digits round: Absolute error: {abs_error_round}, Relative error: {relat_error_round}')
    
def question_4_letter_b(digits_to_truncate, digits_to_round):
    #exactly
    a= (1/3)
    b = (-123/4)
    c = (1/6)

    delta = b**2 - 4*a*c
    x1_result_exactly = (-b + sqrt(delta))/(2*a)
    x2_result_exactly = (-b - sqrt(delta))/(2*a)
    
    # Truncate
    a_trunc = truncate(1/3, digits_to_truncate)
    b_trunc = truncate(-123/4, digits_to_truncate)
    c_trunc = truncate(1/6, digits_to_truncate)

    delta = b_trunc**2 - 4*a_trunc*c_trunc
    x1_trunc_result = (-b_trunc + sqrt(delta))/(2*a_trunc)
    x2_trunc_result = (-b_trunc - sqrt(delta))/(2*a_trunc)
    
    # Round
    a_round = round(1/3, digits_to_round)
    b_round = round(-123/4, digits_to_round)
    c_round = round(1/6, digits_to_round)

    delta = b_round**2 - 4*a_round*c_round
    x1_round_result = (-b_round + sqrt(delta))/(2*a_round)
    x2_round_result = (-b_round - sqrt(delta))/(2*a_round)
    
    abs_error_x1_trunc, relat_error_x1_trunc = error_calculator(x1_result_exactly, x1_trunc_result)
    abs_error_x1_round, relat_error_x1_round = error_calculator(x1_result_exactly, x1_round_result)

    abs_error_x2_trunc, relat_error_x2_trunc = error_calculator(x2_result_exactly, x2_trunc_result)
    abs_error_x2_round, relat_error_x2_round = error_calculator(x2_result_exactly, x2_round_result)

    print('Letter b) x1')
    print(f'{digits_to_truncate} digits truncate: Absolute error: Absolute error: {abs_error_x1_trunc}, Relative error: {relat_error_x1_trunc}')
    print(f'{digits_to_round} digits round: Absolute error: {abs_error_x1_round}, Relative error: {relat_error_x1_round}')

    print('Letter b) x2')
    print(f'{digits_to_truncate} digits truncate: Absolute error: Absolute error: {abs_error_x2_trunc}, Relative error: {relat_error_x2_trunc}')
    print(f'{digits_to_round} digits round: Absolute error: {abs_error_x2_round}, Relative error: {relat_error_x2_round}')

def question_4_letter_c(digits_to_truncate, digits_to_round):
    #exactly
    exactly_result = 0
    for i in range(1, 10):
        i_fatorial = 1
        for j in range(1, i+1):
            i_fatorial = i_fatorial*i
        aux_exactly = ((-1)**i*5**i)/i_fatorial
        exactly_result = exactly_result + aux_exactly
    
    # Truncate
    result_truncate = 0
    for i in range(1, 10):
        i_fatorial = 1
        for j in range(1, i+1):
            i_fatorial = i_fatorial*i
        aux_trunc = ((-1)**i*5**i)/i_fatorial
        result_truncate = result_truncate + truncate(aux_trunc, digits_to_truncate)

    # Round
    result_round = 0
    for i in range(1, 10):
        i_fatorial = 1
        for j in range(1, i+1):
            i_fatorial = i_fatorial*i
        aux_round = ((-1)**i*5**i)/i_fatorial
        result_round = result_round + round(aux_round, digits_to_round)

    abs_error_trunc, relat_error_trunc = error_calculator(exactly_result, result_truncate)
    abs_error_round, relat_error_round = error_calculator(exactly_result, result_round)

    print('Letter c)')
    print(f'{digits_to_truncate} digits truncate: Absolute error: Absolute error: {abs_error_trunc}, Relative error: {relat_error_trunc}')
    print(f'{digits_to_round} digits round: Absolute error: {abs_error_round}, Relative error: {relat_error_round}')
