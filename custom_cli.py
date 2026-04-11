import argparse

class CustomAction(argparse.Action):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def __call__(self, parser, namespace, value, option_string = None):
        """
        Sets the CLI argument's value, EPastore 04/11/2026
        """

        states = {
            'California':'CA',
            'Alaska':'AK',
            'Maryland':'MD',
            'Delaware':'DE'
        }

        capitals = {
            'CA':'Sacramento',
            'AK':'Juneau',
            'MD':'Annapolis',
            'DE':'Dover'
        }

        namespace.state = value.capitalize()
        namespace.abbrev = states.get(namespace.state, None)
        namespace.capital = capitals.get(namespace.abbrev, None)
        # return super().__call__(parser, namespace, value, option_string)

def statehood(state):
    years = {
        "CA":1850,
        "AK":1959,
        "MD":1788,
        "DE":1787
    }
    return years.get(state, None)

parser = argparse.ArgumentParser()
parser.add_argument('state',type=str, metavar='STATE', action=CustomAction, help='full state name')
args = parser.parse_args()
print(args)
results = statehood(args.abbrev)
print('results = ',results)