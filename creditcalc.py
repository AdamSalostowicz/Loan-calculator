import argparse
import math


def calculate_annuity_payments_one(principal, periods, interest):
    i = interest / (12 * 100)  # monthly_interest
    payment = math.ceil(principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
    print("Your annuity payment = {}!".format(payment))
    print("Overpayment = {}".format(payment * periods - principal))


def calculate_annuity_payments_two(payment, periods, interest):
    i = interest / (12 * 100)  # monthly_interest
    principal = math.floor(payment * (math.pow(1 + i, periods) - 1) / (i * math.pow(1 + i, periods)))
    print("Your loan principal = {}".format(principal))
    print("Overpayment = {}".format(round(payment * periods - principal)))
    return principal


def calculate_annuity_payments_three(principal, payment, interest):
    i = interest / (12 * 100)  # monthly_interest
    periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    print(periods)
    if periods / 12 < 1:
        print("It will take {} months to repay this loan".format(periods % 12))
    elif periods % 12 == 0:
        if periods == 1:
            print("It will take {} year to repay this loan".format("one"))
        else:
            print("It will take {} years to repay this loan".format(periods // 12))
    else:
        print("It will take {} years and {} months to repay this loan".format(periods // 12, periods % 12))
    print("Overpayment = {}".format(periods * payment - principal))


def calculate_diferntiated_payments(principal, periods, interest):
    overpayment = 0

    for i in range(1, periods + 1):
        monthly_interest = interest / (12 * 100)
        diff_payment = math.ceil(principal / periods + monthly_interest * (principal -
                                                                           (principal * (i - 1)) / periods))
        overpayment += diff_payment
        print("Month {}: payment is {}".format(i, diff_payment))
    print("\nOverpayment = {}".format(overpayment - principal))


parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=["annuity", "diff"], help='Write type of payment: "annuity", or "diff"')
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=float)
args = parser.parse_args()
arguments = [args.principal is not None, args.periods is not None, args.interest is not None, args.payment is not None]
if not (args.type == "annuity" or args.type == "diff"):
    print("Incorrect parameters")
else:
    if (args.principal and float(args.principal) < 0) or (args.interest and float(args.interest) < 0) or \
            (args.periods and float(args.periods) < 0) or (args.payment and float(args.payment) < 0):
        print("Incorrect parameters")
    elif not args.interest:
        print("Incorrect parameters")
    elif args.type == "diff" and args.principal != "None" and args.interest != "None" and args.payment != "None" \
            and args.periods is None:
        print("Incorrect parameters")
    elif arguments.count(False) > 1:
        print("Incorrect parameters")
    else:
        if args.type == "annuity":
            if args.principal != "None" and args.periods != "None" and args.interest != 0 and args.payment is None:
                calculate_annuity_payments_one(args.principal, args.periods, args.interest)
                # print(1)
            elif args.principal is None and args.periods != "None" and args.interest != 0 and args.payment != "None":
                calculate_annuity_payments_two(args.payment, args.periods, args.interest)
                # print(2)
            elif args.principal != "None" and args.periods is None and args.interest != 0 and args.payment != "None":
                calculate_annuity_payments_three(args.principal, args.payment, args.interest)
                # print(3)
        else:
            calculate_diferntiated_payments(args.principal, args.periods, args.interest)
