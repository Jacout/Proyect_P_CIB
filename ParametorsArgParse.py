import argparse
parser = argparse.ArgumentParser() #hace los parametros con arg
parser.add_argument("-p1", dest="param1", help="parámetro 1")
params = parser.parse_args()
print(params.param1)
